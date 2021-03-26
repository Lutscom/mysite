from django.urls import path

from . import views

urlpatterns = [
    path('65', views.index2, name='index'),
    path('cat', views.html1, name='html1'),
    path('dog', views.html2, name='html2'),
    path('1', views.index, name='1'),
    path('2', views.index1, name='2'),
]