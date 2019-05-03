
def kwtodollar(data):
    dollar = round((data * 0.12), 4)
    return dollar

def btutodollar(data):
    dollar = round((data * 0.00029307107 * 0.12),4)
    return dollar

def gallontodollar(data):
    dollar = round((data * 0.0015),4)
    return dollar

def consumption(values_list):
    if len(values_list) == 0:
        return []
    init = values_list[0]
    consumption = []
    for i in range(len(values_list)-1):
        consumption.append(values_list[i+1]-values_list[i])
    return consumption
