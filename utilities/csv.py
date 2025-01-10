import os
import csv

from flask import app, jsonify, render_template, request


#----------------------------ROUTES----------------------------------#
# Route per visualizzare i dati nel file csv e rederizzazione HTML
@app.route('/data')
def data():
    #Load data from CSV
    data = load_data()
    return render_template('index.html', data=data)


#----------------------------IMPORTAZIONE----------------------------------#
# Funzione per caricare i dati dal file csv
def load_data():
    information = []
    csv_path = os.path.join(os.path.dirname(__file__), 'static/file.csv');

    try:
        with open(csv_path, mode='r', encoding='UTF-8') as csv_file:
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
    

#----------------------------------API--------------------------------------#

# API GET per restituire i dati in formato JSON
@app.route('/api/data', methods=['GET'])
def get_data():
    data = load_data()
    return jsonify(data)


# API GET per restituire i dati in formato JSON con filtro per nome
@app.route('/api/data/<name>', methods=['GET'])
def method_name(name):
    datas = load_data()
    for data in datas:
        if data['Name'] == name:
            return jsonify(data)
    return jsonify({'message': 'Data not found'}), 404


# API POST per aggiungere i dati al file csv
@app.route('/api/data', methods=['POST'])
def add_data():
    try:
        new_data = request.get_json()   #get data from request
        data = load_data()              #load existing data from csv
        
        #Validate incoming data
        if not all(key in new_data for key in ('Name', 'Email', 'Phone', 'Description')):
            return jsonify({'error': 'Missing required fields'}), 400
        
        data.append(new_data)

        #Write data to CSV file
        csv_path = os.path.join(os.path.dirname(__file__), 'static/file.csv')
        with open(csv_path, mode='a', encoding='UTF-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['name', 'email', 'phone', 'description'])
            writer.writerow(new_data)
        return jsonify({'message': 'DATA added successfully', 'data': new_data}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500