from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_frozen import Freezer

import sys
import urllib
from bs4 import BeautifulSoup

app = Flask(__name__)
Bootstrap(app)
freezer = Freezer(app)


class record(object):

    def __init__(self, datee, url):
        self.datee = datee
        self.url = url

records = []


@app.route('/')
def hello_world():

    s1 = "http://amtrckr.info/"
    soup = BeautifulSoup(urllib.urlopen(s1), 'lxml')
    [s.extract() for s in soup('i')]
    [s.extract() for s in soup('span')]

    tables = soup.findAll('table')
    my_table = tables[0]

    rows = my_table.findAll(['th', 'tr'])

    for row in rows:
        cells = row.findAll('td')
        if len(cells) > 5:
            datee = cells[0].string
            url = cells[1].string

            # print cells[2].a.string
            #
            # print cells[3].string
            # print cells[4].a.get('href')
            # print " "

            data = record(datee, url)
            records.append(data)

    return render_template('undex.html', rds=records)


if "__main__" == __name__:

    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host='127.0.0.1', port=5000)
