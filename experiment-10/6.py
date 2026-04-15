import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'Name': ['Aman', 'Riya', None, 'Sita', 'John'],
    'Age': [23, np.nan, 25, None, 30],
    'Salary': [50000, 60000, None, 45000, np.nan]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

# Check missing values
print("\nMissing Values:\n", df.isnull())

# Replace missing values
# Option 1: Fill with default values
df_filled = df.fillna({
    'Name': 'Unknown',
    'Age': df['Age'].mean(),
    'Salary': df['Salary'].median()
})

print("\nDataFrame after replacing missing values:\n", df_filled)

# Option 2: Drop rows with missing values (if no valuable info)
df_dropped = df.dropna()

print("\nDataFrame after dropping missing rows:\n", df_dropped)