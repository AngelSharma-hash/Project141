from flask import Flask, jsonify,request
import csv
import pandas as pd

app = Flask(__name__)

data = pd.read_csv('articles.csv')
data.rename(columns = {'': 'id'},inplace=True)

All_books = []

with open('articles.csv', encoding = 'utf-8') as f:
    reader = csv.reader(f)
    csv.field_size_limit(100000000)
    data2 = list(reader)
    
    All_books = data2[1:]


liked_articles = []
not_liked_articles = []

@app.route('/get_articles')
def get_articles():
    return jsonify({'data':All_books[0], 'status':'success'})

@app.route('/like_the_article', methods=['POST'])
def movies_liked():
    global All_books
    global liked_articles
    articles = All_books[0]
    All_books = All_books[1:]
    liked_articles.append(articles)
    return jsonify({'status':'success'}), 201

@app.route('/not_like_the_article', methods=['POST'])
def movies_not_liked():
    global All_books
    global not_liked_articles
    articles = All_books[0]
    All_books = All_books[1:]
    not_liked_articles.append(articles)
    return jsonify({'status':'success'}), 201

if __name__=='__main__':
    app.run()
