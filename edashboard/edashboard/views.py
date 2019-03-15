from django.http import HttpResponse
from django.shortcuts import render


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
