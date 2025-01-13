# stock-movement-mini-project-
from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load dataset
data = pd.read_csv('datast.csv')

# Features
features = ['Open', 'High', 'Low', 'Volume']
X = data[features]
# Target variable (Price Change: 1 if High > Open, else 0)
y = (data['High'] > data['Open']).astype(int)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Decision Tree model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the form
        open_price = float(request.form['open'])
        high_price = float(request.form['high'])
        low_price = float(request.form['low'])
        volume = float(request.form['volume'])
        
        # Make prediction
        prediction = model.predict([[open_price, high_price, low_price, volume]])[0]
        result = "Up" if prediction == 1 else "Down"
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
