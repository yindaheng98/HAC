#!/bin/bash
mkdir -p HAC
for video in `ls outputs`; do
  folder="outputs/$video/frame1/0.004"
  echo "Processing $folder"
  cp $folder/outputs.log HAC/$video.outputs.log
  cp $folder/results.json HAC/$video.results.json
done
