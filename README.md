# Telco Churn Project

## Objective: 
- Predict what variables are driving customers to churn using the classification methodologies learned.
- Aquire, prepare, explore, test, model and make visualizations of what are the main drivers of churn. 
- Present to the codeup panel of my finding in a jupyter notebook.

## Goal: 
>The goal of this project is try and predict what variables are driving customers to churn using classification methods recently learned. I will be analyzing the telco data set in codeups sql server. The data set contains 72 months of data.

## Data Dictionary:
customer_id: Unique id for each customer
churn: Does not churn = 0, Does Churn = 1
tenure: How many months the customer has been with Telco
tenure_years: How many years the customer has been with Telco
contract_type: Month to Month = 1, 1-Year = 2, 2-Year = 3
tech_support: no = 0, yes = 1, whether they have tech support or not 
online_backup: no = 0, yes = 1, whether they have online backup or not 
phone_service:: no = 0, yes = 1, whether they have phone service or not 

## Thoughts: 
I want to see how other services influence churn. I know tenure and contracts influence churn based on the project performed earlier. 

## Initial Hypothesis: 
### Does online_backup influence churn?
Ho: null hypothesis: Having online backup does not affect churn.
Ha: alt hypothesis: Having online backup affects customers from churning.

### Does tech support mean customers have longer tenures?
Ho: null hypothesis: Having tech support does not increase the tenure.
Ha: alt hypothesis: Having tech support increases the tenure of customers.

## Project Planning:

### Acquire
- Create an aquire.py from the codeup SQL database.

### Prepare
- Create an prepare.py. Address missing data, outliers
- Create dummy variables and encode as needed
- Split data into train, validate and test

### Explore
- Summarize and visualize data
- Test hypothesis


### Model
- Try different algorithms: logistic regression, decesion trees, random forest and KNN. 
- See what features are influencing churn
- Train and adjust parameters in algorithims
- Validate on the top three
- Test on the top model

## Conclusion
- Summarize what is driving churn
- Recommendations
- Next steps

## How to Reproduce:
- Import acquire.py and prepare.py files on a jupyter notebook
- import numpy as np
- import pandas as pd
- import seaborn as sns
- import matplotlib.pyplot as plt
- import statsmodels.formula.api as smf
- from scipy import stats
- from scipy.stats import chi2_contingency
- from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report
- from sklearn.model_selection import train_test_split
- from sklearn.linear_model import LogisticRegression, LinearRegression
- from sklearn.tree import DecisionTreeClassifier
- from sklearn.ensemble import RandomForestClassifier
- from sklearn.neighbors import KNeighborsClassifier
- from acquire import get_telco_data
- from prepare import prepare_telco
- import warnings
- warnings.filterwarnings("ignore")


## 

## How to Reproduce:

