from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DbConnection:
    def __init__(self):
        #self.__connection_string = 'mysql+pymysql://root:root@127.0.0.1:3306/Sielanis'
        self.__connection_string = 'mysql+pymysql://root:root@mysqldb/Sielanis'
        self.session = None

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
