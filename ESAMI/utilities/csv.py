import os
import csv

from flask import app, jsonify, render_template, request


#----------------------------ROUTES----------------------------------#
# Route per visualizzare i dati nel file csv e rederizzazione HTML
@app.route('/data')
def data():
    #Load data from CSV
    data = load_multiple_data()
    return render_template('index.html', data=data)

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

# route for /prodotto/<codice>
@app.route('/prodotto/<codice>')
def prodotto(codice):
    prodotto = None

    with open('data/magazzino.csv', 'r', encoding='utf-8') as file:
        lettore_csv = csv.DictReader(file)
        for riga in lettore_csv:
            if riga['codice'] == codice:
                prodotto = riga
                break

    return render_template('prodotto.html', prodotto=prodotto)


#----------------------------IMPORTAZIONE----------------------------------#
# Funzione per leggere i dati dal file csv
def load_multiple_data():
    information = []
    csv_path = os.path.join(os.path.dirname(__file__), 'static/file.csv');

    try:
        with open('static/file.csv', mode='r', encoding='UTF-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                information.append(row)
        return information
    except FileNotFoundError:
        print(f'Warning: File {csv_path} not found')
        return []
    except Exception as e:
        print(f'Error loading data: {e}')
        return []

# Funzione per scrivere dei dati sul file csv
def write_data(data):
    try:
        csv_path = os.path.join(os.path.dirname(__file__), 'static/file.csv')
        with open(csv_path, mode='a', encoding='UTF-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['name', 'email', 'phone', 'description'])
            writer.writerow(data)
        return jsonify({'message': 'DATA added successfully', 'data': data}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


#----------------------------------API--------------------------------------#

# API GET per restituire i dati in formato JSON
@app.route('/api/data', methods=['GET'])
def get_data():
    data = load_multiple_data()
    return jsonify(data)


# API GET per restituire i dati in formato JSON con filtro per nome
@app.route('/api/data/<name>', methods=['GET'])
def method_name(name):
    datas = load_multiple_data()
    for data in datas:
        if data['Name'] == name:
            return jsonify(data)
    return jsonify({'message': 'Data not found'}), 404


# API POST per aggiungere i dati al file csv
@app.route('/api/data', methods=['POST'])
def add_data():
    new_data = request.get_json()   #get data from request
    data = load_multiple_data()              #load existing data from csv
    
    #Validate incoming data
    if not all(key in new_data for key in ('Name', 'Email', 'Phone', 'Description')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    data.append(new_data)

    #Write data to CSV file
    write_data(new_data)

#-------------------------------API----------------------------------#

# api to get the list of products
@app.route('/api/prodotti')
def get_prodotti():
    prodotti = []

    with open('data/magazzino.csv', 'r', encoding='utf-8') as file:
        lettore_csv = csv.DictReader(file)
        for riga in lettore_csv:
            prodotti.append(riga)

    return {'prodotti': prodotti}

# api to get the product with the specified code
@app.route('/api/prodotto/<codice>')
def get_prodotto(codice):
    prodotto = None

    with open('data/magazzino.csv', 'r', encoding='utf-8') as file:
        lettore_csv = csv.DictReader(file)
        for riga in lettore_csv:
            if riga['codice'] == codice:
                prodotto = riga
                break

    return {'prodotto': prodotto}

# api to delete a product with the specified code in magazzino.csv
@app.route('/api/elimina/<codice>', methods=['DELETE'])
def api_elimina_prodotto(codice):
    prodotti = []

    with open('data/magazzino.csv', 'r', encoding='utf-8') as file:
        lettore_csv = csv.DictReader(file)
        for riga in lettore_csv:
            if riga['codice'] != codice:
                prodotti.append(riga)

    with open('data/magazzino.csv', 'w', encoding='utf-8') as file:
        intestazioni = ['codice', 'nome', 'quantita', 'prezzo']
        scrittore_csv = csv.DictWriter(file, fieldnames=intestazioni)
        scrittore_csv.writeheader()
        for prodotto in prodotti:
            scrittore_csv.writerow(prodotto)

    return {'eliminato': True}