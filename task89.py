

# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv('data1981-2017.csv')

# Data cleaning: Convert year columns to numeric, replace '..' with NaN
year_columns = data.columns[4:]
data[year_columns] = data[year_columns].replace('..', pd.NA).apply(pd.to_numeric, errors='coerce')

# Descriptive statistics using describe() for year columns
descriptive_stats = data[year_columns].describe()
print(descriptive_stats)

def plot_histogram(year):
    plt.figure(figsize=(10, 6))
    plt.hist(data[year].dropna(), bins=30, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {year}', fontsize=15)
    plt.xlabel('Values', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.grid(True)
    plt.show()

# Call the function for 2010 data
plot_histogram('2010 [YR2010]')

def plot_scatter(year1, year2):
    plt.figure(figsize=(10, 6))
    plt.scatter(data[year1], data[year2], alpha=0.5, color='green')
    plt.title(f'Scatter plot between {year1} and {year2}', fontsize=15)
    plt.xlabel(year1, fontsize=12)
    plt.ylabel(year2, fontsize=12)
    plt.grid(True)
    plt.show()

# Call the function to plot scatter for 2010 and 2017
plot_scatter('2010 [YR2010]', '2017 [YR2017]')

def plot_heatmap(corr_matrix):
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, cmap='coolwarm', annot=False, fmt='.2f')
    plt.title('Correlation Heatmap', fontsize=15)
    plt.show()

# Perform correlation analysis and plot the heatmap
correlation_matrix = data[year_columns].corr()
plot_heatmap(correlation_matrix)

