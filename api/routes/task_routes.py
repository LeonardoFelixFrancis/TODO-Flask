from flask import Blueprint, request,g, jsonify
from api.services.task_service import TaskService
from api.utils.status_code import HttpStatus
from api.exceptions.custom_exception import CustomException
from api.services.authentication_service import AuthenticationService

todo = Blueprint('task', __name__, url_prefix='/task')

@todo.before_request
def authenticate():

    if request.method != 'OPTIONS':
        auth_token = request.headers.get('Authorization')

        user = AuthenticationService().authenticate_with_token(auth_token)

        g.user = user
    

@todo.route('/', methods=["POST"])
def create_task():

    data = request.get_json()
    
    title = data.get('title')
    description = data.get('description')
    
    new_task = TaskService().create_task(title = title,
                                        description = description,
                                        authenticated_user = g.user)
    
    return jsonify({"message":f"A tarefa {title} foi criada com sucesso", "data":new_task, "status_code":HttpStatus.OK.value}), HttpStatus.CREATED.value

@todo.route('/', methods=["PUT"])
def update_task():
    
    data = request.get_json()
    
    title = data.get('title')
    description = data.get('description')
    task_id = data.get('id')

    new_task = TaskService().update_task(title = title, description = description, task_id = task_id, authenticated_user = g.user)
    
    return jsonify({"message":f"A tarefa {title} foi atualizada com sucesso", 
    "data":new_task, 
    "status_code":HttpStatus.OK.value}), HttpStatus.OK.value

    
@todo.route('/<int:task_id>', methods=["GET"])
def get_task(task_id:int):

    task = TaskService().retrieve_task(task_id = task_id, authenticated_user = g.user)

    return jsonify({
        "data":task,
        "message":"Tarefa retornada com sucesso",
        "status_code":HttpStatus.OK.value
    }), HttpStatus.OK.value

@todo.route("/list", methods=["GET"])
def list_tasks():
    print(g.user)
    tasks = TaskService().list_tasks(g.user)

    return jsonify({
        "message":"Lista de tarefas retornadas com sucesso",
        "data":tasks,
        "status_code":HttpStatus.OK.value
    }), HttpStatus.OK.value


@todo.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id:int):

    TaskService().delete_task(task_id, g.user)

    return jsonify({
        "message":"Tarefa excluída com sucesso",
        "status_code":HttpStatus.OK.value,
        "data":None
    }), HttpStatus.OK.value

