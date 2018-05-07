from sklearn import preprocessing
import math


def normalize(df):
	'''
	This function makes a copy of the dataset
	Normalizes the column values using Min-Max technique
	'''

	result = df.copy()
	for feature_name in df.columns:
		max_value = df[feature_name].max()
		min_value = df[feature_name].min()
		result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
	return result

def preprocess(pdf):
	'''
	In order to normalize the features, zipcode is removed
	zipcode is a nominal value and need not be normalized
	'''
	cdf_zipcodes = pdf['zipcode']
	pdf.drop(['zipcode'], inplace=True, axis=1)
	pdf = normalize(pdf)
	'''
	The zipcode is added back to the dataset again
	'''
	pdf['zipcode'] = cdf_zipcodes
	return pdf

def function(data):

	'''
	This function maps the values NaN : 0 and Entries : 1

	'''

	if math.isnan(float(data)):
		return 0
	else:
		return int(data)

def map_nan(pdf):
	
	'''
	Uses Map function to map the array values of the columns
	for the pandas dataset

	'''
    
	for c in pdf.columns.values:
		pdf[c] = map(function, pdf[c])
	return pdf

