# 🌐 HDI Prediction System
## A Comprehensive Measure of Well-Being

---

## 📌 Project Summary

HDI Prediction System is an AI-powered Human Development Index prediction platform developed to simplify the assessment of human development levels across countries using machine learning. Instead of manually analyzing complex datasets with 195 countries and 82 indicators, the system takes four key socioeconomic inputs — Life Expectancy, Mean Years of Schooling, Gross National Income per capita, and Internet Users — and instantly predicts the HDI score along with its development category.

Rather than replacing analysts or researchers, the HDI Prediction System acts as an intelligent decision-support tool that enables faster, more consistent, and more accessible human development insights for policymakers, researchers, students, and development organizations worldwide.

---

## ✨ Key Features

- Instant HDI score prediction using a trained Linear Regression model
- HDI category classification — Low, Medium, High, and Very High HDI
- Data preprocessing pipeline with automated null value handling
- Professional Flask web application with Home, Prediction Form, and Result pages
- Three interactive analytics dashboards — HDI Score Comparison, World HDI Map, and HDI Trend Over Years
- Model serialization using Pickle for instant loading without retraining
- Clean professional dark Navy UI theme across all pages

---

## 🏗️ Technical Architecture

The project follows a modular three-layer architecture:

**Machine Learning Layer:** Handles data loading, exploratory data analysis, preprocessing, feature selection, and model training using Linear Regression. Evaluates performance using R-squared score and serializes the model using Pickle.

**Backend Layer:** Implemented using Flask, managing HTTP routes, user input processing, model loading, HDI prediction logic, category classification, and result rendering across all pages including the analytics dashboard.

**Presentation Layer:** Built with HTML5, CSS3, JavaScript, and Chart.js for a professional and responsive user experience including three interactive dashboards with bar charts, pie charts, line charts, and radar charts.

---

## 👥 Team Members

| S.No | Name | Role | Email |
|------|------|------|-------|
| 1 | Spandhana Mondam | Team Lead | r210961@rguktrkv.ac.in |
| 2 | Bhagyalatha Kadali | Member | lathakadali93@gmail.com |
| 3 | Pechetti Lilly Lakshmi Puja Sri | Member | s210417@rguktsklm.ac.in |
| 4 | Balla Kamala Anjali | Member | ballakamalaanjali@gmail.com |
| 5 | Gara Bhandhavi | Member | bhandhavigara@gmail.com |

---

## 🚀 How to Run the Application

**Prerequisites**
- Python 3.x installed and available in PATH
- pip package manager available
- Anaconda or VS Code recommended

**Step 1: Navigate to the Flask Folder**

```bash
cd Flask
```

**Step 2: Install Project Dependencies**

```bash
pip install numpy pandas matplotlib scikit-learn flask seaborn
```

**Step 3: Generate the Machine Learning Model File**

Open `Training/HumDevIndex.ipynb` in Jupyter Notebook and run all cells.
This generates `Flask/HDI.pkl`.

**Step 4: Launch the Flask Web Application**

```bash
python app.py
```

**Step 5: Open the Application**

```
http://127.0.0.1:5000
```

---

## 🧪 Testing the Prediction

| Indicator | Sample Value |
|-----------|-------------|
| Life Expectancy | 72.5 |
| Mean Years of Schooling | 10.2 |
| GNI per capita | 15000 |
| Internet Users (%) | 65.4 |

**Expected Result: High HDI — 0.76** ✅

---

## 📂 Project Structure

```
hdi-prediction-ml/
│
├── 1. Brainstorming & Ideation/
├── 2. Requirement Analysis/
├── 3. Project Design Phase/
├── 4. Project Planning Phase/
├── 5. Project Development Phase/
├── 6. Project Testing/
├── 7. Project Documentation/
├── 8. Project Demonstration/
│
├── Dataset/
│   └── HDI.csv
│
├── Training/
│   └── HumDevIndex.ipynb
│
├── Flask/
│   ├── app.py
│   ├── HDI.pkl
│   └── templates/
│       ├── home.html
│       ├── indexnew.html
│       ├── resultnew.html
│       └── dashboard.html
│
└── README.md
```

---

## 🛠️ Technology Stack

| Layer | Technologies |
|-------|-------------|
| Machine Learning | Python, Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, Pickle |
| Backend | Flask, Jinja2 |
| Frontend | HTML5, CSS3, JavaScript, Chart.js |
| Data Source | Kaggle — HDI Dataset |
| Version Control | Git & GitHub |

---

## 🙏 Acknowledgement

We sincerely thank **SmartBridge** for providing this incredible internship opportunity under the domain of Artificial Intelligence and Machine Learning. This project helped us experience the complete AI/ML lifecycle — from raw data exploration and model training all the way to a fully deployed working web application with interactive analytics dashboards.

*Project ML-0027 | SmartBridge Internship | SkillWallet Platform*
