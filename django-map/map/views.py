from django.shortcuts import render
from django.views import generic
from django.core import serializers

from .models import Problem

class HomePage(generic.View):
    
    def get(self, request):
        context = {
            'queryset': serializers.serialize("json", [x for x in Problem.objects.all()])
        }
        return render(
            request,
            "map/map.html",
            context
        )
    