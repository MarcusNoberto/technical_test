# core/models.py
from django.db import models


class Person(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    height = models.FloatField(help_text="Altura em metros")
    weight = models.FloatField(help_text="Peso em kg")

    def calculate_ideal_weight(self):
        if self.gender == 'M':
            return (72.7 * self.height) - 58
        else:
            return (62.1 * self.height) - 44.7

    def __str__(self):
        return f"{self.id} - {self.name}"
