from django.urls import re_path
from app.views import index,base
urlpatterns =[
    re_path(r'$^',index,name='index'),
    re_path(r'base/',base,name='base')
]
