
COPY "Microscopy"."Box" ("ID", "Section Date", "Sample Name", "Initials", "Disambiguator", "Comment", "Tags") from stdin with csv delimiter ',' quote '"';
20131108-wnt1creZEGG-RES-0,2013-11-08,wnt1creZEGG,RES,0,"My sectioned sample returned from lab",""
20131110-wnt1creZEGG-RES-0,2013-12-01,wnt1creZEGG,RES,0,"Another of my boxes back from lab",""
20140130-wnt1creZEGG-RES-0,2014-01-30,wnt1creZEGG,RES,0,"Box from lab",""
\.

COPY "Microscopy"."Experiment" ("ID", "Experiment Date", "Experiment Description", "Initials", "Disambiguator", "Comment", "Tags") from stdin with csv delimiter ',' quote '"';
20131112-myantibody1-SV-0,2013-11-12,myantibody1,SV,0,"This is Serban's experiment",""
20131115-myantibody2-KC-0,2013-11-15,myantibody2,KC,0,"This is Karl's experiment",""
20140130-myantibody3-RS-0,2014-01-30,myantibody3,RS,0,"This is Rob's experiment",""
\.

COPY "Microscopy"."Slide" ("ID", "Box ID", "Experiment ID", "Seq.", "Rev.", "Comment", "Tags") from stdin with csv delimiter ',' quote '"';
20131108-wnt1creZEGG-RES-0-09-000,20131108-wnt1creZEGG-RES-0,20131115-myantibody2-KC-0,9,0,"under further review",""
20131108-wnt1creZEGG-RES-0-12-000,20131108-wnt1creZEGG-RES-0,20131112-myantibody1-SV-0,12,0,"using in experiment",""
20131108-wnt1creZEGG-RES-0-38-000,20131108-wnt1creZEGG-RES-0,20131112-myantibody1-SV-0,38,0,"looks interesting",""
20131108-wnt1creZEGG-RES-0-38-001,20131108-wnt1creZEGG-RES-0,,38,1,"--",""
20131108-wnt1creZEGG-RES-0-39-000,20131108-wnt1creZEGG-RES-0,20131115-myantibody2-KC-0,39,0,"--",""
20131108-wnt1creZEGG-RES-0-40-000,20131108-wnt1creZEGG-RES-0,,40,0,"--",""
20131108-wnt1creZEGG-RES-0-41-000,20131108-wnt1creZEGG-RES-0,,41,0,"--",""
20131108-wnt1creZEGG-RES-0-42-000,20131108-wnt1creZEGG-RES-0,,42,0,"--",""
20131108-wnt1creZEGG-RES-0-55-000,20131108-wnt1creZEGG-RES-0,20131115-myantibody2-KC-0,55,0,"assigned to experiment",""
20131108-wnt1creZEGG-RES-0-81-000,20131108-wnt1creZEGG-RES-0,,81,0,"--",""
20131108-wnt1creZEGG-RES-0-82-000,20131108-wnt1creZEGG-RES-0,,82,0,"--",""
20131108-wnt1creZEGG-RES-0-83-000,20131108-wnt1creZEGG-RES-0,,83,0,"--",""
20131108-wnt1creZEGG-RES-0-84-000,20131108-wnt1creZEGG-RES-0,,84,0,"--",""
\.

COPY "Microscopy"."Slide" ("ID", "Box ID", "Experiment ID", "Seq.", "Rev.", "Comment", "Tags") from stdin with csv delimiter ',' quote '"';
20131110-wnt1creZEGG-RES-0-06-000,20131110-wnt1creZEGG-RES-0,20131115-myantibody2-KC-0,6,0,"slide to be reviewed further",""
20131110-wnt1creZEGG-RES-0-12-000,20131110-wnt1creZEGG-RES-0,20131112-myantibody1-SV-0,12,0,"assigned to my experiment",""
20131110-wnt1creZEGG-RES-0-25-000,20131110-wnt1creZEGG-RES-0,,25,0,"--",""
20131110-wnt1creZEGG-RES-0-26-000,20131110-wnt1creZEGG-RES-0,,26,0,"--",""
20131110-wnt1creZEGG-RES-0-27-000,20131110-wnt1creZEGG-RES-0,,27,0,"--",""
20131110-wnt1creZEGG-RES-0-28-000,20131110-wnt1creZEGG-RES-0,,28,0,"--",""
20131110-wnt1creZEGG-RES-0-29-000,20131110-wnt1creZEGG-RES-0,20131112-myantibody1-SV-0,29,0,"slide is of interest",""
20131110-wnt1creZEGG-RES-0-29-001,20131110-wnt1creZEGG-RES-0,,29,1,"discard this one",""
20131110-wnt1creZEGG-RES-0-30-000,20131110-wnt1creZEGG-RES-0,,30,0,"--",""
20131110-wnt1creZEGG-RES-0-31-000,20131110-wnt1creZEGG-RES-0,20131115-myantibody2-KC-0,31,0,"slide needs more review",""
20131110-wnt1creZEGG-RES-0-51-000,20131110-wnt1creZEGG-RES-0,,51,0,"--",""
20131110-wnt1creZEGG-RES-0-52-000,20131110-wnt1creZEGG-RES-0,,52,0,"--",""
20131110-wnt1creZEGG-RES-0-53-000,20131110-wnt1creZEGG-RES-0,,53,0,"--",""
\.

COPY "Microscopy"."Slide" ("ID", "Box ID", "Experiment ID", "Seq.", "Rev.", "Comment", "Tags") from stdin with csv delimiter ',' quote '"';
20140130-wnt1creZEGG-RES-0-01-000,20140130-wnt1creZEGG-RES-0,20140130-myantibody3-RS-0,1,0,"slide to be reviewed further",""
20140130-wnt1creZEGG-RES-0-02-000,20140130-wnt1creZEGG-RES-0,20140130-myantibody3-RS-0,2,0,"slide to be reviewed further",""
20140130-wnt1creZEGG-RES-0-03-000,20140130-wnt1creZEGG-RES-0,20140130-myantibody3-RS-0,3,0,"slide to be reviewed further",""
20140130-wnt1creZEGG-RES-0-04-000,20140130-wnt1creZEGG-RES-0,20140130-myantibody3-RS-0,4,0,"slide to be reviewed further",""
20140130-wnt1creZEGG-RES-0-05-000,20140130-wnt1creZEGG-RES-0,20140130-myantibody3-RS-0,5,0,"slide to be reviewed further",""
20140130-wnt1creZEGG-RES-0-06-000,20140130-wnt1creZEGG-RES-0,20140130-myantibody3-RS-0,6,0,"slide to be reviewed further",""
20140130-wnt1creZEGG-RES-0-07-000,20140130-wnt1creZEGG-RES-0,20140130-myantibody3-RS-0,7,0,"slide to be reviewed further",""
20140130-wnt1creZEGG-RES-0-08-000,20140130-wnt1creZEGG-RES-0,20140130-myantibody3-RS-0,8,0,"slide to be reviewed further",""
20140130-wnt1creZEGG-RES-0-09-000,20140130-wnt1creZEGG-RES-0,20140130-myantibody3-RS-0,9,0,"slide to be reviewed further",""
20140130-wnt1creZEGG-RES-0-10-000,20140130-wnt1creZEGG-RES-0,20140130-myantibody3-RS-0,10,0,"slide to be reviewed further",""
\.

COPY "Microscopy"."Scan" ("ID", "Slide ID", "Original Filename", "GO Endpoint", "GO Path", "HTTP URL", "Filename", "File Size", "Thumbnail", "Zoomify", "Comment", "Tags") from stdin with csv delimiter ',' quote '"';
20131108-wnt1creZEGG-RES-0-09-000-000,20131108-wnt1creZEGG-RES-0-09-000,sample2.czi,cirmusc#cirm-usc,/scans/sample2/sample2.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/sample2/sample2.czi,sample2.czi,2465079520,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20131108-wnt1creZEGG-RES-0-09-000/sample2.jpeg,https://piranha.hsc.usc.edu/cirm-usc/html/20131108-wnt1creZEGG-RES-0-09-000/sample2.html,"should use this",""
20131108-wnt1creZEGG-RES-0-12-000-000,20131108-wnt1creZEGG-RES-0-12-000,sample2.czi,cirmusc#cirm-usc,/scans/sample2/sample2.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/sample2/sample2.czi,sample2.czi,2465079520,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20131108-wnt1creZEGG-RES-0-12-000/sample2.jpeg,https://piranha.hsc.usc.edu/cirm-usc/html/20131108-wnt1creZEGG-RES-0-12-000/sample2.html,"scan under review",""
20131108-wnt1creZEGG-RES-0-12-000-001,20131108-wnt1creZEGG-RES-0-12-000,sample3.czi,cirmusc#cirm-usc,/scans/sample3/sample3.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/sample3/sample3.czi,sample3.czi,12330720832,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20131108-wnt1creZEGG-RES-0-12-000/sample3.jpeg,https://piranha.hsc.usc.edu/cirm-usc/html/20131108-wnt1creZEGG-RES-0-12-000/sample3.html,"should use this one",""
20131108-wnt1creZEGG-RES-0-38-000-000,20131108-wnt1creZEGG-RES-0-38-000,sample1.czi,cirmusc#cirm-usc,/scans/sample1/sample1.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/sample1/sample1.czi,sample1.czi,1308622048,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20131108-wnt1creZEGG-RES-0-38-000/sample1.jpeg,https://piranha.hsc.usc.edu/cirm-usc/html/20131108-wnt1creZEGG-RES-0-38-000/sample1.html,"some ROIs",""
20131108-wnt1creZEGG-RES-0-38-000-001,20131108-wnt1creZEGG-RES-0-38-000,sample2.czi,cirmusc#cirm-usc,/scans/sample2/sample2.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/sample2/sample2.czi,sample2.czi,1308622048,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20131108-wnt1creZEGG-RES-0-38-000/sample2.jpeg,https://piranha.hsc.usc.edu/cirm-usc/html/20131108-wnt1creZEGG-RES-0-38-000/sample2.html,"another scan of 38",""
20131108-wnt1creZEGG-RES-0-39-000-000,20131108-wnt1creZEGG-RES-0-39-000,sample1.czi,cirmusc#cirm-usc,/scans/sample1/sample1.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/sample1/sample1.czi,sample1.czi,1308622048,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20131108-wnt1creZEGG-RES-0-39-000/sample1.jpeg,https://piranha.hsc.usc.edu/cirm-usc/html/20131108-wnt1creZEGG-RES-0-39-000/sample1.html,"more ROIs",""
20131108-wnt1creZEGG-RES-0-55-000-000,20131108-wnt1creZEGG-RES-0-55-000,sample3.czi,cirmusc#cirm-usc,/scans/sample3/sample3.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/sample3/sample3.czi,sample3.czi,12330720832,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20131108-wnt1creZEGG-RES-0-55-000/sample3.jpeg,https://piranha.hsc.usc.edu/cirm-usc/html/20131108-wnt1creZEGG-RES-0-55-000/sample3.html,"still working on this",""
\.

COPY "Microscopy"."Scan" ("ID", "Slide ID", "Original Filename", "GO Endpoint", "GO Path", "HTTP URL", "Filename", "File Size", "Thumbnail", "Zoomify", "Comment", "Tags") from stdin with csv delimiter ',' quote '"';
20131110-wnt1creZEGG-RES-0-06-000-000,20131110-wnt1creZEGG-RES-0-06-000,sample3.czi,cirmusc#cirm-usc,/scans/sample3/sample3.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/sample3/sample3.czi,sample3.czi,12330720832,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20131110-wnt1creZEGG-RES-0-06-000/sample3.jpeg,https://piranha.hsc.usc.edu/cirm-usc/html/20131110-wnt1creZEGG-RES-0-06-000/sample3.html,"found something",""
20131110-wnt1creZEGG-RES-0-12-000-000,20131110-wnt1creZEGG-RES-0-12-000,sample2.czi,cirmusc#cirm-usc,/scans/sample2/sample2.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/sample2/sample2.czi,sample2.czi,2465079520,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20131110-wnt1creZEGG-RES-0-12-000/sample2.jpeg,https://piranha.hsc.usc.edu/cirm-usc/html/20131110-wnt1creZEGG-RES-0-12-000/sample2.html,"scan under review",""
20131110-wnt1creZEGG-RES-0-29-000-000,20131110-wnt1creZEGG-RES-0-29-000,sample1.czi,cirmusc#cirm-usc,/scans/sample1/sample1.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/sample1/sample1.czi,sample1.czi,1308622048,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20131110-wnt1creZEGG-RES-0-29-000/sample1.jpeg,https://piranha.hsc.usc.edu/cirm-usc/html/20131110-wnt1creZEGG-RES-0-29-000/sample1.html,"some ROIs",""
20131110-wnt1creZEGG-RES-0-29-000-001,20131110-wnt1creZEGG-RES-0-29-000,sample2.czi,cirmusc#cirm-usc,/scans/sample2/sample2.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/sample2/sample2.czi,sample2.czi,1308622048,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20131110-wnt1creZEGG-RES-0-29-000/sample2.jpeg,https://piranha.hsc.usc.edu/cirm-usc/html/20131110-wnt1creZEGG-RES-0-29-000/sample2.html,"another scan of 29",""
20131110-wnt1creZEGG-RES-0-31-000-000,20131110-wnt1creZEGG-RES-0-31-000,sample2.czi,cirmusc#cirm-usc,/scans/sample2/sample2.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/sample2/sample2.czi,sample2.czi,2465079520,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20131110-wnt1creZEGG-RES-0-31-000/sample2.jpeg,https://piranha.hsc.usc.edu/cirm-usc/html/20131110-wnt1creZEGG-RES-0-31-000/sample2.html,"scan under review",""
\.

COPY "Microscopy"."Scan" ("ID", "Slide ID", "Original Filename", "GO Endpoint", "GO Path", "HTTP URL", "Filename", "File Size", "Thumbnail", "Zoomify", "Comment", "Tags") from stdin with csv delimiter ',' quote '"';
20140130-wnt1creZEGG-RES-0-01-000-001,20140130-wnt1creZEGG-RES-0-01-000,30-01-2014_Barcode-0737.czi,cirmusc#cirm-usc,/scans/20140130-wnt1creZEGG-RES-0-01-000/30-01-2014_Barcode-0737.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/20140130-wnt1creZEGG-RES-0-01-000/30-01-2014_Barcode-0737.czi,30-01-2014_Barcode-0737.czi,755687264,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20140130-wnt1creZEGG-RES-0-01-000/30-01-2014_Barcode-0737.jpg,https://piranha.hsc.usc.edu/cirm-usc/html/20140130-wnt1creZEGG-RES-0-01-000/30-01-2014_Barcode-0737.html,"scan under review",""
20140130-wnt1creZEGG-RES-0-02-000-001,20140130-wnt1creZEGG-RES-0-02-000,30-01-2014_Barcode-0739.czi,cirmusc#cirm-usc,/scans/20140130-wnt1creZEGG-RES-0-02-000/30-01-2014_Barcode-0739.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/20140130-wnt1creZEGG-RES-0-02-000/30-01-2014_Barcode-0739.czi,30-01-2014_Barcode-0739.czi,907742720,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20140130-wnt1creZEGG-RES-0-02-000/30-01-2014_Barcode-0739.jpg,,"scan under review",""
20140130-wnt1creZEGG-RES-0-03-000-001,20140130-wnt1creZEGG-RES-0-03-000,30-01-2014_Barcode-0743.czi,cirmusc#cirm-usc,/scans/20140130-wnt1creZEGG-RES-0-03-000/30-01-2014_Barcode-0743.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/20140130-wnt1creZEGG-RES-0-03-000/30-01-2014_Barcode-0743.czi,30-01-2014_Barcode-0743.czi,525592320,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20140130-wnt1creZEGG-RES-0-03-000/30-01-2014_Barcode-0743.jpg,https://piranha.hsc.usc.edu/cirm-usc/html/20140130-wnt1creZEGG-RES-0-03-000/30-01-2014_Barcode-0743.html,"scan under review",""
20140130-wnt1creZEGG-RES-0-04-000-001,20140130-wnt1creZEGG-RES-0-04-000,30-01-2014_Barcode-0745.czi,cirmusc#cirm-usc,/scans/20140130-wnt1creZEGG-RES-0-04-000/30-01-2014_Barcode-0745.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/20140130-wnt1creZEGG-RES-0-04-000/30-01-2014_Barcode-0745.czi,30-01-2014_Barcode-0745.czi,580849440,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20140130-wnt1creZEGG-RES-0-04-000/30-01-2014_Barcode-0745.jpg,,"scan under review",""
20140130-wnt1creZEGG-RES-0-05-000-001,20140130-wnt1creZEGG-RES-0-05-000,30-01-2014_Barcode-0776.czi,cirmusc#cirm-usc,/scans/20140130-wnt1creZEGG-RES-0-05-000/30-01-2014_Barcode-0776.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/20140130-wnt1creZEGG-RES-0-05-000/30-01-2014_Barcode-0776.czi,30-01-2014_Barcode-0776.czi,607320096,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20140130-wnt1creZEGG-RES-0-05-000/30-01-2014_Barcode-0776.jpg,,"scan under review",""
20140130-wnt1creZEGG-RES-0-06-000-001,20140130-wnt1creZEGG-RES-0-06-000,30-01-2014_Barcode-0819.czi,cirmusc#cirm-usc,/scans/20140130-wnt1creZEGG-RES-0-06-000/30-01-2014_Barcode-0819.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/20140130-wnt1creZEGG-RES-0-06-000/30-01-2014_Barcode-0819.czi,30-01-2014_Barcode-0819.czi,523799680,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20140130-wnt1creZEGG-RES-0-06-000/30-01-2014_Barcode-0819.jpg,https://piranha.hsc.usc.edu/cirm-usc/html/20140130-wnt1creZEGG-RES-0-06-000/30-01-2014_Barcode-0819.html,"scan under review",""
20140130-wnt1creZEGG-RES-0-07-000-001,20140130-wnt1creZEGG-RES-0-07-000,30-01-2014_Barcode-0820.czi,cirmusc#cirm-usc,/scans/20140130-wnt1creZEGG-RES-0-07-000/30-01-2014_Barcode-0820.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/20140130-wnt1creZEGG-RES-0-07-000/30-01-2014_Barcode-0820.czi,30-01-2014_Barcode-0820.czi,567064160,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20140130-wnt1creZEGG-RES-0-07-000/30-01-2014_Barcode-0820.jpg,,"scan under review",""
20140130-wnt1creZEGG-RES-0-08-000-001,20140130-wnt1creZEGG-RES-0-08-000,30-01-2014_Barcode-0821.czi,cirmusc#cirm-usc,/scans/20140130-wnt1creZEGG-RES-0-08-000/30-01-2014_Barcode-0821.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/20140130-wnt1creZEGG-RES-0-08-000/30-01-2014_Barcode-0821.czi,30-01-2014_Barcode-0821.czi,572666784,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20140130-wnt1creZEGG-RES-0-08-000/30-01-2014_Barcode-0821.jpg,,"scan under review",""
20140130-wnt1creZEGG-RES-0-09-000-001,20140130-wnt1creZEGG-RES-0-09-000,30-01-2014_Barcode-0823.czi,cirmusc#cirm-usc,/scans/20140130-wnt1creZEGG-RES-0-09-000/30-01-2014_Barcode-0823.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/20140130-wnt1creZEGG-RES-0-09-000/30-01-2014_Barcode-0823.czi,30-01-2014_Barcode-0823.czi,530951360,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20140130-wnt1creZEGG-RES-0-09-000/30-01-2014_Barcode-0823.jpg,,"scan under review",""
20140130-wnt1creZEGG-RES-0-10-000-001,20140130-wnt1creZEGG-RES-0-10-000,31-01-2014_Barcode-0832.czi,cirmusc#cirm-usc,/scans/20140131-wnt1creZEGG-RES-0-10-000/31-01-2014_Barcode-0832.czi,https://piranha.hsc.usc.edu/cirm-usc/scans/20140131-wnt1creZEGG-RES-0-10-000/31-01-2014_Barcode-0832.czi,31-01-2014_Barcode-0832.czi,521829856,https://piranha.hsc.usc.edu/cirm-usc/thumbnails/20140130-wnt1creZEGG-RES-0-10-000/31-01-2014_Barcode-0832.jpg,,"scan under review",""
\.

SET client_min_messages=ERROR;
VACUUM ANALYZE;

