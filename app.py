import json
from flask import Flask, jsonify, request, render_template, redirect

app = Flask(__name__)

emp = [{'id':1,'name':'Akash'},{'id':2,'name':'kaumi'},{'id':3,'name':'Jash'},{'id':4,'name':'Pooh'}]
book_list =[
  {
    'id': '1001',
    'author': 'John Smith',
    'lang': 'English',
    'title': 'Journey to the Unknown'
  },
  {   
    'id': '1002',
    'author': 'Sarah Johnson',
    'lang': 'Spanish',
    'title': 'El Viento en las Montañas'
  },
  {
    'id': '1003',
    'author': 'Michael Brown',
    'lang': 'French',
    'title': 'Les Secrets du Ciel'
  },
  {
    'id': '1004',
    'author': 'Emily Davis',
    'lang': 'German',
    'title': 'Die Schatten der Vergangenheit'
  },
  {
    'id': '1005',
    'author': 'David Wilson',
    'lang': 'Italian',
    'title': 'Nel Cuore del Labirinto'
  },
  {
    'id': '1006',
    'author': 'Laura Martinez',
    'lang': 'Portuguese',
    'title': 'O Enigma da Floresta'
  },
  {
    'id': '1007',
    'author': 'James Taylor',
    'lang': 'Russian',
    'title': 'Тайна Затмения'
  },
  {
    'id': '1008',
    'author': 'Isabella Garcia',
    'lang': 'Japanese',
    'title': '天空の伝説'
  },
  {
    'id': '1009',
    'author': 'William Harris',
    'lang': 'Chinese',
    'title': '古老的预言'
  },
  {
    'id': '1010',
    'author': 'Sophia Lee',
    'lang': 'Korean',
    'title': '그림자의 세계'
  }
]


@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/books', methods=['GET','POST'])
def books():
    if request.method == 'GET':
        if len(book_list)>0:
            return jsonify(book_list)
        else:
            return 'Nothing found',404
        
    if request.method == 'POST':
      author = request.form['author']
      lang = request.form['lang']
      title = request.form['title']
      id = book_list[-1]['id']+1 

      new_obj = {
          'id':id,
          'author':author,
          'lang':lang,
          'title':title
      }
      book_list.append(new_obj)
      return jsonify(book_list),201


if __name__=='__main__':
    app.run(debug=True, port=5001)