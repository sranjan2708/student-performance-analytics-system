from flask import Flask, render_template, request, session
import pandas as pd
import os

from charts import (
    create_subject_bar_chart,
    create_pass_fail_pie_chart,
    create_marks_histogram
)

from analytics import (
    calculate_overall_statistics,
    calculate_subject_statistics
)

app = Flask(__name__)

app.secret_key = "student-performance-secret"


# =====================================================
# Home Route
# =====================================================

@app.route("/", methods=["GET", "POST"])
def home():

    # ==========================================
    # GET Request
    # ==========================================

    if request.method == "GET":

        return render_template("index.html")


    # ==========================================
    # POST Request
    # ==========================================

    uploaded_file = request.files["marks"]


    # ==========================================
    # Validation 1 : File Selected
    # ==========================================

    if uploaded_file.filename == "":

        return render_template(
            "index.html",
            message="Please select a CSV file."
        )


    # ==========================================
    # Validation 2 : CSV File Check
    # ==========================================

    if not uploaded_file.filename.lower().endswith(".csv"):

        return render_template(
            "index.html",
            message="Please upload a valid CSV file."
        )


    # ==========================================
    # Save Uploaded File
    # ==========================================

    file_path = os.path.join(
        "uploads",
        uploaded_file.filename
    )

    uploaded_file.save(file_path)

    session["file_path"] = file_path


    # ==========================================
    # Read CSV File
    # ==========================================

    try:

        df = pd.read_csv(file_path)

    except Exception:

        return render_template(
            "index.html",
            message="Unable to read the CSV file. Please upload a valid CSV."
        )


    # ==========================================
    # Calculate Analytics
    # ==========================================

    overall_statistics = calculate_overall_statistics(df)

    subject_statistics = calculate_subject_statistics(df)


    # ==========================================
    # Convert Student Data for Jinja
    # ==========================================

    student_records = df.to_dict(
        orient="records"
    )


    # ==========================================
    # Generate Charts
    # ==========================================

    create_subject_bar_chart(subject_statistics)

    create_pass_fail_pie_chart(overall_statistics)

    create_marks_histogram(df)


    # ==========================================
    # Render Dashboard
    # ==========================================

    return render_template(
        "dashboard.html",
        message=f"{uploaded_file.filename} uploaded successfully!",
        overall_statistics=overall_statistics,
        subject_statistics=subject_statistics,
        student_records=student_records
    )


# =====================================================
# Student Search Route
# =====================================================

@app.route("/search", methods=["POST"])
def search_student():

    # ==========================================
    # Get Student Name
    # ==========================================

    search_name = request.form["student_name"].strip()


    # ==========================================
    # Get Saved File Path
    # ==========================================

    file_path = session.get("file_path")


    # ==========================================
    # Check Whether File Exists
    # ==========================================

    if not file_path or not os.path.exists(file_path):

        return render_template(
            "index.html",
            message="Please upload a CSV file first."
        )


    # ==========================================
    # Read Saved CSV
    # ==========================================

    try:

        df = pd.read_csv(file_path)

    except Exception:

        return render_template(
            "index.html",
            message="Unable to read the saved CSV file."
        )


    # ==========================================
    # Calculate Dashboard Statistics
    # ==========================================

    overall_statistics = calculate_overall_statistics(df)

    subject_statistics = calculate_subject_statistics(df)


    # ==========================================
    # Convert Student Data for Jinja
    # ==========================================

    student_records = df.to_dict(
        orient="records"
    )


    # ==========================================
    # Search Student
    # ==========================================

    student = df[
        df["Name"].astype(str).str.lower() == search_name.lower()
    ]


    # ==========================================
    # Student Not Found
    # ==========================================

    if student.empty:

        return render_template(
            "dashboard.html",
            message=f"No student found with the name '{search_name}'.",
            message_type="error",
            overall_statistics=overall_statistics,
            subject_statistics=subject_statistics,
            student_records=student_records
        )


    # ==========================================
    # Convert Student Row to Dictionary
    # ==========================================

    student_data = student.iloc[0].to_dict()


    # ==========================================
    # Display Student Details
    # ==========================================

    return render_template(
        "student.html",
        student=student_data
    )


# =====================================================
# Student Filter and Sort Route
# =====================================================

@app.route("/filter", methods=["POST"])
def filter_students():

    # ==========================================
    # Get Saved File Path
    # ==========================================

    file_path = session.get("file_path")


    # ==========================================
    # Check Whether File Exists
    # ==========================================

    if not file_path or not os.path.exists(file_path):

        return render_template(
            "index.html",
            message="Please upload a CSV file first."
        )


    # ==========================================
    # Read Saved CSV
    # ==========================================

    try:

        df = pd.read_csv(file_path)

    except Exception:

        return render_template(
            "index.html",
            message="Unable to read the saved CSV file."
        )


    # ==========================================
    # Get Filter Value
    # ==========================================

    result_filter = request.form["result_filter"]


    # ==========================================
    # Apply Filter
    # ==========================================

    if result_filter == "Pass":

        filtered_df = df[
            df["Result"] == "Pass"
        ]

    elif result_filter == "Fail":

        filtered_df = df[
            df["Result"] == "Fail"
        ]

    else:

        filtered_df = df


    # ==========================================
    # Get Sorting Values
    # ==========================================

    sort_by = request.form["sort_by"]

    sort_order = request.form["sort_order"]


    # ==========================================
    # Determine Sorting Order
    # ==========================================

    if sort_order == "ascending":

        ascending = True

    else:

        ascending = False


    # ==========================================
    # Apply Sorting
    # ==========================================

    filtered_df = filtered_df.sort_values(
        by=sort_by,
        ascending=ascending
    )


    # ==========================================
    # Calculate Dashboard Statistics
    # ==========================================

    overall_statistics = calculate_overall_statistics(df)

    subject_statistics = calculate_subject_statistics(df)


    # ==========================================
    # Convert Filtered and Sorted Data for Jinja
    # ==========================================

    student_records = filtered_df.to_dict(
        orient="records"
    )


    # ==========================================
    # Render Dashboard
    # ==========================================

    return render_template(
        "dashboard.html",
        message=(
            f"Showing {result_filter} students "
            f"sorted by {sort_by}."
        ),
        overall_statistics=overall_statistics,
        subject_statistics=subject_statistics,
        student_records=student_records
    )


# =====================================================
# Run Application
# =====================================================

if __name__ == "__main__":

    app.run(debug=True)