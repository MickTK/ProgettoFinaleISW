from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def login(request):
  template = loader.get_template("login.html")
  context = {}
  return HttpResponse(template.render(context, request))
