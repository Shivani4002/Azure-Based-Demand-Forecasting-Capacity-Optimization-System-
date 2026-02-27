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
├── Milestone_2_Feature_Engineering.ipynb
├── README.md
└── LICENSE



📈 Outcome

At the end of this milestone:

The dataset is fully cleaned and structured

Time-based features are enriched

Demand-driving indicators are engineered
