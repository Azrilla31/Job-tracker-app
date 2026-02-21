from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

def load_jobs():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        return json.load(f)

def save_jobs(jobs):
    with open(DATA_FILE, "w") as f:
        json.dump(jobs, f, indent=2)

@app.route("/")
def home():
    jobs = load_jobs()
    return render_template("index.html", jobs=jobs)

@app.route("/add", methods=["POST"])
def add():
    jobs = load_jobs()
    jobs.append({
        "company": request.form["company"],
        "role": request.form["role"],
        "status": "Applied"
    })
    save_jobs(jobs)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
