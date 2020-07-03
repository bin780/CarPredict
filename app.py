import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/test')
def test1():
    return "Flask is being running here"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['GET','POST'])
def  predict():
    if request.method =='POST':
        try:
            kms = int(request.form['kms'])
            owner = int(request.form['owner'])
            year = int(request.form['year'])
            year = 2020 - year
            fuel_type = request.form['fuel_type']
            print(fuel_type)

            if fuel_type == 'petrol':
                fuel_type1 = 1
                fuel_type2 = 0
            elif (fuel_type == 'diesel'):
                fuel_type1 = 0
                fuel_type2 = 1
            else:
                fuel_type1 = 0
                fuel_type2 = 0

            seller_type = request.form['seller_type']
            print(seller_type)
            if (seller_type == 'individual'):
                seller_type = 1
            else:
                seller_type = 0

            transmission = request.form['transmission']
            print(transmission)
            if transmission == 'manual':
                transmission = 1
            else:
                transmission = 0

            price = request.form['price']

            pred = model.predict(
                np.array([price, kms, owner, year, fuel_type2, fuel_type1, seller_type, transmission]).reshape((1,-1)))

            print(np.array([price, kms, owner, year, fuel_type2, fuel_type1, seller_type, transmission]).reshape((1,-1)))
        except Exception as e:
            print(e)
            return "ERRRO !!!! SOMETHING WENT WRONG CHK YOUR INPUTS"

    return render_template('predict.html',prediction=np.round(pred[0],2))






if __name__ == "__main__":
    app.run(debug=True)

