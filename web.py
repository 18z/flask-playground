from flask import Flask, render_template
from flask_bootstrap import Bootstrap

import urllib
from bs4 import BeautifulSoup

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def hello_world():

    s1 = "http://amtrckr.info/"
    soup = BeautifulSoup(urllib.urlopen(s1), 'lxml')
    [s.extract() for s in soup('i')]
    [s.extract() for s in soup('span')]

    tables = soup.findAll('table')
    my_table = tables[0]

    rows = my_table.findAll(['th', 'tr'])

    cellzero = []
    cellone = []
    celltwo = []
    total = []

    for row in rows:
        cells = row.findAll('td')
        if len(cells) > 5:
            print cells[0].string
            ss0 = cells[0].string
            cellzero.append(ss0)

            print cells[1].string
            ss1 = cells[1].string
            cellone.append(ss1)

            print cells[2].a.string
            ss2 = cells[2].astring
            celltwo.append(ss2)

            print cells[3].string
            print cells[4].a.get('href')
            print " "

            total.append(cellzero)
            total.append(cellone)
            total.append(celltwo)

            # print cellzero

            # for t in total:
            #     print t

            # print total[0]

    return render_template('index.html', c1=cells[0].string, c2=cells[1].string, cell0=cellzero, cell1=cellone, cell2=celltwo, ttal=total)


if "__main__" == __name__:
    app.run(host='127.0.0.1', port=5000)
