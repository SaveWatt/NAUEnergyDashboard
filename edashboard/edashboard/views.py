from django.http import HttpResponse
from django.shortcuts import render, redirect
import csv
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.template import Template, Context
from django import template
from django.conf import settings
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
    data = BR.getData(building, util_strs[0], datetime.datetime(2018, 10, 1, 0, 0), datetime.datetime(2018, 10, 1, 23, 59), incr=60)
    usage = data[1]
    date = data[0]
    imagePath = '/edashboard/images/buildingPic/' + buildnum + '.jpg'
    if usage:
        percent = sum(usage)/10000*100
        percent_str = ("%d%%" % round(percent, 2))
        mean = round(sum(usage)/len(usage), 2)
        median = round(stats.median(usage), 2)
        trees = round(sum(usage)*24*.0007/.06,2)
        carbon = round(sum(usage)*24,2)
        oil = round(sum(usage)*24*.0007//.43,2)
    else:
        percent = 0
        percent_str = 0
        mean = 0
        median = 0
        total = 0
        trees = 0
        carbon = 0
        oil = 0
    return render(request, 'edashboard/building.html', {'buildlist': buildings,
                                                        'bnum': buildnum,
                                                        'bname':b_name,
                                                        'usage':usage,
                                                        'date':date,
                                                        'percent':percent,
                                                        'percent_str':percent_str,
                                                        'mean': mean,
                                                        'median': median,
                                                        'trees': trees,
                                                        'oil': oil,
                                                        'carbon': carbon,
                                                        'utilities': util_strs,
                                                        'imagePath': imagePath,
                                                        'sensors': sensor_strs,
                                                        'buildlistname':bname,
                                                        'buildlistnum':bnum})

def compare_view(request,builddata=None):
    buildings = BR.getBuildingStrings()
    flag = ""
    permisflag = ""
    buildnames=[]
    sensor = ""
    util = ""
    data = ""
    starttime = ""
    endtime = ""
    builds = []
    senses = []
    datas = []
    sensornums =[]
    #Sets the utility
    if "util=" in str(builddata):
        flag = "util"
    else:
        flag = "sens"
    #Does operations according to utility
    if flag == "util":
        counter = 0;
        #Checks for the number of buildings we have passed
        if "build0=" in str(builddata):
            builds.append("build0=")
        else:
            builds.append("None")

        if "build1=" in str(builddata):
            builds.append("build1=")
        else:
            builds.append("None")

        if "build2=" in str(builddata):
            builds.append("build2=")
        else:
            builds.append("None")

        if "build3=" in str(builddata):
            builds.append("build3=")
        else:
            builds.append("None")
        data = splitUtilUrls(builddata,builds)
        print(data)
        #buildnums = data[0]
        buildnums = ['B88', 'B91']
        util = data[1]
        starttime = getTimes(data[2])
        endtime = getTimes(data[3])
        for i in range(0, len(buildnums)):
            print(buildnums[i])
            building = Building.objects.get(b_num=buildnums[i])
            datas.append(BR.getUtilityData(building, util, starttime, endtime))
        print("Common utils: %s" % str(BR.getCommonUtilites(buildnums)))

    if flag == "sens":
        #Checks for the number of buildings we have passed
        if "sens0=" in str(builddata):
            senses.append("sens0=")
        else:
            senses.append("None")

        if "sens1=" in str(builddata):
            senses.append("sens1=")
        else:
            senses.append("None")

        if "sens2=" in str(builddata):
            senses.append("sens2=")
        else:
            senses.append("None")

        if "sens3=" in str(builddata):
            senses.append("sens3=")
        else:
            senses.append("None")
        data = splitSensUrls(builddata,senses)
        sensornums = data[0]
        starttime = getTimes(data[1])
        endtime = getTimes(data[2])
        for i in range(0, len(sensornums)):
            datas.append(BR.getSensorData(sensornums[i], starttime, endtime))
    #Loads the final data
    usages = []
    dates=[]
    content = []
    bgcolor = ["#ffcc01","#1f61a8","#8c8b86","#10603a"]
    bordercol = ["rgba(255,204,1,.3)","rgba(31,97,168,.3)","rgb(140, 139, 134,.3)","rgb(16, 96, 58,.3)"]
    for i in datas:
        dates.append(i[0])
        usages.append(i[1])
        if flag == "util":
            buildnames.append(i[2])
        else:
            buildnames.append(i[3])
    for i in range(0,len(usages)):
        if '/' in buildnames[i]:
            buildnames[i] = buildnames[i].replace('/', 's per ')
        content.append([usages[i],buildnames[i],bgcolor[i],bordercol[i]])
    for i in range(0,len(dates[0])):
        t = (dates[0])[i]
        (dates[0])[i] = t.strftime('%m:%d:%Y %H:%M')
    return render(request, 'edashboard/compare.html',{'buildlist': buildings,'buildlistname':bname,'sensor':sensor,'buildlistnum':bnum,'builddata':builddata,'date':dates[0], 'utilname':util,'build_names':buildnames,'flag':flag,'content': content})

def export_view(request,builddata=None):
    buildings = BR.getBuildingStrings()
    flag = ""
    permisflag = ""
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
        if request.session.get('user.userprofile.permission') is 3:
            data = splitSensUrls(builddata)
            starttime = getTimes(data[1])
            endtime = getTimes(data[2])
            sensor = data[0]
            data = BR.getSensorData(sensor, starttime, endtime)
        else:
            data = splitSensUrls(builddata)
            starttime = getTimes(data[1])
            endtime = getTimes(data[2])
            sensor = "None"
            data = ("0","0","0","0")
            permisflag = "error"
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

def down_compare(request, data):
        type(data)
        buildings = BR.getBuildingStrings()
        cleandata = data.split(",")
        cleandata = getDownData(cleandata)
        filename = "attachment; filename=" + (cleandata[0][0].replace(":","-")).replace(" ","_") + " to "+ (cleandata[0][-1].replace(":","-")).replace(" ","_") + ".csv"
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = filename
        writer = csv.writer(response, csv)
        response.write(u'\ufeff'.encode('utf8'))
        #Writes our headers
        if len(cleandata[1]) == 1:
            writer.writerow([
            smart_str(cleandata[1][0]),
            smart_str("DATE\n"),
            ])
        elif len(cleandata[1]) == 2:
            writer.writerow([
            smart_str(cleandata[1][0]),
            smart_str(cleandata[1][1]),
            smart_str("DATE\n"),
            ])
        elif len(cleandata[1]) == 3:
            writer.writerow([
            smart_str(cleandata[1][0]),
            smart_str(cleandata[1][1]),
            smart_str(cleandata[1][2]),
            smart_str("DATE\n"),
            ])
        elif len(cleandata[1]) == 4:
            writer.writerow([
            smart_str(cleandata[1][0]),
            smart_str(cleandata[1][1]),
            smart_str(cleandata[1][2]),
            smart_str(cleandata[1][3]),
            smart_str("DATE\n"),
            ])
        #Writes our data
        for i in range(0,len(cleandata[2][0])):
                if len(cleandata[1]) == 1:
                    writer.writerow([
                            smart_str(cleandata[2][0][i]),
                            smart_str(cleandata[0][i]),
                    ])
                elif len(cleandata[1]) == 2:
                    writer.writerow([
                            smart_str(cleandata[2][0][i]),
                            smart_str(cleandata[2][1][i]),
                            smart_str(cleandata[0][i]),
                    ])
                elif len(cleandata[1]) == 3:
                    writer.writerow([
                            smart_str(cleandata[2][0][i]),
                            smart_str(cleandata[2][1][i]),
                            smart_str(cleandata[2][2][i]),
                            smart_str(cleandata[0][i]),
                    ])
                elif len(cleandata[1]) == 4:
                    writer.writerow([
                            smart_str(cleandata[2][0][i]),
                            smart_str(cleandata[2][1][i]),
                            smart_str(cleandata[2][2][i]),
                            smart_str(cleandata[2][3][i]),
                            smart_str(cleandata[0][i]),
                    ])
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
