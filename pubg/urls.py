from django.urls import path
from .import views
from .import pubg

urlpatterns = [
<<<<<<< HEAD
    path ('',views.home, name = "home"),
    path ('/pubg',pubg.home, name = "pubg"),
=======
    path ('',views.Pubg, name = "Pubg")
>>>>>>> e9b9e34290a59b402c55c91cbf901657ad9a4d52

]