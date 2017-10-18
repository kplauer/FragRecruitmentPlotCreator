PROJECT TITLE: frhit_frag_plot.py
PURPOSE: Produces fragment recruitment plots from FR-HIT output
DATE: October 16, 2016
HOW TO RUN: Tested using Python 3.4.0
    At command prompt run python3  frhit_frag_plot.py directory_where_samples_are
AUTHOR: Kim Lauer

ASSUMPTIONS:

Input file must be FRHIT default output format
Data should already be sorted, first by reference genome and then by ref start point
Reference Genomes must be new format and not include GI numbers

FURTHER INSTRUCTIONS:

At the command line, a directory where the samples are located is needed to run the program.  
The only files that should be in the directory are the sample files.  FR-HIT data files do 
not specify a specific extension and this script will read all files located within the 
directory regardless of file extension.  Programmed errors will appear if the format of 
the files do not match the FR-HIT output format and no plot will be produced.  However, if 
there is an encoding error (i.e. there are .jpeg files within that directory) then python errors 
will appear.  

If the correct formatted files are given the program will produce fragment plots for each reference 
genome.  While running each reference genome that is being generated will print out on the screen and 
at the very end how long it took for the program to run will be shown.  Each file will be treated as 
a separate set of data with a 1:1 between file:color on the fragment plot.        	
