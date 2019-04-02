from edashboard.models import *
from edashboard.StaticDataRetriever import StaticDataRetriever

def dom_pie():
    sdr = StaticDataRetriever()
    usage_dom= []
    domwater1= Sensor.objects.get(s_log="215_16")
    domwater2= Sensor.objects.get(s_log="215_19")
    domwater3= Sensor.objects.get(s_log="255_2")
    domwater4= Sensor.objects.get(s_log="433_42")
    domwater5= Sensor.objects.get(s_log="609_0")
    domwater6= Sensor.objects.get(s_log="621_2")
    domwater7= Sensor.objects.get(s_log="691_62")
    domwater8= Sensor.objects.get(s_log="691_63")

    log_dict1 = sdr.get_log(domwater1.s_log)
    log_dict2 = sdr.get_log(domwater2.s_log)
    log_dict3 = sdr.get_log(domwater3.s_log)
    log_dict4 = sdr.get_log(domwater4.s_log)
    log_dict5 = sdr.get_log(domwater5.s_log)
    log_dict6 = sdr.get_log(domwater6.s_log)
    log_dict7 = sdr.get_log(domwater7.s_log)
    log_dict8 = sdr.get_log(domwater8.s_log)

    count = 0

    for key in reversed(sorted(log_dict1.keys())):
        if count == 1:
            count = 0
            break;
        usage_dom.append(log_dict1[key][1])
        count += 1
    for key in reversed(sorted(log_dict2.keys())):
        if count == 1:
            count = 0
            break;
        usage_dom.append(log_dict2[key][1])
        count += 1
    for key in reversed(sorted(log_dict3.keys())):
        if count == 1:
            count = 0
            break;
        usage_dom.append(log_dict3[key][1])
        count += 1
    for key in reversed(sorted(log_dict4.keys())):
        if count == 1:
            count = 0
            break;
        usage_dom.append(log_dict4[key][1])
        count += 1
    for key in reversed(sorted(log_dict5.keys())):
        if count == 1:
            count = 0
            break;
        usage_dom.append(log_dict5[key][1])
        count += 1
    for key in reversed(sorted(log_dict6.keys())):
        if count == 1:
            count = 0
            break;
        usage_dom.append(log_dict6[key][1])
        count += 1
    for key in reversed(sorted(log_dict7.keys())):
        if count == 1:
            count = 0
            break;
        usage_dom.append(log_dict7[key][1])
        count += 1
    for key in reversed(sorted(log_dict8.keys())):
        if count == 1:
            count = 0
            break;
        usage_dom.append(log_dict8[key][1])
        count += 1

    return usage_dom

def elec_pie():
    sdr = StaticDataRetriever()
    usage_elec = []
    elec1 = Sensor.objects.get(s_log="601_5")
    log_dict1 = sdr.get_log(elec1.s_log)

    count = 0

    for key in reversed(sorted(log_dict1.keys())):
        if count == 1:
            count = 0
            break;
        usage_elec.append(log_dict1[key][1])
        count += 1
    return usage_elec

def reclaimed_pie():
    sdr = StaticDataRetriever()
    usage_reclaimed = []
    reclaimed1 = Sensor.objects.get(s_log="609_1")
    reclaimed2 = Sensor.objects.get(s_log="621_3")
    log_dict1 = sdr.get_log(reclaimed1.s_log)
    log_dict2 = sdr.get_log(reclaimed2.s_log)
    count = 0

    for key in reversed(sorted(log_dict1.keys())):
        if count == 1:
            count = 0
            break;
        usage_reclaimed.append(log_dict1[key][1])
        count += 1

    for key in reversed(sorted(log_dict1.keys())):
        if count == 1:
            count = 0
            break;
        usage_reclaimed.append(log_dict1[key][1])
        count += 1
    return usage_reclaimed

def heat_pie():
    sdr = StaticDataRetriever()
    usage_heat = []
    heat1 = Sensor.objects.get(s_log="609_1")
    heat2 = Sensor.objects.get(s_log="621_3")
    log_dict1 = sdr.get_log(heat1.s_log)
    log_dict2 = sdr.get_log(heat2.s_log)
    count = 0

    for key in reversed(sorted(log_dict1.keys())):
        if count == 1:
            count = 0
            break;
        usage_heat.append(log_dict1[key][1])
        count += 1

    for key in reversed(sorted(log_dict1.keys())):
        if count == 1:
            count = 0
            break;
        usage_heat.append(log_dict1[key][1])
        count += 1
    return usage_heat

def cool_pie():
    sdr = StaticDataRetriever()
    usage_cool = []
    cool1 = Sensor.objects.get(s_log="609_1")
    cool2 = Sensor.objects.get(s_log="621_3")
    log_dict1 = sdr.get_log(cool1.s_log)
    log_dict2 = sdr.get_log(cool2.s_log)
    count = 0

    for key in reversed(sorted(log_dict1.keys())):
        if count == 1:
            count = 0
            break;
        usage_cool.append(log_dict1[key][1])
        count += 1

    for key in reversed(sorted(log_dict1.keys())):
        if count == 1:
            count = 0
            break;
        usage_cool.append(log_dict1[key][1])
        count += 1
    return usage_cool

def steam_pie():
    sdr = StaticDataRetriever()
    usage_steam = []
    steam1 = Sensor.objects.get(s_log="609_1")
    steam2 = Sensor.objects.get(s_log="621_3")
    log_dict1 = sdr.get_log(steam1.s_log)
    log_dict2 = sdr.get_log(steam2.s_log)
    count = 0

    for key in reversed(sorted(log_dict1.keys())):
        if count == 1:
            count = 0
            break;
        usage_steam.append(log_dict1[key][1])
        count += 1

    for key in reversed(sorted(log_dict1.keys())):
        if count == 1:
            count = 0
            break;
        usage_steam.append(log_dict1[key][1])
        count += 1
    return usage_steam
# 일단 목록부터 불러오고
# 그리고 그 목록으로 값 뽑아내고
# 그리고 값 이용해서 추가하기?
def sum_usage(usage):
    sum = 0
    for data in usage:
        sum += data
    return sum
