import pandas as pd

PASS_MARKS = 40

SUBJECTS = [
    "Maths",
    "Physics",
    "Chemistry",
    "English"
]

def calculate_overall_statistics(df):
    total_students = len(df)
    overall_statistics = {}

    overall_statistics["total_students"] = total_students
    
    df["Total"] = df[SUBJECTS].sum(axis=1)

    pass_count = 0
    fail_count = 0

    for index, row in df.iterrows():

        is_pass = True

        for subject in SUBJECTS:
            if row[subject] < PASS_MARKS:
                is_pass = False
                break

        if is_pass:
            pass_count += 1
        else:
            fail_count += 1

    overall_statistics["pass_count"] = pass_count
    overall_statistics["fail_count"] = fail_count

    overall_statistics["overall_average"] = round(df["Total"].mean(), 2)
    overall_statistics["highest_total"] = df["Total"].max()
    overall_statistics["lowest_total"] = df["Total"].min()
    overall_statistics["topper"] = df.loc[df["Total"].idxmax(), "Name"]


    return overall_statistics


def calculate_subject_statistics(df):
    subject_statistics = {}

    for subject in SUBJECTS:

        average = round(df[subject].mean(), 2)
        highest = df[subject].max()
        lowest = df[subject].min()

        subject_statistics[subject] = {
            "average" : average,
            "highest" : highest,
            "lowest"  : lowest
        }
    return subject_statistics