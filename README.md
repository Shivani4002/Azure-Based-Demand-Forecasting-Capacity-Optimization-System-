**Milestone 1**

# Azure-Based-Demand-Forecasting-Capacity-Optimization-System-

Project Overview

The Azure Based Demand Forecasting & Capacity Optimization System is a data-driven solution designed to analyze Azure datasets and generate insights for demand forecasting and capacity optimization.

This project processes an Azure synthetic dataset using Python (Pandas) and visualizes trends using Matplotlib.

Objectives

1.Clean and preprocess Azure dataset

2.Handle null (missing) values

3.Standardize inconsistent text formatting

4.Convert text data into Camel Case

5.Generate demand forecasting insights

6.Support capacity optimization decisions

Technologies Used

1.Microsoft Azure Dataset

2.Python

3.Pandas

4.Matplotlib

Dataset Information

Dataset Name: azure_synthetic _dataset_5000.csv

Location: Stored in C:\ drive

Data Issues Identified:

    1.Null values
    2.Mixed uppercase and lowercase letters
    3.Minor formatting inconsistencies

Data Preprocessing Steps

1️⃣ Handling Missing Values

Detect null values

Fill using mean/median/mode or drop if necessary


2️⃣ Text Standardization

Convert inconsistent text into Camel Case

Clean categorical values

Remove formatting errors


3️⃣ Data Cleaning

Remove duplicates

Ensure consistent structure

Prepare data for analysis


Visualization

1.The system uses Matplotlib to generate:

2.Demand trend graphs

3.Capacity utilization charts

4.Time-series visualizations

5.Comparative demand analysis


C:\CODING\PandasApp

                │
                ├── azure_synthetic _dataset_5000.csv
                ├── test_pandas.py
                └── README.md

How to Run the Project (Windows – C Drive)

  1️⃣ Open Terminal 
      New Terminal
           test_pandas.py

             or
 2️⃣ Simply run the python file through 
          Run Button


Install Required Libraries (If Not Installed)
1.pip install pandas
2.pip install matplotlib


Key Features
✔ Azure dataset processing
✔ Null value handling
✔ Camel Case text normalization
✔ Automated data cleaning
✔ Demand trend visualization
✔ Capacity optimization support



                
Conclusion
This project demonstrates how Azure-based datasets can be efficiently processed in a Windows environment using Python. By combining data cleaning, transformation, and visualization, it provides meaningful insights for demand forecasting and capacity optimization.





**Milestone 2**

Feature Engineering & Data Wrangling


🎯 Objective

Prepare the dataset for predictive modeling through data enrichment, transformation, and structured preprocessing.

This milestone focuses on identifying demand-driving factors and engineering meaningful features to improve model performance.


📂 Dataset

File: azure_synthetic_dataset_5000.csv
The dataset contains synthetic Azure service usage data including:

Service usage metrics

Service uptime records

User behavior indicators

Time-based activity logs

🔍 Project Tasks
1️⃣ Identify Demand-Driving Features

Analyzed and extracted key variables influencing demand, including:

Usage trends over time

Service uptime percentages

User activity patterns

Peak vs off-peak behavior


2️⃣ Feature Engineering

Created derived and enriched features such as:

📅 Seasonality Flags

Month, quarter, weekday/weekend indicators

Peak-hour flags

📈 Usage Spike Indicators

Threshold-based spike detection

Rolling mean deviations

🔁 Lag Variables

Previous day/week usage

Rolling averages

Moving windows for trend capture

📊 Trend-based and behavior-driven metrics


3️⃣ Data Wrangling & Transformation

Cleaned and handled missing values

Standardized schema and column naming

Ensured consistent time granularity

Reshaped data into model-ready format

Verified data types and normalization readiness



🛠 Technologies Used

Python

Pandas

NumPy

Matplotlib 

Jupyter Notebook (.ipynb)


📁 Repository Structure
├── azure_synthetic_dataset_5000.csv
├── Milestone2.ipynb
├── README.md
└── LICENSE



📈 Outcome

At the end of this milestone:

The dataset is fully cleaned and structured

Time-based features are enriched

Demand-driving indicators are engineered





**
Milestone 3 – Machine Learning Model Development**

## Project Title

Demand Prediction using Machine Learning Models

---

# Objective

The objective of this milestone is to develop machine learning models that can accurately predict demand using historical usage data.

In this project, different models are trained and tested using a dataset. Their performance is compared using evaluation metrics such as MAE, RMSE, and Forecast Bias. The best-performing model is selected based on accuracy.

---

# Dataset

Dataset Name: **azure_synthetic_dataset_5000.csv**

This dataset contains synthetic cloud usage data.
It represents demand patterns over time and is used to train machine learning models to predict future demand.

The dataset is loaded into Python using the pandas library.

---

# Technologies and Libraries Used

The project is implemented using Python and the following libraries:

* pandas – used for loading and managing the dataset
* numpy – used for numerical calculations
* matplotlib – used for plotting graphs and visualizations
* scikit-learn – used for train-test splitting and evaluation metrics
* xgboost – used for building the XGBoost machine learning model
* statsmodels – used for implementing the ARIMA time-series forecasting model

---

# Installation Steps

Before running the project, install the required libraries.

Open the terminal or command prompt and run:

pip install pandas numpy matplotlib scikit-learn xgboost statsmodels jupyter

After installing the libraries, launch Jupyter Notebook:

jupyter notebook

Place the dataset file **azure_synthetic_dataset_5000.csv** in the same folder as the notebook file.

# Step 1 – Import Required Libraries

In this step, all necessary Python libraries are imported.

These libraries help with:

* data handling
* machine learning
* statistical modeling
* visualization



# Step 2 – Load the Dataset

The dataset is loaded using the pandas function:

df = pd.read_csv("azure_synthetic_dataset_5000.csv")



# Step 3 – Data Preprocessing

Before training the models, the dataset is cleaned.

Tasks performed in this step include:

• Handling missing values using forward fill
• Selecting the target column **usage_units**
• Separating the dataset into features and target variable

Where:

X → input features
y → demand value that the model will predict

---

# Step 4 – Train-Test Split

The dataset is divided into two parts:

Training Data → 80%
Testing Data → 20%



# Step 5 – XGBoost Model

The first model used is **XGBoost Regressor**.

XGBoost is a powerful machine learning algorithm based on gradient boosting.

Purpose of this model:

* learn patterns from historical data
* predict future demand values


# Step 6 – ARIMA Model

The second model used is **ARIMA (AutoRegressive Integrated Moving Average)**.

ARIMA is commonly used for time-series forecasting.

Purpose of ARIMA:

* analyze historical demand patterns
* forecast future demand values based on past observations



# Step 7 – Model Evaluation

A custom evaluation function is created to measure model performance.

The following metrics are calculated:

RMSE (Root Mean Squared Error)
Measures the square root of the squared prediction errors.


# Step 8 – Model Comparison

The results from each model are stored in a comparison table.

The table includes:

RMSE Score




# Step 9 – Best Model Selection

The best model is selected based on the **lowest RMSE value**.

Lower RMSE indicates that the model's predictions are closer to the actual demand values.


# Step 10 – Visualization

A graph is created using matplotlib to compare:

Actual Demand
Predicted Demand


# Conclusion

In this milestone, machine learning models were developed to predict demand using historical usage data.

The models implemented include:

• XGBoost
• ARIMA

Both models were evaluated using RMSE.

Based on these evaluation metrics, the best-performing model was selected for demand prediction.



