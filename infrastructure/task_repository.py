from api.schemas import task_schema
from infrastructure import models
from infrastructure.database import db
from api.exceptions.custom_exception import CustomException


class TaskRepository:

    def create_task(self, task:task_schema.Task) -> task_schema.Task:
        
        '''
            Cria uma nova tarefa no banco de dados
        '''

        new_task = models.Task(
            title = task.title,
            description = task.description,
            user_id = task.user_id
        )

        db.session.add(new_task)

        db.session.commit()

        db.session.refresh(new_task)

        task.id = new_task.id

        return task

    def update_task(self, task:task_schema.Task) -> task_schema.Task:

        '''
            Atualiza uma tarefa no banco de dados
        '''

        existing_task = models.Task.query.get(task.id)
        
        if existing_task is None:
            raise CustomException("O Id informado não é associado a nenhuma tarefa válida")

        if existing_task.user_id != task.user_id:
            raise CustomException("A Tarefa informada não pertence ao usuário autenticado")

        existing_task.title = task.title
        existing_task.description = task.description

        db.session.commit()

        return task
    
    def delete_task(self, task:task_schema.Task) -> task_schema.Task:

        '''
            Deleta uma tarefa do banco de dados
        '''

        existing_task = models.Task.query.get(task.id)

        db.session.delete(existing_task)

        db.session.commit()
        
        return task_schema.Task(
            id = existing_task.id,
            title = existing_task.title,
            description = existing_task.description,
            user_id = existing_task.user_id
        )

    def retrieve_task(self, task_id:int) -> task_schema.Task:
        
        '''
            Retorna uma tarefa do banco de dados
        '''

        existing_task = models.Task.query.get(task_id)

        if existing_task is None:
            raise CustomException("O Id informado não é associado a nenhuma tarefa válida")

        return task_schema.Task(
            id = existing_task.id,
            title = existing_task.title,
            description = existing_task.description,
            user_id = existing_task.user_id
        )

    def list_task(self, user_id:int=None) -> list[task_schema.Task]:
        

        '''
            Lista tarefas do banco de dados, quando recebe um user_id traz apenas as tarefas do usuário informado.
        '''

        task_list = []

        if user_id is None:
            tasks = models.Task.query.all()
        else:
            tasks = models.Task.query.filter_by(user_id = user_id)

        for task in tasks:
            task_list.append(
                task_schema.Task(
                    id = task.id,
                    title = task.title,
                    description = task.description,
                    user_id = task.user_id
                )
            )

        return task_list
