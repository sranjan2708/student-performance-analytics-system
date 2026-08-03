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