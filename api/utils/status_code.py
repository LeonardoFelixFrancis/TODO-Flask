from enum import Enum

class HttpStatus(Enum):
    '''
        Enum para encapsular os códigos de retorno HTTP
    '''

    OK = 200
    CREATED = 201

    BAD_REQUEST = 400 
