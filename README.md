Para instalar e executar o projeto:
1) Clone o repositório em um diretório qualquer.
2) Abra o terminal para realizar as instruções abaixo.
3) Crie um ambiente virtual do python novo dentro do repositório clonado com: `python -m venv .venv`.
4) Acesse o ambiente virtual com

  a) Windows: `.venv/Scripts/activate`
  b) Linux: `source .venv/bin/activate`

5) Instale todas as dependências do projeto com `pip install -r requirements.txt`.
6) Crie um arquivo .env e adicione nele a variável DATABASE_URL contendo a connection string do banco de dados postgress, ex: DATABASE_URL='postgresql://postgres:123@localhost/my_todo'.
   6.1) É necessário ter o postgress rodando localmente, e criar um banco de dados, após isso é só trocar o 'my_todo' da connection string acima pelo nome do banco de dados que foi criado.
8) Rode as migrations executando os comandos:
   ```
    flask db init
    flask db migrate
    flask db upgrade
   ```
    
10) Rode o projeto Flask com `flask run`.

##### Versão python usada no desenvolvimento: 3.11.9

### POST /user/login

Input: {  "email": string, "password": string" }

Responses:

HTTP 200: { "data": {"email": string, "id": int}, "message": string, "status_code": int, "token": string }  
HTTP 400: { "data": null, "logout": false, "message": string, "status_code": int}
      	
### POST /user/register

Input: {  "email": string, "password": string" }

Responses:

HTTP 200: { "data": {"email": string, "id": int}, "message": string, "status_code": int}  
HTTP 400: { "data": null, "logout": false, "message": string, "status_code": int}

### POST /task/

Input: {  "title": string, "description": string" }

Responses:

HTTP 200: { "data": {"description": string, "title":string, "id": int}, "message": string, "status_code": int}  
HTTP 400: { "data": null, "logout": false, "message": string, "status_code": int}

### PUT /task/

Input: {  "title": string, "description": string", "id":int }

Responses:

HTTP 200: { "data": {"description": string, "title":string, "id": int}, "message": string, "status_code": int}  
HTTP 400: { "data": null, "logout": false, "message": string, "status_code": int}

### DELETE /task/<task_id:int>
Responses:

HTTP 200: { "data": null, "message": string, "status_code": int}  
HTTP 400: { "data": null, "logout": false, "message": string, "status_code": int}

### GET /task/<task_id:int>
Responses:

HTTP 200: {"data": {"description": string, "title":string, "id": int}, "message": string, "status_code": int}, 
HTTP 400: { "data": null, "logout": false, "message": string, "status_code": int}

### GET /task/list
Responses:

HTTP 200: {"data": [{"description": string, "title":string, "id":int},...], "message": string, "status_code": int}, 
HTTP 400: { "data": null, "logout": false, "message": string, "status_code": int}

