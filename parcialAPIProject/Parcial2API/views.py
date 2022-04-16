from django.shortcuts import render
from django.views import View
from .models import Years
from django.http import JsonResponse
from django.forms import model_to_dict
# Create your views here.

class YearsListView(View):
    def get(self, request):
        clist = Years.objects.all()
        return JsonResponse(list(clist.values()), safe=False)

class YearsDetailView(View):
    def get(self, request, pk):
        years = Years.objects.get(pk=pk)
        return JsonResponse(model_to_dict(years))

