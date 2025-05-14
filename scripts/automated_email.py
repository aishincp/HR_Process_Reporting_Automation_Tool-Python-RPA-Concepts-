import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load summary
df = pd.read_csv("hr_training_alert_2024.csv")
summary_text = df.to_string(index=False)

# Email details
sender_email = "aishinahmed20@gmail.com"          # Replace with your Gmail
receiver_email = "yousufali.n@gmail.com"       # Replace with recipient email
app_password = "kudn bymk ozhu hfqh"        # Paste the 16-character Gmail App Password

# Email content
subject = "Automated HR Training Summary - 2024"
body = f"""
Hello HR Team,

Here is the list of department(s) with employee(s) details who have NOT completed their training (Joined in 2024):

{summary_text}

Please check the Power BI dashboard for full employee-level insights.

Regards,
Automated Reporting Team 🤖
"""

# Create email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Send email using Gmail SMTP
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)
        print("Email sent successfully!")
except Exception as e:
    print("Failed to send email:", e)
