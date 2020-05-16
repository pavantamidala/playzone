from django.shortcuts import render
from django.http import HttpResponse
from .models import PubgTournaments
from django.template import loader

def Pubg(request):
        latest_pubg_list = PubgTournaments.objects.order_by('time')[:5]
        template = loader.get_template('Pubg.html')
        context = {
            'latest_pubg_list': latest_pubg_list,
        }
        return HttpResponse(template.render(context, request))

