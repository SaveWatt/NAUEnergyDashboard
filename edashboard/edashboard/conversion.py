def kbtutobtu(data):
    btu = round((data * 1000), 4)
    return btu

def kwtobtu(data):
    btu = round((data / 0.00029307107), 4)
    return btu

def gallonstobtu(data):
    btu = round(((data/.7)*(8.887)), 4)
    return btu

def tonstobtu(data):
    btu = round((data/.0008), 4)
    return btu

def dollorstobtu(data):
    btu = round(((data/.00029307107)/0.12), 4)
    return btu
