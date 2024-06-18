# Integrando Python com SQLite e MongoDB

Este projeto demonstra como integrar Python com SQLite e MongoDB para gerenciar dados de clientes e contas.

## Descrição - Parte 1

O código Python implementa as seguintes funcionalidades:

* **Modelo ORM (Object-Relational Mapping) com SQLAlchemy:**
    * Define classes `Client` e `Account` para representar as tabelas no SQLite.
    * Utiliza o SQLAlchemy para criar as tabelas no banco de dados.
    * Permite persistência de dados através de sessões.
* **Conexão com SQLite:**
    * Cria uma conexão com o banco de dados SQLite.
    * Realiza operações de inserção, consulta e ordenação de dados.
* **Consulta e Exibição de Dados:**
    * Consulta os dados inseridos no SQLite usando instruções SQL.
    * Imprime os resultados das consultas.

## Pré-requisitos

* Python 3.x
* Biblioteca SQLAlchemy (instale com `pip install sqlalchemy`)

  
## Descrição - Parte 2

## Funcionalidades:

* **Conexão com MongoDB:** O código estabelece uma conexão com um servidor MongoDB usando a biblioteca `pymongo`.
* **Criação de Banco de Dados e Coleção:** Define um banco de dados chamado "bank" e uma coleção chamada "clients".
* **Inserção de Dados:** Insere um conjunto de dados de clientes na coleção "clients", incluindo informações como agência, nome, CPF, endereço, tipo de conta, número da conta e saldo.
* **Recuperação de Dados:**
    * Recupera informações de um cliente específico pelo nome.
    * Lista todos os clientes presentes na coleção.
    * Recupera dados de clientes em ordem alfabética pelo nome.
    * Filtra clientes por agência, tipo de conta (conta corrente ou poupança).
* **Impressão de Resultados:** Imprime os resultados das consultas usando a biblioteca `pprint`.

## Pré-requisitos:

* Python instalado
* Biblioteca `pymongo` instalada (use `pip install pymongo`)
* MongoDB instalado e configurado

## Instruções:

1. **Substitua o "link-para-o-mongo-db"** na primeira linha do código com o link do seu servidor MongoDB.
2. **Execute o código** usando um interpretador Python (por exemplo, `python mongodb.py`).

## Observações:

* Este código é um exemplo básico de como integrar Python com o MongoDB. 
* Você pode adaptá-lo para suas necessidades específicas, adicionando mais funcionalidades, como atualização e exclusão de dados.


