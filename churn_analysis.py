import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
df = pd.read_csv('telecom_customer_churn.csv')

# 2. Data Cleaning
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

# Convert Churn column to binary
df['Churn_Binary'] = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)

# 3. Exploratory Data Analysis: Churn by Contract Type
plt.figure(figsize=(10, 6))
sns.barplot(x='Contract', y='Churn_Binary', data=df, palette='viridis', ci=None)
plt.title('Churn Rate by Contract Type', fontsize=14, fontweight='bold')
plt.xlabel('Contract Type', fontsize=12)
plt.ylabel('Churn Rate', fontsize=12)
plt.savefig('churn_by_contract.png', bbox_inches='tight')
plt.close()

# 4. Summary Statistics
print("Summary Analysis:")
print(df.groupby('Contract')['Churn_Binary'].mean() * 100)
