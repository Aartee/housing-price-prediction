def apply_model(model):
	y_pred = model.predict(X_test)
 	# plt.plot( y_test, y_test,  color='black')
 	# plt.scatter( y_test, y_pred, color='blue', linewidth=3)

	# # plt.xticks(())
	# # plt.yticks(())
	# plt.xlabel('actual prices')
	# plt.ylabel('predicted prices')
	# plt.show(

	mse = mean_squared_error(y_test,y_pred)
	mae = metrics.median_absolute_error(y_test, y_pred)
	return mse, mae

def train_model(X_train,y_train):
		params = {'n_estimators': 300, 'max_depth': 4, 'min_samples_split': 2,'learning_rate': 0.2, 'loss': 'ls'}
		clf = ensemble.GradientBoostingRegressor(**params)
		clf.fit(X_train, y_train)