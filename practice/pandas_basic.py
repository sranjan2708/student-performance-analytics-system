import pandas as pd

# students = {
#     "Name": ["Rahul", "Priya", "Aman", "Rohit", "Sneha"],
#     "Physics": [85, 90, 70, 95, 81],
#     "Maths": [92, 88, 65, 99, 79]
# }

# df = pd.DataFrame(students)

df = pd.read_csv("data/students.csv")
print(df[df["Physics"] > 80][["Name", "Physics"]])