# Student Performance Analytics System

A Flask-based web application for uploading student performance CSV files, performing academic analytics, visualizing results, searching individual students, maintaining report history, and generating downloadable reports.

---

## 📌 Overview

The **Student Performance Analytics System** converts raw student performance data stored in CSV files into useful academic insights through a web-based dashboard.

The application allows users to:

- Upload student performance CSV files
- Validate uploaded datasets
- Calculate overall performance statistics
- Analyze subject-wise performance dynamically
- Generate performance visualizations
- Search for individual students
- View detailed student performance reports
- Maintain report history using SQLite
- View previously generated reports
- Export analyzed data as CSV
- Generate PDF performance reports
- Handle invalid input and application errors
- Maintain application logs

---

## 🎯 Problem Statement

Educational performance data is often stored as raw tabular data, making it difficult to quickly understand overall student performance or identify individual academic trends.

This project provides a web-based analytics system that converts uploaded CSV data into:

- Overall performance statistics
- Subject-wise analysis
- Performance visualizations
- Individual student reports
- Historical reports
- Downloadable CSV and PDF outputs

---

## ✨ Features

### 1. CSV Upload

Users can upload student performance datasets through the web interface.

The application:

1. Receives the uploaded CSV file
2. Validates the dataset
3. Saves the uploaded file
4. Reads the dataset using Pandas
5. Calculates analytics
6. Displays the dashboard

---

### 2. Data Validation

The project contains centralized validation functionality in:

```text
validation.py
```

Validation helps ensure that uploaded datasets have the required structure and valid data before analytics are performed.

---

### 3. Overall Performance Analytics

The system calculates important academic statistics such as:

- Total number of students
- Average marks
- Highest score
- Lowest score
- Pass count
- Fail count
- Topper information

These statistics are displayed on the dashboard.

---

### 4. Dynamic Subject Analysis

Subject information is derived from the uploaded dataset rather than relying permanently on a fixed list of subjects.

This allows the system to work with datasets containing different subjects, such as:

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

---

### 5. Performance Visualization

The project generates graphical representations of student performance using Matplotlib and Seaborn.

Current visualizations include:

- Student performance chart
- Marks histogram
- Pass/fail chart

Chart-related functionality is implemented in:

```text
charts.py
```

---

### 6. Individual Student Search

Users can search for a specific student by name.

The system:

1. Reads the currently uploaded dataset
2. Searches for the student
3. Converts the matching record into a dictionary
4. Displays an individual performance report

The student report includes:

- Student name
- Total marks
- Average
- Result
- Subject performance

---

### 7. Dashboard

The dashboard provides a central place for exploring the uploaded dataset and its analytics.

It includes:

- Overall statistics
- Subject statistics
- Performance charts
- Student records
- Student search
- Filtering and sorting
- CSV export
- PDF generation
- Report history navigation

---

### 8. SQLite Report History

The application uses SQLite to maintain report history.

Database functionality is implemented in:

```text
database.py
```

The database stores report-level information such as:

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

The SQLite database is generated locally at runtime and is intentionally excluded from Git.

---

### 9. PDF Report Generation

The project supports generating PDF reports from analyzed student performance data.

PDF functionality is implemented in:

```text
pdf_report.py
```

Generated PDF files are stored locally and are excluded from Git.

---

### 10. CSV Export

The application provides CSV export functionality so that analyzed student records can be downloaded and reused outside the application.

---

### 11. Error Handling

The application includes dedicated error pages for common HTTP errors:

```text
templates/404.html
templates/500.html
```

This provides a better user experience than exposing raw server errors.

---

### 12. Logging

Application activity is recorded using Python logging.

Logs are stored locally in:

```text
logs/
```

The logs directory is intentionally excluded from Git because log files are runtime-generated data.

---

### 13. Dashboard Navigation & UX

The application provides consistent navigation between the upload page, dashboard, student details, report history, and report details.

```text
Upload CSV
    ↓
Dashboard
    ├── Search Student
    │      ↓
    │  Student Details
    │      ↓
    │  Dashboard
    │
    └── Report History
           ↓
       Report Details
           ↓
        Dashboard
```

The application keeps the currently uploaded CSV path in the session so that users can continue working with the same dataset without repeatedly uploading it.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Web application framework |
| Pandas | Data processing and analytics |
| NumPy | Numerical operations |
| SQLite | Report history database |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| ReportLab | PDF report generation |
| Jinja2 | Server-side HTML templating |
| HTML | Web page structure |
| CSS | User interface styling |

---

## 🏗️ Project Architecture

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
       │ analytics.py│  │    .py      │  │ database.py │
       └─────────────┘  └─────────────┘  └─────────────┘
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
├── practice/
│   └── pandas_basic.py
│
├── static/
│   └── style.css
│
├── templates/
│   ├── 404.html
│   ├── 500.html
│   ├── dashboard.html
│   ├── history.html
│   ├── index.html
│   ├── report_details.html
│   └── student.html
│
├── uploads/
│   └── Runtime-generated uploads
│
├── logs/
│   └── Runtime-generated logs
│
├── analytics.py
├── app.py
├── charts.py
├── database.py
├── pdf_report.py
├── practice.py
├── seaborn_basic.py
├── validation.py
├── requirements.txt
├── README.md
└── .gitignore
```

> Runtime-generated files such as uploaded CSV/PDF files, logs, SQLite databases, generated chart images, virtual environments, and Python cache files are excluded from Git using `.gitignore`.

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
 ├── Filter / Sort
 │
 ├── Export CSV
 │
 ├── Generate PDF
 │
 └── Report History
```

---

## 📊 Analytics

Analytics functionality is implemented primarily through:

```text
analytics.py
```

The system processes uploaded student data and calculates meaningful academic statistics.

The analytics logic is separated from Flask routing to keep data-processing responsibilities modular and maintainable.

---

## 🗄️ Database

SQLite is used for persistent report history.

The database layer is implemented in:

```text
database.py
```

The database stores report-level information rather than replacing the uploaded CSV as the primary student dataset.

The local SQLite database is ignored by Git:

```gitignore
*.db
```

---

## 📄 Reporting

The application supports two major output formats:

### CSV

Used for exporting analyzed student records.

### PDF

Used for generating formatted performance reports.

PDF generation is implemented in:

```text
pdf_report.py
```

Generated reports are runtime files and are excluded from Git.

---

## ✅ Validation & Error Handling

The project uses centralized validation logic through:

```text
validation.py
```

This keeps validation rules separate from Flask route handling.

The application also provides:

```text
404.html
500.html
```

for dedicated error responses.

---

## 📝 Logging

Application logging is configured in Flask and writes runtime events to:

```text
logs/app.log
```

Examples of logged events include:

```text
Application started
File uploaded successfully
CSV file read successfully
Analytics calculated successfully
```

The `logs/` directory is excluded from Git.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/sranjan2708/student-performance-analytics-system.git
```

### 2. Open the project

```bash
cd student-performance-analytics-system
```

### 3. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```powershell
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Flask application:

```powershell
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

Use the available reporting options to download analyzed information.

### Step 7 — View Report History

Open Report History to view previously generated reports.

---

## 📸 Screenshots

The GitHub repository can be enhanced with screenshots of the main application pages.

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

Example:

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
- Machine learning based performance prediction
- Advanced student performance forecasting

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