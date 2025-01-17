import os
import csv
from datetime import datetime
import json
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)


DATA_PATH = 'static\\data'

blog_path = os.path.join(DATA_PATH, 'blog.csv')
comments_path = os.path.join(DATA_PATH, 'comments.csv')


post_categories = [
                    {"name": "Tecnologia", "description": "Articoli all'avanguardia sulle ultime innovazioni tecnologiche"},
                    {"name": "Viaggi", "description": "Racconti di viaggio, consigli e avventure da tutto il mondo"},
                    {"name": "Lifestyle", "description": "Riflessioni e consigli per migliorare la qualità della vita"}
                ]


@app.route('/index', methods = ['GET'])
def index():
    return jsonify({'message': 'Not implemented!'})


@app.route('/new_post', methods=['POST', 'GET'])
def new_post():
    post_blog = load_multiple_data()  # Load existing data from CSV
    length = len(post_blog) + 1

    if request.method == 'POST':
        try:
            new_post = request.get_json()  # Get data from request
            print(new_post)  # Debugging print

            # Validate incoming data
            if not all(key in new_post for key in ('id', 'title', 'author', 'date', 'content', 'category')):
                return jsonify({'error': 'Missing required fields'}), 400

            post_blog.append(new_post)
            write_data(new_post)  # Write data to CSV

            return jsonify({'message': 'Post creato con successo!', 'status': 'success'}), 200
        except Exception as e:
            print(e)  # Debugging print
            return jsonify({'error': 'Errore nella creazione del post'}), 500
    else:
        return render_template('new_post.html', length=length)

    
# REACT API

@app.route('/react')
def index_react():
    return render_template('index_react.html', post_categories=post_categories)


# API REST
# api to get the list of products
@app.route('/api/posts', methods=['GET'])
def get_prodotti():
    posts = []
    try:
        with open(blog_path, 'r', encoding='utf-8') as file:
            lettore_csv = csv.DictReader(file)
            for riga in lettore_csv:
                posts.append(riga)
        return jsonify(posts), 200
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500

@app.route('/api/post/<post_id>', methods=['GET'])
def get_prodotto(post_id):
    post = None
    comments = []

    with open(blog_path, 'r', encoding='utf-8') as file:
        lettore_csv = csv.DictReader(file)
        for riga in lettore_csv:
            if riga['id'] == post_id:
                post = riga
                break
    
    with open(comments_path, 'r', encoding='utf-8') as file:
        lettore_csv = csv.DictReader(file)
        for riga in lettore_csv:
            if riga['post_id'] == post_id:
                comments.append(riga)

    if post is None:
        return jsonify({'error': 'Post not found'}), 404
    
    return jsonify({'post': post, 'comments': comments})


# api to add a new product
@app.route('/api/comments/<post_id>', methods=['POST'])
def add_comment(post_id):
    try:
        post = None

        with open(blog_path, 'r', encoding='utf-8') as file:
            lettore_csv = csv.DictReader(file)
            for riga in lettore_csv:
                if riga['id'] == post_id:
                    post = riga
                    break
        
        if not post:
            return jsonify({'success': False, 'message': 'Post not found'}), 404

        new_comment = request.get_json()

        comments = load_comments()

        ids = [int(comment["id"][1:]) for comment in comments]

        new_comment = {
                            'id': 'C' + '00' + (str(ids) + 1),
                            'post_id': new_comment['post_id'],
                            'author': new_comment['author'],
                            'email': new_comment['email'],
                            'text': new_comment['text'],
                            'date': datetime.now().strftime('%Y-%m-%d')
        }
        
        # Rewrite all the file
        with open(comments_path, mode='a', encoding='utf-8', newline='') as file:
            fieldnames = ['id', 'post_id', 'author', 'email', 'text', 'date']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(new_comment)

        return jsonify({'success': True, 'message': 'Comment added'}), 201
    except Exception as e:
        print(e)
        return jsonify({'success': False, 'message': str(e)}), 500

#--------------------------------ROUTES--------------------------------------
@app.route('/blog')
def blog():
    posts = []

    with open('static/data/blog.csv', 'r', encoding='utf-8') as file:
        lettore_csv = csv.DictReader(file)
        for riga in lettore_csv:
             posts.append(riga)

    return render_template('blog_list.html',  posts=posts)

@app.route('/')
def index_page():
    return render_template('index.html', post_categories=post_categories)

#------------------------------ FUNZIONI CSV-----------------------------------

# Funzione per caricare i dati da un file csv
def load_multiple_data():
    information = []
    csv_path = os.path.join(os.path.dirname(__file__), './static/data/blog.csv')
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

# Funzione per scrivere dei dati sul file csv
def write_data(data):
    try:
        csv_path = os.path.join(os.path.dirname(__file__), './static/data/blog.csv')
        with open(csv_path, mode='a', encoding='UTF-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['id','title','author','date','content','category'])
            writer.writerow(data)
        return jsonify({'message': 'Post added successfully', 'data': data}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def create_csv_if_not_exists(filename, header=[]):
    # Controlla se il file non esiste
    if not os.path.exists(filename):
        # Crea il file CSV con gli header passati
        with open(filename, mode='w+', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
        print(f"File '{filename}' creato con successo con header: {header}")
    else:
        print(f"File '{filename}' esiste già. Nessuna azione necessaria.")


# Funzione per leggere tutti i post.
def load_posts():
    # Controlla se il file CSV esiste. Se no, crealo passandogli degli header
    create_csv_if_not_exists(blog_path, header=['id', 'title', 'author', 'date', 'content', 'category'])

    with open(blog_path, 'r+', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        posts = list(csv_reader)

        return posts  
    
# Funzione per leggere tutti i commenti.
def load_comments():
    create_csv_if_not_exists(comments_path, header=['id', 'post_id', 'author', 'email', 'text', 'date'])

    with open(comments_path, 'r+', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        comments = list(csv_reader)

        return comments

if __name__ == '__main__':
    app.run(debug=True)
