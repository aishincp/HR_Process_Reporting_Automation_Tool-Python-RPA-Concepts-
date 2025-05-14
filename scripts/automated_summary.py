import pandas as pd
from openai import OpenAI    

# Read API key from file
with open("api_key.txt", "r") as file:
    api_key = file.read().strip()
# # Load your summary
# summary = pd.read_csv("hr_training_alert_2024.csv")
# summary_text = summary.to_string(index=False)

# key = "api=key will here" 
# # OpenAI API key
client = OpenAI(api_key=api_key)

summary = pd.read_csv("hr_training_alert_2024.csv")
summary_text = summary.to_string(index=False)

# Prepare the GPT prompt
prompt = f"""
You are an assistant helping HR understand training completion stats.

Given this table:

{summary_text}

Write a short natural language summary highlighting:
- Total number of departments
- Total employees with incomplete training
- Department with the highest number

Be professional but concise.
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
)

gpt_summary = response.choices[0].message.content.strip()

print("\nAgentic Summary:\n")
print(gpt_summary)


with open("automated_summary.txt", "w") as file:
    file.write(gpt_summary)
'''
How to add in this in my file "automated_email.py"

You’ve now added AI to your automation system.

You can now insert this summary into your email instead of plain tables!
'''