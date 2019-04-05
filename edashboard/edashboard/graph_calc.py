from edashboard.models import *
from edashboard.StaticDataRetriever import StaticDataRetriever

def elec_list():
    sdr = StaticDataRetriever()
    eleclist = []
    listslog = []

    for data in Sensor.objects.filter(s_type="Current Demand KW"):
        listslog.append(data.s_log)

    for data in listslog:
        eleclist.append(Sensor.objects.get(s_log=data))

    return eleclist

def elec_pie():
    sdr = StaticDataRetriever()
    eleclist = elec_list()
    usage_elec = []
    log_dict = []
    list = 0

    for data in eleclist:
        log_dict.append(sdr.get_log(data.s_log))
        list += 1

    for i in range (0,list):
        count = 0;
        for key in reversed(sorted(log_dict[i].keys())):
            if count == 1:
                count = 0
                break;
            usage_elec.append(log_dict[i][key][1])
            count += 1
        i += 1

    return usage_elec

# def heat_list():
#     sdr = StaticDataRetriever()
#     listslog = []
#
#     for data in Sensor.objects.filter(s_type="HHW"):
#         listslog.append(data.s_log)
#
#     return listslog
#
# def heat_pie():
#     sdr = StaticDataRetriever()
#     listslog = heat_list()
#     usage_heat = []
#     heatlist = []
#     log_dict = []
#     list = 0
#
#     for data in listslog:
#         heatlist.append(Sensor.objects.get(s_log=data))
#
#     for data in heatlist:
#         log_dict.append(sdr.get_log(data.s_log))
#         list += 1
#
#     for i in range (0,list):
#         count = 0;
#         for key in reversed(sorted(log_dict[i].keys())):
#             if count == 1:
#                 count = 0
#                 break;
#             usage_heat.append(log_dict[i][key][1])
#             count += 1
#         i += 1
#
#     return usage_heat

# def cool_list():
#     sdr = StaticDataRetriever()
#     listslog = []
#
#     for data in Sensor.objects.filter(s_type="CHW"):
#         listslog.append(data.s_log)
#
#     return listslog
#
# def heat_pie():
#     sdr = StaticDataRetriever()
#     listslog = cool_list()
#     usage_cool = []
#     coollist = []
#     log_dict = []
#     list = 0
#
#     for data in listslog:
#         coollist.append(Sensor.objects.get(s_log=data))
#
#     for data in coollist:
#         log_dict.append(sdr.get_log(data.s_log))
#         list += 1
#
#     for i in range (0,list):
#         count = 0;
#         for key in reversed(sorted(log_dict[i].keys())):
#             if count == 1:
#                 count = 0
#                 break;
#             usage_cool.append(log_dict[i][key][1])
#             count += 1
#         i += 1
#
#     return usage_cool

def dom_list():
    sdr = StaticDataRetriever()
    listslog = []
    domlist = []

    for data in Sensor.objects.filter(s_type="Dom Water Gallons"):
        listslog.append(data.s_log)

    for data in listslog:
        domlist.append(Sensor.objects.get(s_log=data))

    return domlist

def dom_pie():
    sdr = StaticDataRetriever()
    domlist = dom_list()
    usage_dom = []
    log_dict = []
    list = 0


    for data in domlist:
        log_dict.append(sdr.get_log(data.s_log))
        list += 1

    for i in range (0,list):
        count = 0;
        for key in reversed(sorted(log_dict[i].keys())):
            if count == 1:
                count = 0
                break;
            usage_dom.append(log_dict[i][key][1])
            count += 1
        i += 1

    return usage_dom

def reclaimed_list():
    sdr = StaticDataRetriever()
    listslog = []
    reclaimedlist =[]

    for data in Sensor.objects.filter(s_type="Reclaimed Water Gallons"):
        listslog.append(data.s_log)

    for data in listslog:
        reclaimedlist.append(Sensor.objects.get(s_log=data))

    return reclaimedlist

def reclaimed_pie():
    sdr = StaticDataRetriever()
    reclaimedlist = reclaimed_list()
    usage_reclaimed = []
    log_dict = []
    list = 0

    for data in reclaimedlist:
        log_dict.append(sdr.get_log(data.s_log))
        list += 1

    for i in range (0,list):
        count = 0;
        for key in reversed(sorted(log_dict[i].keys())):
            if count == 1:
                count = 0
                break;
            usage_reclaimed.append(log_dict[i][key][1])
            count += 1
        i += 1

    return usage_reclaimed

def steam_list():
    sdr = StaticDataRetriever()
    listslog = []
    steamlist = []
    for data in Sensor.objects.filter(s_type="Steam KBTU"):
        listslog.append(data.s_log)

    for data in listslog:
        steamlist.append(Sensor.objects.get(s_log=data))

    return steamlist

def steam_pie():
    sdr = StaticDataRetriever()
    steamlist = steam_list()
    usage_steam = []
    log_dict = []
    list = 0

    for data in steamlist:
        log_dict.append(sdr.get_log(data.s_log))
        list += 1

    for i in range (0,list):
        count = 0;
        for key in reversed(sorted(log_dict[i].keys())):
            if count == 1:
                count = 0
                break;
            usage_steam.append(log_dict[i][key][1])
            count += 1
        i += 1

    return usage_steam

def sum_usage(usage):
    sum = 0
    for data in usage:
        sum += data
    return sum
