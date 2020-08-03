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

palapye_lon = 22.5515
palapye_lat = 27.1147


def sqrt(self)
	sqr_diff_lon = (pal_lon - lon)**2
	sqr_diff_lat = (pal_lat - lat)**2
	
	return sqr_diff_lat, sqr_diff_lon
	
years = []
def get_file():
	for file in glob.glob('*.nc'):
		print(file)
		data = Dataset(file, 'r')
		time = data.variables['T']
		year = p
		years.append(year)
		
data = {'Year':[data.variables['T'].units[11:21]],
		'Longitude': [data.variables['X'][:]]
		'Latitude': [data.variables['Y'][:]]
		'Precipitation': [data.variables['precipitation'][:]]}
df = pd.DataFrame(data)

