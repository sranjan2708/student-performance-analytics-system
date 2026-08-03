from flask import Flask, render_template, request
import pandas as pd 
from charts import create_subject_bar_chart
from analytics import (
    calculate_overall_statistics,
    calculate_subject_statistics
)

app = Flask(__name__)

@app.route("/", methods = ["GET" , "POST"])
def home():

    if request.method == "POST":

        uploaded_file = request.files["marks"]

        df = pd.read_csv(uploaded_file)

        overall_statistics = calculate_overall_statistics(df)

        subject_statistics = calculate_subject_statistics(df)

        # Generate the subject average bar chart

        create_subject_bar_chart(subject_statistics)

        return render_template(
            "index.html",
            message = f"{uploaded_file.filename} uploaded successfully!",
            overall_statistics = overall_statistics,
            subject_statistics = subject_statistics
        )

    return render_template(
        "index.html",
        message = None,
        overall_statistics = None,
        subject_statistics = None
    )


if __name__ == "__main__":
    app.run(debug=True)