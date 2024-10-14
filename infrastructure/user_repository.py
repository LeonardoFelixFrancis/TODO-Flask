from api.schemas import user_schema
from infrastructure import models
from infrastructure.database import db
from api.exceptions.custom_exception import CustomException
import bcrypt

class UserRespository:

    def get_user(self, user_id:int) -> user_schema.User:

        '''
            Retorna um usuário do banco de dados
        '''

        existing_user = models.User.query.get(user_id)

        if existing_user is None:
            raise CustomException("O Id informado não é associado a nenhum usuário")
        
        return user_schema.User(
            id = existing_user.id,
            email = existing_user.email,
            password = existing_user.password
        )
    
    def get_user_with_email(self, email:str) -> user_schema.User:

        '''
            Retorna um usuário do banco de dados com base em um e-mail
        '''

        existing_user = models.User.query.filter_by(email = email).first()

        if existing_user is None:
            raise CustomException("O E-mail informado não é associado a nenhum usuário")
        
        return user_schema.User(
            id = existing_user.id,
            email = existing_user.email,
            password = existing_user.password
        )
    
    def create_user(self, user:user_schema.User) -> user_schema.User:
        
        '''
            Cria um novo usuário no banco de dados
        '''

        existing_user = models.User.query.filter_by(email = user.email).first()
        
        if existing_user != None:
            raise CustomException('E-mail informado já existe no sistema')
        
        bytes_password = user.password.encode('utf-8')
        hashed_password = bcrypt.hashpw(bytes_password, bcrypt.gensalt())

        new_user = models.User(
            email = user.email,
            password = hashed_password.decode('utf-8')
        )

        db.session.add(new_user)

        db.session.commit()

        return user
    
    