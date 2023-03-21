from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from dodaj_zadanie import dodaj_zadanie
from pobierz_zadania import pobierz_zadania
from usun_zadanie import usun_zadanie

app = Flask(__name__)

@app.route('/')
def index():
    zadania = pobierz_zadania()
    return render_template('index.html', zadania=zadania)

@app.route('/dodaj', methods=['POST'])
def dodaj():
    tresc = request.form['tresc']
    dodaj_zadanie(tresc)
    return redirect(url_for('index'))

@app.route('/usun/<int:id>')
def usun(id):
    usun_zadanie(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
