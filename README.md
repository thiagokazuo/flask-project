- # Documentação do Projeto Flask

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

![image](https://github.com/user-attachments/assets/42842840-b767-4118-a7ac-c29c27401efe)

**Configuração**

**1. Instalação das Dependências**
Crie um ambiente virtual e instale as dependências necessárias:

![image-2](https://github.com/user-attachments/assets/7db9f8a7-6a14-449b-ba5e-5c9b8c6a0a73)


**2. Configuração do Banco de Dados**
O projeto utiliza SQLite por padrão. Configure a URI do banco de dados e a chave secreta no arquivo <u>config.py:</u>

![image-3 - Copia](https://github.com/user-attachments/assets/bc802ae0-93e6-4d8d-b7c9-abce893c3a2e)


**3. Inicialização do Banco de Dados**
Se estiver usando migrações com **Flask-Migrate:**

![image-4 - Copia](https://github.com/user-attachments/assets/5ee45a77-5f7b-4a3f-a24a-4a1c893d1776)


Se não estiver usando migrações, crie as tabelas manualmente:

![image-5](https://github.com/user-attachments/assets/5563eb47-cf48-4b80-bbdc-1b4dbb3adff1)

No shell Python:

![image-6](https://github.com/user-attachments/assets/55b9de27-b2c5-473f-84b8-878b63a26180)

**Estrutura de Arquivos**

**run.py**

Arquivo para iniciar a aplicação Flask.

**run.py:**

![image-7](https://github.com/user-attachments/assets/b60d19e0-cfdb-4a6b-a88c-14946f54d3ad)

**app/__init__.py**

Configura a aplicação Flask, o banco de dados e o Flask-Login.

**app/__init__.py:**

![image-8](https://github.com/user-attachments/assets/c5f1c35f-f3f9-498e-b09f-6ab1efa93875)

**app/models.py**

Define o modelo de dados e a configuração do banco de dados.

**app/models.py:**

![image-9](https://github.com/user-attachments/assets/87094d47-1514-4a9d-93e2-cc831af70f89)

**app/controllers.py**

Define as rotas e a lógica de autenticação.

**app/controllers.py:**

![image-10](https://github.com/user-attachments/assets/d320b4b1-7561-4d29-b057-81646a2f1feb)

![image-11](https://github.com/user-attachments/assets/df7fb0da-2a2d-4a7d-ba2b-d8f964912a38)

**app/templates/home.html**

Template para a página inicial.

**app/templates/home.html:**

![image-12](https://github.com/user-attachments/assets/f409785e-c1d3-43bd-94f0-03a0b5ffc561)

**app/templates/login.html** e **app/templates/register.html**

Templates para login e registro.

**app/static/styles.css**

Arquivo CSS para estilização.

**app/static/styles.css:**

![image-13 - Copia (2)](https://github.com/user-attachments/assets/d5fba0cb-0ac9-428b-8847-fd6a031a4017)

**Uso**

Inicie o ambiente virtual:

![image-14 - Copia (2)](https://github.com/user-attachments/assets/fdd67e1a-e015-48aa-a1c5-7b652de28410)

Inicie a aplicação Flask:

![image-15 - Copia](https://github.com/user-attachments/assets/e1fc0e2f-de32-4a30-b422-5f347017b34f)

Acesse a aplicação no navegador em http://127.0.0.1:5000.

**Contribuição**
Se você quiser contribuir para o projeto, sinta-se à vontade para fazer um fork e enviar um pull request. Para quaisquer problemas ou sugestões, abra uma issue no repositório.

---
