
#Converts the given time to SQL Datetime
def getTimes(times):
    #Convert to month number
    months = {"January":"01","February":"02","March":"03","April":"04","May":"05",
    "June":"06","July":"07","August":"08","September":"09","October":"10","November":"11", "December": "12"}
    splittime = times.split(" ")
    month = splittime[0]
    day = ((splittime[1]).split(",", 1))[0]
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
      colon = ":"
      mins = colon + mins
      time = str(hour) + mins + ":00"
    return year + "-" + months[month] + "-" + day + " " + time
