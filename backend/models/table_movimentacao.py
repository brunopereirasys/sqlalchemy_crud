from backend.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Date, Numeric
from decimal import Decimal
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.models.table_conta import Conta

class Movimentacao(Base):
    
    __tablename__ = 'movimentacoes'
    
    id_movimentacao: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_conta: Mapped[int] = mapped_column(Integer, ForeignKey("contas.id_conta"))
    tipo: Mapped[str] = mapped_column(String(20), nullable=False)
    valor: Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)
    descricao: Mapped[str] = mapped_column(String(200), nullable=False)
    data_movimentacao: Mapped[str] = mapped_column(String, nullable=False)
    
    conta: Mapped["Conta"] = relationship("Conta", back_populates= "movimentacao") #Atributo de relacionamento (relationship) que aponta pra outro objeto ORM, nesse caso representa um registro da tabela conta
    
    
    def __init__(self, id_conta, tipo, valor, descricao, data_movimentacao):
        
        self.id_conta = id_conta
        self.tipo = tipo
        self.valor =  valor
        self.descricao = descricao
        self.data_movimentacao = data_movimentacao
        
