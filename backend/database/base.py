from sqlalchemy.orm import declarative_base
from sqlalchemy import MetaData





convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)




#Para evitar Constraint must have a name, configure naming_convention no MetaData do SQLAlchemy. Assim constraints criadas com unique=True, foreign keys etc. recebem nomes automaticamente(nos arquivos de migração), evitando ter que corrigir None manualmente nas migrations.

Base =  declarative_base(metadata=metadata) # O SQLAlchey utiliza esse propriedade para mapear as classes em python, assim podendo reconhecer as mesmas como entidades de um banco de dados


# Crio a convenção
#        ↓
# Crio o MetaData usando a convenção
#        ↓
# Crio a Base usando esse MetaData
#        ↓
# Meus models herdam da Base
#        ↓
# Constraints recebem nomes automaticamente