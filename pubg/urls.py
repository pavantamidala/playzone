from django.urls import path
from .import views
from .import pubg

urlpatterns = [
    path ('',views.Pubg, name = "Pubg")
]