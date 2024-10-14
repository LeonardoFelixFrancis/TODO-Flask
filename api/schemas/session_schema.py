from dataclasses import dataclass
from datetime import datetime

@dataclass
class Session:

    id:int
    user_id:int
    access_token:str
    created_date:datetime
    minutes_alive:int