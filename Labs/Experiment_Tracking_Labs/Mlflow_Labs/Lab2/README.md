# MLflow Lab 2 - Breast Cancer Detection 
# About This Lab
This lab is a modified version of the original Wine Quality Prediction Lab.
Instead of predicting wine quality, this lab predicts whether a tumor is Malignant or Benign using the Breast Cancer dataset.

# Modifications Made
Original LabMy Modified LabWine Quality Dataset (CSV)Breast Cancer Dataset (sklearn)Predict wine qualityPredict Malignant/BenignOnly Random ForestRandom Forest + Gradient BoostingNo model comparisonModel comparison with AUC scoresBasic feature importanceFeature importance + Bar chart

# Dataset

Source: sklearn.datasets (load_breast_cancer)
Total Samples: 569
Total Features: 30
Target: 0 = Malignant, 1 = Benign


# Models Used

Random Forest Classifier (Baseline)

n_estimators = 10
AUC Score = 0.9759


Gradient Boosting Classifier (Modified/Added)

n_estimators = 100
learning_rate = 0.1
AUC Score = 0.9949




# Results
ModelAUC ScoreRandom Forest0.9759Gradient Boosting0.9949 ✅
# Best Model: Gradient Boosting

# MLflow Steps Covered

 Step 1-2: Data Loading & Exploration
 Step 3: Data Preprocessing
 Step 4: Data Visualization
 Step 5: Define Target Variable
 Step 6: EDA with Box Plots
 Step 7: Missing Value Check
 Step 8: Train/Val/Test Split (60/20/20)
 Step 9: Model Training + MLflow Logging
 Step 10: Feature Importance Analysis
 Step 11: Model Registration in MLflow
 Step 12: Transition Model to Production
 Step 13: Model Inference & Evaluation
 Step 14-15: Batch Inference
 Step 16: Model Serving (MLflow Server)
 Step 17: Real-Time Inference
 Step 18: Conclusion & Summary

# Test Cases
All 10 test cases passed successfully!
TestDescriptionStatusTest 1Dataset shape (569, 31)
PassedTest 2No missing values
PassedTest 3Target column is binary
PassedTest 4Data split (341/114/114) 
PassedTest 5RF AUC > 0.90
PassedTest 6GB AUC > 0.90
PassedTest 7GB better than RF
PassedTest 8Model registered in MLflow
PassedTest 9Production model predictions valid
PassedTest 10Feature importances valid

# How to Run

## 1. Install dependencies:

bashpip install mlflow scikit-learn pandas numpy seaborn matplotlib cloudpickle requests

## 2. Open Jupyter Notebook:

bashjupyter notebook

Run lab2_breast_cancer.ipynb cell by cell
## 3. To serve the model:

bashpython -m mlflow models serve -m models:/breast_cancer_detection/production -h 0.0.0.0 -p 5001 --no-conda


## Name: Vaishnavi Mallikarjun Gajarla
Lab: MLflow Lab 2
Dataset: Breast Cancer (sklearn)
