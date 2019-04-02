def kwtobtu(data):
    btu = round((data / 0.00029307107), 4)
    return btu

def btutokw(data):
    kw = round((data * 0.00029307107), 4)
    return kw

def kwtogallons(data):
    gallon = round((((data/.00029307107)*.0007)/(8.887*(Math.pow(10,-3)))), 4)
    return gallon

def gallonstokw(data):
    kw = round((((data*.00029307107)/.0007)*(8.887/(Math.pow(10,-3)))), 4)
    return kw

def kwtotons(data):
    ton = round(((data/.00029307107)*.0008), 4)
    return ton

def tonstokw(data):
    kw = round(((data*.00029307107)/.0008), 4)
    return kw

def kwtodollar(data):
    dollar = round((data*0.12), 4)
    return dollar

def dollartokw(data):
    kw = round((data/0.12), 4)
    return kw

def btutogallons(data):
    gallon = round(((data*.0007)/(8.887*(Math.pow(10,-3)))), 4)
    return gallon

def gallonstobtu(data):
    btu = round(((data/.0007)*(8.887/(Math.pow(10,-3)))), 4)
    return btu

def btutotons(data):
    ton = round((data*.0008), 4)
    return ton

def tonstobtu(data):
    btu = round((data/.0008), 4)
    return btu

def btutodollors(data):
    dollors = round((data*.00029307107*0.12), 4)
    return dollar

def dollorstobtu(data):
    btu = round((data/.00029307107/0.12), 4)
    return btu

def gallonstodollar(data):
    kw = gallontokw(data)
    dolloar = round(kwtodollar(kw), 4)
    return dollar

def dollartogallons(data):
    kw = dollartokw(data)
    gallon = round(kwtogallons(kw), 4)
    return gallon

def tonstodollar(data):
    kw = tonstokw(data)
    dollar = round(kwtodollar(kw), 4)
    return dollar

def dollartotons(data):
    kw = dollartokw(data)
    ton = round(kwtotons(kw), 4)
    return ton
