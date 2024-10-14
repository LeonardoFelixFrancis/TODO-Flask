from api.exceptions.custom_exception import CustomException
from infrastructure.task_repository import TaskRepository
from api.schemas.user_schema import User
from api.schemas.task_schema import Task

class TaskService:

    """
        Classe contendo todos os serviços associados as Tarefas

        No seu construtor cria uma instância de um TaskRepository para ser utilizado como self.infrastructure.
    """

    def __init__(self):
        self.infrastructure = TaskRepository()

    def create_task(self, title:str, description:str, authenticated_user:User) -> dict:

        '''
            Serviço para criar uma nova tarefa, recebe um Título uma descrição e o Usuário autenticado para fazer a relação Tarefa -> Usuário.
        '''

        self.__validate_common_fields(title, description)

        new_task = self.infrastructure.create_task(Task(
            id = None,
            title = title,
            description = description,
            user_id = authenticated_user.id
        ))

        return new_task.to_dict()
    
    def retrieve_task(self, task_id:int, authenticated_user:User) -> dict:

        '''
            Serviço para recuperar uma tarefa do banco de dados com base em um Id e no usuário autenticado.
        '''

        self.__validate_task_id(task_id)

        existing_task = self.infrastructure.retrieve_task(task_id)

        if existing_task.user_id != authenticated_user.id:
            raise CustomException('A Tarefa informada não percente ao usuário autenticado')

        return existing_task.to_dict()
        
    def update_task(self, title:str, description:str, task_id:int, authenticated_user:User) -> dict:

        '''
            Serviço para fazer a atualização de uma tarefa, recebendo o usuário autenticado para fazer a validação de sua permissão sob a tarefa informada.
        '''

        self.__validate_common_fields(title, description)
        self.__validate_task_id(task_id)

        new_task = self.infrastructure.update_task(Task(id = task_id,
                                                        title = title,
                                                        description = description,
                                                        user_id=authenticated_user.id))

        return new_task.to_dict()
    
    def delete_task(self, task_id:int, authenticated_user:User) -> dict:
        
        '''
            Serviço para deletar uma tarefa, recebendo o usuário autenticado para fazer a validação de sua permissão sob a tarefa informada.
        '''

        
        self.__validate_task_id(task_id)

        existing_task = self.infrastructure.retrieve_task(task_id)

        if existing_task.user_id != authenticated_user.id:
            raise CustomException('Tarefa informada não pertence ao usuário informado')

        self.infrastructure.delete_task(existing_task)

        return existing_task.to_dict()

    def list_tasks(self, authenticated_user:User) -> list[dict]:

        tasks = self.infrastructure.list_task(authenticated_user.id)

        return [task.to_dict() for task in tasks]


    def __validate_common_fields(self, title:str, description:str):

        '''
            Faz as validações básicas de input dos campos Título e descrição
        '''

        if title is None or len(title) == 0:
            raise CustomException('O Título de uma tarefa é um campo obrigatório')
        
        if description is None or len(description) == 0:
            raise CustomException('A descrição de uma tarefa é um campo obrigatório')
        
        if not isinstance(title, str):
            raise CustomException('O Título de uma tarefa precisa ser um campo do tipo Texto')
        
        if not isinstance(description, str):
            raise CustomException('O Campo descrição precisa ser um campo do tipo Texto')

        if len(title) > 55:
            raise CustomException('O Título de uma tarefa não pode ter mais de 55 caracteres')
        
        if len(description) > 255:
            raise CustomException('A Descrição de uma tarefa não pode ter mais de 255 caracteres')
        
    def __validate_task_id(self, task_id:int):

        '''
            Valida o input do Id de uma tarefa
        '''

        if task_id is None:
            raise CustomException('O Id de uma tarefa precisa ser informado')
        
        if not isinstance(task_id, int):
            raise CustomException("O campo 'task_id' precisa ser um numero inteiro")
        
        if task_id <= 0:
            raise CustomException("O campo 'task_id' precisa ser um número inteiro positivo")






        

