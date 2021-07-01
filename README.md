# FlexStationFormatToCSV
Converts a Molecular Devices FlexStation 3 Microplate Reader .csv file to a easier to use format

The output from the Microplate reader places each plate in a separate block. Ex:  

Plate:	Row13_DMI_t0	1.3  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Temperature(C)	A1  
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;24.5	-0.004283333  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 24.5	-0.002208333  
		
~End  
Plate:	Row13_QoI_t0	1.3  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Temperature(C)	A1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 24.5	0.1707  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;24.5	0.1259  

FlexStationFormatToCSV.py coverts this horizontal format to one with 5 columns. Ex:

Sample, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TimePoint, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Well, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Coordinate, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Absorbance  
1,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A1,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.022333333  
2,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A2,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-0.031166667  

Sample, TimePoint, Well, Coordinate, Absorbance  
On the command line run: cat "your_file".csv | FlexStationFormatToCSV.py > "output".csv  
If you use the wildcard * you can run it on all your files at once  

Expected input format in test_file.csv  
Expected output format in test_output.csv  
