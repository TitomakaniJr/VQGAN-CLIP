#!/bin/bash
# The timestamp which will be used as the output directory name for all the random images 
TIMESTAMP=`date +%Y-%m-%d_%H-%M-%S`

# Generate some images
for number in {1..50}
do
   python generate.py -rp -o Output\\Random\\"$TIMESTAMP\\$number".png -s 512 288 -os 1920 1080 -ppfn
done


