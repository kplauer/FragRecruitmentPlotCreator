PROJECT TITLE: 
frhit_frag_plot.py

PURPOSE: 
Produces fragment recruitment plots from a FR-HIT output file

DATE: December 8th, 2016

HOW TO RUN: Tested using Python 3.4.0
    $run python3  frhit_frag_plot.py fr_hit_defaultoutputfile

AUTHOR: Kim Lauer

FURTHER INSTRUCTIONS:

Input file must be FRHIT default output format
FR-HIT Output file should already be sorted, first by reference genome and then by ref start point
Reference Genomes must be new format and not include GI numbers
X and Y coordinates determined by data read in so sparsely mapped genomes don't appear to be empty    	
