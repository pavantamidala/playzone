from django.urls import path
from .import view2,views
urlpatterns=[
    path('',views.home,name="home"),
    path('createnewtournament',view2.createnewtournament,name="createnewtournament"),
]