from dataclasses import dataclass

@dataclass
class User:

    id:int|None
    email:str
    password:str|None

    def to_dict(self):

        return {
            "id":self.id,
            "email":self.email
        }