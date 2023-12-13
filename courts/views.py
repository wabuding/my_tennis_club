from django.http import HttpResponse
from django.template import loader
from .models import Court
from django.shortcuts import render

def courts(request):
  mycourts = Court.objects.all().values()
  template = loader.get_template('all_courts.html')
  context = {
    'mycourts': mycourts,
  }
  return HttpResponse(template.render(context, request))

def court_details(request, id):
  mycourt = Court.objects.get(id=id)
  template = loader.get_template('court_details.html')
  context = {
    'mycourt': mycourt,
  }
  return HttpResponse(template.render(context, request))