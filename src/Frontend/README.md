# Estimation of Housing Prices

This project intends to find correlations of the criminal incidents with the house values and predict the going rate for a particular house based on the crime zone or zip code. We have used San Francisco police department incidents dataset for criminal reports and Zillow’s house value index dataset for San Francisco house values. The criminal records dataset contains all of the San Francisco’s zip codes and associated crime reports. On the other hand, the Zillow dataset has a limited set of listings in San Francisco. In this prototype, we plan to use the Zillow’s dataset for training the module and test the model with listings from other agencies like Redfin and compare the prices.

The front-end has been developed using nodejs, expressjs and backend in python flask, python notebooks.

## Environment setup
* Install the project requirements:
  pip install -r requirements.txt
* Run the backend application (localhost:5000) as: 
  export FLASK_APP=python-backend.py
  flask run
* Start the front end user interface (localhost:9000) as:
* Enter the house address and then click on Get Estimate Price button to get the estmted housing price.
* The prediction for the given address will be displayed based on GradientBoostRegressor technique in the data mining:

