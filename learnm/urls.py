
from django.urls import path
from .views import Indexlibra, Indexjob

urlpatterns = [
    path('', Indexlibra.as_view(), name='index'),
    path('indexjob/', Indexjob.as_view(), name='indexjob')

]