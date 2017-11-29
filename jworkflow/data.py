import os
import pandas as pd
from urllib.request import urlretrieve

FREMONT_URL = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"

def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL, force_download=False):
	"""Download and cache the fremont data

	Paramters
	---------
	filename : string (optional)
		location to save data
	url : string (optional)
		web location of data
	force_download : bool (optional)
		if True, force redownload of data

	Returns
	-------
	data : pandas.DataFrame
		Fremont bridge data
	"""

	if not os.path.exists(filename) or force_download:
		urlretrieve(url, filename)
	# data = pd.read_csv(filename, index_col='Date', parse_dates=True)
	data = pd.read_csv('Fremont.csv', index_col='Date')

	try:
	    data.index = pd.to_datetime(data.index, format='%m/%d/%Y %I:%M:%S %p')
	except TypeError:
	    data.index = pd.to_datetime(data.index)
	data.columns = ['West', 'East']
	data['Total'] = data['West'] + data['East']
	return data
