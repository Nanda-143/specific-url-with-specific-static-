from django.urls import path
from app1.views import *

urlpatterns=[
    path('one/',one,name='one'),
    path('two/',two,name='two'),

]