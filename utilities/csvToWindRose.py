# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 12:21:41 2022

@author: Arnav

DESCRIPTION:
Reads in raw wind data and creates a frequency table based on:
    - wind direction (0-359 degrees, 1 degree increments) 
    - wind speed (0-max wind speed, 1 m/s incremenets)
This frequency table is used as the input file for the FLORIS
simulator and is also used to generate the wind rose plot.
"""

import csv
import pandas as pd

windDataFile = "WIND_DATA.csv"
windRoseFile = "BLANK_WIND_ROSE.csv"

windData = open(windDataFile,"r")
windDataRead = csv.reader(windData)

windRose = pd.read_csv(windRoseFile)

for row in windDataRead:
    # If there is no wind data in the current row, quietly continue reading the data in the next row
    # This is done just in case some data is missing from the dataset which would cause the code to throw an error.
    try:
        direction = round(float(row[0]))
    except:
        continue
    try:
        speed = round(float(row[1]))
    except:
        continue
    
    index = speed * 360 + direction
    currentData = windRose.iat[index,2]
    windRose.iat[index,2] = currentData + 1

windRose.to_csv(windRoseFile,index=False)