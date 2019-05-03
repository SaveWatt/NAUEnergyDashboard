from edashboard.models import *
from edashboard.backend import StaticDataRetriever

sdr = StaticDataRetriever()

def elec_list():
    eleclist = []
    listslog = []

    for data in Sensor.objects.filter(s_type="Elec Demand Kw"):
        listslog.append(data.s_log)
    for data in Sensor.objects.filter(s_type="Electric Demand"):
        listslog.append(data.s_log)

    for data in listslog:
        eleclist.append(Sensor.objects.get(s_log=data))

    return eleclist

def steam_list():
    steamlist = []
    listslog = []

    for data in Sensor.objects.filter(s_type="Steam Usage"):
        listslog.append(data.s_log)
    for data in Sensor.objects.filter(s_type="Steam Usage Btu"):
        listslog.append(data.s_log)

    for data in listslog:
        steamlist.append(Sensor.objects.get(s_log=data))
    return steamlist

def chilled_list():
    chilledlist = []
    listslog = []

    for data in Sensor.objects.filter(s_type="Chilled Water"):
        listslog.append(data.s_log)
    for data in Sensor.objects.filter(s_type="Chilled Water Btu"):
        listslog.append(data.s_log)

    for data in listslog:
        chilledlist.append(Sensor.objects.get(s_log=data))

    return chilledlist

def dom_list():
    domlist = []
    listslog = []

    for data in Sensor.objects.filter(s_type="Dom Water"):
        listslog.append(data.s_log)
    for data in Sensor.objects.filter(s_type="Dom Water Usage"):
        listslog.append(data.s_log)
    for data in Sensor.objects.filter(s_type="Domestic Water Usage"):
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

def gas_list():
    gaslist = []
    listslog = []

    for data in Sensor.objects.filter(s_type="Gas Usage"):
        listslog.append(data.s_log)
    for data in Sensor.objects.filter(s_type="Nat Gas Usage"):
        listslog.append(data.s_log)

    for data in listslog:
        gaslist.append(Sensor.objects.get(s_log=data))

    return gaslist

def usage(list):
    temp = []
    usage = []
    log_dict = []

    for data in list:
        log_dict.append(sdr.get_change(data.s_log))

    for i in range (0,len(list)):
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
        calc = abs(temp[(i*2)] - temp[(i*2)+1])
        usage.append(calc)

    return usage

    # for i in range (0,len(list)):
    #     try:
    #         for key in reversed(sorted(log_dict[i].keys())):
    #             usage.append(log_dict[i][key][1])
    #     except:
    #         usage = 0
    #
    # return usage

def sum(data):
    sum = 0
    for i in range (0,len(data)):
        sum += data[i]

    return round(sum,4)

def avg(data):
    avg = sum(data)
    try:
        average = round(avg / len(data), 4)
    except:
        average = 0
    return average
