import os
import pandas as pd
from datetime import datetime

# Step 1: Load Data
dir = os.path.dirname(os.path.abspath(__file__))  # Gets folder of the script
file_path = os.path.join(dir, "hr_dummy_data.csv")  # Adjust path accordingly
df = pd.read_csv(file_path)

# Step 2: Date Cleanup
df['Join_Date'] = pd.to_datetime(df['Join_Date'])
df['Left_Date'] = pd.to_datetime(df['Left_Date'], errors='coerce')  # NaT if not left

# Step 3: Metrics
total_employees = len(df)
employees_left = df['Status'].str.lower().eq('left').sum()
attrition_rate = round((employees_left / total_employees) * 100, 2)

# Tenure only for current employees
current_employees = df[df['Status'].str.lower() == 'active']
current_employees['Tenure_Years'] = (pd.to_datetime("today") - current_employees['Join_Date']).dt.days / 365
avg_tenure = round(current_employees['Tenure_Years'].mean(), 2)

training_completed_pct = round((df['Training_Completed'].str.lower() == 'yes').mean() * 100, 2)

avg_leaves_per_dept = df.groupby('Department')['Leaves_Taken'].mean().round(2).reset_index()

# Step 4: Save Summary Metrics
summary = {
    'Total Employees': [total_employees],
    'Attrition Rate (%)': [attrition_rate],
    'Avg Tenure (Years)': [avg_tenure],
    'Training Completion (%)': [training_completed_pct]
}
summary_df = pd.DataFrame(summary)
summary_df.to_csv("summary_metrics.csv", index=False)

# Save avg leaves per department
avg_leaves_per_dept.to_csv("avg_leaves_by_department.csv", index=False)

# Step 5: Optional - Save cleaned data
df.to_excel("cleaned_hr_data.xlsx", index=False, date_format='%Y-%m-%d', engine='openpyxl')

print("Analysis complete. Files saved.")
