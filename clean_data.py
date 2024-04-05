import pandas as pd

# Load the CSV file
file_path = 'data/listings.csv'
df = pd.read_csv(file_path)

# 1. Remove duplicate rows
df_cleaned = df.drop_duplicates()

# 2. Handle missing values
# Remove columns with more than 50% missing values
missing_values = df_cleaned.isnull().mean().sort_values(ascending=False)
columns_to_drop = missing_values[missing_values > 0.5].index
df_cleaned = df_cleaned.drop(columns=columns_to_drop)

# Fill missing values in numeric columns
numeric_columns = ['review_scores_value', 'review_scores_checkin', 'review_scores_location',
                   'review_scores_communication', 'review_scores_cleanliness']

for col in numeric_columns:
    median_value = df_cleaned[col].median()
    df_cleaned[col] = df_cleaned[col].fillna(median_value)

# Save the cleaned data to a new CSV file
df_cleaned.to_csv('data/listings_clean.csv', index=False)
