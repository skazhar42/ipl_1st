import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = ['Mat_t20', 'Inns_t20', 'NO_t20', 'HS_t20', 'Ave_t20', 'SR_t20',
       '4s_t20', '6s_t20', 'Runs_t20', '100s_t20', '50s_t20', '0s_t20',
       'Mat_odi', 'Inns_odi', 'NO_odi', 'HS_odi', 'Ave_odi', 'SR_odi',
       '4s_odi', '6s_odi', 'Runs_odi', '100s_odi', '50s_odi', '0s_odi',
       'year']
    req_features = ['Mat_t20','Ave_t20', 'SR_t20','Runs_t20', '100s_t20', '50s_t20','year']
    int_features = [int(x) for x in request.form.values()]
    int_dic={}
    for feature,value in  zip(req_features,int_features):
        int_dic[feature]=value
    input=[]
    for feature in features:
        if feature in int_dic:
            if feature !='year':
                input.append(int_dic[feature])
            else:
                input.append(int_dic[feature]-2016)
        elif feature=='Inns_t20':
            input.append(int_dic['Mat_t20'])
        else:
            input.append(0)
    final_features = [np.array(input)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text='Player cost should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)