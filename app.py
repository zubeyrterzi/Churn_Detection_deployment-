from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd




app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def Home():
    return render_template('index.html')


@app.route("/predict/", methods = ["GET", "POST"])
def predict():
    model = pickle.load(open('basic_m.pkl', 'rb'))
    total_night_minutes = request.form['Total Night Minutes']
    voice_mail = request.form['Voice Mail']
    evening_charge = request.form['Total Evening Charge']
    itl_planpre = request.form['International Plan']

    if itl_planpre.lower() == 'no':
        itl_plan = 0
    elif itl_planpre.lower() == 'yes':
        itl_plan = 1

    total_day_calls = request.form['Total Day Calls']
    total_intl_charge = request.form['Total International Charge']

    list_values = [[total_night_minutes, voice_mail, evening_charge, itl_plan, total_day_calls, total_intl_charge]]

    predicted_churn = model.predict(list_values)
  

    return render_template('index.html', prediction_text = {'Customer Churn : {}'.format(predicted_churn[0])})

if __name__ == '__main__':
    app.run(debug= True)
