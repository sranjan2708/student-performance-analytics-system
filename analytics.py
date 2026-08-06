import pandas as pd

# =====================================================
# Constants
# =====================================================

PASS_MARKS = 40


# =====================================================
# Detect Subject Columns
# =====================================================

def get_subject_columns(df):
    """
    Detects all subject columns automatically.

    Any numeric column except 'Total'
    is treated as a subject.
    """

    excluded_columns = [
        "Total",
        "Average",
        "Percentage"
    ]

    subject_columns = []

    for column in df.columns:

        if (
            pd.api.types.is_numeric_dtype(df[column])
            and column not in excluded_columns
        ):

            subject_columns.append(column)

    return subject_columns


# =====================================================
# Overall Statistics
# =====================================================

def calculate_overall_statistics(df):

    """
    Calculates

    • Total Students
    • Pass Count
    • Fail Count
    • Overall Average
    • Highest Score
    • Lowest Score
    • Topper
    """

    overall_statistics = {}

    subject_columns = get_subject_columns(df)

    total_students = len(df)

    overall_statistics["total_students"] = total_students


    # -----------------------------------------
    # Calculate Total
    # -----------------------------------------

    if "Total" not in df.columns:

        df["Total"] = df[subject_columns].sum(axis=1)


    # -----------------------------------------
    # Pass / Fail Calculation
    # -----------------------------------------

    pass_count = 0

    fail_count = 0


    for _, row in df.iterrows():

        is_pass = True

        for subject in subject_columns:

            if row[subject] < PASS_MARKS:

                is_pass = False

                break

        if is_pass:

            pass_count += 1

        else:

            fail_count += 1


    overall_statistics["pass_count"] = pass_count

    overall_statistics["fail_count"] = fail_count


    # -----------------------------------------
    # Overall Analytics
    # -----------------------------------------

    overall_statistics["overall_average"] = round(
        df["Total"].mean(),
        2
    )

    overall_statistics["highest_total"] = df["Total"].max()

    overall_statistics["lowest_total"] = df["Total"].min()


    # -----------------------------------------
    # Detect Name Column
    # -----------------------------------------

    if "Name" in df.columns:

        overall_statistics["topper"] = df.loc[
            df["Total"].idxmax(),
            "Name"
        ]

    else:

        overall_statistics["topper"] = "N/A"

    return overall_statistics


# =====================================================
# Subject Statistics
# =====================================================

def calculate_subject_statistics(df):

    """
    Calculates

    • Average
    • Highest
    • Lowest

    for every detected subject.
    """

    subject_statistics = {}

    subject_columns = get_subject_columns(df)


    for subject in subject_columns:

        subject_statistics[subject] = {

            "average": round(
                df[subject].mean(),
                2
            ),

            "highest": df[subject].max(),

            "lowest": df[subject].min()

        }

    return subject_statistics