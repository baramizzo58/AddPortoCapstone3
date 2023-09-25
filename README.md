# Fetal Health Classification

Optimization of Bachelor Thesis Project that made by Universitas Sebelas Maret Student

First Version: https://colab.research.google.com/drive/1I-JS_I4VoIu2qzuiicPNHzUY_mEbQcGY?usp=sharing<br>
Upgraded Version: https://colab.research.google.com/drive/1QZ5kg6A1UGQ0bWAKakgvKWclj1-PVi4n?usp=sharing

## **A. Business Problem Understanding**
### **1. Background**
[Cardiotocograms (CTGs)](https://en.wikipedia.org/wiki/Cardiotocography) are a simple and cost accessible option to assess fetal health, allowing healthcare professionals to take action in order to prevent child and maternal mortality. The equipment itself works by sending ultrasound pulses and reading its response, thus shedding light on fetal heart rate (FHR), fetal movements, uterine contractions and more. In this notebook we will try to analyze the CTGs data to solve the above issues.

![529556_1_En_8_Fig1_HTML](https://github.com/baramizzo58/AddPortoCapstone3/assets/119744134/d20c3a6c-a3e8-495c-b4e2-b45f0d651ecb)

### **2. Problem Statement**
**Early detection is very important to determine appropriate treatment. Especially for fetal health which concerns the lives of the mother and baby**. Using the available data, An appropriate model is needed to built to determine fetal health.

### **3. Goals**
The aim of this project is **to predict and classify the health of the fetus with the best accuracy possible**. Hopefully, with this model, it can prevent child and maternal deaths.

### **4. Analytic Approach**
Seeing the existing problem, we will build a **machine learning model** because we need to build predictions more than just using an inferential and/or descriptive analysis approach.

### **5. Modelling**
The existing data has labels so we use a supervised machine learning model. We will use [**Classification**](https://www.datacamp.com/blog/classification-machine-learning) because we need the model that can predict the correct label of a given input data.

We will try 5 supervised classification machine learning models:
1. Gradient Boosting Machine (GBM)
2. K-nearest neighbors (KNN)
3. Logistic Regression (LR)
4. Random Forest (RF)
5. Support Vector Machine (SVM)

## **C. Data**
This dataset obtain from [Kaggle](https://www.kaggle.com/datasets/andrewmvd/fetal-health-classification) that contains 2,126 records of features extracted from [Cardiotocogram exams](https://onlinelibrary.wiley.com/doi/10.1002/1520-6661(200009/10)9:5%3C311::AID-MFM12%3E3.0.CO;2-9), which were then classified by three expert obstetritians into 3 classes:
* Normal
* Suspect
* Pathological

### **1. Data Understanding**
#### a. Data Overview
![data overview](https://github.com/baramizzo58/AddPortoCapstone3/assets/119744134/55b4dd0a-715c-4e81-9ef1-914e51b5c290)

#### b. Data Outlier
![data outlier](https://github.com/baramizzo58/AddPortoCapstone3/assets/119744134/324345b2-8219-47ae-852b-68fd48d45378)

#### c. Data Correlation
![data correlation](https://github.com/baramizzo58/AddPortoCapstone3/assets/119744134/46f9acc2-54c9-40b8-bc8c-241ea3577ec8)

### **2. Data Cleaning**
Before oversampling
![pie before](https://github.com/baramizzo58/AddPortoCapstone3/assets/119744134/db2e2618-ee8f-4eea-b195-accf14dfe10f)
![bar before](https://github.com/baramizzo58/AddPortoCapstone3/assets/119744134/ceab71c3-65b3-4216-94d5-e5efa829cdd3)

After oversampling
![pie after](https://github.com/baramizzo58/AddPortoCapstone3/assets/119744134/ecaa2bf9-5e04-4c8c-8fde-ea16b7b853b3)
![bar after](https://github.com/baramizzo58/AddPortoCapstone3/assets/119744134/493d38ab-f9f0-441d-a55c-b3f7359094ae)

### **3. Data Modeling**
1. Gradient Boosting Machine (GBM)
2. K-nearest neighbors (KNN)
3. Logistic Regression (LR)
4. Random Forest (RF)
5. Support Vector Machine (SVM)

![image](https://github.com/baramizzo58/AddPortoCapstone3/assets/119744134/aa5c8ae6-2d9f-4a58-a22c-4be53eb4a636)

#### Best Model: K-nearest neighbors (KNN)
Learning Curve
![knn learning curve](https://github.com/baramizzo58/AddPortoCapstone3/assets/119744134/e3b2b545-2b36-429b-9281-01aaab434b93)

Confusion Metrics
![knn confusion metrics](https://github.com/baramizzo58/AddPortoCapstone3/assets/119744134/a8dbee2c-9aa9-4edb-af7d-a2585cea0b5a)

## **D. Conclusion & Recommendation**
### **1. Conclusion**
* This dataset is quite clean with no extreme & unreasonable outlier. This dataset also has no missing value found. But for the label (`fetal_health`) is not too good because of imbalance classification, where the dataset contain **77.85%** normal fetus label (1.0). This problem solved by do the oversampling.
* The most correlated factor with fetal health is **Abnormal Fetal Heart Rate - FHR** (`prolongued_decelerations`) with value **0.48**. The other factor is **Abnormal Short & Long Term Variability** also have high correlation with the value **0.47** & **0.43**, respectively. Short Term Variability is the percentage of subsequent FHR signals differing less than 1 bpm (`abnormal_short_term_variability`). Abnormal Long Term Variability is the percentage of FHR signals with a difference between the minimum and maximum values in a 1 min window lower than 5 bpm (`percentage_of_time_with_abnormal_long_term_variability`). [Source](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8442730/).
* The Best Model is **K-nearest neighbors** with training score **99.97%** & testing score **98.19%** with error **1.78%**. The model added, Support Vector Machine, has the most improved tuning model with improvement **5.5%**.

### **2. Recommendation**
* Building a model using feature selection to select column that only have high correlation with target
* Hyperparameter tuning optimization can use [Optuna](https://optuna.org/) to improve model performance
