import csv
from flask import Flask, render_template, request

app = Flask(__name__)

# ESERCIZIO 1
@app.route('/')
def index():
    prodotti = []
    intestazioni = []

    with open('data/magazzino.csv', 'r', encoding='utf-8') as file:
        lettore_csv = csv.DictReader(file)
        intestazioni = lettore_csv.fieldnames
        for riga in lettore_csv:
            prodotti.append(riga)

    return render_template('index.html', prodotti=prodotti, intestazioni=intestazioni)

@app.route('/prodotto/<string:codice>')
def prodotto(codice):
    prodotto = None

    with open('data/magazzino.csv', 'r', encoding='utf-8') as file:
        lettore_csv = csv.DictReader(file)
        for riga in lettore_csv:
            if (riga['codice']) == codice:
                prodotto = riga
                break

    return render_template('prodotto.html', prodotto=prodotto)


@app.route('/api/elimina/<string:codice>', methods=['DELETE'])
def elimina_prodotto(codice):
    prodotti = []
    intestazioni = []

    with open('data/magazzino.csv', 'r', encoding='utf-8') as file:
        lettore_csv = csv.DictReader(file)
        intestazioni = lettore_csv.fieldnames
        for riga in lettore_csv:
            if riga['codice'] != codice:
                prodotti.append(riga)

    with open('data/magazzino.csv', 'w', encoding='utf-8', newline='') as file:
        scrittore_csv = csv.DictWriter(file, fieldnames=intestazioni)
        scrittore_csv.writeheader()
        scrittore_csv.writerows(prodotti)

    return {'eliminato': True}


@app.route('/api/prodotto/<string:codice>', methods=['POST'])
def ritorna_prodotto(codice):
    prodotto = None

    with open('data/magazzino.csv', 'r', encoding='utf-8') as file:
        lettore_csv = csv.DictReader(file)
        for riga in lettore_csv:
            if (riga['codice']) == codice:
                prodotto = riga
                break

    return {'prodotto': prodotto}

@app.route('/react')
def react():
    return render_template('index_react.html')

@app.route('/api/prodotti', methods=['POST'])
def react_ritorna_prodotti():
    prodotti = []

    with open('data/magazzino.csv', 'r', encoding='utf-8') as file:
        lettore_csv = csv.DictReader(file)
        for riga in lettore_csv:
            prodotti.append(riga)

    return {'prodotti': prodotti}

if __name__ == '__main__':
    app.run(debug=True)