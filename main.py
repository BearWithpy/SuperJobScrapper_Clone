from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

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
        fromDB = db.get(keyword)

        if fromDB:
            jobs = fromDB
        else:
            jobs = get_jobs(keyword)
            db[keyword] = jobs

    else:
        return redirect("/")

    return render_template("report.html", searchingBy=keyword, resultsNumber=len(jobs))


# Hello! Welcome to mi casa!
# @app.route("/<username>")
# def contact(username):
#     return f"Contact ME, {username}!"


app.run(host="0.0.0.0", port=7000)
