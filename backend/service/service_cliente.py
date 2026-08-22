from backend.repositories.repo_cliente import Repocliente
from sqlalchemy.exc import IntegrityError
from validate_docbr import CPF





class ClienteService():
    def __init__(self):
        self.repocliente = Repocliente()
    
    def adicionar_cliente(self, nome, cpf, data_nascimento):
        cpf_validacao = CPF() #Vefifique se o cpf digitado é válido(segue as padronizações de um CPF)
        try:
            if cpf_validacao.validate(cpf) == True:# #Se o cpf for válido retorna True
                self.repocliente._insert(nome, cpf, data_nascimento)
                print("Cliente cadastrado com sucesso")
            else:
                print("Digite um CPF válido")
        except IntegrityError: #Capta o erro caso o usuário tente cadastrado um CPF que já está na base de dados [cpf: unique=True]
            print("CPF já cadastrado. Tente um CPF diferente")

    def buscar_cliente(self, cpf):
        cpf = str(cpf)
        if self.repocliente._buscar(cpf) == False:
            print("Usuário não encontrado")
    
    def atualizar_cadastro(self, cpf, nome):
        operation = self.repocliente._update_nome(cpf, nome)
        if operation == False:
            print("Usuário não encontrado na base ")
        else:
            print("Cadastro atualizado com sucesso")
    
    def excluir_usuário(self, cpf):
        try:
            if self.repocliente._delete(cpf) == False:
                print("Usuário não encontrado na base para exclusão")
            else:
                print("O usuário e todos os dados vinculados (conta e histórico) foram excluídos com sucesso.")
        except Exception as error:
            print(error)
