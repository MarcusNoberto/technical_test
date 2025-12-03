from django.shortcuts import get_object_or_404
from .models import Person


class PersonTask:
    def create(self, data):
        return Person.objects.create(**data)

    def update(self, person_id, data):
        person = get_object_or_404(Person, pk=person_id)
        for field, value in data.items():
            setattr(person, field, value)
        person.save()
        return person

    def delete(self, person_id):
        person = get_object_or_404(Person, pk=person_id)
        person.delete()

    def get_all(self):
        return Person.objects.all().order_by('id')

    def get_by_id(self, person_id):
        return get_object_or_404(Person, pk=person_id)
