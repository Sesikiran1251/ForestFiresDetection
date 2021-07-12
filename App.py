import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
model = pickle.load(open('model_.pkl', 'rb'))
@app.route('/')
def prediction():
    return render_template('prediction.html')


@app.route('/predict',methods=['POST'])
def predict():
    int_features=[]
    
    X=request.form['x-axis']
    int_features.append(float(X))
    Y=request.form['y-axis']
    int_features.append(float(Y))
    month=request.form['month']
    int_features.append(float(month))
    day=request.form['day']
    int_features.append(float(day))
    ffmc=request.form['ffmc']
    int_features.append(float(ffmc))
    dmc=request.form['dmc']
    int_features.append(float(dmc))
    dc=request.form['dc']
    int_features.append(float(dc))
    isi=request.form['isi']
    int_features.append(float(isi))
    temperature=request.form['temperature']
    int_features.append(float(temperature))
    rh=request.form['rh']
    int_features.append(float(rh))
    wind=request.form['wind']
    int_features.append(float(wind))
    rain=request.form['rain']
    int_features.append(float(rain))
    print(int_features)
    final_features=[np.array(int_features)]
    print(final_features)
    prediction = model.predict(final_features)
    print(prediction)

    output = float(prediction)
    #print(output)
    #return 0;
    if(output>0):
        return render_template('prediction.html', prediction_result=' OCCURENCE OF FIRE')
    else:
        return render_template('prediction.html',prediction_result='NO OCCURENCE OF FIRE')
    '''if((output>0) and (output<=50)):
        return render_template('prediction.html', prediction_result='Medium Burned Area')
    
    elif((output>50) and (output<=100)):
        return render_template('prediction.html', prediction_result='High Burned Area')
    
    elif output>100:
        return render_template('prediction.html', prediction_result='Very High Burned Area')
    
    else:
        return render_template('prediction.html', prediction_result='No Burned Area')
'''

if __name__=="__main__":
    app.run(debug=True)
