import math
import pandas as pd
from zipcode_generator import get_zipcode

from data_preprocess import *


def prepare_crime_data():
	'''
	This function reads the csv file on the disk as a pandas Dataframe
	Transforms the dataset into set of features based on crime category
	'''
	print "Reading the dataset"
	df = pd.read_csv('/Users/aarteekasliwal/Documents/255-David/Project/src_pavana/2018_sfo_crime.csv')
	print "Done"
	'''
	It fetches the Category and the latitude, longitude values
	Maps the Location with zipcode
	'''
	print "Calculating the zipcode"
	cdf = df[['Category', 'X','Y']]
	cdf['zipcode'] = get_zipcode(cdf)
	cdf = cdf.drop(['X','Y'], axis=1)
	print "Done"
	'''
 	The data now contains records with different combinations of 
	zipcode and crime category. These rows are grouped by zipcode,
	the count of categories are aggregated for each group.	
	'''
	print "Transforming dataset"
	df = pd.DataFrame({'count' : cdf.groupby( [ "zipcode", "Category"] ).size()}).reset_index()

	print "Done"
	'''
	The resultant dataset now is transformed into another dataframe where
	the counts of crime are on the axis 0.
	'''
	pdf = df.pivot(index = 'zipcode',columns='Category', values='count').reset_index()
	'''
	The dataset now needs to be mapped for NaN values. 
	'''
	pdf = map_nan(pdf)
	'''
	Persisting the dataset on the disk for future use
	'''
	# pdf.to_csv('2018_crime_counts_grouped.csv')
	# print "Written to file 2018_crime_counts_grouped.csv"
	# return '2018_crime_counts_grouped.csv'
	return pdf



def prepare_housing_data():
	'''
	This functions reads the housing dataset
	aggregates the price values for last one year
	associates the price value with zipcode
	returns the dataframe
	'''
	print "Reading housing dataset"
	zdf = pd.read_csv('/Users/aarteekasliwal/Documents/255-David/Project/src_pavana/Zip/Zip_Zhvi_AllHomes.csv')
	print "Done"

	print "Transforming the dataset"
	sfo_1b_df = zdf[zdf['City'] == 'San Francisco']
	sfo_1b_df = sfo_1b_df[['RegionName','2017-03','2017-04','2017-05',\
							'2017-06','2017-07','2017-08','2017-09',\
							'2017-10','2017-11','2017-12','2018-01']]
	zipcode_ = sfo_1b_df['RegionName']
	sfo_1b_df.drop(['RegionName'], inplace=True, axis=1)
	mean = sfo_1b_df.mean(axis=1)
	new_df = pd.DataFrame({'zipcode':zipcode_, 'Mean_Price': mean})
	print "Done"

	return new_df



def merge_datasets(cdf_norm, new_df):
	print "Merging the dataset"
	mdf = cdf_norm.merge(new_df,left_on='zipcode', right_on='zipcode', how='inner')
	mdf.drop(['zipcode'], inplace=True, axis=1)
	print "Done"
	return mdf