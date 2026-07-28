
# Fake Job Posting Detection

An end-to-end machine learning web application that analyzes job advertisements and predicts whether they are **Real** or **Fake**.

The system combines Natural Language Processing (NLP) with additional job-posting features, serves predictions through a FastAPI backend, and provides a web interface for users to submit job postings for analysis.

## Project Overview

Online job scams can make it difficult for job seekers to determine whether a posting is trustworthy. This project was developed to help identify potentially fraudulent job advertisements using machine learning.

The application analyzes the job title and description, preprocesses the text, converts it into TF-IDF features, adds selected binary indicators, and sends the resulting feature vector to a trained classification model.

## How It Works

```text
Job Title + Description
        ↓
Text Preprocessing
        ↓
TF-IDF Vectorization
        ↓
Additional Job Features
        ↓
Machine Learning Model
        ↓
Real / Fake Prediction
        ↓
Confidence Score
```

The current prediction pipeline also checks selected indicators such as:

- Salary-related terms
- Remote-work terms
- Additional binary job-posting features used during model training

## Main Features

- Real vs. fake job-posting prediction
- Confidence score for each prediction
- NLP text preprocessing
- TF-IDF feature extraction
- Trained machine learning model
- FastAPI backend
- Web-based user interface
- Database storage for submitted postings and analysis results
- Feedback and administrative API routes

## Technologies

### Machine Learning & Data

- Python
- scikit-learn
- pandas
- NumPy
- SciPy
- imbalanced-learn
- NLTK
- joblib

### Backend

- FastAPI
- Uvicorn

### Frontend

- HTML
- CSS
- JavaScript

### Data Storage

- SQLite

## Prediction Pipeline

The backend performs the following steps:

1. Combines the job title and job description.
2. Converts the text to lowercase.
3. Removes numbers and punctuation.
4. Transforms the cleaned text using a trained TF-IDF vectorizer.
5. Creates additional binary features used by the trained model.
6. Combines the text and binary features into one feature matrix.
7. Generates a **Real** or **Fake** prediction.
8. Returns a confidence score.
9. Stores the submitted job and prediction result in the database.

## Installation

This project was developed with Python 3.11.

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Backend

From the project root, run:

```bash
uvicorn backend.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000
```



## Model Files

The application requires the trained model and TF-IDF vectorizer:

```text
backend/model/best_model.pkl
backend/model/tfidf_vectorizer.pkl
```

These files must remain in the expected locations for the prediction API to work.

## Dataset

The original project used a fake-job-posting dataset for model development and evaluation.

**Dataset source:** https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction

## API

The backend includes routes for:

- Job-posting analysis
- User feedback
- Administrative functionality

The main prediction endpoint accepts job-posting information and returns:

- Prediction: `Real` or `Fake`
- Confidence score

## Project Context

This project was developed as a **senior project at Saudi Electronic University**.

It was completed as a team project, combining machine learning, NLP, backend development, database integration, and a web interface.

### My Contributions

- Machine learning model development and evaluation
- NLP preprocessing and feature engineering
- Backend/API development
- Testing and documentation


## Privacy and Repository Notes

Before publishing the repository:

- Do not upload `__pycache__`, `.pyc`, or `.DS_Store` files.
- Avoid uploading large duplicate dataset files.
- Make sure no passwords, API keys, or private credentials are included.

## Future Improvements

Possible future improvements include:

- More advanced transformer-based NLP models
- Expanded explainability for predictions
- Improved confidence calibration
- User authentication
- Additional fraud indicators
- Model monitoring and retraining
- Deployment automation

## Disclaimer

This application is intended as a machine learning project and decision-support tool. Predictions should not be treated as definitive proof that a job posting is legitimate or fraudulent.
