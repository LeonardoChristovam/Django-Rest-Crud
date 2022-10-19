from django.shortcuts import render

from api.serializers import PessoaSerializer
from rest_framework import viewsets, permissions
from api.models import Pessoa


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = []
