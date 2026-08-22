from sqlalchemy import create_engine


URL = create_engine('sqlite:///backend/data/sistema_bancario.db') # Criando a conexão(engine) e passando o caminho de onde o banco de dados estará


