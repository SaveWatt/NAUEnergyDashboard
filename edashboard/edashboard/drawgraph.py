from edashboard.models import *
from edashboard.Backend import StaticDataRetriever

sdr = StaticDataRetriever()

def elec_list():
    eleclist = []
    listslog = []

    for data in Sensor.objects.filter(s_type="Meter Current Demand KW"):
        listslog.append(data.s_log)

    for data in listslog:
        eleclist.append(Sensor.objects.get(s_log=data))

    return eleclist

def steam_list():
    steamlist = []
    listslog = []

    for data in Sensor.objects.filter(s_type="Meter Steam KBTU"):
        listslog.append(data.s_log)

    for data in listslog:
        steamlist.append(Sensor.objects.get(s_log=data))

    return steamlist

def chilled_list():
    chilledlist = []
    listslog = []

    for data in Sensor.objects.filter(s_type="Meter Chilled Water"):
        listslog.append(data.s_log)

    for data in listslog:
        chilledlist.append(Sensor.objects.get(s_log=data))

    return chilledlist

def dom_list():
    domlist = []
    listslog = []

    for data in Sensor.objects.filter(s_type="Meter Dom Water Gallons"):
        listslog.append(data.s_log)

    for data in listslog:
        domlist.append(Sensor.objects.get(s_log=data))

    return domlist

def reclaimed_list():
    reclaimedlist = []
    listslog = []

    for data in Sensor.objects.filter(s_type="Meter Reclaimed Water Gallons"):
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

def avg(data):
    sum = 0
    for i in range (0,len(data)):
        sum += data[i]

    try:
        average = round(sum / len(data), 4)
    except:
        average = 0

    return average
