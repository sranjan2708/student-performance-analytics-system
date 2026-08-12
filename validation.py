import pandas as pd


# =====================================================
# Required CSV Columns
# =====================================================

REQUIRED_COLUMNS = [
    "Name",
    "Math",
    "Science",
    "English",
    "Total",
    "Average",
    "Result"
]


# =====================================================
# Validate Student Dataset
# =====================================================

def validate_student_data(df):

    # ==========================================
    # Check Empty Dataset
    # ==========================================

    if df.empty:

        return False, "The CSV file is empty."


    # ==========================================
    # Check Required Columns
    # ==========================================

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]


    if missing_columns:

        return False, (
            "Missing required columns: "
            + ", ".join(missing_columns)
        )


    # ==========================================
    # Check Numeric Columns
    # ==========================================

    numeric_columns = [
        "Math",
        "Science",
        "English",
        "Total",
        "Average"
    ]


    for column in numeric_columns:

        if not pd.api.types.is_numeric_dtype(
            df[column]
        ):

            return False, (
                f"Column '{column}' must contain numeric values."
            )


    # ==========================================
    # Check Marks Range
    # ==========================================

    subject_columns = [
        "Math",
        "Science",
        "English"
    ]


    for column in subject_columns:

        if (
            (df[column] < 0).any()
            or
            (df[column] > 100).any()
        ):

            return False, (
                f"Marks in '{column}' must be between 0 and 100."
            )


    # ==========================================
    # Check Result Values
    # ==========================================

    valid_results = [
        "Pass",
        "Fail"
    ]


    if not df["Result"].isin(
        valid_results
    ).all():

        return False, (
            "Result column must contain only "
            "'Pass' or 'Fail'."
        )


    # ==========================================
    # Validation Successful
    # ==========================================

    return True, "CSV file is valid."