from flask import Flask, render_template
import os
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from numpy import random

app = Flask(__name__)

def get_headline():
    # should probs get more descriptors but hey
    lines = ['TANKS', 'PLUMMETS', 'SOARS']

    news_url="https://news.google.com/news/rss"
    Client=urlopen(news_url)
    xml_page=Client.read()
    Client.close()

    soup_page=soup(xml_page,"lxml")
    news_list=soup_page.findAll("item")
    # Print news title, url and publish date

    headlines = []

    for news in news_list:
        x = random.randint(len(lines))
        news = (news.title.text).split(' - ')[0]
        headlines.append('Stock market ' + lines[x] + ' as ' + news)

    return headlines[random.randint(len(headlines))]


@app.route('/')
def index():
    headline = get_headline()
    return render_template("index.html", headline=headline)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 8080)))