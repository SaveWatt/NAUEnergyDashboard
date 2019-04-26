from django.http import HttpResponse
from django.shortcuts import render, redirect
import csv
from django.utils.encoding import smart_str
from edashboard.clean import *
from edashboard.models import *
from edashboard.charts import *
from edashboard.conversion import *
from edashboard.weather import *
from django.http import JsonResponse
from edashboard.forms import *
import statistics as stats
import datetime
from edashboard.backend import BackendRetriever
from edashboard.backend import StaticDataRetriever as SDR

sdr = SDR()
BR = BackendRetriever()
bname = BR.getBuildingStrings()
bnum = BR.getNumStrings()
bname.sort()



def index(request):
    buildings = BR.getBuildingStrings()
    list_elec = elec_list()
    list_steam = steam_list()
    list_dom = dom_list()
    list_reclaimed = reclaimed_list()
    list_chilled = chilled_list()
    usage_elec = usage(list_elec)
    usage_steam = usage(list_steam)
    usage_dom = usage(list_dom)
    usage_reclaimed = usage(list_reclaimed)
    usage_chilled = usage(list_chilled)
    avg_elec = avg(usage_elec)
    avg_steam = avg(usage_steam)
    avg_dom = avg(usage_dom)
    avg_reclaimed = avg(usage_reclaimed)
    avg_chilled = avg(usage_chilled)
    elecDollar = kwtodollar(avg_elec)
    steamDollar = btutodollar(avg_steam)
    domDollar = gallontodollar(avg_dom)
    reclaimedDollar = gallontodollar(avg_reclaimed)
    chilledDollar = gallontodollar(avg_chilled)
    overall = elecDollar + steamDollar + domDollar + reclaimedDollar + chilledDollar
    return render(request, 'edashboard/index.html',{'buildlist': buildings,'buildlistname':bname,
    'buildlistnum':bnum,'usage_elec':usage_elec,'usage_steam':usage_steam,'usage_chilled':usage_chilled,
    'usage_dom':usage_dom,'usage_reclaimed':usage_reclaimed,'avg_elec':avg_elec,'avg_steam':avg_steam,
    'avg_chilled':avg_chilled,'avg_dom':avg_dom,'avg_reclaimed':avg_reclaimed,'elecDollar':elecDollar,
    'steamDollar':steamDollar,'domDollar':domDollar,'reclaimedDollar':reclaimedDollar,'chilledDollar':chilledDollar,
    'overall':overall})

def building_view(request, buildnum):
    weather_day1 = day1()
    weather_day2 = day2()
    weather_day3 = day3()
    #TODO: Have the selector pass an increment and sensor type
    buildings = BR.getBuildingStrings()
    building = Building.objects.get(b_num=buildnum)
    b_name = building.b_name
    sensors = Sensor.objects.filter(building_id=building.id)
    sensor_strs = []
    util_strs = []
    for sens in sensors:
        sensor_strs.append(str(sens))
        if sens.s_type != 'None':
            util_strs.append(str(sens.s_type))
    #data = BR.getData(building, "Meter Current Demand kwh", datetime.datetime.now()-datetime.timedelta(hours=24), datetime.datetime.now())
    data = BR.getData(building, "Meter Current Demand KW", datetime.datetime(2018, 10, 1, 0, 0), datetime.datetime(2018, 10, 1, 23, 59), incr=60)
    usage = data[1]
    date = data[0]
    imagePath = '/edashboard/images/buildingPic/' + buildnum + '.jpg'
    if usage:
        percent = sum(usage)/10000*100
        percent_str = ("%d%%" % round(percent, 2))
        mean = round(sum(usage)/len(usage), 2)
        median = round(stats.median(usage), 2)
        minimum = min(usage)
        maximum = max(usage)
    else:
        percent = 0
        percent_str = 0
        mean = 0
        median = 0
        minimum = 0
        maximum = 0
    return render(request, 'edashboard/building.html', {'buildlist': buildings,
                                                        'bnum': buildnum,
                                                        'bname':b_name,
                                                        'usage':usage,
                                                        'date':date,
                                                        'percent':percent,
                                                        'percent_str':percent_str,
                                                        'mean': mean,
                                                        'median': median,
                                                        'minimum':minimum,
                                                        'maximum':maximum,
                                                        'utilities': util_strs,
                                                        'imagePath': imagePath,
                                                        'sensors': sensor_strs,
                                                        'buildlistname':bname,
                                                        'buildlistnum':bnum,
                                                        'weather_day1':weather_day1,
                                                        'weather_day2':weather_day2,
                                                        'weather_day3':weather_day3})

def compare_view(request):
    buildings = BR.getBuildingStrings()
    return render(request, 'edashboard/compare.html',{'buildlist': buildings,'buildlistname':bname,
    'buildlistnum':bnum,})

def export_view(request,builddata=None):
    buildings = BR.getBuildingStrings()
    flag = ""
    sensor = ""
    util = ""
    data = ""
    starttime = ""
    endtime = ""
    if "util=" in str(builddata):
        flag = "util"
    if "sensor=" in str(builddata):
        flag = "sens"
    if flag == "util":
        data = splitUtilUrls(builddata)
        buildnum = data[0]
        util = data[1]
        starttime = getTimes(data[2])
        endtime = getTimes(data[3])
        building = Building.objects.get(b_num=buildnum)
        data = BR.getUtilityData(building, util, starttime, endtime)
    if flag == "sens":
        data = splitSensUrls(builddata)
        starttime = getTimes(data[1])
        endtime = getTimes(data[2])
        sensor = data[0]
        data = BR.getSensorData(sensor, starttime, endtime)

    usage = data[1]
    date = data[0]
    build_name = data[2]
    utilname = data[3]
    for i in range(0,len(date)):
        t = date[i]
        date[i] = t.strftime('%m:%d:%Y %H:%M')
    return render(request, 'edashboard/export.html',{'buildlist': buildings,'buildlistname':bname,'sensor':sensor,
    'buildlistnum':bnum,'builddata':builddata,'usage':usage,'date':date, 'utilname':utilname,'build_name':build_name,'flag':flag})

def down_export(request,data):
    buildings = BR.getBuildingStrings()
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
    buildings = BR.getBuildingStrings()
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
        buildings = BR.getBuildingStrings()
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'edashboard/index.html',{'buildlist': buildings,'buildlistname':bname,
            'buildlistnum':bnum})
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
    buildings = BR.getBuildingStrings()
    return render(request, 'edashboard/compare.html',{'buildlist': buildings,'buildlistname':bname,
    'buildlistnum':bnum})

def compare_view(request,builddata=None):
    buildings = BR.getBuildingStrings()
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
        buildings = BR.getBuildingStrings()
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
    buildings = BR.getBuildingStrings()
    return render(request, 'edashboard/help.html',{'buildlist': buildings,'buildlistname':bname,
    'buildlistnum':bnum})

def construction_view(request):
    buildings = BR.getBuildingStrings()
    return render(request, 'edashboard/construction.html',{'buildlist': buildings,'buildlistname':bname,
    'buildlistnum':bnum})

def login_view(request):
    buildings = BR.getBuildingStrings()
    return render(request, 'edashboard/login.html',{'buildlist': buildings})

def admin_view(request):
    buildings = BR.getBuildingStrings()
    return render(request, 'edashboard/admin.html',{'buildlist': buildings})
