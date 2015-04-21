#!/usr/bin/env python

import sys
import os
from PIL import Image

#import pdb

# you need to install this library yourself
# recent versions handle bigtiff too...
import tifffile

"""
Extract a pyramidal TIFF with JPEG tiled storage into a tree of
separate JPEG files into DZI compliant that is usable by openseadragon.

usage: extract2dzi.py pyramid-file dest-dir 0/1
         
1 = add the missing level 0
0 = forget it

The pyramid-file must be a multi-page TIFF with each page having an
image scaled by 1/2 from the previous page.  All pages must be tiled
with the same tile size, and tiles must be stored using the new-style
JPEG compression format, i.e. TIFF compression == 7.

The lowest resolution page must have 4 or fewer tiles.  If it has
more than 1, this script will leave space for the user to decide whether
final lowest zoom tile 0/0_0.jpg that is 1/2 scaled version of the image 
represented by that last page should be generated or not.

File directory generated
   
    dest-dir
      ImageProperties.xml
      pyramid.dzi
      pyramid_files
        0 
          0_0.jpg
        1
          0_0.jpg
          1_0.jpg
        ...
"""

try:
    fname = sys.argv[1]
    outdir = sys.argv[2]
    add0 = False
    if( len(sys.argv) > 3 ) :
        if (sys.argv[3]== "1") :
            add0 = True
        else :
            add0 = False

    infile = open(fname, 'rb')
    if not os.path.exists(outdir):
        os.makedirs(outdir)
except:
    sys.stderr.write('\nusage: extract.py pyramid-file dest-dir [0|1]\n\n')
    raise

t=fname.rsplit('/',1);
dir_name=t[-1].replace('.tif','_files');
dzi_name=t[-1].replace('.tif','.dzi');

topdir_template = '%(outdir)s/%(dir_name)s'
dir_template = topdir_template +'/%(zoomno)d'
tile_template = dir_template + '/%(tcolno)d_%(trowno)d.jpg'
dzi_template = '%(outdir)s/%(dzi_name)s'
image_template = '%(outdir)s/ImageProperties.xml'

tiff = tifffile.TiffFile(fname)
pages = list(tiff)

# we need to go from lowest to highest zoom level
pages.reverse()

# skip pages that aren't tiled... thumbnails?!
outpages = [ page for page in pages if hasattr(page.tags, 'tile_offsets') ]
if type(outpages[0].tags.tile_offsets.value) is int:
    outpages[0].tags.tile_offsets.value=[outpages[0].tags.tile_offsets.value]
    outpages[0].tags.tile_byte_counts.value=[outpages[0].tags.tile_byte_counts.value]

if hasattr(outpages[0].tags, 'tile_offsets') and len(outpages[0].tags.tile_offsets.value) > 1:
    # first input zoom level is multi-tile
#    assert len(outpages[0].tags.tile_offsets.value) <= 4

    if (len(outpages[0].tags.tile_offsets.value) > 4) :
# don't make level0 even if user wants to
      add0 = False;

    zoomno = 1
    total_tiles = 1
    need_to_build_0 = True
    if (add0):
      lowest_level = 0;
    else:
      lowest_level=1;

else:
    # input includes first zoom level already
    zoomno = 0
    lowest_level = 0
    total_tiles = 0
    need_to_build_0 = False

# remember values for debugging sanity checks
prev_page = None
tile_width = None
tile_length = None

def jpeg_assemble(jpeg_tables_bytes, jpeg_bytes):
    # start-image + tables + rest of image to end-image
    return jpeg_bytes[0:2] + jpeg_tables_bytes + jpeg_bytes[2:]

def load_tile(tile_offset, tile_length):
    infile.seek(tile_offset)
    return infile.read(tile_length)

def dump_tile(tileno, trow, tcol, jpeg_tables_bytes, tile_offset, tile_length):
    """Output one tile.  Note this manages global state for tile grouping in subdirs."""
    global zoomno
    global total_tiles

    total_tiles += 1

    topdir = topdir_template % dict(
        outdir = outdir,
        dir_name = dir_name
    )
    if not os.path.exists(topdir):
        os.makedirs(topdir, mode=0755)

    dirname = dir_template % dict(
        outdir = outdir,
        dir_name = dir_name,
        zoomno = zoomno
        )

    if not os.path.exists(dirname):
        # create tile group dir on demand
        os.makedirs(dirname, mode=0755)

    outname = tile_template % dict(
        outdir = outdir,
        dir_name = dir_name,
        zoomno = zoomno,
        tcolno = tcol,
        trowno = trow
        )
    
    outfile = open(outname, 'wb')
    outfile.write( jpeg_assemble(jpeg_tables_bytes, load_tile(tile_offset, tile_length)) )
    outfile.close()

outinfo = []

def get_page_info(page):

    pxsize = page.tags.image_width.value
    pysize = page.tags.image_length.value

    # get common JPEG tables to insert into all tiles
    if hasattr(page.tags, 'jpeg_tables'):
        # trim off start-image/end-image byte markers at prefix and suffix
        jpeg_tables_bytes = bytes(bytearray(page.tags.jpeg_tables.value))[2:-2]
    else:
        # no common tables to insert?
        jpeg_tables_bytes = bytes(bytearray([]))

    # this page has multiple JPEG tiles
    txsize = page.tags.tile_width.value
    tysize = page.tags.tile_length.value

    tcols = pxsize / txsize + (pxsize % txsize > 0)
    trows = pysize / tysize + (pysize % tysize > 0)

    return pxsize, pysize, txsize, tysize, tcols, trows, jpeg_tables_bytes

for page in outpages:
    # panic if these change from reverse-engineered samples
    assert page.tags.fill_order.value == 1
    assert page.tags.orientation.value == 1
    assert page.tags.compression.value == 7 # new-style JPEG

    if prev_page is not None:
        assert prev_page.tags.image_width.value == (page.tags.image_width.value / 2)
        assert prev_page.tags.image_length.value == (page.tags.image_length.value / 2)

    pxsize, pysize, txsize, tysize, tcols, trows, jpeg_tables_bytes = get_page_info(page)
    
    for tileno in range(0, len(page.tags.tile_offsets.value)):
        # figure position of tile within tile array
        trow = tileno / tcols
        tcol = tileno % tcols

        assert trow >= 0 and trow < trows
        assert tcol >= 0 and tcol < tcols

        dump_tile(tileno, trow, tcol, jpeg_tables_bytes, page.tags.tile_offsets.value[tileno], page.tags.tile_byte_counts.value[tileno])
    
    if tile_width is not None:
        assert tile_width == txsize
        assert tile_height == tysize
    else:
        tile_width = txsize
        tile_height = tysize

    outinfo.append(
        dict(
            tile_width= txsize,
            tile_length= tysize,
            image_width_orig= pxsize,
            image_length_orig= pysize,
            image_width_padded= tcols * txsize,
            image_length_padded= trows * tysize,
            image_level = zoomno,
            total_tile_count= total_tiles
            )
    )

    # each page is next higher zoom level
    zoomno += 1
    prev_page = page

infile.close()

if need_to_build_0 :
# add only if user wants to
    if add0:
      # tier 0 was missing from input image, so built it from tier 1 data
      page = outpages[0]

      pxsize, pysize, txsize, tysize, tcols, trows, jpeg_tables_bytes = get_page_info(page)

      tier1 = None

      for tileno in range(0, len(page.tags.tile_offsets.value)):
          trow = tileno / tcols
          tcol = tileno % tcols

          image = Image.open(tile_template % dict(zoomno=1, tcolno=tcol, trowno=trow, outdir=outdir, dir_name=dir_name))
  
          if tier1 is None:
            # lazily create with proper pixel data type
              tier1 = Image.new(image.mode, (tcols * txsize, trows * tysize))
  
          # accumulate tile into tier1 image
          tier1.paste(image, (tcol * txsize, trow * tysize))
  
      # generate reduced resolution tier and crop to real page size
      tier0 = tier1.resize( (txsize * tcols / 2, tysize * trows / 2), Image.ANTIALIAS ).crop((0, 0, pxsize / 2, pysize / 2))
      assert tier0.size[0] <= txsize
      assert tier0.size[1] <= tysize

      dirname = dir_template % dict(
          outdir = outdir,
          dir_name = dir_name,
          zoomno = 0 
          )
  
      if not os.path.exists(dirname):
          # create tile group dir on demand
          os.makedirs(dirname, mode=0755)
  
#MEI pdb.set_trace()
      # write final tile
      tier0.save(tile_template % dict(zoomno=0, tcolno=0, trowno=0, outdir=outdir, dir_name=dir_name), 'JPEG')
else:
    # tier 0 must be cropped down to the page size...
    page = outpages[0]
    pxsize, pysize, txsize, tysize, tcols, trows, jpeg_tables_bytes = get_page_info(page)
    image = Image.open(tile_template % dict(zoomno=0, tcolno=0, trowno=0, outdir=outdir, dir_name=dir_name))
    image = image.crop((0,0, pxsize,pysize))
    image.save(tile_template % dict(zoomno=0, tcolno=0, trowno=0, outdir=outdir, dir_name=dir_name), 'JPEG')

imageinfo=outinfo[-1]

dzi_descriptor = """\
<?xml version="1.0" encoding="UTF-8"?>
<Image TileSize="%(tile_width)d" 
       Overlap="1" 
       Format="jpg" 
       xmlns="http://schemas.microsoft.com/deepzoom/2008">
       <Size Width="%(image_width_padded)d" Height="%(image_length_padded)d"/>
</Image>
""" % imageinfo
dname= dzi_template % dict(outdir = outdir, dzi_name=dzi_name)
f = open('%s' % dname, 'w')
f.write(dzi_descriptor)
f.close

imageinfo['image_lowest_level']=lowest_level
imageinfo['data_location']=dir_name;

image_descriptor = """\
<?xml version="1.0" encoding="UTF-8"?>
<IMAGE_PROPERTIES
                  WIDTH="%(image_width_padded)d" 
                  HEIGHT="%(image_length_padded)d" 
                  NUMTILES="%(total_tile_count)d" 
                  NUMIMAGES="1" 
                  VERSION="1.8" 
                  TILESIZE="%(tile_width)d" 
                  MINLEVEL="%(image_lowest_level)d" 
                  MAXLEVEL="%(image_level)d" 
                  DATA="%(data_location)s"
/>
""" % imageinfo

iname= image_template % dict(outdir = outdir)
f = open('%s' % iname, 'w')
f.write(image_descriptor)
f.close
