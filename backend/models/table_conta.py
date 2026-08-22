
from backend.database.base import Base
from sqlalchemy import String, Integer, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from decimal import Decimal
from typing import TYPE_CHECKING



if TYPE_CHECKING:
    from backend.models.table_cliente import Cliente
    from backend.models.table_banco import Banco
    from backend.models.table_movimentacao import Movimentacao

    
class Conta(Base):
    
    __tablename__ = 'contas'#Nome da tabela no banco de dados
    
    id_conta: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_cliente: Mapped[int] = mapped_column(Integer, ForeignKey('clientes.id_cliente'), unique=True) # Chave estrangeira da Tabela 'clientes'(Responsavel por criar a tabela id_cliente)
    id_banco: Mapped[int] = mapped_column(Integer, ForeignKey('bancos.id_banco'))
    numero_conta: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    agencia: Mapped[int] = mapped_column(Integer, nullable=False)
    saldo: Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)
    tipo: Mapped[str] =mapped_column(String(20), nullable=False)
    limite_especial: Mapped[Decimal] = mapped_column(Numeric(10,20), nullable=False)
    
    # Relationships
    cliente: Mapped["Cliente"] = relationship("Cliente", back_populates="conta") #Atributo de relacionamento (relationship) que aponta pra outro objeto ORM, nesse caso representa um registro da tabela Cliente
    banco: Mapped["Banco"] = relationship("Banco", back_populates="conta") #Atributo de relacionamento (relationship) que aponta pra outro objeto ORM, nesse caso representa um registro da tabela Banco
    movimentacao: Mapped[list["Movimentacao"]] = relationship("Movimentacao", back_populates="conta",cascade="all, delete-orphan") #Atributo de relacionamento (relationship) que aponta pra outro objeto ORM, nesse caso representa um registro da tabela movimentacao
    
    
    
    def __init__(self, id_cliente,id_banco,numero_conta, saldo, tipo,limite_especial) -> None:
        self.id_cliente = id_cliente
        self.id_banco = id_banco
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.tipo = tipo
        self.agencia = 1826 #numéro da agéncia é fixo
        self.limite_especial = limite_especial


    def __repr__(self):# método que permite printar o objeto 'print(objeto)'
        return f" Tipo da conta: {self.tipo} | Saldo R$ {self.saldo} | Agência: {self.agencia}"
    
    


