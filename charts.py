import matplotlib.pyplot as plt


def create_subject_bar_chart(subject_stats):

    subjects = []

    averages = []

    for subject, stats in subject_stats.items():

        subjects.append(subject)

        averages.append(stats["average"])

    plt.figure(figsize=(8, 5))

    plt.bar(subjects, averages, color="skyblue")

    plt.title("Subject Average Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")

    plt.grid(axis="y")

    plt.tight_layout()

    plt.savefig("static/chart.png")

    plt.close()


def create_pass_fail_pie_chart(overall_statistics):

    pass_count = overall_statistics["pass_count"]
    fail_count = overall_statistics["fail_count"]

    labels = ["pass","Fail"]

    sizes = [pass_count,fail_count]
    plt.figure(figsize=(6,6))

    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        colors=["green", "red"],
        explode=[0, 0.1]
    )

    plt.title("pass vs Fail Students")

    plt.tight_layout()

    plt.savefig("static/pass_fail_chart.png")

    plt.close()


def create_marks_histogram(df):

    marks = df["Total"]

    plt.figure(figsize=(8,5))

    plt.hist(
        marks,
        bins=5,
        color="orange",
        edgecolor="black"
    )

    plt.title("Student Marks Distribution")

    plt.xlabel("Total Marks")
    plt.ylabel("Number of Students")

    plt.grid(axis="y")

    plt.tight_layout()

    plt.savefig("static/marks_histogram.png")

    plt.close()



    