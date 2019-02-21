#!/usr/bin/python
#- * -coding: utf - 8 - * -
#Author: Ian A. Wardell
#Description: This script intakes a.csv file and outputs the first 5 columns into a.txt file
import argparse
import csv
import os
import time

# collect user input
parser = argparse.ArgumentParser(description = 'Input .csv file')
parser.add_argument('-f', "--file", required = True,
    help = 'a .csv file to be processed, use -f <filename.csv> ')

args = vars(parser.parse_args())

print "Input File %s" % args["file"]
current_time = time.strftime("%m-%d-%y-%H:%M", time.localtime())


# create directory output
output_path = "%s-output" % current_time
os.mkdir(output_path)
pathName = args["file"]
file = open(pathName, 'rU')
reader = csv.reader(file, delimiter = ',')

## loop
filenumberian = 0
for row in reader:
	# create each output file, set name to the content in the title column
	output_file_name = output_path + "/%d_%s_%s.txt" % (filenumberian,row[0], row[3])
	filenumberian += 1
	output_file = open(output_file_name, 'ab+')
	output_file.write(row[0] + "\n")
	output_file.write(row[1] + "\n")
	output_file.write(row[3] + "\n")#[last]
	output_file.write(row[4] + "\n")#[district]
	output_file.write(row[5] + "\n")#[state]
	output_file.write(row[6] + "\n")#[party]
	output_file.write(row[7] + "\n")#[title]
	output_file.write(row[8] + "\n")#[link]
	output_file.write(row[11] + "\n")#[date]
	output_file.write(row[10] + "\n")#[cleantext]
	output_file.write(row[12] + "\n")#[tone]
	output_file.write(row[14] + "\n")#[Political / regular]
	output_file.write(row[15] + "\n")#[Counter - majoritarian]
	output_file.write(row[16] + "\n")#[Democratic process]
	output_file.close
print "Output location is the directory %s" % output_path
