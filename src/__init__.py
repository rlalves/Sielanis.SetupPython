from .config import DbConnection
from .entities import livros

class LivrosRepositorio:

    def insert(self, nome):
        with DbConnection() as db:
            livro = livros.Livro(nome=nome)
            db.session.add(livro)
            db.session.commit()

