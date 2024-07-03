#!/usr/bin/env python3

from urllib.request import urlopen
import csv

BASE_URL = "https://firms.modaps.eosdis.nasa.gov"
MAP_KEY = "578c2b66d72914caba3c666be9d942be"

def get_today_data_by_source(source):
	return urlopen(f"{BASE_URL}/api/area/csv/{MAP_KEY}/{source}/world/1").read()

stream = get_today_data_by_source("MODIS_NRT")
print(stream)
csv_stream = csv.reader(stream)

for line in csv_stream:
	print(line)
