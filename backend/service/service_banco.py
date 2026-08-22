from backend.repositories.repo_banco import RepoBanco
from backend.repositories.repo_cliente import Repocliente
from backend.repositories.repo_conta import Repoconta
from backend.service.service_contacorrente import ContaCorrenteservice
from backend.service.service_contapoupanca import ContaPoupancaservice



class BancoService:
    
    def __init__(self):
        self.repobanco = RepoBanco()
        self.repocliente = Repocliente()
        self.repoconta = Repoconta()
        self.servicecontaCC = ContaCorrenteservice()
        self.servicecontaPP = ContaPoupancaservice()
    
    def adicionar_banco(self, nome_banco):
        try:
            self.repobanco._insert(nome_banco)
            print("Banco adicionado com sucesso")
        except:
            print("Falha na operação. Por favor tente mais tarde")
    
    def tipo_conta(self, numero_conta): #Essa função verifica se a conta é do tipo C. Corrente ou C. Poupança
        tipo = self.repoconta.select_type(numero_conta)
        return tipo
        
    def transferir(self, conta_origem, conta_destinatario, valor, descricao):
        if self.tipo_conta(conta_origem) and self.tipo_conta(conta_destinatario) in ("Conta Corrente", "Conta Poupança"): #Se a conta de origem e destino for conta corrente ou poupança(conta válida)
            
            saldo_inicialCO = self.repoconta.select_saldo(conta_origem) # Capturando o saldo inical da conta que vai fazer a transferência antes de tal ação
            print(f"Saldo Inicial da conta de Origem: R$ {saldo_inicialCO}")
            print("...")
            saldo_inicialCD = self.repoconta.select_saldo(conta_destinatario) #Capturando o saldo inical da conta que vai receber a transferência antes de tal ação
            print(f"Saldo Inicial da conta de Destino: R$ {saldo_inicialCD}")
            print("...")
            
            if self.tipo_conta(conta_origem) == "Conta Corrente": #Se a conta for do tipo conta corrente, usasse o método de saque da conta corrente(por conta do cheque especial)
                self.servicecontaCC.sacar(conta_origem, valor, descricao)
            elif self.tipo_conta(conta_origem) ==  "Conta Poupança":
                self.servicecontaPP.sacar(conta_origem, valor, descricao) #Tenta efetuar o saque
                
            saldo_atualCO = self.repoconta.select_saldo(conta_origem) #Depois captura o valor do saldo de origem após a trasferência
            if saldo_atualCO == (saldo_inicialCO - valor): #Se o valor da transferência saiu do saldo da conta de origem ai realiza o depósito na conta de destino
                self.servicecontaPP.depositar(conta_destinatario,valor,"Transferência PIX")
                
                saldo_atualCD = self.repoconta.select_saldo(conta_destinatario) #Pega o saldo da conta de destino após o suposto recebimento
                if valor >0: #Sem essa validação se o valor fosse 0 o saque não ocorreria, mas dispararia a mensagem de transferência concluida, pois o saldo seria atual seria igual ao saldo inical + valor(sendo que é zero)
                    if saldo_atualCD == (saldo_inicialCD + valor): #Verifique se o valor da transferência entrou no saldo da conta de destino
                        print("Transferência realizada")
                    else:
                        self.servicecontaPP.depositar(conta_origem,valor,"Estorno") #Se houver alguma falha e não for possivel o depósito na conta de destino, o valor é estornado para a conta de origem
                        print("Transferência não concluida. Valor Estornado")
                else: pass
                    
            else:
                print("A transferência não realizada")
        else:
            print("Número da conta inválida, verifique os digitos da sua conta ou a conta que deseja enviar o depósito")
            
    
    def relatorio(self, num_banco):
        print("Relatório - Clientes e Contas: ")
        if self.repobanco._select(num_banco) == False: #Executará a função, caso seja diferente de false, executará a função
            print("Nenhum entidade banco cadastrada")