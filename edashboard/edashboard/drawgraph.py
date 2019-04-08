from edashboard.models import *
from edashboard.Backend import StaticDataRetriever

sdr = StaticDataRetriever()

def elec_list():
    eleclist = []
    listslog = []

    for data in Sensor.objects.filter(s_type="Current Demand KW"):
        listslog.append(data.s_log)

    for data in listslog:
        eleclist.append(Sensor.objects.get(s_log=data))

    return eleclist

def steam_list():
    steamlist = []
    listslog = []

    for data in Sensor.objects.filter(s_type="Steam KBTU"):
        listslog.append(data.s_log)

    for data in listslog:
        steamlist.append(Sensor.objects.get(s_log=data))

    return steamlist

def dom_list():
    domlist = []
    listslog = []

    for data in Sensor.objects.filter(s_type="Dom Water Gallons"):
        listslog.append(data.s_log)

    for data in listslog:
        domlist.append(Sensor.objects.get(s_log=data))

    return domlist

def reclaimed_list():
    reclaimedlist = []
    listslog = []

    for data in Sensor.objects.filter(s_type="Reclaimed Water Gallons"):
        listslog.append(data.s_log)

    for data in listslog:
        reclaimedlist.append(Sensor.objects.get(s_log=data))

    return reclaimedlist

def usage(list):
    usage = []
    log_dict = []

    for data in list:
        log_dict.append(sdr.get_log(data.s_log))

    for i in range (0,len(log_dict)):
        count = 0;
        for key in reversed(sorted(log_dict[i].keys())):
            if count == 1:
                count = 0
                break;
            usage.append(log_dict[i][key][1])
            count += 1
        i += 1

    return usage
