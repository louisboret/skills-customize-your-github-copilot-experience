from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = []

@app.route("/")
def index():
    return render_template("index.html", students=students)

@app.route("/add-student", methods=["GET", "POST"])
def add_student():
    error = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        grade = request.form.get("grade", "").strip()

        if not name or not grade:
            error = "Please enter both a name and a grade."
        else:
            students.append({"name": name, "grade": grade})
            return redirect(url_for("index"))

    return render_template("add_student.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)
