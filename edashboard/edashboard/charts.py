from edashboard.models import *
from edashboard.backend import StaticDataRetriever

sdr = StaticDataRetriever()

def elec_list():
    eleclist = []
    listslog = []

    for data in Sensor.objects.filter(s_type="Electrical Usage"):
        listslog.append(data.s_log)
    print(listslog)

    for data in listslog:
        eleclist.append(Sensor.objects.get(s_log=data))

    return listslog

def steam_list():
    steamlist = []
    listslog = []

    for data in Sensor.objects.filter(s_type="Steam KBTU"):
        listslog.append(data.s_log)

    for data in listslog:
        steamlist.append(Sensor.objects.get(s_log=data))

    return steamlist

def chilled_list():
    chilledlist = []
    listslog = []

    for data in Sensor.objects.filter(s_type="Chilled Water"):
        listslog.append(data.s_log)

    for data in listslog:
        chilledlist.append(Sensor.objects.get(s_log=data))

    return chilledlist

def dom_list():
    domlist = []
    listslog = []

    for data in Sensor.objects.filter(s_type="Dom Water Gallons"):
        listslog.append(data.s_log)
    for data in Sensor.objects.filter(s_type="Domestic Water"):
        listslog.append(data.s_log)

    for data in listslog:
        domlist.append(Sensor.objects.get(s_log=data))

    return domlist

def reclaimed_list():
    reclaimedlist = []
    listslog = []

    for data in Sensor.objects.filter(s_type="Reclaimed Water"):
        listslog.append(data.s_log)

    for data in listslog:
        reclaimedlist.append(Sensor.objects.get(s_log=data))

    return reclaimedlist

def usage(list):
    temp = []
    usage = []
    log_dict = []

    for data in list:
        log_dict.append(sdr.get_log(data.s_log))

    for i in range (0,len(log_dict)):
        count = 0;
        try:
            for key in reversed(sorted(log_dict[i].keys())):
                if count == 2:
                    count = 0
                    break;
                temp.append(log_dict[i][key][1])
                count += 1
            i += 1
        except:
            usage = 0

    for i in range (0,len(log_dict)):
        calc = temp[(i*2)] - temp[(i*2)+1]
        usage.append(calc)

    return usage

def sum(data):
    sum = 0
    for i in range (0,len(data)):
        sum += data[i]

    return round(sum,4)

def avg(data):
    avg = sum(data)
    average = round(avg / len(data), 4)

    return average
