from django.urls import path
from .import views
from .import pubg

urlpatterns = [
    path ('',views.home, name = "home"),
    path ('/pubg',pubg.home, name = "pubg"),

]