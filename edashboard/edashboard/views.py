from django.http import HttpResponse
from django.shortcuts import render, redirect
from http.server import BaseHTTPRequestHandler, HTTPServer
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
import csv
from django.contrib import auth
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.template import Template, Context
from django import template
from edashboard.clean import *
from edashboard.models import *
from django.views import View
from django.http import JsonResponse
from edashboard.forms import *
import json
import time
#from edashboard.StaticDataRetriever import StaticDataRetriever
import statistics as stats
import datetime
from edashboard.Backend import Backend

register = template.Library()
b = Backend()
bnum = b.getNumStrings()
#sorts by name
bname = b.getBuildingStrings()
bname.sort()
#sdr = StaticDataRetriever()



def index(request):
    #Sorts by number
    buildings = b.getBuildingStrings()
    return render(request, 'edashboard/index.html',{'buildlist': buildings,'buildlistname':bname,
    'buildlistnum':bnum})

def building_view(request, buildnum):
    sdr = StaticDataRetriever()
    buildings = b.getBuildingStrings()
    building = Building.objects.get(b_num=buildnum)
    buildname = building.b_name
    build_id = building.id
    sens = Sensor.objects.get(building_id=build_id, s_type='Current Demand KW')
    log_dict = sdr.get_log(sens.s_log)
    usage = []
    date = []
    count = 0
    for key in reversed(sorted(log_dict.keys())):
        if count > 99:
            break;
        date.append(log_dict[key][0])
        usage.append(log_dict[key][1])
        count += 1
    percent = sum(usage)/10000*100
    percent_str = ("%d%%" % round(percent, 2))
    mean = round(sum(usage)/len(usage), 2)
    median = round(stats.median(usage), 2)
    usage.reverse()
    date.reverse()
    return render(request, 'edashboard/building.html', {'buildlist': buildings,
                                                        'buildlistname':bname,
                                                        'buildlistnum':bnum,
                                                        'bnum': buildnum,
                                                        'bname':buildname,
                                                        'usage':usage,
                                                        'date':date,
                                                        'percent':percent,
                                                        'percent_str':percent_str,
                                                        'mean': mean,
                                                        'median': median})

def compare_view(request):
    buildings = b.getBuildingStrings()
    return render(request, 'edashboard/compare.html',{'buildlist': buildings,'buildlistname':bname,
    'buildlistnum':bnum})

def export_view(request,builddata=None):
    flag = ""
    sensor = ""
    util = ""
    if "util=" in str(builddata):
        flag = "util"
    if "sensor=" in str(builddata):
        flag = "sens"
    data = splitUrls(builddata, flag)
    buildnum = data[0]
    starttime = getTimes(data[2])
    endtime = getTimes(data[3])
    if flag == "util":
        util = data[1]
    if flag == "sens":
        sensor = data[1]
    # buildings = Building.objects.all()
    buildings = b.getBuildingStrings()
    usage = []
    date = []
    print(buildnum)
    if buildnum and buildnum != 'B':
        building = Building.objects.get(b_num=buildnum)
        buildname = building.b_name
        build_id = building.id
        try:
            sens = Sensor.objects.get(building_id=build_id, s_type=util)
        except:
            sens = Sensor.objects.get(building_id=57, s_log='601_2')
        log_dict = sdr.get_log(sens.s_log)
        count = 0
        for key in reversed(sorted(log_dict.keys())):
            if count > 99:
                break;
            date.append(log_dict[key][0].strftime("%Y-%m-%d %H:%M:%S"))
            usage.append(log_dict[key][1])
            count += 1
        #date = reversed(date)
        #usage = reversed(usage)

    return render(request, 'edashboard/export.html',{'buildlist': buildings,'builddata':builddata,'usage':usage,'date':date,'buildlistname':bname,
    'buildlistnum':bnum})

def down_export(request,data):
    buildings = b.getBuildingStrings()
    i=0
    finalstr="USAGE,DATE\n"
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=data_usage.csv'
    writer = csv.writer(response, csv)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"DATE"),
        smart_str(u"USAGE"),
    ])
    cleandata = data.split(",")
    j=cleandata.index("date")+1
    for i in range(0,cleandata.index("date")):
        writer.writerow([
            smart_str(cleandata[j]),
            smart_str(cleandata[i]),
        ])
        j+=1
    return response


def exporth_view(request):
    buildings = b.getBuildingStrings()
    return render(request, 'edashboard/export.html',{'buildlist': buildings,'buildlistname':bname,
    'buildlistnum':bnum})

def get_data(request):
    date = "Tues"
    usage = 10
    return JsonResponse({'data': usage,'date':date,'buildlistname':bname,
    'buildlistnum':bnum})

def login(request):
   return render(request, 'edashboard/login.html',{
       'form': form_login,
       'username': username})

def register(request):
    if request.method =="POST":
        buildings = b.getBuildingStrings()
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'edashboard/index.html',{'buildlist': buildings})
    else:
        form = RegistrationForm()
    return render(request, 'edashboard/register.html',{'form':form})


def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return HttpResponse("<strong>You are logged out.</strong>")

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)

def compareh_view(request):
    buildings = b.getBuildingStrings()
    return render(request, 'edashboard/compare.html',{'buildlist': buildings,'buildlistname':bname,
    'buildlistnum':bnum})

def compare_view(request,builddata=None):
    buildings = b.getBuildingStrings()
    flag = ""
    sensor = ""
    util = ""
    if "util=" in str(builddata):
        flag = "util"
    if "sensor=" in str(builddata):
        flag = "sens"
    data = splitUrls(builddata, flag)
    buildnum = data[0]
    starttime = getTimes(data[2])
    endtime = getTimes(data[3])
    if flag == "util":
        util = data[1]
    if flag == "sens":
        sensor = data[1]
    usage=[1,5,8,3,5]
    date=[1,2,3,4,5]
    return render(request, 'edashboard/compare.html',{'buildlist': buildings,'builddata':builddata,'usage':usage,'date':date,'buildlistname':bname,
    'buildlistnum':bnum})

def down_compare(request, data):
        buildings = b.getBuildingStrings()
        i=0
        finalstr="USAGE,DATE\n"
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=data_usage.csv'
        writer = csv.writer(response, csv)
        response.write(u'\ufeff'.encode('utf8'))
        writer.writerow([
            smart_str(u"USAGE"),
            smart_str(u"DATE"),
        ])
        cleandata = data.split(",")
        j=cleandata.index("date")+1
        for i in range(0,cleandata.index("date")):
            writer.writerow([
                smart_str(cleandata[i]),
                smart_str(cleandata[j]),
            ])
            j+=1
        return response

def help_view(request):
    buildings = b.getBuildingStrings()
    return render(request, 'edashboard/help.html',{'buildlist': buildings,'buildlistname':bname,
    'buildlistnum':bnum})

def construction_view(request):
    buildings = b.getBuildingStrings()
    return render(request, 'edashboard/construction.html',{'buildlist': buildings,'buildlistname':bname,
    'buildlistnum':bnum})

def login_view(request):
    buildings = b.getBuildingStrings()
    return render(request, 'edashboard/login.html',{'buildlist': buildings,'buildlistname':bname,
    'buildlistnum':bnum})

def demo(request):
    buildings = b.getBuildingStrings()
    return render(request, 'edashboard/forms_demo.html',{'buildlist': buildings,'buildlistname':bname,
    'buildlistnum':bnum})

def admin_view(request):
    buildings = b.getBuildingStrings()
    return render(request, 'edashboard/admin.html',{'buildlist': buildings,'buildlistname':bname,
    'buildlistnum':bnum})
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
