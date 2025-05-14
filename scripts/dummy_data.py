import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import numpy as np

fake = Faker()

# Constants
departments = ['HR', 'Finance', 'IT', 'Marketing', 'Sales']
statuses = ['Active', 'Left']
training_status = ['Yes', 'No']
genders = ['Male', 'Female']
# Employee counts
n = 100  

# Generate employee data
data = []
for i in range(1, n + 1):
    join_date = fake.date_between(start_date='-5y', end_date='-1y')
    has_left = random.choice([True, False])
    left_date = fake.date_between(start_date=join_date, end_date='today') if has_left else None
    status = 'Left' if has_left else 'Active'
    training = random.choices(training_status, weights=[0.7, 0.3])[0]
    leaves_taken = random.randint(5, 25) if status == 'Active' else random.randint(0, 20)
    salary = random.randint(40000, 90000)

    data.append({
        'Employee_ID': f'E{i:03}',
        'Name': fake.name(),
        'Gender': random.choice(genders),
        'Age': random.randint(22, 60),
        'Department': random.choice(departments),
        'Join_Date': join_date,
        'Left_Date': left_date,
        'Status': status,
        'Training_Completed': training,
        'Leaves_Taken': leaves_taken,
        'Salary': salary
    })

df_hr = pd.DataFrame(data)

# Save to CSV
csv_path = r'C:\Users\yousuf\source\DataAnalysisProjects\HR_Process_Automation_Reporting_Tool\data\dummy_data\hr_dummy_data.csv'
df_hr.to_csv(csv_path, index=False)

csv_path
