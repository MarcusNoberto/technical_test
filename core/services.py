from .tasks import PersonTask


class PersonService:
    def __init__(self):
        self.task = PersonTask()

    def process_request(self, action, data=None, person_id=None):
        if action == 'create':
            return self.task.create(data)
        elif action == 'update':
            return self.task.update(person_id, data)
        elif action == 'delete':
            return self.task.delete(person_id)
        elif action == 'list_all':
            return self.task.get_all()
        elif action == 'get':
            return self.task.get_by_id(person_id)
        elif action == 'calculate_ideal_weight':
            person = self.task.get_by_id(person_id)
            return person.calculate_ideal_weight()
        else:
            raise ValueError(f"Ação desconhecida: {action}")
