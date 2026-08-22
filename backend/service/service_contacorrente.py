from backend.repositories.repo_conta import Repoconta
from datetime import datetime
from backend.base.account import Conta
from decimal import Decimal

data = datetime.today().strftime("%d/%m/%Y") #captura a data de hoje
data_hoje = str(data) 

class ContaCorrenteservice(Conta):
    
    limite_especial = Decimal(500)

    def __init__(self):
        self.repo_conta = Repoconta()

    
    def listar_contas(self):
        self.repo_conta.select()

    
    def ver_saldo(self, numero_conta):
        valor_saldo = self.repo_conta.select_saldo(numero_conta)

        if valor_saldo == None:
            print("Nenhum conta foi encontrada")
        else:
            print(f"Saldo disponivel R$ {valor_saldo}")
        
        return valor_saldo

    def extrato(self, numero_conta=""):
        try:
            if numero_conta != "":
                if self.repo_conta.select_movimentacao(numero_conta) == False: #Se o usuário não for encontrado na base de dados retorna false
                    print("Número da conta inválido. Verifique e tente novamente.")
                #Se não retornar False a função select_movimentação trará as movimentações que encontrou, pois a mesma(função), já está sendo executada no ato da comparação(ele não trará as informações pelo return e sim pelo print da função select_movimentação)
                #Função sem retorno definido retorna None
            else:
                raise TypeError  
        except TypeError:
            print("Número da conta não informado. Verifique e tente novamente")

        
    def registrar_conta(self, id_cliente, id_banco, saldo):
            if saldo > 0:
                self.repo_conta.insert(id_cliente, id_banco, saldo, tipo="Conta Corrente", limite_especial=500)
                
                print(f"Sua Conta-Corrente foi registrada com sucesso")
            else:
                print("Para registrar uma conta é necessário saldo acima de R$ 00,00")
    
    def depositar(self, numero_conta, valordeposito, descricao) ->None: 
        try:
            if valordeposito > 0:
                self.repo_conta.insert_saldo(numero_conta, valordeposito, tipo="Entrada", descricao=descricao,data_movimentacao=data_hoje) #A camada service 'depositar' já implementa um registro de "entrada" automaticamente
            else:
                print("O valor do depósito não pode ser igual ou menor zero")
        except TypeError:
            print("O tipo do dado é incompatível com a operação.")
            
        except Exception as Error:
            print(Error)
    
    def sacar(self, numero_conta, valorsaque, descricao):
        try:
            if valorsaque > 0:
                self.repo_conta.saque(numero_conta,valorsaque,tipo="Saida",descricao=descricao,data_movimentacao=data_hoje)
            else:
                print("O valor do saque deve ser superior a R$00,00 ")
        except ValueError:
            print("Erro no tipo de dado")
            
        
        
       
    
