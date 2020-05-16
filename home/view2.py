from django.shortcuts import render

# Create your views here.
def createnewtournament(request):
    return render (request,'NewTournament.html')