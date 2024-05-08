# app.py

from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)  # Specify the template folder

# Load model
model = joblib.load('trained_model/crop_recommendation_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')  # Render the index.html template

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json.get('features')
    prediction = model.predict([data])
    return jsonify({"prediction": prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
