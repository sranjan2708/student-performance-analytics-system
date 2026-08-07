from flask import Flask, render_template, request
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




    # ==========================================
    # Read CSV File
    # ==========================================

    try:

        df = pd.read_csv(uploaded_file)

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
        subject_statistics=subject_statistics
    )


# =====================================================
# Run Application
# =====================================================

if __name__ == "__main__":
    app.run(debug=True)