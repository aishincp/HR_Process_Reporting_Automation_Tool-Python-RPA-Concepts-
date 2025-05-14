
import pandas as pd

# Cleaned data
df = pd.read_excel("cleaned_hr_data.xlsx")

# Extracting date columns to Year format
df['Join_Date'] = pd.to_datetime(df['Join_Date'])
df['Left_Date'] = pd.to_datetime(df['Left_Date'], errors='coerce')

# To calculte tenure for employee who hasn't left
today = pd.to_datetime('today')
df['Effective_Exit_Date'] = df['Left_Date'].fillna(today)

# Calculate Tenure (years)
df['Tenure (Years)'] = (df['Effective_Exit_Date'] - df['Join_Date']).dt.days / 365

# Extract Join_Date
df['Join_Year'] = df['Join_Date'].dt.year

# Apply filters like "Join_Year: 2024" and "Training: Not Completed"
filtered_df = df[(df['Join_Year'] == 2024) & (df['Training_Completed'] == 'No')]

# Preparing summarize : count employees without training, grouped by department
summary = filtered_df[['Name', 'Department', 'Tenure (Years)', 'Leaves_Taken', 'Training_Completed']]

# Save the detailed filtered summary to a CSV file
summary.to_csv('hr_training_alert_2024.csv', index=False)

# Print summary on screen
print(summary)
