import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

subjects = [
    "Maths",
    "Physics",
    "Chemistry",
    "English"
]

averages = [
    78,
    85,
    72,
    90
]

sns.barplot(
    x=subjects,
    y=averages
)
plt.title("Subject Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()