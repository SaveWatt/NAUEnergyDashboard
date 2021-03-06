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
import edashboard.conversion as conv
from django.contrib.auth.models import User

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
    list_gas = gas_list()
    usage_elec = usage(list_elec)
    usage_steam = usage(list_steam)
    usage_dom = usage(list_dom)
    usage_reclaimed = usage(list_reclaimed)
    usage_chilled = usage(list_chilled)
    usage_gas = usage(list_gas)
    avg_elec = avg(usage_elec)
    avg_steam = avg(usage_steam)
    avg_dom = avg(usage_dom)
    avg_reclaimed = avg(usage_reclaimed)
    avg_chilled = avg(usage_chilled)
    avg_gas = avg(usage_gas)
    elecDollar = kwtodollar(avg_elec)
    steamDollar = btutodollar(avg_steam)
    domDollar = gallontodollar(avg_dom)
    reclaimedDollar = gallontodollar(avg_reclaimed)
    chilledDollar = gallontodollar(avg_chilled)
    gasDollar = gastodollar(avg_gas)
    overall = round(elecDollar + steamDollar + domDollar + reclaimedDollar + chilledDollar + gasDollar, 4)
    return render(request, 'edashboard/index.html',{'buildlist': buildings,'buildlistname':bname,'buildlistnum':bnum,
    'list_elec':list_elec,'list_steam':list_steam,'list_dom':list_dom,'list_reclaimed':list_reclaimed,'list_chilled':list_chilled,'list_gas':list_gas,
    'usage_elec':usage_elec,'usage_steam':usage_steam,'usage_chilled':usage_chilled,'usage_dom':usage_dom,'usage_reclaimed':usage_reclaimed,'usage_gas':usage_gas,
    'avg_elec':avg_elec,'avg_steam':avg_steam,'avg_chilled':avg_chilled,'avg_dom':avg_dom,'avg_reclaimed':avg_reclaimed,'avg_gas':avg_gas,
    'elecDollar':elecDollar,'steamDollar':steamDollar,'domDollar':domDollar,'reclaimedDollar':reclaimedDollar,'chilledDollar':chilledDollar,'gasDollar':gasDollar,
    'overall':overall})

def building_view(request, buildnum):

    buildings = BR.getBuildingStrings()
    inputs = []
    util = ""
    if 'incr' in buildnum:
        inputs = getBuildData(buildnum)
        buildnum = inputs[0]
    building = Building.objects.get(b_num=buildnum)
    b_name = building.b_name
    sensors = Sensor.objects.filter(building_id=building.id)
    sensor_strs = []
    util_strs = []
    for sens in sensors:
        sensor_strs.append(str(sens))
        if sens.s_sub_type != 'None':
            util_strs.append(str(sens.s_type))
    for t in util_strs:
        if 1 < util_strs.count(t):
            util_strs = [x for x in util_strs if x != t]
    if inputs != []:
        data = BR.getData(building, inputs[2], datetime.datetime(2018, 10, 1, 0, 0), datetime.datetime(2018, 10, 1, 23, 59), incr=int(inputs[1]))
        if data == 0:
            context = {'buildlist': buildings}
            url = 'edashboard/error.html'
            return render(request, url, context)
        util = inputs[2]
    else:
        #data = BR.getData(building, "Meter Current Demand kwh", datetime.datetime.now()-datetime.timedelta(hours=24), datetime.datetime.now())
        data = BR.getData(building, util_strs[0], datetime.datetime(2018, 10, 1, 0, 0), datetime.datetime(2018, 10, 1, 23, 59), incr=60)
        util = util_strs[0]
    raw_usages = data[1]
    usage = conv.consumption(data[1])
    for i in usage:
        if i < 0:
            usage = raw_usages
            break
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
                                                        'util': util,
                                                        'carbon': carbon,
                                                        'utilities': util_strs,
                                                        'imagePath': imagePath,
                                                        'sensors': sensor_strs,
                                                        'buildlistname':bname,
                                                        'buildlistnum':bnum,
                                                        })

def commonutils_view(request,utildata=None):
    buildings = BR.getBuildingStrings()
    autofill = utildata.split(",")
    builds = utildata.split(",")
    buildnums = []
    for i in builds:
        buildnums.append(getBuildInfo(i)[1])
    utils = BR.getCommonUtilites(buildnums)
    autofill.append("util")
    return render(request, 'edashboard/compare.html',{'buildlist': buildings,'buildlistname':bname,
    'buildlistnum':bnum,'autofill':autofill,'utils':utils})

def compare_view(request,builddata=None):
    try:
        buildings = BR.getBuildingStrings()
        flag = ""
        permisflag = ""
        buildnames=[]
        sensor = ""
        util = ""
        data = ""
        starttime = ""
        endtime = ""
        c_utils=""
        searchtime = builddata.split('time=')
        searchtime = searchtime[1].split("util=")
        searchtime = str(searchtime[0])
        builds = []
        senses = []
        datas = []
        sensornums =[]
        autofill=[]
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
            buildnums = data[0]
            util = data[1]
            starttime = getTimes(data[2])
            endtime = getTimes(data[3])
            for i in range(0, len(buildnums)):
                building = Building.objects.get(b_num=buildnums[i])
                temp_data = BR.getUtilityData(building, util, starttime, endtime)
                if  temp_data == 0:
                    context = {'buildlist': buildings}
                    url = 'edashboard/error.html'
                    return render(request, url, context)
                datas.append(temp_data)
                #buildnums[i]=building.b_name
            c_utils = BR.getCommonUtilites(buildnums)
            autofill = buildnums
            #Loads the final data
            usages = []
            dates=[]
            content = []
            bgcolor = ["#ffcc01","#1f61a8","#8c8b86","#10603a"]
            bordercol = ["rgba(255,204,1,.3)","rgba(31,97,168,.3)","rgb(140, 139, 134,.3)"
            ,"rgb(16, 96, 58,.3)"]
            for i in datas:
                dates.append(i[0])
                usages.append(i[1])
                if flag == "util":
                    buildnames.append(i[2])
                else:
                    buildnames.append(i[3])
            c_usages = []
            for i in datas:
                c_usages.append(conv.consumption(i[1]))
            raw_usages = usages
            for i in range(0,len(buildnames)):
                raw_usages[i] = [raw_usages[i],buildnames[i]]
            usages = c_usages
            for i in range(len(usages)):
                for j in usages[i]:
                    if j < 0:
                        usages[i] = raw_usages[i]
                        break
            if flag =="util":
                for i in range(0,len(usages)):
                    if '/' in buildnames[i].b_name:
                        buildnames[i] = buildnames[i].b_name.replace('/', 's per ')
                    content.append([usages[i],buildnames[i],bgcolor[i],bordercol[i]])
            else:
                for i in range(0,len(usages)):
                    if '/' in buildnames[i]:
                        buildnames[i] = buildnames[i].replace('/', 's per ')
                    content.append([usages[i],buildnames[i],bgcolor[i],bordercol[i]])
            for i in range(0,len(dates[0])):
                t = (dates[0])[i]
                (dates[0])[i] = t.strftime('%m:%d:%Y %H:%M')

            clean_autofill = []
            for i in range(0, len(autofill)):
                if autofill[i] != "None":
                    building = Building.objects.get(b_num=autofill[i])
                    clean_autofill.append(building.b_name + " (" + autofill[i] + ")")
            autofill = clean_autofill
            autofill.append('util')
            url = 'edashboard/compare.html'
            context = {'raw_usages':raw_usages,'buildlist': buildings,
            'buildlistname':bname,'sensor':sensor,'buildlistnum':bnum,
            'builddata':builddata,'date':dates[0], 'utilname':util,
            'build_names':buildnames,'flag':flag,'content': content,
            'searchtime':str(searchtime),'utils':c_utils,'autofill':autofill}
            return render(request, url, context)

        elif flag == "sens":
            if(request.user.is_authenticated):
                username = request.user.id
                user = UserProfile.objects.get(user=username)
                if(user.permission is 3):
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
                    data = splitSensUrls(builddata, senses)
                    sensornums = data[0]
                    starttime = getTimes(data[1])
                    endtime = getTimes(data[2])
                    for i in range(0, len(sensornums)):
                        datas.append(BR.getSensorData(sensornums[i], starttime, endtime))
                    autofill = sensornums
                    autofill.append('sens')
                    c_utils = []
                    #Loads the final data
                    usages = []
                    dates=[]
                    content = []
                    bgcolor = ["#ffcc01","#1f61a8","#8c8b86","#10603a"]
                    bordercol = ["rgba(255,204,1,.3)","rgba(31,97,168,.3)","rgb(140, 139, 134,.3)"
                    ,"rgb(16, 96, 58,.3)"]
                    for i in datas:
                        dates.append(i[0])
                        usages.append(i[1])
                        if flag == "util":
                            buildnames.append(i[2])
                        else:
                            buildnames.append(i[3])
                    c_usages = []
                    for i in datas:
                        c_usages.append(conv.consumption(i[1]))
                    raw_usages = usages
                    usages = c_usages
                    for i in usages:
                        if i < 0:
                            usages = raw_usages
                            break
                    if flag =="util":
                        for i in range(0,len(usages)):
                            if '/' in buildnames[i].b_name:
                                buildnames[i] = buildnames[i].b_name.replace('/', 's per ')
                            content.append([usages[i],buildnames[i],bgcolor[i],bordercol[i]])
                    else:
                        for i in range(0,len(usages)):
                            if '/' in buildnames[i]:
                                buildnames[i] = buildnames[i].replace('/', 's per ')
                            content.append([usages[i],buildnames[i],bgcolor[i],bordercol[i]])
                    for i in range(0,len(dates[0])):
                        t = (dates[0])[i]
                        (dates[0])[i] = t.strftime('%m:%d:%Y %H:%M')
                    for i in range(0, len(autofill)):
                        if autofill[i] == "None":
                            autofill.remove(autofill[i])
                    url = 'edashboard/compare.html'
                    context = {'buildlist': buildings,
                    'buildlistname':bname,'sensor':sensor,'buildlistnum':bnum,
                    'builddata':builddata,'date':dates[0], 'utilname':util,
                    'build_names':buildnames,'flag':flag,'content': content, 'searchtime':str(searchtime),'utils':c_utils,'autofill':autofill}
                    return render(request, url, context)
            else:
                context = {'buildlist': buildings}
                url = 'edashboard/error.html'
                return render(request, url, context)
        else:
            context = {'buildlist': buildings}
            url = 'edashboard/error.html'
            return render(request, url, context)
    except:
        context = {'buildlist': buildings}
        url = 'edashboard/error.html'
        return render(request, url, context)


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
        if data == 0:
            context = {'buildlist': buildings}
            url = 'edashboard/error.html'
            return render(request, url, context)

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
    searchtime = starttime + ' - ' + endtime
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
    autofill = None
    return render(request, 'edashboard/compare.html',{'buildlist': buildings,'buildlistname':bname,
    'buildlistnum':bnum,'autofill':autofill})

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
            smart_str("DATE\n"),
            smart_str(cleandata[1][0]),
            ])
        elif len(cleandata[1]) == 2:
            writer.writerow([
            smart_str("DATE\n"),
            smart_str(cleandata[1][0]),
            smart_str(cleandata[1][1]),
            ])
        elif len(cleandata[1]) == 3:
            writer.writerow([
            smart_str("DATE\n"),
            smart_str(cleandata[1][0]),
            smart_str(cleandata[1][1]),
            smart_str(cleandata[1][2]),
            ])
        elif len(cleandata[1]) == 4:
            writer.writerow([
            smart_str("DATE\n"),
            smart_str(cleandata[1][0]),
            smart_str(cleandata[1][1]),
            smart_str(cleandata[1][2]),
            smart_str(cleandata[1][3]),
            ])
        #Writes our data
        for i in range(0,len(cleandata[2][0])):
                if len(cleandata[1]) == 1:
                    writer.writerow([
                            smart_str(cleandata[0][i]),
                            smart_str(cleandata[2][0][i]),
                    ])
                elif len(cleandata[1]) == 2:
                    writer.writerow([
                            smart_str(cleandata[0][i]),
                            smart_str(cleandata[2][0][i]),
                            smart_str(cleandata[2][1][i]),
                    ])
                elif len(cleandata[1]) == 3:
                    writer.writerow([
                            smart_str(cleandata[0][i]),
                            smart_str(cleandata[2][0][i]),
                            smart_str(cleandata[2][1][i]),
                            smart_str(cleandata[2][2][i]),
                    ])
                elif len(cleandata[1]) == 4:
                    writer.writerow([
                            smart_str(cleandata[0][i]),
                            smart_str(cleandata[2][0][i]),
                            smart_str(cleandata[2][1][i]),
                            smart_str(cleandata[2][2][i]),
                            smart_str(cleandata[2][3][i]),
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
