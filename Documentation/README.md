# Documentação do Projeto Flask
-

**Visão Geral**
Este projeto é uma aplicação web básica construída com Flask, utilizando a arquitetura MVC. Ele inclui funcionalidades de autenticação, registro de usuários e uma página inicial protegida que só pode ser acessada após o login.

## Requisitos
Python 3.6+
Flask
Flask-WTF
Flask-Login
Flask-SQLAlchemy
Flask-Migrate
Werkzeug
SQLite (para o banco de dados)

**Estrutura do Projeto**

![alt text](image-1.png)

**Configuração**

**1. Instalação das Dependências**
Crie um ambiente virtual e instale as dependências necessárias:

![alt text](image-2.png)

**2. Configuração do Banco de Dados**
O projeto utiliza SQLite por padrão. Configure a URI do banco de dados e a chave secreta no arquivo <u>config.py:</u>

![alt text](image-3.png)

**3. Inicialização do Banco de Dados**
Se estiver usando migrações com **Flask-Migrate:**

![alt text](image-4.png)

Se não estiver usando migrações, crie as tabelas manualmente:

![alt text](image-5.png)

No shell Python:

![alt text](image-6.png)

**Estrutura de Arquivos**

**run.py**

Arquivo para iniciar a aplicação Flask.

**run.py:**

![alt text](image-7.png)

**app/__init__.py**

Configura a aplicação Flask, o banco de dados e o Flask-Login.

**app/__init__.py:**

![alt text](image-8.png)

**app/models.py**

Define o modelo de dados e a configuração do banco de dados.

**app/models.py:**

![alt text](image-9.png)

**app/controllers.py**

Define as rotas e a lógica de autenticação.

**app/controllers.py:**

![alt text](image-10.png)

![alt text](image-11.png)

**app/templates/home.html**

Template para a página inicial.

**app/templates/home.html:**

![alt text](image-12.png)

**app/templates/login.html** e **app/templates/register.html**

Templates para login e registro.

**app/static/styles.css**

Arquivo CSS para estilização.

**app/static/styles.css:**

![alt text](image-13.png)

**Uso**

Inicie o ambiente virtual:

![alt text](image-14.png)

Inicie a aplicação Flask:

![alt text](image-15.png)

Acesse a aplicação no navegador em http://127.0.0.1:5000.

**Contribuição**
Se você quiser contribuir para o projeto, sinta-se à vontade para fazer um fork e enviar um pull request. Para quaisquer problemas ou sugestões, abra uma issue no repositório.

---
