from backend.models.table_banco import Banco 
from backend.database.session import SessionManager
from backend.models.table_conta import Conta

#Camada de repositórios, para realizar operações CRUD sobre as tabelas/models

class RepoBanco:
    
    def _insert(self, nome_banco):
        with SessionManager() as session:
            banco = Banco(nome_banco)
            session.add(banco)

    def _select(self,num_banco):
        with SessionManager() as session:
            banco = session.query(Banco).filter(Banco.num_banco == num_banco).first()#Armazenado na variavel banco o resultado da query por banco
            if banco is None:
                return False
            else:
                for conta in banco.conta:
                    print(f"{conta.cliente} - {conta}")
    
