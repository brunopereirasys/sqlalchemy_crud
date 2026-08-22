from backend.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from typing import TYPE_CHECKING #TYPE_CHECKING é usado só pra tipagem, não roda em execuçã.Ele serve para colocar imports que o Python não executa em runtime, evitando:import circular, imports pesados desnecessários...



if TYPE_CHECKING:
    from backend.models.table_conta import Conta


class Banco(Base): #Classe representando a tabela 'bancos'
    
    __tablename__ = "bancos" # nome da tabela
    
    id_banco: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome_banco: Mapped[str] = mapped_column(String(30), nullable=False,)
    num_banco: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    
    
    conta: Mapped[list["Conta"]] = relationship("Conta", back_populates='banco') #Atributo de relacionamento (relationship) que aponta pra outro objeto ORM, nesse caso representa um registro da tabela Conta
    
    def __init__(self, nome_banco:str) -> None:
        self.nome_banco = nome_banco
        self.num_banco = 237 
        
    

