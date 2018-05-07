from flask import Flask, request, json, render_template
import sys  
sys.path.append("/Users/aarteekasliwal/Documents/255-David/Project/src_pavana/src")

from main import *
app = Flask(__name__, template_folder='templates')

obj = Model()
obj.start()
obj.split_train_test()
obj.train_model()
obj.predict(int(94104))

@app.route('/', methods=['GET'])
def ping():
    return render_template('price-prediction.html')
    
@app.route('/getPredictedPrice', methods=['POST', 'GET'])
def getPredictedPrice():
    if request.method == 'POST':
        result = request.form
        print(result)
        resultDict = dict(result)
        for _, value in resultDict.items():
            address = value[0]
            zipcode = int(address[-6:])
            predicted_price = obj.predict(int(zipcode))

        return render_template("price-prediction.html", result = {"Estimated Price is     ": predicted_price[0]})

if __name__ == '__main__':
    app.run(debug = True)

