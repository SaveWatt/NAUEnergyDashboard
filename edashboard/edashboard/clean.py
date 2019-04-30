import datetime
#Converts the given time to SQL Datetime
def getTimes(times):
    #Convert to month number
    months = {"January":"01","February":"02","March":"03","April":"04","May":"05",
    "June":"06","July":"07","August":"08","September":"09","October":"10","November":"11", "December": "12"}
    splittime = times.split(" ")
    month = splittime[0]
    day = ((splittime[1]).split(",", 1))[0]
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
    i=0
    for i in range(0,len(months)-1):
        if(months[i] in start):
            monDay = start.split(",")
            num = monDay[0].split(months[i])
            start = "" + str(months[i]) + " " + str(num[1]) +","+ monDay[1]
    for i in range(0,len(senses)):
        if(senses[i]=="None"):
            continue
        else:
            fsense.append(sens[0].split(senses[len(sens)-1-i])[1].strip())
            sens[0] = sens[0].split(senses[len(sens)-1-i])[0]
    #Adds sensor
    cleandata.append(fsense)
    #Adds start time
    cleandata.append(start)
    #Adds end time
    cleandata.append(end)
    return cleandata

def splitUtilUrls(builddata, buildss):
    #print(builddata)
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
    i=0
    fbuilds = []
    fbuilds2=[]
    for i in range(0,len(months)-1):
        if(months[i] in start):
            monDay = start.split(",")
            num = monDay[0].split(months[i])
            start = "" + str(months[i]) + " " + str(num[1]) +","+ monDay[1]
    for i in range(0,len(buildss)):
        if(buildss[i]=="None"):
            continue
        else:
            fbuilds.append(builds[0].split(buildss[len(builds)-1-i])[1])
            builds[0] = builds[0].split(buildss[len(builds)-1-i])[0]
    #Adds building numbers
    cleandata.append(fbuilds)
    #Adds Utility
    cleandata.append(util)
    #Adds start time
    cleandata.append(start)
    #Adds end time
    cleandata.append(end)
    #print(cleandata)
    return cleandata
