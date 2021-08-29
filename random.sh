#!/bin/bash

# Generate some images
for number in {1..50}
do
   python generate.py -rp -o Output\\Random\\$(date +%Y-%m-%d_%H-%M-%S)\\"$number".png
done


