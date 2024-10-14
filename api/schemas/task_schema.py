from dataclasses import dataclass

@dataclass
class Task:

    id:int | None
    title:str
    description:str
    user_id:int | None

    def to_dict(self):
        
        return {
            "id":self.id,
            "title":self.title,
            "description":self.description
        }