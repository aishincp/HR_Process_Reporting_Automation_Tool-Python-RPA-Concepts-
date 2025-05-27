# HR Process Reporting Automation Tool 
### Automated HR reporting solution (Power BI + Python + RPA + SMTP auto-send email trigger automation)

---

This project demonstrates a practical and automated HR reporting solution that combines Python, Power BI, and Robotic Process Automation (RPA). It simulates a common HR use case—tracking mandatory training completion—using dummy data, smart visualizations, and automated email alerts.

---

![image](https://github.com/user-attachments/assets/baaff798-6d79-41df-8f85-3a93d0f7be59)

---

## Project Overview

In HR departments, keeping track of employee training compliance can be tedious and prone to delays (a hectic manual task). This project simplifies that by:

- Generating and analyzing HR data with Python (**Automated Analysis**)
- Visualizing key insights in Power BI (**Reporting & Dashboarding**)
- Automatically emailing alerts using Python scripting  (**Automated Email Notification**) 
- Triggering the workflow weekly using Windows Task Scheduler  (**Automated Trigger**)

This end-to-end automated workflow mimics real workplace needs and enhances efficiency, data accessibility, and decision-making.

---

### Step 1: Dummy HR Data Generation

To simulate a realistic environment, I created a synthetic HR dataset including the following fields:

- Employee Name  
- Department  
- Join Date  
- Tenure  
- Leaves Taken  
- Training Status  

I also included cases where some employees had not completed their mandatory training—allowing us to track compliance issues like in real HR audits.

---

### Step 2: Data Cleaning & Preparation (Python)

I used Python and Pandas to process the data in `scripts/alert_summary.py`.

### Key Tasks:
- Converted the **Join Date** into a **Join Year** using `pd.to_datetime()`.
- Filtered employees who:
  - Joined in **2024**
  - Had **"Not Completed"** training status

    ```python
    filtered_df = df[
        (df['Join_Year'] == 2024) & 
        (df['Training Status'] == 'Not Completed')
    ]
    ```

- Grouped the filtered data by department to summarize non-compliant cases
- Exported this summary as a CSV file:

### *This prepared dataset serves as the basis for both visualization and automation.*

### Step 3: Power BI Dashboard Creation

![image](https://github.com/user-attachments/assets/0a0885f2-44b7-483e-ad8c-0dcb4bb5a6c4)

A. Using Power BI, I built an interactive dashboard that allows HR managers to:

- Monitor training completion status
- Filter employees by year and training status
- Explore department-wise trends

B. Visuals Included:
- Bar Chart: Employees per department
- Pie Chart: Completed vs Not Completed training
- Line Chart: Join year trends

C. Table View: Detailed employee list with training status

📸 [Insert Power BI Dashboard Screenshot Here]

### *This dashboard empowers decision-makers to take action based on real-time (if using real-time data) insights.*


### Step 4: Email Automation via Python
To ensure stakeholders receive timely updates, I created scripts/automated_email.py which:

- Reads the department-wise summary from the CSV
- Formats the output into a readable email body using to_string()
- Sends the summary via email using Gmail's SMTP server

    ```python
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login("your_email@gmail.com", "your_app_password")
        server.send_message(ms
    ```

 ### *Result: A professional summary email lands in the inbox—no manual steps required.*

### Step 5: Automation via Windows Task Scheduler

See the Screenshot below:

![image](https://github.com/user-attachments/assets/96564446-eb73-47de-82c3-22f7a6d0e28b)

To automate the weekly reporting process without any manual effort, I created a Windows batch file (run_email_alert.bat) that runs the email script [See the screenshot below].

![image](https://github.com/user-attachments/assets/45c6df2b-6c2e-4cbb-9d87-e0e6104c3080)

This batch file eliminates the need to manually run the Python script each time. Instead of scheduling the Python file directly, the Task Scheduler runs this .bat file, which:
- Activates the correct virtual environment
- Runs the automated_email.py script with the appropriate interpreter
- Ensures consistent execution, even when no user is logged in

This setup provides a lightweight but effective RPA-style automation, ensuring HR summary emails are delivered regularly (e.g., every Monday at 10 AM) without human intervention.


---

Note 
---

#### *This project reflects my interest in solving real-world problems through automation and analytics, as well as building agents or RPA systems to automate tasks with minimal or low-code. It brings my technical skills together with practical implementation and a focus on user-centric delivery, a foundation I look forward to building upon in future roles.*

