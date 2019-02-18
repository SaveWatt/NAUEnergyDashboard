from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView
from django.template import Template, Context


def index(request):
    return render(request, 'edashboard/index.html')

def building_view(request):
    return render(request, 'edashboard/building.html')

def compare_view(request):
    return render(request, 'edashboard/compare.html')

def export_view(request):
    return render(request, 'edashboard/export.html')

def help_view(request):
    return render(request, 'edashboard/help.html')

def construction_view(request):
    return render(request, 'edashboard/construction.html')

'''FOR REFERENCE LATER
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
