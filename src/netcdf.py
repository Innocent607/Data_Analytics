from netCDF4 import Dataset
import numpy as np
import pandas as pd


# data variables
lat = data.variables['Y'] # latitude {lat.standard_name}
lon = data.variables['X'] # longitude {lon.standard_name}
rainfall = data.variables['precipitation'] # longitude {rainfall.standard_name}


# accessing data from data variables
lat = data.variables['Y'][:]
lon = data.variables['X'][:]
rainfall = data.variables['precipitation'][:]

#we would like to get weather conditions around palapye region
palapye_lon = 22.5515
palapye_lat = 27.1147

radius = 10 # 10m radius

# a function to compute the difference between the desired location
# and the data point location
def sqrt(self)
	self.sqr_diff_lon = (palapye_lon - lon)**2
	self.sqr_diff_lat = (palapye_lat - lat)**2
	
	#return sqr_diff_lat, sqr_diff_lon
'''
def min_value(self):
	pal_lat = [] # palapye data in the latitude
	pal_lon = [] # palapye data in the longitude
	if self.sqr_diff_lat < radius:
		if self.sqr_diff_lon < radius:
			pal_lat.append(self.sqr_diff_lat.argmin()) #stpre data
			pal_lat.append(self.sqr_diff_lat.argmin())
	return pal_lat, pal_lon
'''	

def get_file():
	years = []
	for file in glob.glob('*.nc'):
		print(file)
		data = Dataset(file, 'r')
		time = data.variables['T']
		year = p
		return years.append(year)
		
		
data = {'Year':[data.variables['T'].units[11:21]],
		'Longitude': [data.variables['X'][:]]
		'Latitude': [data.variables['Y'][:]]
		'Precipitation': [data.variables['precipitation'][:]]}
df = pd.DataFrame(data)

