from backend.database.base import Base
from backend.database.connection import URL
from backend.service.service_contacorrente import ContaCorrenteservice
from backend.service.service_contapoupanca import ContaPoupancaservice
from backend.service.service_cliente import ClienteService
from backend.service.service_banco import BancoService

Base.metadata.create_all(bind=URL)

banco = BancoService()
contacorrente = ContaCorrenteservice()
contapoupanca = ContaPoupancaservice()
clientes = ClienteService()

#Clientes
# clientes.adicionar_cliente("Valtin","15791824025","19/09/1987")
# clientes.adicionar_cliente("Crispin", "38814640009", "18/01/1967")
# clientes.adicionar_cliente("Bruno","10133455335","16/01/2003")
# clientes.adicionar_cliente("Vanessa Soares", "09830048381","02/09/2003")
#clientes.atualizar_cadastro("10133455335","Bruno Joan")
# clientes.excluir_usuário("10133455335")
# clientes.buscar_cliente("10133455335")


#Contas(Corrente e Poupança)
# contacorrente.registrar_conta(1,1,50)
# contacorrente.registrar_conta(2,1,500)
# contapoupanca.registrar_conta(3,1,750)
# contapoupanca.registrar_conta(4,1,350)

#contacorrente.depositar(22690720,1612,"Salário")
# contacorrente.sacar(22690720,87, "Conta da internet")
# contacorrente.sacar(22690720,87,"Conta de Energia")
# contacorrente.sacar(22690720,1600,"Parcela do Carro") #Testando o limite de cheque especial
#contacorrente.sacar(22690720,387,"Feira")
#contacorrente.extrato(22690720)

# contapoupanca.depositar(27517650,150,"Déposito")
# contapoupanca.sacar(27517650,100,"Saque")
# contapoupanca.rentabilizar(27517650)
#contapoupanca.rentabilizar(22690720)

#Banco
#banco.adicionar_banco("Inter S.A")
#banco.relatorio(237)
# print(banco.tipo_conta(51916559))
# print(banco.tipo_conta(18854291))