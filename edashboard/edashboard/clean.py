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

def splitSensUrls(builddata):
    cleandata = []
    months = ["January","February","March","April","May",
    "June","July","August","September","October","November", "December"]
    build = builddata.split("time=")
    times=""
    timesens = build[1].split("sensor=")
    times = timesens[0]
    sensor = timesens[1]
    splitimes = times.split(" - ")
    start = splitimes[0]
    end = splitimes[1]
    i=0
    for i in range(0,len(months)-1):
        if(months[i] in start):
            monDay = start.split(",")
            num = monDay[0].split(months[i])
            start = "" + str(months[i]) + " " + str(num[1]) +","+ monDay[1]
    #Adds sensor
    cleandata.append(sensor)
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
    fbuilds=[]
    fbuilds2=[]
    print(buildss)
    for i in range(0,len(months)-1):
        if(months[i] in start):
            monDay = start.split(",")
            num = monDay[0].split(months[i])
            start = "" + str(months[i]) + " " + str(num[1]) +","+ monDay[1]
    print(builds[0])
    for i in range(0,len(buildss)):
        if(buildss[i]=="None"):
            continue
        else:
            print("Splitting")
            print(builds[0])
            print("Splitting on")
            print(buildss[len(builds)-1-i])
            print("split 0")
            print(builds[0].split(buildss[len(builds)-1-i])[0])
            print("split 1")
            print(builds[0].split(buildss[len(builds)-1-i])[1])
            builds[0] = builds[0].split(buildss[len(builds)-1-i])[0]
            fbuilds.append(builds[0].split(buildss[len(builds)-1-i])[1])
    print(fbuilds)
    print(builddata)
    print("----")
    print(buildss)
    for i in range(0,len(fbuilds)):
        if(buildss[len(buildss)-1-i] == "None"):
            continue
        else:
            print("1")
            print(builds[0])
            print("2")
            print(buildss[len(buildss)-i])
            builds[0] = builds[0].split(buildss[len(buildss)-1-i])
            print("3")
            print(builds[0])
            key = builds[0].split("build"+i+"=")
            fbuilds2.append(key)
            keyy = "build%d"%i
            fbuilds2.append(finalbuilds[i])
    print(fbuilds2)
    #print(fbuilds)
    #Adds building number
    #cleandata.append(build1)
    #cleandata.append(build2)
    #cleandata.append(build3)
    #cleandata.append(build4)
    #Adds Utility
    cleandata.append(util)
    #Adds start time
    cleandata.append(start)
    #Adds end time
    cleandata.append(end)
    #print(cleandata)
    return cleandata
