from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET" , "POST"])
def home():

    if request.method == "POST":

        uploaded_file = request.files["marks"]

        return render_template(
            "index.html",
            message = f"{uploaded_file.filename} uploaded successfully!"
        )

    return render_template("index.html", message=None)


if __name__ == "__main__":
    app.run(debug=True)