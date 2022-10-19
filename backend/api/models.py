from django.db import models

import uuid


class Pessoa(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True
    )

    nome = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )

    data_nasc = models.CharField(
        max_length=10,
        null=False,
        blank=False,
    )

    telefone = models.CharField(
        max_length=15,
        null=False,
        blank=False,
    )

    email = models.CharField(
        max_length=150,
        null=False,
        blank=False,
    )

    sexo = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        choices=[
            ('m', 'Masculino'), ('f', 'Feminino')
        ]
    )