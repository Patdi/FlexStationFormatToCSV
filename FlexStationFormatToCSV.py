i#!/usr/bin/env python3

#Converts a Molecular Devices FlexStation 3 Microplate Reader .csv file to a easier to use format
#On the command line run: cat "your_file".csv | FlexStationFormatToCSV.py > "your_output".csv
#If you use the wildcard * you can run it on all your files at once

import re
import sys

def pretty_print(start_idx, plate_name, well_co, absorbance, temp, wave):
    for i in range(len(well_co)):
        print(
            f"{start_idx + i},{plate_name},{well_co[i]},{absorbance[i]},{temp},{wave}"
        )

n = 0 
abs_row = 0
sample = 1
wbool = False
wpos = 0 

print("Sample, Plate, Well, Absorbance, Temperature, Wavelenght")

for raw_line in sys.stdin:
    line = raw_line.strip()
    if re.search(r"##BLOCKS=", line):
        block = line.split(",")[0].split(" ")[1]
    elif not line.replace(",", "").rstrip():
        continue
    elif re.search(r"Plate:", line):
        plate = line.split(",")[1]
        wavelenght = line.split(",")[15].split(" ")
        if len(wavelenght) >= 2:
            wbool = True
    elif re.search(r"Temperature", line):
        well = line.split(",")[2:]
        abs_row = n + 1
    elif abs_row != 0 and abs_row == n:
        temperature = line.split(",")[1]
        absorbances = line.split(",")[2:]
        pretty_print(sample, plate, well, absorbances, temperature, wavelenght[wpos])
        sample += len(well)
        wpos += 1
    elif wbool is True and re.search(re.escape(temperature), line):
        temperature = line.split(",")[1] 
        absorbances = line.split(",")[2:]
        pretty_print(sample, plate, well, absorbances, temperature, wavelenght[wpos])
        sample += len(well)
        wpos += 1
    elif re.search(r"~End", line):
        wpos = 0

    n += 1