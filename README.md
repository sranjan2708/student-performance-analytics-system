# Student Performance Analytics System

A Flask-based web application for uploading student performance CSV files, performing academic analytics, visualizing results, searching individual students, maintaining report history, and generating downloadable reports.

---

## 📌 Overview

The **Student Performance Analytics System** is designed to turn raw student performance data stored in CSV files into useful academic insights.

The application allows a user to:

- Upload a student performance CSV file
- Validate the uploaded dataset
- Calculate overall performance statistics
- Analyze subject-wise performance dynamically
- Visualize student performance using charts
- Search for individual students
- View detailed student performance reports
- Store report history using SQLite
- View previously generated reports
- Export report data
- Generate PDF performance reports
- Handle invalid input and application errors
- Maintain application logs

The application is built using Flask, Pandas, SQLite, Matplotlib, Seaborn, and Jinja2.

---

## 🎯 Problem Statement

Educational performance data is often stored as raw tabular data, making it difficult to quickly understand overall student performance or identify individual academic trends.

This project provides a simple web-based analytics system that converts uploaded CSV data into:

- Overall statistics
- Subject-wise analysis
- Performance visualizations
- Individual student reports
- Historical reports
- Downloadable PDF and CSV outputs

---

## ✨ Features

### 1. CSV Upload

Users can upload student performance datasets through the web interface.

The application:

1. Receives the uploaded CSV file
2. Validates the file
3. Saves the file
4. Reads the dataset using Pandas
5. Calculates analytics
6. Displays the dashboard

---

### 2. Data Validation

The project contains centralized validation functionality.

Validation helps ensure that uploaded datasets contain the required structure and valid data before analytics are performed.

The project includes:

```text
validation.py
```

This keeps validation logic separate from the main Flask application.

---

### 3. Overall Performance Analytics

The system calculates important statistics such as:

- Total number of students
- Average marks
- Highest score
- Lowest score
- Pass count
- Fail count
- Topper information

These values are displayed on the dashboard.

---

### 4. Dynamic Subject Analysis

Subject information is derived from the uploaded dataset rather than permanently depending on a fixed list of subjects.

This allows the system to work with datasets containing different subjects.

For example:

```text
Mathematics
Science
English
```

or:

```text
Physics
Chemistry
Biology
Economics
```

The analytics system can work with the subjects present in the uploaded CSV.

---

### 5. Performance Visualization

The project generates graphical representations of student performance.

Current visualizations include:

- Student performance chart
- Marks histogram
- Pass/fail chart

Chart generation is handled separately through:

```text
charts.py
```

The project also contains Seaborn practice/visualization work.

---

### 6. Individual Student Search

Users can search for a specific student by name.

The system:

1. Reads the currently uploaded dataset
2. Searches for the student
3. Converts the matching record into a dictionary
4. Displays an individual performance report

The student report includes information such as:

- Student name
- Total marks
- Average
- Result
- Subject performance

---

### 7. Dashboard

The dashboard provides a central place for viewing the uploaded dataset and its analytics.

It includes:

- Overall statistics
- Subject statistics
- Performance charts
- Student records
- Student search
- Export functionality
- PDF report generation
- Navigation to report history

---

### 8. SQLite Report History

The application uses SQLite to maintain report history.

Database file:

```text
student_analytics.db
```

Database-related functionality is separated into:

```text
database.py
```

The history system stores information such as:

- Report ID
- Filename
- Upload date
- Total students
- Average marks
- Highest marks
- Lowest marks
- Pass count
- Fail count
- Topper

Users can:

- View report history
- Open report details
- Delete reports

---

### 9. PDF Report Generation

The project supports generating a PDF report from the analyzed student data.

PDF functionality is handled through:

```text
pdf_report.py
```

Generated reports can be stored in the uploads directory.

Example:

```text
uploads/student_performance_report.pdf
```

---

### 10. CSV Export

The application provides export functionality so that analyzed student data can be downloaded as CSV output.

This makes the analytics results reusable outside the application.

---

### 11. Error Handling

The application includes custom error pages for application errors.

Current error templates include:

```text
404.html
500.html
```

These provide a better user experience than displaying raw server errors.

---

### 12. Logging

Application activity is recorded using Python logging.

Log file:

```text
logs/app.log
```

The application records useful events such as:

- Application startup
- File upload
- CSV reading
- Analytics calculation
- Request activity
- Errors and warnings

Logging helps with debugging and application monitoring.

---

### 13. Dashboard Navigation & UX

The project includes navigation between:

```text
Upload
   ↓
Dashboard
   ├── Student Search
   │      ↓
   │   Student Details
   │      ↓
   │   Dashboard
   │
   └── Report History
          ↓
      Report Details
          ↓
       Dashboard
```

The dashboard session is preserved so that users do not have to repeatedly upload the same CSV file simply to search another student or navigate through reports.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Web application framework |
| Pandas | Data processing and analytics |
| SQLite | Report history database |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Jinja2 | HTML templating |
| HTML | Web page structure |
| CSS | User interface styling |

---

## 🏗️ Project Architecture

The application follows a modular structure where different responsibilities are separated into different Python files.

```text
                    ┌─────────────────────┐
                    │       Browser       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Flask App      │
                    │       app.py        │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
       │   Pandas    │  │ Validation  │  │   SQLite    │
       │  Analytics  │  │ validation  │  │  Database   │
       └─────────────┘  │    .py      │  │ database.py │
                        └─────────────┘  └─────────────┘
              │
              ▼
       ┌─────────────┐
       │   Charts    │
       │  charts.py  │
       └─────────────┘
              │
              ▼
       ┌─────────────┐
       │ PDF Reports │
       │pdf_report.py│
       └─────────────┘
              │
              ▼
       ┌─────────────┐
       │ Jinja2 HTML │
       │  Templates  │
       └─────────────┘
```

---

## 📂 Project Structure

```text
Student Performance Analytics System/
│
├── data/
│
├── logs/
│   └── app.log
│
├── practice/
│   └── pandas_basic.py
│
├── static/
│   ├── chart.png
│   ├── marks_histogram.png
│   ├── pass_fail_chart.png
│   └── style.css
│
├── templates/
│   ├── 404.html
│   ├── 500.html
│   ├── dashboard.html
│   ├── history.html
│   ├── report_details.html
│   ├── student.html
│   └── ...
│
├── uploads/
│   ├── *.csv
│   └── *.pdf
│
├── analytics.py
├── app.py
├── charts.py
├── database.py
├── pdf_report.py
├── practice.py
├── requirements.txt
├── seaborn_basic.py
├── validation.py
├── .gitignore
└── student_analytics.db
```

> `venv/`, `__pycache__/`, generated files, and other local runtime artifacts should be excluded from Git using `.gitignore` where appropriate.

---

## 🔄 Application Workflow

```text
User
 │
 ▼
Upload CSV
 │
 ▼
Validation
 │
 ├── Invalid → Error Message
 │
 ▼
Save Uploaded File
 │
 ▼
Read CSV using Pandas
 │
 ▼
Calculate Analytics
 │
 ├── Overall Statistics
 │
 ├── Subject Statistics
 │
 └── Student Records
 │
 ▼
Generate Charts
 │
 ▼
Store Report Metadata in SQLite
 │
 ▼
Dashboard
 │
 ├── Search Student
 │
 ├── Filter Data
 │
 ├── Export CSV
 │
 ├── Generate PDF
 │
 └── Report History
```

---

## 📊 Analytics

The analytics layer is implemented primarily through:

```text
analytics.py
```

The system processes uploaded student data and calculates meaningful academic statistics.

The application separates analytics logic from Flask routing so that data-processing functionality is easier to maintain and reuse.

---

## 🗄️ Database

SQLite is used for persistent report history.

Database:

```text
student_analytics.db
```

The database layer is implemented in:

```text
database.py
```

The database stores report-level information rather than replacing the uploaded CSV as the primary student dataset.

This allows the application to maintain a history of generated reports.

---

## 📄 Reporting

The application supports two major output formats:

### CSV

Used for exporting analyzed student records.

### PDF

Used for generating a formatted student performance report.

PDF generation is handled by:

```text
pdf_report.py
```

---

## ✅ Validation & Error Handling

The project uses centralized validation logic through:

```text
validation.py
```

This improves consistency by keeping validation rules separate from the Flask routes.

The application also provides dedicated error pages:

```text
404.html
500.html
```

---

## 📝 Logging

Logging is configured in the Flask application and writes application events to:

```text
logs/app.log
```

Example logged events include:

```text
Application started
File uploaded successfully
CSV file read successfully
Analytics calculated successfully
```

Logging makes it easier to diagnose application behavior without relying only on terminal output.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project

```bash
cd Student-Performance-Analytics-System
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```bash
venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

The development server will normally be available at:

```text
http://127.0.0.1:5000
```

Open that address in your browser.

---

## 💻 How to Use

### Step 1 — Upload Dataset

Open the application and select a valid CSV file.

### Step 2 — Generate Analytics

Upload the file and allow the system to process the dataset.

### Step 3 — Explore Dashboard

Review:

- Overall statistics
- Subject statistics
- Charts
- Student records

### Step 4 — Search Student

Enter a student name in the search section.

### Step 5 — View Individual Report

Open the student's detailed academic performance page.

### Step 6 — Export / Generate PDF

Use the available reporting options to download the analyzed information.

### Step 7 — View Report History

Open Report History to view previously generated report records.

---

## 📸 Screenshots

Add project screenshots here when preparing the final GitHub repository.

Recommended screenshots:

```text
1. Upload page
2. Dashboard
3. Analytics charts
4. Student details page
5. Report history
6. Report details
7. Generated PDF
```

Example Markdown:

```markdown
![Dashboard](screenshots/dashboard.png)
```

---

## 🔮 Future Improvements

Possible future enhancements include:

- User authentication
- Role-based access
- More advanced filtering
- Interactive charts
- Cloud deployment
- REST API support
- Improved responsive design
- Pagination for large datasets
- Advanced student performance prediction
- Machine learning based performance forecasting

---

## 🎤 Interview Explanation

### Short Explanation

> "Student Performance Analytics System is a Flask-based web application that allows users to upload student performance CSV files and automatically generate academic analytics. I used Pandas for data processing, Matplotlib and Seaborn for visualization, SQLite for maintaining report history, and Jinja2 for rendering the frontend. The system supports student-level search, dynamic subject analysis, CSV export, PDF report generation, validation, centralized error handling, logging, and report history. I structured the project into separate modules for analytics, database operations, chart generation, PDF generation, and validation to keep the application maintainable."

### Key Interview Topics

Be prepared to explain:

- Why Flask was used
- How CSV uploads work
- How Pandas processes the dataset
- How dynamic subjects are detected
- How analytics are calculated
- Why SQLite was selected
- How Flask sessions are used
- How Jinja2 passes backend data to HTML
- How charts are generated
- How PDF reports are generated
- Why validation is centralized
- Why logging is useful
- How error handling works
- How report history works
- How the application is structured into modules

---

## 👨‍💻 Author

**Sudhansu Ranjan**

Building Reliable Backend Systems with Python, Flask & FastAPI
