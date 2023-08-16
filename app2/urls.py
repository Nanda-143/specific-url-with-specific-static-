from django.urls import path
from app2.views import *
urlpatterns=[
    path('three/',three,name='three'),
    path('four/',four,name='four'),

]