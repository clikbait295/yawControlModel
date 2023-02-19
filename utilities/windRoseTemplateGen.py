# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 12:23:29 2022

@author: Arnav
DESCRIPTION:
Generates a blank wind rose frequency table file for csvToWindRose.py to use.
"""
import csv

# Use Microsoft Excel to find the maximum wind speed in the raw data.
maxWindSpeed = 0 # Must be an integer, be sure to round up!
windRoseFile = "BLANK_WIND_ROSE.csv"

with open(windRoseFile, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ws", "wd", "freq_val"])
    for windSpeed in range(0, maxWindSpeed + 1): # Add 1 to maxWindSpeed so the loop includes the maxWindSpeed
        for windDirection in range(0,360):
            writer.writerow([windSpeed, windDirection, 0])