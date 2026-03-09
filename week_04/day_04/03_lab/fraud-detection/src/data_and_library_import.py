import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import (
    classification_report, roc_auc_score, average_precision_score,
    accuracy_score, f1_score, precision_score, recall_score
)

import mlflow
import mlflow.sklearn
from mlflow import MlflowClient

import joblib


# Load the dataset
trades = pd.read_csv('data/trades.csv')
user_activity = pd.read_csv('data/user_activity.csv')


# Quick sanity checks
print(trades.head())
print(trades.info())
print(trades.shape)
print(user_activity.head())
print(user_activity.info())
print(user_activity.shape)



# Convert object columns to int where possible
for column in trades.select_dtypes(include=["object"]):
    try:
        trades[column] = trades[column].astype("int")
    except:
        pass

# Check missing values as percentages
missing = 100 * trades.isnull().sum() / len(trades)
print(missing)

# Check feature cardinality
print(trades.nunique())

pd.set_option('display.float_format', '{:,.2f}'.format)
print(trades[['volume', 'amount']].describe())

# Skewness check
print('Volume skew:', trades['volume'].skew())
print('Amount skew:', trades['amount'].skew())