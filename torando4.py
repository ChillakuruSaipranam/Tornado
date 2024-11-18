# -*- coding: utf-8 -*-
"""torando4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RY2d-zuqGH_3geIVQl3dyP4JJ_EcCjk9

# **TORNADO**

Loading the Torando Dataset into a pandas DataFrame.
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/1950-2023_all_tornadoes.csv')
print("First 5 rows of the dataset:")
df.head()

"""Identifying Categorical and Numerical Columns"""

categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
print("Categorical columns:")
print(categorical_cols)
print("\nNumerical columns:")
print(numerical_cols)

"""Finding the unique values in the columns to understand them better."""

print("\nNumber of unique values in categorical columns:")
for col in categorical_cols:
    print(f"{col}: {df[col].nunique()} unique values")

state_names = df['st'].unique()
for state in state_names:
    print(state)

"""Finding Missing Values in the dataset"""

df_cleaned = df.dropna()
print("Dataset after handling missing values:")
print(df_cleaned.head())
missing_numerical_cols = df[numerical_cols].isnull().sum()
if missing_numerical_cols[missing_numerical_cols > 0].empty:
    print("\nNumerical columns with missing values : No missing values in numerical columns.")
else:
    print("nNumerical columns with missing values :" ,missing_numerical_cols[missing_numerical_cols > 0])

"""To know whether there is duplicate values in the dataset and remove them."""

print("\nNumber of duplicate rows:", df_cleaned.duplicated().sum())
df_cleaned = df_cleaned.drop_duplicates()
print("Dataset after removing duplicates:")
print(df_cleaned.head())

"""We will find the correlation between the columns,to understand which is most important column and we will visualize correlation matrix."""

print("\nCorrelation between numerical columns:")
correlation_matrix = df[numerical_cols].corr()
print(correlation_matrix)

"""Visualizing the Correlation Matrix"""

import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(20, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Numerical Columns')
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the function to process the dataset
def analyze_tornado_dataset(df):
    # Step 2: View the first 5 rows
    print("First 5 rows of the dataset:")
    print(df.head())

    # Step 3: Identify categorical and numerical columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    print("\nCategorical columns:")
    print(categorical_cols)

    print("\nNumerical columns:")
    print(numerical_cols)

    # Step 4: Number of unique values in categorical columns
    print("\nNumber of unique values in categorical columns:")
    for col in categorical_cols:
        print(f"{col}: {df[col].nunique()} unique values")

    # Step 5: Correlation between numerical columns
    print("\nCorrelation between numerical columns:")
    correlation_matrix = df[numerical_cols].corr()
    print(correlation_matrix)

    # Step 6: Handle missing values
    df_cleaned = df.dropna()

    print("\nDataset after handling missing values:")
    print(df_cleaned.head())

    # Step 7: Check for missing values in numerical columns
    missing_numerical_cols = df[numerical_cols].isnull().sum()
    if missing_numerical_cols[missing_numerical_cols > 0].empty:
        print("\nNumerical columns with missing values: No missing values in numerical columns.")
    else:
        print("\nNumerical columns with missing values:")
        print(missing_numerical_cols[missing_numerical_cols > 0])

    # Step 8: Check for duplicate rows and remove them
    print("\nNumber of duplicate rows:", df_cleaned.duplicated().sum())
    df_cleaned = df_cleaned.drop_duplicates()

    print("\nDataset after removing duplicates:")
    print(df_cleaned.head())

    # Step 9: Visualize the correlation matrix
    plt.figure(figsize=(20, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix of Numerical Columns')
    return st.pyplot(plt)

# Call the function by passing the path to your CSV file
analyze_tornado_dataset('/content/drive/MyDrive/1950-2023_all_tornadoes.csv')

import pandas as pd

# Load the tornado dataset (assuming the state codes are under the column 'st')
tornado_data = pd.read_csv('/content/drive/MyDrive/1950-2023_all_tornadoes.csv')

# Load the dataset with state areas in square miles
state_areas = {
    'State': [
        'NC', 'KY', 'MS', 'PA', 'IL', 'AR', 'MO', 'TX', 'OH', 'LA', 'TN', 'FL',
        'AL', 'SC', 'KS', 'WY', 'NE', 'GA', 'IA', 'SD', 'ND', 'MN', 'WI', 'NM',
        'CT', 'IN', 'CO', 'MD', 'WV', 'VA', 'MA', 'OR', 'CA', 'NJ', 'MI', 'NH',
        'AZ', 'NY', 'MT', 'VT', 'UT', 'ME', 'ID', 'WA', 'DE', 'HI', 'AK', 'PR',
        'NV', 'RI', 'DC', 'VI'
    ],
    'Area (square miles)': [
        53819, 40409, 48432, 46055, 57914, 53179, 69707, 268596, 44825, 51843,
        42144, 65758, 52420, 32020, 82278, 97100, 77348, 59425, 56273, 77000,
        70700, 86936, 65498, 121590, 5543, 35817, 104094, 12407, 24230, 42774,
        10554, 98379, 163696, 8722, 96714, 9349, 113990, 54555, 147040, 9616,
        84899, 35385, 83569, 71298, 1949, 10931, 663300, 3515, 110572, 1214, 68, 133
    ]
}

# Create a DataFrame from the area data
df_areas = pd.DataFrame(state_areas)

# Group tornado data by state and count the number of tornadoes in each state
tornado_counts = tornado_data['st'].value_counts().reset_index()
tornado_counts.columns = ['State', 'Tornado Count']

# Merge the tornado counts with the state areas
df_merged = pd.merge(tornado_counts, df_areas, on='State', how='left')

# Calculate the average number of tornadoes per square mile for each state
df_merged['Tornadoes per Square Mile'] = df_merged['Tornado Count'] / df_merged['Area (square miles)']

# Sort by Tornadoes per Square Mile to find the state with the highest density
df_sorted = df_merged.sort_values(by='Tornadoes per Square Mile', ascending=False)


# Optionally, display all states sorted by tornado density
print(df_sorted[['State', 'Tornado Count', 'Area (square miles)', 'Tornadoes per Square Mile']])


# Display the state with the highest average tornadoes per square mile
print(df_sorted.head(1))




highest_tornado_state = df_sorted.head(1)['State'].values[0]
print("State with highest average tornadoes per square mile: ", highest_tornado_state)
# Save to a new CSV file if needed
df_merged.to_csv('/content/drive/MyDrive/tornadoes_per_square_mile.csv', index=False)

import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Suppress specific warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Plot the top 10 states with the highest tornadoes per square mile
plt.figure(figsize=(10, 6))
top_10_states = df_sorted.head(10)

# Barplot without 'hue' and with palette applied directly
sns.barplot(x='Tornadoes per Square Mile', y='State', data=top_10_states, palette='coolwarm')

# Add labels and title
plt.title('Top 10 States with Highest Tornadoes per Square Mile')
plt.xlabel('Tornadoes per Square Mile')
plt.ylabel('State')

# Show the plot
plt.show()

# 1. Time-Series Analysis: Plot the number of tornadoes over time for each state.
#python



import matplotlib.pyplot as plt

# Group by year and state to get the tornado counts

df_time_series = df.groupby(['yr', 'st']).size().reset_index(name='Tornado_Count')

top_5_states = df_time_series.groupby('st')['Tornado_Count'].sum().nlargest(5).index

plt.figure(figsize=(12, 6))

for state in top_5_states:

    state_data = df_time_series[df_time_series['st'] == state]

    plt.plot(state_data['yr'], state_data['Tornado_Count'], label=state)

plt.title('Tornado Occurrences Over Time for Top 5 States')

plt.xlabel('Year')

plt.ylabel('Number of Tornadoes')

plt.legend()

plt.show()

import pandas as pd

# Create the dataset with correct state areas in square miles
data = {
    'State': [
        'NC', 'KY', 'MS', 'PA', 'IL', 'AR', 'MO', 'TX', 'OH', 'LA', 'TN', 'FL',
        'AL', 'SC', 'KS', 'WY', 'NE', 'GA', 'IA', 'SD', 'ND', 'MN', 'WI', 'NM',
        'CT', 'IN', 'CO', 'MD', 'WV', 'VA', 'MA', 'OR', 'CA', 'NJ', 'MI', 'NH',
        'AZ', 'NY', 'MT', 'VT', 'UT', 'ME', 'ID', 'WA', 'DE', 'HI', 'AK', 'PR',
        'NV', 'RI', 'DC', 'VI'
    ],
    'Area (square miles)': [
        53819, 40409, 48432, 46055, 57914, 53179, 69707, 268596, 44825, 51843,
        42144, 65758, 52420, 32020, 82278, 97100, 77348, 59425, 56273, 77000,
        70700, 86936, 65498, 121590, 5543, 35817, 104094, 12407, 24230, 42774,
        10554, 98379, 163696, 8722, 96714, 9349, 113990, 54555, 147040, 9616,
        84899, 35385, 83569, 71298, 1949, 10931, 663300, 3515, 110572, 1214, 68, 133
    ]
}

# Create a DataFrame from the data
df_areas = pd.DataFrame(data)

# Load the tornado dataset (assuming the state codes are under the column 'st')
tornado_data = pd.read_csv('/content/drive/MyDrive/1950-2023_all_tornadoes.csv')

# Merge the tornado dataset with the area dataset based on the 'st' column
# Use suffixes to handle potential column name conflicts
tornado_data = tornado_data.merge(df_areas, left_on='st', right_on='State', how='left', suffixes=('', '_y'))

# Drop the duplicate 'State' column
tornado_data = tornado_data.drop(columns=['State'])

# Save the updated tornado_data back to the same file
tornado_data.to_csv('/content/drive/MyDrive/1950-2023_all_tornadoes.csv', index=False)

# Display first few rows to confirm
tornado_data.head()

import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset (replace the file path with your dataset's location)
df = pd.read_csv('/content/drive/MyDrive/1950-2023_all_tornadoes.csv')

# Function to plot tornado occurrences by year range for a state
def plot_tornadoes_by_state_and_year(df, state, years):
    # Ensure years input is sorted and handle cases for a single or multiple years
    years = sorted(years)
    start_year, end_year = years[0], years[-1]

    # Filter the dataset for the specified state and range of years
    state_data = df[(df['st'] == state) & (df['yr'] >= start_year) & (df['yr'] <= end_year)]

    if state_data.empty:
        print(f"No data available for the state: {state} in the specified year range: {start_year}-{end_year}.")
        return

    # Group by year to get the total tornado count per year within the range
    yearly_data = state_data.groupby('yr').size().reset_index(name='Tornado Count')

    # Plot the trend line for tornado counts over the specified year range
    plt.figure(figsize=(12, 6))
    plt.plot(yearly_data['yr'], yearly_data['Tornado Count'], marker='o', color='b', linestyle='-')
    plt.fill_between(yearly_data['yr'], yearly_data['Tornado Count'], color="skyblue", alpha=0.4)
    plt.title(f"Tornado Occurrences in {state} from {start_year} to {end_year}")
    plt.xlabel("Year")
    plt.ylabel("Tornado Count")
    plt.grid(True)
    plt.xticks(yearly_data['yr'], rotation=45)
    plt.tight_layout()
    plt.show()

# Function to plot tornado occurrences by month for a single year
def plot_tornadoes_by_month_for_year(df, year, state):
    # Filter data for the specified year and state
    year_data = df[(df['yr'] == year) & (df['st'] == state)]

    if year_data.empty:
        print(f"No data available for the state: {state} in the specified year: {year}.")
        return

    # Group by month and count the number of tornadoes
    tornado_counts_by_month = year_data.groupby('mo').size()

    # Plot tornado occurrences by month
    plt.figure(figsize=(10, 6))
    tornado_counts_by_month.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title(f"Tornado Occurrences in {state} for Each Month of {year}")
    plt.xlabel("Month")
    plt.ylabel("Tornado Count")
    plt.xticks(range(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Get user input for state and year(s)
state = input("Enter the state abbreviation (e.g., TX, FL): ").upper()
years_input = input("Enter one or two years (comma-separated, e.g., '2000' or '2000, 2020'): ")
years = list(map(int, years_input.split(',')))

# Determine which plot function to use based on the number of years provided
if len(years) == 1:
    plot_tornadoes_by_month_for_year(df, years[0], state)
else:
    plot_tornadoes_by_state_and_year(df, state, years)