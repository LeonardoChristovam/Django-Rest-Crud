from rest_framework import serializers
from api.models import Pessoa


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = [
            'id',
            'nome',
            'data_nasc',
            'telefone',
            'email',
            'sexo',
        ]