from prepare_data import *
from data_preprocess import preprocess

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import ShuffleSplit


import sklearn.grid_search
from sklearn import linear_model, decomposition
from sklearn.model_selection import GridSearchCV

from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.model_selection import KFold


import seaborn as sns

from matplotlib import pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error
from sklearn import metrics
import numpy as np

from sklearn import ensemble
from sklearn import linear_model
from sklearn.grid_search import GridSearchCV
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
import sklearn.metrics as metrics
import matplotlib.pyplot as plt

class Model(object):
	def __init__(self):
		self.train = None
		self.target = None
		self.clf = None
		self.cdf = None
		self.hdf = None
		self.X_train = None
		self.y_train = None
	
	def start(self):
		cdf = prepare_crime_data()
		self.hdf = prepare_housing_data()
		self.cdf = preprocess(cdf)
		mdf = merge_datasets(self.cdf,self.hdf)
		self.train = mdf.drop(['Mean_Price'], axis=1)
		self.target = mdf.Mean_Price
		return
		
	def split_train_test(self):
		self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.train, self.target, test_size=0.2, random_state=10)
		return

	def train_model(self):
		params = {'n_estimators': 300, 'max_depth': 4, 'min_samples_split': 2, 'learning_rate': 0.2, 'loss': 'ls'}
		self.clf = ensemble.GradientBoostingRegressor(**params)
		self.clf.fit(self.X_train, self.y_train)
		return
	
	def grid_Search(self):
		rs = 1
		ests = [ linear_model.LinearRegression(), linear_model.Ridge(),
		        linear_model.Lasso(), linear_model.ElasticNet(),
		        linear_model.BayesianRidge(), linear_model.OrthogonalMatchingPursuit(), ensemble.GradientBoostingRegressor() ]
		ests_labels = np.array(['Linear', 'Ridge', 'Lasso', 'ElasticNet', 'BayesRidge', 'OMP','GradientBoostRegressor'])
		errvals = np.array([])

		
		for e in ests:
		    e.fit(self.X_train, self.y_train)
		    this_err = mean_squared_error(self.y_test, e.predict(self.X_test))
		    #print"got error %0.2f" % this_err
		    errvals = np.append(errvals, math.sqrt(this_err))

		pos = np.arange(errvals.shape[0])
		srt = np.argsort(errvals)
		plt.figure(figsize=(12,10))
		plt.bar(pos, errvals[srt], align='center')
		plt.xticks(pos, ests_labels[srt])
		plt.xlabel('Estimator')
		plt.ylabel('Root Mean Square Error')
		plt.show()

		return
	
	def get_rows(self, val):
		row = self.cdf.loc[self.cdf['zipcode'] == val]
		return row.drop(['zipcode'], axis=1)

	def predict(self,val):
		row = self.get_rows(val)
		predicted_price = self.clf.predict(row)
		return predicted_price 