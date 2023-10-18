from src import LivrosRepositorio
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Bem vindo ao meu primeiro app em Flask, corrigindo bug 11!"

@app.route('/insert', methods=['POST'])
def insert():
    
    repositorio = LivrosRepositorio()
    body = request.json
    repositorio.insert(body["nome"])

    return "ok"
