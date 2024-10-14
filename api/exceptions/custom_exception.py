from flask import jsonify
from api.utils.status_code import HttpStatus

class CustomException(Exception):
    def __init__(self, message, status_code=HttpStatus.BAD_REQUEST.value, logout=False):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.logout = logout

    def to_dict(self):
        
        response = dict()
        response['message'] = self.message
        response['status_code'] = self.status_code
        response['data'] = None
        response['logout'] = self.logout
        return response
