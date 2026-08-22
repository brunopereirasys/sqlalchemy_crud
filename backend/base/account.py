from abc import ABC, abstractmethod



class Conta(ABC):
    
    @abstractmethod
    def listar_contas(self):
        pass
    
    @abstractmethod
    def ver_saldo(self, numero_conta) -> int:
        pass
    
    @abstractmethod
    def extrato(self, numero_conta) -> None: 
        pass
    
    @abstractmethod
    def registrar_conta(self, id_cliente, id_banco, saldo):
        pass

    @abstractmethod
    def depositar(self, numero_conta, valordeposito, descricao) ->None:
        pass
            
    @abstractmethod
    def sacar(self, numero_conta, valordeposito, descricao) -> None: 
        pass
    

class ContaRentavel(Conta):
    
    @abstractmethod
    def rentabilizar(self, numero_conta) -> None:
        pass