from infrastructure.session_repository import SessionRepository
from infrastructure.user_repository import UserRespository
from api.schemas.user_schema import User
from api.schemas.session_schema import Session
from api.exceptions.custom_exception import CustomException
from typing import Union
import datetime
import bcrypt
import re

class AuthenticationService:

    '''
    Classe contendo os serviços de autenticação do sistema
    '''

    def __init__(self):
        self.user_repository = UserRespository()
        self.session_repository = SessionRepository()

    def login(self, email:str, password:str) -> Union[User, Session]:
        
        '''
            Serviço para realizar o login de um usuário com base em um e-mail e uma senha, retornando o usuário e a sessão associada a esse usuário.
        '''

        
        self.__validate_common_fields(email = email,
                                      password = password)

        existing_user = self.user_repository.get_user_with_email(email = email)

        byte_password = password.encode('utf-8')
        
        if not bcrypt.checkpw(byte_password, existing_user.password.encode('utf-8')):
            raise CustomException('Senha incorreta informada')
        
        new_session = self.session_repository.create_session(existing_user.id)
        
        return existing_user, new_session

    def register(self, email:str, password:str) -> User:

        '''
            Serviço para realizar o cadastro de um usuário novo
        '''
        
        self.__validate_common_fields(email = email,
                                      password = password)

        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        if not re.fullmatch(regex, email):
            raise CustomException('Favor informar um e-mail valido')
        
        new_user = self.user_repository.create_user(User(None, email = email, password = password))

        return new_user
    
    def authenticate_with_token(self, token:str) -> User:
        
        '''
            Serviço para autenticar o usuário com um token
        '''

        if token is None:
            raise CustomException('Nenhum token de acesso foi informado', logout=True)

        session = self.session_repository.get_session_by_access_token(token)

        curr_date = datetime.datetime.now()

        time_delta = datetime.timedelta(minutes=session.minutes_alive)

        if (session.created_date + time_delta) < curr_date:
            self.session_repository.delete_session(session)
            raise CustomException('A Sessão do usuário já expirou, favor autenticar novamente', logout=True)
        


        user = self.user_repository.get_user(session.user_id)

        return user

    def __validate_common_fields(self, email:str, password:str):
        
        if not isinstance(email, str):
            raise CustomException('O E-mail precisa ser do tipo texto')
        
        if not isinstance(password, str):
            raise CustomException('A Senha precisa ser do tipo texto')

        if email is None or email == '':
            raise CustomException('O E-mail é um campo obrigatório')
        
        if password is None or password == '':
            raise CustomException('A Senha é um campo obrigatório')
        
        if len(password) < 8:
            raise CustomException('A Senha precisa ter no mínimo 8 caracteres')