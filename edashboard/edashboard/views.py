from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView
from django.template import Template, Context


def index(request):
    return render(request, 'edashboard/index.html')

def construction(request):
    return render(request, 'edashboard/construction.html')

def building_view(request):
    return render(request, 'edashboard/building.html')

def compare_view(request):
    return render(request, 'edashboard/compare.html')

def export_view(request):
    return render(request, 'edashboard/export.html')

def help_view(request):
    return render(request, 'edashboard/help.html')
