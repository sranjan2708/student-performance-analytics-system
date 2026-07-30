from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    students = [
        "Rahul",
        "Priya",
        "Aman",
        "Neha"
    ]
    return render_template("index.html", students = students)

if __name__ == "__main__":
    app.run(debug=True)