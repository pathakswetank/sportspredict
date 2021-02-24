import numpy as np
import pandas as pd
from flask import Flask, request,render_template
import pickle
import json

app= Flask(__name__)


@app.route('/')
def home():
    return render_template('Sports.html')

# prediction function 
def ValuePredictor(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1, 9) 
    loaded_model = pickle.load(open("sport.pkl", "rb")) 
    result = loaded_model.predict(to_predict) 
    return result[0] 
  
@app.route('/result', methods = ['POST']) 
def result(): 
    if request.method == 'POST': 
        _json = request.data
        data_dict = json.loads(_json)
        to_predict_list = list(data_dict.values())
        predict_input_feature = [int(v) for v in to_predict_list]
        result = ValuePredictor(predict_input_feature)         
        if int(result)== 1: 
            prediction ='Endurance Sports'
        else: 
            prediction ='Anaerobic Sports'            
        #return render_template("result.html", prediction = prediction) 
        return{"prediction":prediction} 
if __name__ == "__main__":
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
