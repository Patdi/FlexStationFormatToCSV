#!/usr/bin/env python2.7

#Converts a Molecular Devices FlexStation 3 Microplate Reader .csv file to a easier to use format
#On the command line run: cat "your_file".csv | FlexStationFormatToCSV.py > "your_output".csv
#If you use the wildcard * you can run it on all your files at once

import re
import sys

def pretty_print(s, plate_name, well_co, absorbance, temp, wave):
	for i in range(len(well_co)):
		print str(s+i) + "," + str(plate_name)  + "," + str(well_co[i])  + "," + str(absorbance[i]) + "," + str(temp) + "," + str(wave)
	
n = 0 #current line number
abs_row = 0 #line number of abs row
sample = 1 #sample number
wbool = False #More one wavelenght
wpos = 0 #position in list of wavelenght

#header
print "Sample, Plate, Well, Absorbance, Temperature, Wavelenght"

#parse file, when key words found, split line on comma
for raw_line in sys.stdin:
	line = raw_line.strip()
	#block number
	if re.search('##BLOCKS=', line):
		block = line.split(",")[0].split(" ")[1]
	elif line.replace(",","").rstrip() == False:
		continue
	#time
	elif re.search('Plate:', line):
		#plate = line.split(",")[1].replace("t","")
		plate = line.split(",")[1]
		#wavelenght list
		wavelenght = line.split(",")[15].split(" ")
		if len(wavelenght) >= 2:
			wbool = True
	#well nums and find first abs_row
	elif re.search('Temperature', line):
		well = line.split(",")[2:]
		abs_row = n + 1 
	#temperature
	elif abs_row != 0 and abs_row == n:
		temperature = line.split(",")[1]
		abs = line.split(",")[2:]
		pretty_print(sample, plate, well, abs, temperature, wavelenght[wpos])
		sample = sample + len(well)
		wpos += 1
	elif wbool == True and re.search(temperature, line):
		temperature = line.split(",")[1]# prob delete later
		abs = line.split(",")[2:]
		pretty_print(sample, plate, well, abs, temperature, wavelenght[wpos])
		sample = sample + len(well)
		wpos += 1
	#end of record print
	elif re.search('~End', line):
		temp_bool = False
		wpos = 0
	n += 1
