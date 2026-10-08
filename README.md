# ❤️ HeartCheck

**HeartCheck** is a simple machine-learning-powered web application for **heart disease risk screening**.

The application collects basic health information from a user, processes the information using the same feature structure used to train the machine-learning model, and returns a predicted risk class.

> **Important:** HeartCheck is an experimental screening tool. It is **not a medical diagnostic system** and does not predict whether a person will have a heart attack.

---

## 🚀 Features

* Simple and beginner-friendly web interface
* Heart-health information form
* Machine learning prediction
* Uses a trained Logistic Regression model
* Uses the saved feature scaler
* Automatically converts user-friendly answers into model features
* Displays prediction probability
* Responsive interface
* No login required
* No database required

---

## 🧠 Machine Learning

The application uses a trained machine-learning model stored as a `.pkl` file.

### Model files

```text
model/
├── heart_disease_model.pkl
├── scaler.pkl
└── columns.pkl
```

### What they contain

**`heart_disease_model.pkl`**

The trained heart-disease classification model.

**`scaler.pkl`**

The scaler used to transform the continuous numerical features before prediction.

**`columns.pkl`**

The exact feature order expected by the trained model.

---

## 📊 Model Features

The model uses **15 features**:

| Feature             | Description                   |
| ------------------- | ----------------------------- |
| `Age`               | Age                           |
| `RestingBP`         | Resting blood pressure        |
| `Cholesterol`       | Cholesterol level             |
| `FastingBS`         | Fasting blood sugar indicator |
| `MaxHR`             | Maximum heart rate            |
| `Oldpeak`           | ST depression                 |
| `is_male`           | Encoded sex                   |
| `ChestPainType_ATA` | Atypical angina               |
| `ChestPainType_NAP` | Non-anginal pain              |
| `ChestPainType_TA`  | Typical angina                |
| `RestingECG_Normal` | Normal resting ECG            |
| `RestingECG_ST`     | ST-T wave abnormality         |
| `ExerciseAngina_Y`  | Exercise-induced angina       |
| `ST_Slope_Flat`     | Flat ST slope                 |
| `ST_Slope_Up`       | Up-sloping ST slope           |

The user does **not** have to enter these 15 values manually.

The application converts normal user answers into the required model features automatically.

---

## 🔄 Prediction Pipeline

```text
User
  ↓
Web Form
  ↓
User-friendly health information
  ↓
Feature conversion
  ↓
Numerical feature scaling
  ↓
15 model features
  ↓
Machine Learning Model
  ↓
Prediction + Probability
  ↓
Result displayed to user
```

The scaler is applied to the continuous numerical features before the complete feature vector is passed to the model.

---

## 🛠️ Technology Stack

### Frontend

* HTML
* CSS
* Jinja templates

### Backend

* Python
* Flask

### Machine Learning

* scikit-learn
* NumPy
* Pandas
* Joblib

---

## 📁 Project Structure

```text
heartcheck/
│
├── app.py
├── README.md
├── requirements.txt
│
├── model/
│   ├── heart_disease_model.pkl
│   ├── scaler.pkl
│   └── columns.pkl
│
└── templates/
    └── index.html
```

---

## 💻 Installation

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
```

Move into the project:

```bash
cd heartcheck
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

You should see something similar to:

```text
Running on http://127.0.0.1:5000
```

Open the address in your browser.

---

## 🧪 Testing

Enter the required health information and click:

**Check Result**

The application will:

1. Receive the form data.
2. Convert categorical answers into numerical features.
3. Scale the required numerical features.
4. Arrange all features according to `columns.pkl`.
5. Send the processed data to the trained model.
6. Generate a prediction.
7. Calculate the model probability.
8. Display the result.

---

## 📌 Prediction Output

The model returns two possible classes.

### Class `0`

```text
Lower Risk Indicated
```

### Class `1`

```text
Higher Risk Indicated
```

The application also displays the model's probability for the predicted class.

---

## ⚠️ Medical Disclaimer

HeartCheck is an **experimental machine-learning screening project** created for educational and hackathon purpos
