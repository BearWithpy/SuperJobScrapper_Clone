# from flask import Flask, render_template, request, redirect, send_file
# from scrapper import get_jobs
# from exporter import save_to_file
#
# app = Flask("Superscrapper")
#
# db = {}
#
#
# @app.route("/")
# def home():
#     return render_template("index.html")
#
#
# @app.route("/report")
# def report():
#     # print(request.args.get("word"))
#     keyword = request.args.get("word")
#     if keyword:
#         keyword = keyword.lower()
#         existing_jobs = db.get(keyword)
#
#         if existing_jobs:
#             jobs = existing_jobs
#         else:
#             jobs = get_jobs(keyword)
#             db[keyword] = jobs
#
#     else:
#         return redirect("/")
#
#     return render_template(
#         "report.html", searchingBy=keyword, resultsNumber=len(jobs), jobs=jobs
#     )
#
#
# @app.route("/export")
# def export():
#     try:
#         keyword = request.args.get("word")
#         if not keyword:
#             raise Exception()
#         keyword = keyword.lower()
#         jobs = db.get(keyword)
#         if not jobs:
#             raise Exception()
#         save_to_file(jobs)
#         return send_file("jobs.csv")
#     except:
#         return redirect("/")
#
#
# # Hello! Welcome to mi casa!
# # @app.route("/<username>")
# # def contact(username):
# #     return f"Contact ME, {username}!"
#
#
# app.run(host="0.0.0.0", port=7000)

import os
import requests
from bs4 import BeautifulSoup
from country import iban
from babel.numbers import format_currency

os.system("clear")
"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

# print(format_currency(5000, "KRW", locale="ko_KR"))


def ask(country):
    try:
        print(f"How many {country[0]} do you want to convert to {country[1]}")
        amount = int(input())
        convert: list = convertCurr(country, amount)
        print(
            f"\n >> {format_currency(convert[0], country[0])} is {format_currency(convert[0]*convert[1], country[1])}"
        )
        return

    except:
        print("That wasn't a number.\n")
        ask(country)


def convertCurr(country, amount):
    url = f"https://transferwise.com/gb/currency-converter/{country[0].lower()}-to-{country[1].lower()}-rate?amount={amount}"

    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    value_from = soup.find("input", {"id": "cc-amount-from"}).get("value")
    value_to = soup.find_all("input")[0].get("value")

    return [eval(value_from), eval(value_to)]


def main():
    print("Welcome to CurrencyConvert PRO 2000\n")
    cou = iban()
    ask(cou)


main()
