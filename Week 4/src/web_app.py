from flask import Flask, request, jsonify, render_template, redirect, url_for
import joblib
import numpy as np

app = Flask("CO Prediction Web App")
model = joblib.load('../model/linear_regressor_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        float_features = [float(x) for x in request.form.values()]
        final_features = [np.array(float_features)]
        predicted_result = model.predict(final_features)

        # Redirect to the results page with the calculated prediction
        return redirect(url_for('results', prediction=predicted_result[0]))
    else:
        # If the method is GET, render the input form template
        return render_template('index.html')

@app.route('/results', methods=['GET'])
def results():
    # Get the prediction value from the URL parameter
    prediction = request.args.get('prediction')

    return render_template('results.html', prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)