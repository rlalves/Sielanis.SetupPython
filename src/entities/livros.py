from sqlalchemy import Column, Integer, String
from src.config import Base

class Livro(Base):
    __tablename__ = 'livros'
    id = Column(Integer, primary_key=True)
    nome = Column(String) 

    def __repr__(self):
        return f'Livro [nome={self.nome}]'