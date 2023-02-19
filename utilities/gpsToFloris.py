# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 15:16:21 2022

@author: Arnav

DESCRIPTION:
Converts GPS coordinates given in raw wind data into 
Cartesian coordinates with meters. The outputted 
x coordinates and y coordinates are added to the FLORIS
simulator and represent the relative locations of wind
turbines in the wind farm.
"""

import csv

locationDataFile = "LOCATION_DATA.csv"

locationData = open(locationDataFile,"r")
locationDataRead = csv.reader(locationData)

gpsCoords = [list(map(float, i)) for i in locationDataRead]

originX, originY = gpsCoords[0][0], gpsCoords[0][1]

xCoords = [0]
yCoords = [0]

for i in range(1, len(gpsCoords)):
    x, y = gpsCoords[i][0], gpsCoords[i][1]
    dx = round((x - originX) * 111139, 2) # There are approx. 111,139 meters in one degree of longitude
    dy = round((y - originY) * 111139, 2) # There are approx. 111,139 meters in one degree of latitude
    xCoords.append(dx)
    yCoords.append(dy)
    
print("Converted x coordinates: ")
print(xCoords)

print("Converted y coordinates: ")
print(yCoords)    

    