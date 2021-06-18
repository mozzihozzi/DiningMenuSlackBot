from flask import Flask, request, make_response, jsonify
import requests
from Crawler.JigokCrawler import JigokCrawler

# app
app = Flask(__name__)


@app.route('/menu/daily')
def crawling():
    url = "https://dining.postech.ac.kr/"
    crawler = JigokCrawler()

    return crawler.startCrawling(requests.get(url), "")


@app.route('/')
def main():
    return {}


def runAPI():
    app.run(debug=True, host="localhost", port=22411)


if __name__ == '__main__':
    runAPI()
