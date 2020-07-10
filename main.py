from flask import Flask

app = Flask("Superscrapper")


@app.route("/")
def home():
    return "Hello! Welcome to mi casa!"


@app.route("/contact")
def contact():
    return "Contact ME"


app.run(host="0.0.0.0", port=7000)
