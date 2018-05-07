from uszipcode import ZipcodeSearchEngine
import pandas as pd


def get_zipcode(cdf):
	
	'''
	This function fetches the latitude, longitude values 
	Uses the ZipCodeSearchEngine module to retrieve the zipcode
	
	'''

	crime_zipcodes = []
	crime_latitudes = cdf["Y"].astype(float)
	crime_longitudes = cdf["X"].astype(float)
	search = ZipcodeSearchEngine()
	for lat, lon in zip(crime_latitudes, crime_longitudes):
		try:
			zipcode = search.by_coordinate(lat, lon, radius=2)
			#     print(zipcode)
			crime_zipcodes.append(zipcode[0].Zipcode)
		except:
			print lat, lon, zipcode  
			print(len(crime_zipcodes))
	return crime_zipcodes
