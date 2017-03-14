#!/bin/bash


folders=(tifffile czifile czi2tiff)

for folder in ${folders[@]}; do
	cd $folder
	python2 ./setup.py install
	cd ..
done





