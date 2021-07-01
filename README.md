# FlexStationFormatToCSV
Converts a Molecular Devices FlexStation 3 Microplate Reader .csv file to a easier to use format

The output from the Microplate reader places each plate in a separate block
Ex:

##BLOCKS= 10		
Plate:	Row13_DMI_t0	1.3
	Temperature(¡C)	A1
	24.5	-0.004283333
		
	24.5	-0.002208333
		
~End		
Plate:	Row13_QoI_t0	1.3
	Temperature(¡C)	A1
	24.5	0.1707
		
	24.5	0.1259

FlexStationFormatToCSV.py coverts this horizontal format to one with 5 columns
Ex:

Sample, TimePoint, Well, Coordinate, Absorbance
1,0,A1,0.022333333
2,0,A2,-0.031166667
3,0,A3,0.031933333
4,0,A4,0.005733333
5,0,A5,0.037733333
6,0,A6,-0.005766667
7,0,A7,0.003733333
8,0,A8,0.038033333
9,0,A9,0.001633333

#Sample, TimePoint, Well, Coordinate, Absorbance
#On the command line run: cat "your_file".csv | FlexStationFormatToCSV.py > "output".csv
#If you use the wildcard * you can run it on all your files at once

Expected input format in test_file.csv
Expected output format in test_output.csv
