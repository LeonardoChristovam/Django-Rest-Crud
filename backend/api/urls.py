from django.urls import path
from .views import PessoaViewSet

app_name = 'api'

urlpatterns = [
    path('pessoas', PessoaViewSet.as_view({'get': 'list'}), name='pessoa-list'),
    path('pessoa', PessoaViewSet.as_view({'post': 'create'}), name='pessoa-post'),
    path('pessoa/<str:pk>', PessoaViewSet.as_view({
            'get': 'retrieve',
            'put': 'partial_update',
            'delete': 'destroy'
        }), name='pessoa-detail'),
]