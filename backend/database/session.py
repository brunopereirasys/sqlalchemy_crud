from sqlalchemy.orm import sessionmaker
from backend.database.connection import URL # Importando a engine

SessionLocal = sessionmaker(bind=URL) # Criando uma fabrica de sessões




class SessionManager: # A classe SessionManager age como um gerenciador de sessão, garantindo que cada operação/sessão criada seja aberta, trabalha e fecha no final de cada sessão
    def __enter__(self):
        self.session = SessionLocal() #Criando a sessão, entrega uma sessão pronta para uso
        return self.session #Retorna a sessão

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.session.rollback() #Caso haja algum erro a operação é cancelada e retorna as configurações iniciais
            print(exc_type)
        else:
            self.session.commit() #Caso não tenha erro a operação é gravada/realizada

        self.session.close()#Sessão encerrada automaticamente
