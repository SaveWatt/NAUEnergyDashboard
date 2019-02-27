from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView
from django.template import Template, Context
from django import template
from edashboard.models import Demo
register = template.Library()


def index(request):
    return render(request, 'edashboard/index.html')

def building_view(request):
    return render(request, 'edashboard/building.html')

def compare_view(request):
    return render(request, 'edashboard/compare.html')

def export_view(request):
    db_data = Demo.objects.all().values_list('value', flat=True)
    db_date = Demo.objects.all().values_list('date', flat=True)
    db_id = Demo.objects.all().values_list('id', flat=True)
    return render(request, 'edashboard/export.html',{'db_data':db_data, 'db_id':db_id})

def compare_view(request):
    db_data = Demo.objects.all().values_list('value', flat=True)
    db_date = Demo.objects.all().values_list('date', flat=True)
    db_id = Demo.objects.all().values_list('id', flat=True)
    return render(request, 'edashboard/compare.html',{'db_data':db_data, 'db_id':db_id})

def help_view(request):
    return render(request, 'edashboard/help.html')

def construction_view(request):
    return render(request, 'edashboard/construction.html')

def login_view(request):
    return render(request, 'edashboard/login.html')

def admin_view(request):
    return render(request, 'edashboard/admin.html')
'''
def data(request):
    db_data = Demo.objects.all().values_list('value', flat=True)
    db_date = Demo.objects.all().values_list('date', flat=True)
    return TemplateResponse(request, 'edashboard/export.html', {"db_data" : db_data})

def data_com(request):
    db_data = Demo.objects.all().values_list('value', flat=True)
    db_date = Demo.objects.all().values_list('date', flat=True)
    return TemplateResponse(request, 'edashboard/compare.html', {"db_data" : db_data})

@register.building_name
def getBuildingsName():
    building = []
    filename="buildings.csv"
    with open(filename,'r') as f:
        lines= f.readlines()
        for line in lines:
            if "number,name" not in line:
                building.insert(len(building),line.rsplit(',', 1)[1])
    f.close()
    return building

@register.building_num
def getBuildingsNumber():
    building = []
    filename="buildings.csv"
    with open(filename,'r') as f:
        lines= f.readlines()
        for line in lines:
            if "number,name" not in line:
                building.insert(len(building),line.rsplit(',', 1)[0])
    f.close()
    return building

    FOR REFERENCE LATER
    #Pass in value and convert to kwH and convert based on string that conversion is.
    #CONVERSION LINK https://www.epa.gov/energy/greenhouse-gases-equivalencies-calculator-calculations-and-references
    def greenComp(value,conversion):

        kwh = value
        mtons = value*.0007
        kilog=value*0.707
        lbs=value*1.6
        #BARRELS OF OIL 5.80 mmbtu/barrel × 20.31 kg C/mmbtu × 44 kg CO2/12 kg C × 1 metric ton/1,000 kg
        if conversion=="oil":
            return mtons/.43
        #TREE'S GROWN FOR 10 YEARS
        elif conversion=="tree":
            return mtons/.06
        #CARBON OFFSET
        elif conversion=="carbon" :
            return value
        #Converts to Tons
        elif conversion=="tons" :
            return value*.0008
        # Converts to Gas
        elif conversion=="gas" :
            return mtons/(8.887*(10 ** (-3)))
        # CONVERTS BTU TO kWh
        elif conversion=="btu" :
            return kwh * 3412.14
        # Converts to DOLLARS
        else:
            return kwh * 11.1
    '''
