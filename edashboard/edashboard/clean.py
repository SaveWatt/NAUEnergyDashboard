import datetime
from decimal import Decimal
#Converts the given time to SQL Datetime
def getTimes(times):
    #Convert to month number
    months = {"January":"01","February":"02","March":"03","April":"04","May":"05",
    "June":"06","July":"07","August":"08","September":"09","October":"10","November":"11", "December": "12"}
    splittime = times.split(" ")
    month = splittime[0]
    day = ((splittime[1]).split(","))[0]
    hour=0
    mins=0
    #Adds leading 0
    if(int(day)<10):
      day = "0"+day
    year = splittime[2]
    time = splittime[3]
    if(splittime[4] == "am" and int((time.split(":"))[0])<10):
      time="0" + time.split(":")[0]+":"+time.split(":")[1]+":00"
    #Convert to military time
    if(splittime[4] == "pm" and int(time.split(":",1)[0]) != 12):
      mins = time.split(":")[1]
      hour = (int(time.split(":",1)[0]))
      hour +=12
      time = str(hour) + mins + ":00"
      #datetime.datetime(2018, 10, 1, 0, 0)
    return datetime.datetime(int(year), int(months[month]), int(day), int(hour), int(mins))

def getBuildData(builddata):
    util = builddata.split('util=')
    incr = util[0].split('incr=')
    buildnum=incr[0]
    incr = incr[1]
    content=[buildnum,incr,util[1]]
    return content

def getDownData(data):
    usages = [[],[],[],[]]
    labels = []
    date = []
    content=[]
    flag = 'usage'
    flag2 = 'stay'
    iteration = -1
    for i in data:
        #Changes iteration's Flag
        if flag2 == 'change':
            iteration +=1
            flag2 = 'stay'
        #Changes our util flag
        if i == 'usage':
            flag = 'usage'
            flag2 = 'change'
            continue
        elif i == 'label':
            flag = 'label'
            continue
        elif i == 'date':
            flag = 'date'
            continue

        if flag == 'date':
            i=i.replace("[","")
            i=i.replace("]","")
            i=i.replace("'", "")
            i=i.strip()
            date.append(i)

        elif flag == 'label':
            labels.append(i)
        #its usage data
        else:
            i=float(i)
            usages[iteration].append(i)

    content=[date,labels,usages]
    return content

def getBuildInfo(str):
    starr = str.split(" ")
    bnum = starr[len(starr)-1]
    bnum = bnum.replace("(","")
    bnum = bnum.replace(")","")
    bname = ""
    for i in range(0,len(starr)-1):
        bname += starr[i]
    return [bname,bnum]

def splitSensUrls(builddata,senses):
    cleandata = []
    months = ["January","February","March","April","May",
    "June","July","August","September","October","November", "December"]
    sens = builddata.split("time=")
    times = sens[1]
    splitimes = times.split(" - ")
    start = splitimes[0]
    end = splitimes[1]
    fsense=[]
    for i in range(0,len(senses)):
        if(senses[len(senses)-1-i]=="None"):
            continue
        else:
            fsense.append(((sens[0]).split(senses[len(senses)-1-i]))[1].strip())
            sens[0] = ((sens[0]).split(senses[len(senses)-1-i]))[0]
    #Adds sensor
    cleandata.append(fsense)
    #Adds start time
    cleandata.append(start)
    #Adds end time
    cleandata.append(end)
    return cleandata

def splitUtilUrls(builddata, buildss):
    cleandata = []
    months = ["January","February","March","April","May",
    "June","July","August","September","October","November", "December"]
    builds = builddata.split("time=")
    times=""
    timeutil = builds[1].split("util=")
    times = timeutil[0]
    util = timeutil[1]
    splitimes = times.split(" - ")
    start = splitimes[0]
    end = splitimes[1]
    fbuilds = []
    for i in range(0,len(buildss)):
        if(buildss[len(buildss)-1-i] == "None"):
            continue
        else:
            fbuilds.append(((builds[0]).split(buildss[len(buildss)-1-i]))[1].strip())
            builds[0] = ((builds[0]).split(buildss[len(buildss)-1-i]))[0].strip()
    #Adds building numbers
    cleandata.append(fbuilds)
    #Adds Utility
    cleandata.append(util)
    #Adds start time
    cleandata.append(start)
    #Adds end time
    cleandata.append(end)
    return cleandata
