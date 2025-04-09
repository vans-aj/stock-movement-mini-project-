
# 📈 Stock Price Movement Predictor

This is a simple web application built using **Flask** and **scikit-learn** that predicts whether a stock's price will go **Up** or **Down** based on market features like Open, High, Low, and Volume using a **Decision Tree Classifier**.

---

## 🚀 Features

- Input Open, High, Low, and Volume values
- Predict if the stock price will go **Up** (High > Open) or **Down**
- Built with Flask for the backend
- Decision Tree Classifier from scikit-learn for prediction
- Simple frontend with HTML + form handling

---

## 🛠️ Tech Stack

- Python
- Flask
- Pandas
- scikit-learn
- HTML/CSS

---

## 📂 Project Structure
├── app.py               # Flask app and model logic
├── datast.csv           # Dataset used for training
├── templates/
│   └── index.html       # Frontend UI
└── README.md            # Project documentation

---

## 📊 Dataset

- The dataset should have at least the following columns:
  - `Open`
  - `High`
  - `Low`
  - `Volume`

The target is determined by checking if `High > Open`.

---

## 🧠 Model

- **Model Used**: DecisionTreeClassifier from `scikit-learn`
- **Target Variable**: 1 if `High > Open`, else 0
- **Split**: 80% training, 20% testing

---

## ⚙️ How to Run

1. Clone the repo or download the files.

2. Make sure you have the required packages:

```bash
pip install flask pandas scikit-learn
