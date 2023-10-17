from src import LivrosRepositorio
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Alo mundo!"

@app.route('/insert', methods=['POST'])
def insert():
    
    repositorio = LivrosRepositorio()
    body = request.get_json()

    repositorio.insert(body)

    return 'OK'
