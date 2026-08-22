from backend.database.session import SessionManager
from backend.models.table_conta import Conta
from backend.models.table_movimentacao import Movimentacao
from decimal import Decimal
import random

class Repoconta:
    
    def select(self):
        with SessionManager() as session:
            lista_contas = session.query(Conta).all() #Lista todas as contas presente na tabela 'contas'
            for conta in lista_contas: # Percorrendo cada conta dentro do dicionário 'lista_contas'
                print(conta)
    
    def select_saldo(self, numero_conta):
        with SessionManager() as session:
            saldo = session.query(Conta.saldo).filter(Conta.numero_conta == numero_conta).scalar() #scalar() → um único valor
            return saldo
    
    def select_type(self, numero_conta):
        with SessionManager() as session:
            type = session.query(Conta.tipo).filter(Conta.numero_conta == numero_conta).scalar()
            return type
    
        
    def select_movimentacao(self, numero_conta):
         with SessionManager() as session:
            id = session.query(Conta.id_conta).filter(Conta.numero_conta == numero_conta).scalar() #O .scalar() existe justamente para os casos em que você quer um único valor, e não uma linha inteira. ex: first() retorna uma linha
            if id is  None:
                return False
            else:
                movimentacoes = session.query(Movimentacao).filter(Movimentacao.id_conta == id).all()
                for movimentacao in movimentacoes:
                    print(f"Valor: R${movimentacao.valor},00 | Tipo: {movimentacao.tipo} | Descrição: {movimentacao.descricao} | Data: {movimentacao.data_movimentacao}")
                    
            
        
        
    def insert(self,id_cliente, id_banco, saldo, tipo,limite_especial):
        with SessionManager() as session:
            #Por mais improvável que seja o módulo random pode gerar de forma aleatório uma sequencia de número que já esteja cadastrado como número de alguma conta no banco de dados, devido a isso, criamos um loop para validar o número gerado pelo módulo e comparar com os números das contas cadastados no banco de dados, antes de inserimos no cadastro do cliente

            bloco1 = random.randint(100, 999)#Numero da conta é gerado automaticamente no ato da criação do registro conta
            bloco2 = random.randint(100, 999)
            bloco3 = random.randint(10, 99)

            numero = int(f"{bloco1}{bloco2}{bloco3}")

            conta = Conta(id_cliente, id_banco,numero_conta=numero, saldo=saldo, tipo=tipo, limite_especial=limite_especial) #Crindo novo registro/conta
            session.add(conta)#Inserido o registro/objeto 'contas'


            


    def insert_saldo(self, numero_conta, valordeposito,tipo, descricao, data_movimentacao):
        with SessionManager() as session:
            conta = session.query(Conta).filter(Conta.numero_conta == numero_conta).first() #Capta a conta pela coluna numero_conta
            if conta is None: #Verifica se aquela conta existe na base se dados, senão, retorna None
                print("Número da conta não encontrada. Tente novamente!")
            else: #Se a conta existir, a operação é feita
                transacao = Movimentacao(conta.id_conta,tipo, valordeposito,descricao,data_movimentacao) #Automaticamente um transação é registrada na tabela'movimentacao'
                session.add(transacao)
                
                valordeposito = conta.saldo + valordeposito # O valor do depósito passar a ser a soma do saldo que já existia + o valor que está sendo depositado
                session.query(Conta).filter(Conta.numero_conta == numero_conta).update({"saldo": valordeposito})#  o Saldo é atualizado
      
                print(f"Depósito Efetuado com sucesso para {conta.cliente.nome}")
    
    
    def saque(self, numero_conta, valorsaque,tipo, descricao, data_movimentacao):
        with SessionManager() as session:
            # Busca a conta antes de qualquer operação. Se a conta não existir,
            # o saque não deve tentar alterar saldo nem registrar movimentação.
            conta = session.query(Conta).filter(Conta.numero_conta == numero_conta).first()
            if conta != None:
                    # Caso simples: a conta tem saldo suficiente para cobrir o saque.
                    # Basta subtrair o valor solicitado e registrar a saída no extrato.
                    if conta.saldo >= valorsaque:
                        saldo_atual = conta.saldo - valorsaque
                        session.query(Conta).filter(Conta.numero_conta == numero_conta).update({"saldo": saldo_atual})
                        transacao = Movimentacao(conta.id_conta,tipo, valorsaque,descricao,data_movimentacao)
                        session.add(transacao)
                        print(f"Saque efetuado com sucessooo")
                    else:
                        print("Você não tem saldo suficiente")
                        # Quando o saldo não cobre o saque, só a Conta Corrente pode tentar completar o valor usando o limite de cheque especial.
                        if conta.tipo == "Conta Corrente":
                            print("Verificando seu limite de cheque especial...")
                            # Se ainda existe saldo positivo, parte do saque sai do saldo
                            # e apenas a diferença é abatida do limite especial.
                            if conta.saldo > 0:
                                if valorsaque > conta.limite_especial + conta.saldo:
                                    print("Limite de cheque especial insuficiente")
                                else:
                                    valor_faltante = valorsaque - conta.saldo
                                    session.query(Conta).filter(Conta.numero_conta == numero_conta).update({"limite_especial": conta.limite_especial - valor_faltante})
                                    session.query(Conta).filter(Conta.numero_conta == numero_conta).update({"saldo": conta.saldo-valorsaque})
                                    transacao = Movimentacao(conta.id_conta,tipo, valorsaque,descricao,data_movimentacao)
                                    session.add(transacao)
                                    print("Saque efetuado com sucesso!! ")
                            else:
                                # Se o saldo já está zerado ou negativo, o saque depende
                                # somente do limite especial disponível.
                                # Aqui não somamos saldo + limite como no caso acima:
                                # quando o saldo está negativo, essa soma reduziria o
                                # limite disponível e poderia bloquear um saque válido.
                                if valorsaque > conta.limite_especial:
                                    print("Limite de cheque especial insuficiente")
                                else:
                                    session.query(Conta).filter(Conta.numero_conta == numero_conta).update({"limite_especial": conta.limite_especial-valorsaque})
                                    transacao = Movimentacao(conta.id_conta,tipo, valorsaque,descricao,data_movimentacao)
                                    # Como o saldo já está zerado ou negativo, o saque aumenta
                                    # a dívida da conta. O abs garante que o valor do saque seja
                                    # subtraído do saldo atual, mantendo o resultado negativo.
                                    session.query(Conta).filter(Conta.numero_conta == numero_conta).update({"saldo": conta.saldo + -abs(valorsaque)})
                                    session.add(transacao)
                                    print("Saque efetuando(Usando o cheque especial)")
                        else:
                            # Conta Poupança não usa cheque especial. Sem saldo suficiente,
                            # a operação termina sem alterar saldo nem movimentações.
                            pass

                                       
            else:
                print("Número da conta não encontrada. Tente novamente!")
    
    
