
#
# Copyright 2017 University of Southern California
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
#

from distutils.core import setup

setup(
    name="czi2tiff",
    description="CZI to TIFF pyramidal tile converter",
    version="0.1-prerelease",
    scripts=[
        "czi2tiff.py",
    ],
    requires=["numpy", "scipy", "tifffile", "czifile"],
    maintainer_email="torin.gerhart@cammlab.org",
    license='(new) BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ])

