#!/usr/bin/env python3

from urllib.request import urlopen
from datetime import date
import csv

class Fire:
	def __init__(self, latitude, longitude, brightness, scan, track,
			acq_date, acq_time, satellite, instrument, confidence,
			version, bright_t31, frp, daynight):
		self.latitude = float(latitude)
		self.longitude = float(longitude)
		self.brightness = float(brightness)
		self.scan = float(scan)
		self.track = float(track)
		self.acq_date = date.fromisoformat(acq_date)
		self.acq_time = int(acq_time)
		self.satellite = str(satellite)
		self.instrument = str(instrument)
		self.confidence = None if confidence in ('n', 'h', 'l') else int(confidence) 
		self.version = str(version)
		self.bright_t31 = float(bright_t31)
		self.frp = float(frp)
		self.daynight = str(daynight)

class API:
	url = "https://firms.modaps.eosdis.nasa.gov"

	sources = [
		"LANDSAT_NRT",      # [US/Canada only] (LANDSAT Near Real-Time, Real-Time and Ultra Real-Time *)
		"MODIS_NRT",        # (MODIS Near Real-Time, Real-Time and Ultra Real-Time *)
		"MODIS_SP",         # (MODIS Standard Processing)
		"VIIRS_NOAA20_NRT", # (VIIRS NOAA-20 Near Real-Time, Real-Time and Ultra Real-Time *)
		"VIIRS_NOAA21_NRT", # (VIIRS NOAA-21 Near Real-Time, Real-Time and Ultra Real-Time *)
		"VIIRS_SNPP_NRT",   # (VIIRS Suomi-NPP Near Real-Time, Real-Time and Ultra Real-Time *)
		"VIIRS_SNPP_SP",    # (VIIRS Suomi-NPP Standard Processing)
	]

	countries = [
		"ABW", "AFG", "AGO", "AIA", "ALA", "ALB", "AND", "ARE", "ARG", "ARM", "ASM", "ATA", "ATF", "ATG", "AUS", "AUT",
		"AZE", "BDI", "BEL", "BEN", "BFA", "BGD", "BGR", "BHR", "BHS", "BIH", "BLM", "BLR", "BLZ", "BMU", "BOL", "BRA",
		"BRB", "BRN", "BTN", "BWA", "CAF", "CAN", "CHE", "CHL", "CHN", "CIV", "CMR", "COD", "COG", "COK", "COL", "COM",
		"CPV", "CRI", "CUB", "CUW", "CYM", "CYP", "CZE", "DEU", "DJI", "DMA", "DNK", "DOM", "DZA", "ECU", "EGY", "ERI"
		"ESP", "EST", "ETH", "FIN", "FJI", "FLK", "FRA", "FRO", "FSM", "GAB", "GBR", "GEO", "GGY", "GHA", "GIB", "GIN",
		"GLP", "GMB", "GNB", "GNQ", "GRC", "GRD", "GRL", "GTM", "GUF", "GUM", "GUY", "HKG", "HMD", "HND", "HRV", "HTI",
		"HUN", "IDN", "IMN", "IND", "IOT", "IRL", "IRN", "IRQ", "ISL", "ISR", "ITA", "JAM", "JEY", "JOR", "JPN", "KAZ",
		"KEN", "KGZ", "KHM", "KIR", "KNA", "KOR", "KOS", "KWT", "LAO", "LBN", "LBR", "LBY", "LCA", "LIE", "LKA", "LSO",
		"LTU", "LUX", "LVA", "MAC", "MAF", "MAR", "MCO", "MDA", "MDG", "MDV", "MEX", "MHL", "MKD", "MLI", "MLT", "MMR",
		"MNE", "MNG", "MNP", "MOZ", "MRT", "MSR", "MTQ", "MUS", "MWI", "MYS", "MYT", "NAM", "NCL", "NER", "NFK", "NGA",
		"NIC", "NIU", "NLD", "NOR", "NPL", "NRU", "NZL", "OMN", "PAK", "PAN", "PCN", "PER", "PHL", "PLW", "PNG", "POL",
		"PRI", "PRK", "PRT", "PRY", "PSE", "PYF", "QAT", "REU", "ROU", "RUS", "RWA", "SAU", "SDN", "SEN", "SGP", "SGS",
		"SHN", "SJM", "SLB", "SLE", "SLV", "SMR", "SOM", "SPM", "SRB", "SSD", "STP", "SUR", "SVK", "SVN", "SWE", "SWZ",
		"SXM", "SYC", "SYR", "TCA", "TCD", "TGO", "THA", "TJK", "TKM", "TLS", "TON", "TTO", "TUN", "TUR", "TUV", "TWN",
		"TZA", "UGA", "UKR", "UMI", "URY", "USA", "UZB", "VAT", "VCT", "VEN", "VGB", "VIR", "VNM", "VUT", "WLF", "WSM",
		"YEM", "ZAF", "ZMB", "ZWE"]

	def __init__(self, key):
		self.key = key

	def get_today_world_fires_by_source(self, source):
		response = urlopen(f"{self.url}/api/area/csv/{self.key}/{source}/world/1")
		lines = (line.decode('utf-8') for i, line in enumerate(response) if i > 0)
		return (Fire(* values) for values in csv.reader(lines))
	
	def get_today_fires_by_source_and_country(self, source, country):
		response = urlopen(f"{self.url}/api/country/csv/{self.key}/{source}/{country}/1")
		lines = (line.decode('utf-8') for i, line in enumerate(response) if i > 0)
		return (Fire(* values) for country, * values in csv.reader(lines))
