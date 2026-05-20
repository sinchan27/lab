import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Program 1: Creating the dataset with missing values
data = {
    'Age': [25, 30, np.nan, 35, 40, np.nan, 50], 
    'salary': [5000, 6000, 7000, np.nan, 65000, 7000, np.nan],
    'experience': [1.0, 2.0, 3.0, 5.0, np.nan, 7.0, 10.0]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Program 2: Heatmap to visualize missing (null) values
plt.figure(figsize=(6, 4))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap (Before Imputation)")
plt.show()


# Program 3: Filling missing values with column means
df_filled = df.fillna(df.mean())
print("\nDataFrame After Mean Imputation:")
print(df_filled)

# Heatmap to check if null values are gone
plt.figure(figsize=(6, 4))
sns.heatmap(df_filled.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap (After Imputation)")
plt.show()


from sklearn.preprocessing import MinMaxScaler

# Program 4: Feature Scaling
scaler = MinMaxScaler()
df_scaled_array = scaler.fit-transform(df_filled)

# Converting back to DataFrame for easier plotting
df_minmax = pd.DataFrame(df_scaled_array, columns=df_filled.columns)
print("\nScaled DataFrame (MinMax):")
print(df_minmax)

# Plotting Before vs After scaling comparisons
plt.figure(figsize=(10, 4))

# Subplot 1: Before Scaling
plt.subplot(1, 2, 1)
sns.boxplot(data=df_filled)
plt.title('Before scaling')

# Subplot 2: After Scaling
plt.subplot(1, 2, 2)
sns.boxplot(data=df_minmax)
plt.title('After scaling')

plt.tight_layout()
plt.show()

# Program 5: Bar chart of species distribution
df_iris = sns.load_dataset('iris')

plt.figure(figsize=(6,4))
df_iris['species'].value_counts().plot(kind='bar')
plt.title('Bar Graph')
plt.xlabel('Species')
plt.ylabel('count')
plt.show()

# Program 6: Correlation matrix heatmap
plt.figure(figsize=(6,4))
co = df_iris.corr(numeric_only=True)
sns.heatmap(co, annot=True, cmap="coolwarm")
plt.title('Correlation heatmap')
plt.show()


# Program 7: Scatter plot
plt.figure(figsize=(6,4))
plt.scatter(df_iris['sepal_length'], df_iris['sepal_width'])
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()

# Program 8: Histogram distribution of value counts
plt.figure(figsize=(6,4))
df_iris['species'].value_counts().plot(kind='hist')
plt.title('Histogram')
plt.xlabel('Species Class Count')
plt.ylabel('Frequency')
plt.show()

# --- Assignment 1: Data Preprocessing & Visualization ---

import numpy as np # [cite: 3]
import pandas as pd # [cite: 3]
import matplotlib.pyplot as plt # [cite: 3]
import seaborn as sns # [cite: 3]

# Program 1: Creating the dataset with missing values [cite: 3, 4]
data = {
    'Age': [25, 30, np.nan, 35, 40, np.nan, 50], 
    'salary': [5000, 6000, 7000, np.nan, 65000, 7000, np.nan],
    'experience': [1.0, 2.0, 3.0, 5.0, np.nan, 7.0, 10.0]
}
df = pd.DataFrame(data) # [cite: 4]
print("Original DataFrame:\n", df) # [cite: 4]

# Program 2: Heatmap to visualize missing (null) values [cite: 6]
plt.figure(figsize=(6, 4)) # [cite: 6]
sns.heatmap(df.isnull(), cbar=False, cmap='viridis') # [cite: 6]
plt.title("Missing Values Heatmap (Before Imputation)")
plt.show() # [cite: 6]

# Program 3: Filling missing values with column means [cite: 7]
df_filled = df.fillna(df.mean()) # [cite: 7]
print("\nDataFrame After Mean Imputation:\n", df_filled) # [cite: 7]

plt.figure(figsize=(6, 4)) # [cite: 7]
sns.heatmap(df_filled.isnull(), cbar=False, cmap='viridis') # [cite: 7]
plt.title("Missing Values Heatmap (After Imputation)")
plt.show()

# Program 4: Feature Scaling [cite: 8, 9]
from sklearn.preprocessing import MinMaxScaler # [cite: 8]
scaler = MinMaxScaler() # [cite: 8]
df_scaled_array = scaler.fit_transform(df_filled) # [cite: 8, 9]

# Converting back to a DataFrame so columns are preserved for Seaborn
df_minmax = pd.DataFrame(df_scaled_array, columns=df_filled.columns)
print("\nScaled DataFrame (MinMax):\n", df_minmax) # [cite: 9]

plt.figure(figsize=(10, 4)) # [cite: 9]
plt.subplot(1, 2, 1) # [cite: 9]
sns.boxplot(data=df_filled) # [cite: 9]
plt.title('Before scaling') # [cite: 9]

plt.subplot(1, 2, 2) # [cite: 9]
sns.boxplot(data=df_minmax) # [cite: 9]
plt.title('After scaling') # [cite: 9]
plt.tight_layout()
plt.show() # [cite: 9]


# --- Assignment 2: Analysis on the 'Iris' Dataset --- [cite: 12]

# Program 5: Bar chart of species distribution [cite: 12, 13]
df_iris = sns.load_dataset('iris') # [cite: 12]

plt.figure(figsize=(6,4))
df_iris['species'].value_counts().plot(kind='bar') # [cite: 12]
plt.title('Bar Graph') # [cite: 13]
plt.xlabel('Species') # [cite: 13]
plt.ylabel('count') # [cite: 13]
plt.show() # [cite: 13]

# Program 6: Correlation matrix heatmap [cite: 13]
plt.figure(figsize=(6,4))
co = df_iris.corr(numeric_only=True) # [cite: 13]
sns.heatmap(co, annot=True, cmap="coolwarm") # [cite: 13]
plt.title('Correlation heatmap') # [cite: 13]
plt.show() # [cite: 13]

# Program 7: Scatter plot [cite: 16]
plt.figure(figsize=(6,4))
plt.scatter(df_iris['sepal_length'], df_iris['sepal_width']) # [cite: 16]
plt.title('Sepal Length vs Sepal Width') # [cite: 16]
plt.xlabel('Sepal Length') # [cite: 16]
plt.ylabel('Sepal Width') # [cite: 16]
plt.show() # [cite: 16]

# Program 8: Histogram distribution of value counts [cite: 16]
plt.figure(figsize=(6,4))
df_iris['species'].value_counts().plot(kind='hist') # [cite: 16]
plt.title('Histogram') # [cite: 16]
plt.xlabel('Species Class Count') # [cite: 16]
plt.ylabel('Frequency') # [cite: 16]
plt.show() # [cite: 16]
