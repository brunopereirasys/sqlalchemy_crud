from backend.database.session import SessionManager
from backend.models.table_cliente import Cliente



class Repocliente:
    
    def _buscar(self, cpf):
        with SessionManager() as session:
            busca = session.query(Cliente).filter(Cliente.cpf == cpf).first()
            if busca is None: #Se a busca retornar None(ou seja, não encontrar niguém com aquele CPF)
                return False
            else:
                if busca.conta is None: #Verifica se o cliente(encontrado) possui uma conta vinculada a ele
                    print(f"{busca} | Usuário sem conta cadastrada")
                else:
                    print(f"{busca} | {busca.conta}")
        
    def _insert(self, nome, cpf, data_nascimento):
        with SessionManager() as session:
            cliente = Cliente(nome, cpf, data_nascimento)
            session.add(cliente)
    
    def _delete(self, cpf):
        with SessionManager() as session:
            resultado = session.query(Cliente).filter(Cliente.cpf == cpf).first()
            if resultado is None:
                return False # Se o return for False a função encerra aqui
            session.delete(resultado) #Apaga via ORM: o cascade leva cliente -> conta -> movimentações junto
    
    def _update_nome(self,cpf,nome):
        with SessionManager() as session:
            resultado = session.query(Cliente).filter(Cliente.cpf == cpf).first()
            
            if resultado is None:
                return False
            else:
                session.query(Cliente).filter(Cliente.cpf == cpf).update({"nome":nome})


