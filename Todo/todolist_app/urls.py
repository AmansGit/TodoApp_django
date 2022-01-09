from django.urls import path
from . import views

urlpatterns = [
    path('todolist', views.todolist, name='todolist'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    # path('todolist/', views.todolist, name='todolist'),
]
