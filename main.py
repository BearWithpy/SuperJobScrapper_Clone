from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("Superscrapper")

db = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/report")
def report():
    # print(request.args.get("word"))
    keyword = request.args.get("word")
    if keyword:
        keyword = keyword.lower()
        existing_jobs = db.get(keyword)

        if existing_jobs:
            jobs = existing_jobs
        else:
            jobs = get_jobs(keyword)
            db[keyword] = jobs

    else:
        return redirect("/")

    return render_template(
        "report.html", searchingBy=keyword, resultsNumber=len(jobs), jobs=jobs
    )


@app.route("/export")
def export():
    try:
        keyword = request.args.get("word")
        if not keyword:
            raise Exception()
        keyword = keyword.lower()
        jobs = db.get(keyword)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")


# Hello! Welcome to mi casa!
# @app.route("/<username>")
# def contact(username):
#     return f"Contact ME, {username}!"


app.run(host="0.0.0.0", port=7000)
