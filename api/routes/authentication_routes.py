from flask import Blueprint, jsonify, request
from api.services.authentication_service import AuthenticationService
from api.utils.status_code import HttpStatus

auth = Blueprint('auth', __name__, url_prefix='/api/user')

@auth.post('/register/')
def register():

    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    user = AuthenticationService().register(email, password)    

    return jsonify({
        "message":"Usuário cadastrado com sucesso",
        "data":user.to_dict(),
        "status_code":HttpStatus.OK.value
    }), HttpStatus.OK.value

@auth.post('/login/')
def login():

    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    user, session = AuthenticationService().login(email, password)    

    return jsonify({
        "message":"Usuário entrou com sucesso no sistema",
        "data":user.to_dict(),
        "token":session.access_token,
        "status_code":HttpStatus.OK.value
    }), HttpStatus.OK.value