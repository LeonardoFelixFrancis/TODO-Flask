Para instalar e executar o projeto:
1) Clone o repositório em um diretório qualquer
2) Crie um ambiente virtual do python novo dentro do repositório clonado com: `python -m venv .venv`
3) Acesse o ambiente virtual com

  a) Windows: `.venv/Scripts/activate`
  b) Linux: `source .venv/bin/activate`

5) Instale todas as dependências do projeto com `pip install -r requirements.txt`
6) Crie um arquivo .env e adicione a variável DATABASE_URL contendo a connection string do banco de dados postgress, ex: DATABASE_URL='postgresql://postgres:123@localhost/my_todo'
8) Rode as migrations com:
   `flask db upgrade`
9) Rode o projeto Flask com `flask run`

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

