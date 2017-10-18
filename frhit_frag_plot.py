#!/usr/bin/env python3
# Kim Lauer (klauer2)
# Date: 12/08/16 v.4
# Part of Final Project
#
# Assumptions:
# Input file must be FRHIT default output format
# Data is already sorted, first by reference genome and then by ref start point
# Reference Genomes must be new format and not include GI numbers
 
import re
import glob
import argparse
from datetime import datetime
import matplotlib
# stackflow answer to error otherwise "TclError..." when run in Dockerfile
# https://stackoverflow.com/questions/4931376/generating-matplotlib-graphs-without-a-running-x-server
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# stores fr-hit default output 
class Sample(object):
    def _init_ (self, y_coord=None, ref=None, x_coord=None):
        self.y = None
        self.ref = None
        self.x = None

# variables
error_check = False

# storage for frhit data
dataList = []
# master list of ref genomes, used in plotting
refGenList = []
        
# Creates master reference list for plotting
def ref_plots(ref_genome, line):
    if ref_genome not in refGenList:
        refGenList.append(ref_genome)

# file_name - frhit default format output file.  Will not work with psl or sam format
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file_name', required=True, help="Required - Frhit default format output file with path")
args = parser.parse_args()
file_name = args.file_name

# determing how long program runs
startTime = datetime.now()

file_open = open(file_name)

line_count = 0
reads_matched = 0
# parses lines and stores in a list of objects
for line in file_open:
    x = []
    y = []
    try:
        # default format of frhit results
        t = re.search(r'\t.*\t.*\t.*\t.*\t.*\t(.*)%\t(.*)\t(.*)\t(.*)', line)            
        percent = float((t.group(1).rstrip()))
        percentID = round(percent)
        ref_genome = t.group(2).rstrip() 
        start = t.group(3).rstrip()
        stop = t.group(4).rstrip()         
    except AttributeError:
        print("Format of line did match FR-HITs default output format, please check your files")
        print("File name: " + file_name + " at line " + str(line_count))
        print(line)
        error_check = True
        break
    # stores (x,y) coordinates
    y.append(float(percentID))
    y.append(float(percentID))
    x.append(float(start))
    x.append(float(stop))
    # Ref Genome checked to see if it is unique and write to stat file 
    ref_plots(ref_genome, line)
    # creates object and stores data as objects
    z = Sample()
    z.x_coord = x
    z.ref = ref_genome
    z.y_coord = y
    # adds data to list
    dataList.append(z)
    line_count += 1
file_open.close()

num_of_refgenomes = len(refGenList)

# labels to be used on all plots
plt.xlabel("Matching Positions on Reference Genome")
plt.ylabel("Percent Identity") 

# creates fragment recruitment plot using matplotlib
if (error_check==False):
    # each plot stored as .jpeg 
    while num_of_refgenomes > 0:
        # a reference genome is removed from master list
        to_plot = refGenList.pop()
        # kept for user to see program progressing 
        # print(to_plot)
        # x,y coordinates determined by data read in.  For sparsely populated
        # plots, data may not been seen if x-axis was entire length of genome
        min_x = 100000000000
        max_x = 1
        min_y = 100
        max_y = 100
        seqList = []
        q = 0
       # obtaining data from dataList
        for p in dataList:
            # Plotting one reference genome at a time
            if (p.ref == to_plot):
                # finding x,y coordinates
                for t in p.x_coord:
                    if(min_x > t):
                        min_x = t
                    if(max_x < t) & (t != min_x):
                        max_x = t
                for t in p.y_coord:
                    if(min_y > t):
                        min_y = t           
                plt.plot(p.x_coord, p.y_coord, 'b')
                # once used data removed
                dataList.remove(p)
        # plotting x,y coordinates
        plt.xlim(min_x, max_x)
        plt.ylim(min_y, max_y)
        # Name of Reference Genome is used as title 
        plt.title(to_plot)
        # files named by stat file name + .jpeg
        name_of_file = to_plot + '.jpeg'
        plt.savefig(name_of_file)
        # plt.close() kept matlibplot from hanging up
        plt.close()
        num_of_refgenomes -= 1

print(datetime.now() - startTime)

