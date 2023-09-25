# Fetal Health Classification

Optimization of Bachelor Thesis Project that made by Universitas Sebelas Maret Student

First Version: https://colab.research.google.com/drive/1I-JS_I4VoIu2qzuiicPNHzUY_mEbQcGY?usp=sharing
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
