import matplotlib.pyplot as plt

# subjects = ["Math", "Science", "English", "History", "Computer"]
# marks = [78, 85, 72, 80, 91]

# plt.plot(
#     subjects,
#     marks,
#     color="red",
#     marker="o",
#     linestyle="--",
#     linewidth=3,
#     markersize=10
# )

# plt.bar(subjects, marks)

# for i in range(len(subjects)):
#     plt.text(i, marks[i] + 1, marks[i], ha="center")

# plt.title("Subject Marks Comparison")
# plt.xlabel("Subjects")
# plt.ylabel("Average Marks")
# plt.grid()

# plt.show()

##pie chart 

# labels = ["Pass", "Fail"]

# students = [80, 20]

# explode = [0, 0.1]

# plt.pie(
#     students,
#     labels=labels,
#     autopct="%1.1f%%",
#     colors=["green", "red"],
#     explode=explode
# )

# plt.title("Pass vs Fail Students")

# plt.show()

##Histogram


# marks = [45, 52, 56, 61, 65, 67, 70, 72, 74, 75,
#          78, 80, 82, 85, 88, 90, 91, 93, 95, 98]

# plt.hist(
#     marks,
#     bins=5,
#     color="skyblue",
#     edgecolor="black"
# )

# plt.title("Marks Distribution")
# plt.xlabel("Marks")
# plt.ylabel("Number of Students")

# plt.show()

#boxplot

# marks = [45, 52, 55, 60, 62, 65, 68,
#          70, 72, 75, 78, 80, 82, 85, 95]

# plt.boxplot(marks, vert=False)

# plt.title("Student Marks Box Plot")

# plt.ylabel("Marks")

# plt.show()

#saving the figure to send it to the browser 

subjects = ["Math", "Science", "English", "History", "Computer"]

marks = [78, 85, 72, 80, 91]

plt.bar(subjects, marks)

plt.title("Subject Marks Comparison")

plt.xlabel("Subjects")

plt.ylabel("Average Marks")

plt.savefig("static/chart.png")