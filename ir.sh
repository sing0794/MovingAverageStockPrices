#!/bin/bash
hadoop fs -rmr output
dumbo start MovingAverages.py -hadoop /usr/lib/hadoop -input input -output output 
dumbo cat output/part-00000 -hadoop /usr/lib/hadoop > output.txt

