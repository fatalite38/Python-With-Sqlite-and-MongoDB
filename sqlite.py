# DESAFIO DIO - Integrando Python com SQLite e MongoDB - Desenvolvido Por Luiz Fernando D. Pedrozo


# Importando as classes com o sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey


# Declaração das Classes para o Modelo ORM
Base = declarative_base()


class Client(Base):
    """
        Esta classe representa a tabela cliente dentro do SQlite.
    """
    __tablename__ = "client"
    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    cpf = Column(String(9))
    address = Column(String(30))

    def __repr__(self):
        return f"Client(id={self.id}, name={self.name}, address={self.address})"


class Account(Base):
    """
            Esta classe representa a tabela account dentro do SQlite.
        """
    __tablename__ = "account"
    # atributos
    id = Column(Integer, primary_key=True)
    tipo = Column(String(2))
    agency = Column(Integer)
    number = Column(Integer)
    balance = Column(Float)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)

    def __repr__(self):
        return f"Account(id={self.id}, tipo={self.tipo}, saldo={self.balance})"


# Realiza a conexão com o banco de dados
engine = create_engine("sqlite://")


# Cria as classes como tabelas no banco de dados
Base.metadata.create_all(engine)


# Faz a persistência das Informações no Banco de Dados SQLite
with Session(engine) as session:
    luiz = Client(name='Luiz Pedrozo',
                     cpf='289.569.523.28',
                     address='Rua Maria, número 456'
                     )

    mauro = Client(name='Mauro Silva',
                   cpf='141.606.586.28',
                   address='Rua zacarias, número 15'
                   )

    lais = Client(name='Lais Pirra',
                     cpf='426.268.789.77',
                     address='Rua lazaro, número 589'
                     )
    
    carla = Client(name='Carla Moraes',
                     cpf='125.123.355.88',
                     address='Rua lazaro, número 489'
                     )
    

    account1 = Account(client_id='1',
                     tipo='cc',
                     agency=1580,
                     number=520991,
                     balance=20015
                     )
    account2 = Account(client_id='2',
                     tipo='cp',
                     agency=1610,
                     number=315080,
                     balance=21560
                     )
    account3 = Account(client_id='3',
                       tipo='cc',
                       agency=4563,
                       number=155896,
                       balance=15001
                       )
    account4 = Account(client_id='4',
                       tipo='cc',
                       agency=4563,
                       number=120588,
                       balance=13466
                       )

    # Envia as informações para o BD (persitência de dados)
    session.add_all([luiz, mauro, lais, carla])
    session.add_all([account1, account2, account3, account4])
    session.commit()


# Consulta as Informações Salvas no Banco de Dados SQLite

print('Recuperando clientes a partir de uma condição de filtragem:')
stmt_clients = select(Client).where(Client.name.in_(['Luiz Pedrozo', 'Carla Moraes']))
for result in session.scalars(stmt_clients):
    print(result)


print("\nRecuperando clientes de maneira ordenada:")
stmt_order = select(Client).order_by(Client.name.desc())
for result in session.scalars(stmt_order):
    print(result)


print("\nRecuperando contas de maneira ordenada:")
stmt_accounts = select(Account).order_by(Account.tipo.desc())
for result in session.scalars(stmt_accounts):
    print(result)


print("\nRecuperando contas e clientes:")
stmt_join = select(Client.name, Account.tipo, Account.balance).join_from(Client, Account)
connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
for result in results:
    print(result)

session.close()
