from backend.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from backend.models.table_conta import Conta

class Cliente(Base):
    
    __tablename__ = 'clientes'
    
    id_cliente: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)
    data_nascimento: Mapped[str] = mapped_column(String, nullable=False)
    # Relationships
    conta: Mapped[Optional["Conta"]] = relationship("Conta", back_populates="cliente",cascade="all, delete-orphan") #Atributo de relacionamento (relationship) que aponta pra outro objeto ORM, nesse caso representa um registro da tabela conta, pode ou não ter uma conta veiculada
    
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        
    def __repr__(self):
        return f"Titular da conta: {self.nome} | CPF: {self.cpf} | Data de nascimento {self.data_nascimento}"
    
    