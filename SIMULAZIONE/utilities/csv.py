import os
import csv

from flask import app, jsonify, render_template, request


#----------------------------ROUTES----------------------------------#

# VERSIONE CON FUNZIONI ESTERNE

# Route per visualizzare i dati nel file csv e rederizzazione HTML
@app.route('/')
def index():
    #Load data from CSV
    data = load_informations()
    return render_template('index.html', data=data)

# route for /prodotto/<codice>
@app.route('/prodotto/<codice>')
def prodotto(codice):
    prodotto = load_information(codice)
    return render_template('prodotto.html', prodotto=prodotto)

#VERSIONE CON FUNZIONI INTERNE
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
def load_informations():
    informations = []
    csv_path = os.path.join(os.path.dirname(__file__), 'static/file.csv');

    try:
        with open(csv_path, mode='r', encoding='UTF-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                informations.append(row)
        return informations
    
    except FileNotFoundError:
        print(f'Warning: File {csv_path} not found')
        return []
    except Exception as e:
        print(f'Error loading data: {e}')
        return []

# Funzione per leggere i dati dal file csv con filtro per codice
def load_information(codice):
    information = None

    csv_path = os.path.join(os.path.dirname(__file__), 'static/file.csv')

    try:
        with open(csv_path, mode='r', encoding='UTF-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if row['codice'] == codice:
                    information = row
                    break
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


#----------------------------------API CON FUNZIONI ESTERNE--------------------------------------#

# API GET per restituire i dati in formato JSON
@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        data = load_informations()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# API GET per restituire i dati in formato JSON con filtro per id
@app.route('/api/data/<id>', methods=['GET'])
def method_name(id):
    try:
        datas = load_informations()

        for data in datas:
            if data['id'] == id:
                return jsonify(data), 200
            
        return jsonify({'message': 'Data not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# API POST per aggiungere i dati al file csv
@app.route('/api/data', methods=['POST'])
def add_data():
    new_data = request.get_json()   #get data from request
    data = load_informations()              #load existing data from csv
    
    #Validate incoming data
    if not all(key in new_data for key in ('Name', 'Email', 'Phone', 'Description')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    data.append(new_data)

    #Write data to CSV file
    write_data(new_data)

#-------------------------------API CON FUNZIONI INTERNE----------------------------------#

# api to get the list of products
@app.route('/api/prodotti')
def get_prodotti():
    prodotti = []

    with open('data/magazzino.csv', 'r', encoding='utf-8') as file:
        lettore_csv = csv.DictReader(file)
        for riga in lettore_csv:
            prodotti.append(riga)

    return jsonify({'prodotti': prodotti})

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

    return jsonify({'prodotto': prodotto})

# API TO DELETE a product with the specified code in magazzino.csv
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

    return jsonify({'eliminato': True})


