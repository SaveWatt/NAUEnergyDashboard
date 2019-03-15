from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = None
    return render(request, 'edashboard/index.html')
