from api.schemas import session_schema
from infrastructure import models
from infrastructure.database import db
from api.exceptions.custom_exception import CustomException
import uuid
import datetime

class SessionRepository:

    def get_session_by_user_id(self, user_id:int) -> session_schema.Session:

        existing_session = models.Session.query.filter_by(user_id = user_id).first()
        print(existing_session)
        if existing_session is None:
            raise CustomException('O usuário informado não possuí nenhuma sessão ativa')
        
        return session_schema.Session(
            id = existing_session.id,
            user_id = existing_session.user_id,
            access_token = existing_session.access_token,
            created_date = existing_session.created_date,
            minutes_alive = existing_session.minutes_alive
        )
    
    def get_session_by_access_token(self, access_token:str) -> session_schema.Session:

        existing_session = models.Session.query.filter_by(access_token = access_token).first()

        if existing_session is None:
            raise CustomException('O Token informado não está associado a nenhuma sessão ativa', logout=True)
        
        return session_schema.Session(
            id = existing_session.id,
            user_id = existing_session.user_id,
            access_token = existing_session.access_token,
            created_date = existing_session.created_date,
            minutes_alive = existing_session.minutes_alive
        )
    
    def create_session(self, user_id:int) -> session_schema.Session:

        existing_session = models.Session.query.filter_by(user_id = user_id).first()

        if existing_session:

            db.session.delete(existing_session)
            
        new_session = models.Session(
            user_id = user_id,
            access_token = uuid.uuid4(),
            created_date = datetime.datetime.now(),
            minutes_alive = 60*24
        )

        db.session.add(new_session)

        db.session.commit()

        return new_session
    
    def delete_session(self, session:session_schema.Session) -> session_schema.Session:

        existing_session = models.Session.query.filter_by(user_id = session.user_id).first()
        
        db.session.delete(existing_session)

        db.session.commit()

        return session_schema.Session(
            id = existing_session.id,
            user_id = existing_session.user_id,
            access_token = existing_session.access_token,
            created_date = existing_session.created_date,
            minutes_alive = existing_session.minutes_alive
        )