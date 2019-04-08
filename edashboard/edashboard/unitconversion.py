def kbtutobtu(data):
    btu = round((data * 1000), 4)
    return btu

def kwtobtu(data):
    btu = round((data / 0.00029307107), 4)
    return btu

def gallonstobtu(data):
    btu = round(((data/.7)*(8.887)), 4)
    return btu
