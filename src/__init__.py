from .config import DbConnection
from .entities import livros as LivrosModel

class LivrosRepositorio ():

    def insert(self, livro):
        with DbConnection() as db:
            db.session.add(livro)
            db.session.commit()
            db.session.refresh(livro)
            return livro
