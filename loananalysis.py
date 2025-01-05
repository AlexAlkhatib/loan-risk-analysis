# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:16:31 2024

@author: Alex Alkhatib
"""

# Import libraries 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =============================================================================
# Load dataset
# =============================================================================

loan_data = pd.read_excel('loandataset.xlsx')
customer_data = pd.read_csv('customer_data.csv', sep=';')

# Display the first few rows of our dataset
loan_data.head()
customer_data.head()


# =============================================================================
# Merging two data frames
# =============================================================================

complete_data = pd.merge(loan_data, customer_data, left_on='customerid', right_on='id')

# =============================================================================
# Cleaning Data in Python
# =============================================================================

# Check for missing data
complete_data.isnull().sum()

# Remove the rows with missing data
complete_data = complete_data.dropna()
complete_data.isnull().sum()

# Check for duplicated data
complete_data.duplicated().sum()

# Drop duplicated rows
complete_data = complete_data.drop_duplicates()

# =============================================================================
# Functions in Python
# =============================================================================

# Define a function to categorize purpose into categories
# There are many purposes in the purpose column. 
# this function takes the purpose column as input and output the broader categories

def categorize_purpose(purpose):
    if purpose in ['credit_card', 'debt_consolidation']:
        return 'Financial'
    elif purpose in ['educational', 'small_business']:
        return 'Educational/Business'
    else:
        return 'Other'
    
categorize_purpose('credit_card')

complete_data['purpose_category'] = complete_data['purpose'].apply(categorize_purpose)


# Creating a conditional statement function
def check_number(number):
    if number < 0:
        return 'Negatif'
    if number > 0:
        return 'Positif'
    else:
        return 'Zero'

result = check_number(5)

# Create a new function based on criteria
# dti ratio > 20 and the deling.2years > 2 and the revol.util > 60 then the borrower is on high risk

def assess_risk(row):
    if row['dti'] > 20 and row['delinq.2yrs'] > 2 and row['revol.util'] > 60:
        return 'High Risk'
    else:
        return 'Low Risk'

complete_data['Risk Level'] = complete_data.apply(assess_risk, axis=1)


# Create a function to categorize the FICO score based on different ranges
def categorize_fico(fico_score):
    if fico_score >= 800 and fico_score <= 850:
        return 'Excellent'
    elif fico_score >= 740 and fico_score < 800:
        return 'Very Good'
    elif fico_score >= 670 and fico_score < 740:
        return 'Good'
    elif fico_score >= 580 and fico_score < 670:
        return 'Fair'
    else:
        return 'Poor'
    
complete_data['FICO Category'] = complete_data['fico'].apply(categorize_fico)


# Identify customers with more than average inquiries and derogatories records

def identify_high_inq_derog(row):
    average_inq = complete_data['inq.last.6mths'].mean()
    average_derog = complete_data['pub.rec'].mean()
    
    if row['inq.last.6mths'] > average_inq and row['pub.rec'] > average_derog:
        return True
    else:
        return False
    
complete_data['High_Inquieries_and_Public_Records'] = complete_data.apply(identify_high_inq_derog, axis=1)


class DataAnalysis:
    
    def __init__(self, df, column_name):
        self.df = df
        self.column_name = column_name
        
    def calculate_mean(self):
        return self.df[self.column_name].mean()
    
    def calculate_median(self):
        return self.df[self.column_name].median()
    

analysis = DataAnalysis(complete_data, 'fico')
analysis.calculate_mean()
analysis.calculate_median()


# Bar chart to show distribution of loans by purpose

# Set the style of our visualization (darkgrid, whitegrid, dark, white)
sns.set_style('whitegrid')

plt.figure(figsize=(10, 6))
sns.countplot(x = 'purpose', data = complete_data, palette='dark')
plt.title('Loan purpose distribution')
plt.xlabel('Purpose of loans')
plt.ylabel('Number of loans')
plt.xticks(rotation=45)
plt.show()

# Create a scatterplot for 'dti' vs 'income'
plt.figure(figsize=(10, 6))
sns.scatterplot(x = 'log.annual.inc', y = 'dti', data = complete_data)
plt.title('Debt to Income Ratio vs Annual Income')
plt.show()

# Distribution of FICO score
plt.figure(figsize=(10, 6))
sns.histplot(complete_data['fico'], bins=30, kde=True)
plt.title('Distribution of FICO Scores')
plt.show()

# Subplots

# Initialize the subplot figure
fig, axs = plt.subplots(2, 2, figsize=(20, 20))

# 1. Loan Purpose Distribution
sns.countplot(x='purpose', data=complete_data, ax=axs[0, 0])
axs[0, 0].set_title('Loan Purpose Distribution')
plt.setp(axs[0, 0].xaxis.get_majorticklabels(), rotation=45)

# 2. Debt-to-Income Ratio vs. FICO Score
sns.scatterplot(x='fico', y='dti', data=complete_data, ax=axs[0, 1])
axs[0, 1].set_title('Debt-to-Income Ratio vs. FICO Score')

# 3. Distribution of FICO Scores
sns.histplot(complete_data['fico'], bins=30, kde=True, ax=axs[1, 0])
axs[1, 0].set_title('Distribution of FICO Scores')

# 4. Risk Category vs Interest Rate
sns.boxplot(x='Risk Level', y='int.rate', data=complete_data, ax=axs[1, 1])
axs[1, 1].set_title('Interest Rate vs. Risk Category')

# Adjust layout for readability
plt.tight_layout()
plt.show()

    
    
