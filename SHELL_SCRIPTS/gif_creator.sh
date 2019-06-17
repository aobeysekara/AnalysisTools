#!/bin/bash
#newest multiphase 

read -p 'AVI file: ' avi 
read -p 'output GIF filename: ' gif 
echo "creating gif $gif.gif using $avi" 

T="$(ffprobe -i $avi -show_entries format=duration -v quiet -of csv="p=0")"

ffmpeg -i $avi -t $T out%02d.gif
gifsicle --delay=10 --loop out%02d.gif > $gif.gif

