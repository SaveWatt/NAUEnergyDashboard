'''
FILE MARKED FOR DELETION

import datetime
from django.db import models
from django.utils import timezone
from django import template
register = template.Library()

@register.building_name
def getBuildingsName():
    building = []
    filename="buildings.csv"
    with open(filename,'r') as f:
        lines= f.readlines()
        for line in lines:
            if "number,name" not in line:
                building.insert(len(building),line.rsplit(',', 1)[1])
    f.close()
    return building

@register.building_num
def getBuildingsNumber():
    building = []
    filename="buildings.csv"
    with open(filename,'r') as f:
        lines= f.readlines()
        for line in lines:
            if "number,name" not in line:
                building.insert(len(building),line.rsplit(',', 1)[0])
    f.close()
    return building


    FOR REFERENCE LATER
    #Pass in value and convert to kwH and convert based on string that conversion is.
    #CONVERSION LINK https://www.epa.gov/energy/greenhouse-gases-equivalencies-calculator-calculations-and-references
    def greenComp(value,conversion):

        kwh = value
        mtons = value*.0007
        kilog=value*0.707
        lbs=value*1.6
        #BARRELS OF OIL 5.80 mmbtu/barrel × 20.31 kg C/mmbtu × 44 kg CO2/12 kg C × 1 metric ton/1,000 kg
        if conversion=="oil":
            return mtons/.43
        #TREE'S GROWN FOR 10 YEARS
        elif conversion=="tree":
            return mtons/.06
        #CARBON OFFSET
        elif conversion=="carbon" :
            return value
        #Converts to Tons
        elif conversion=="tons" :
            return value*.0008
        # Converts to Gas
        elif conversion=="gas" :
            return mtons/(8.887*(10 ** (-3)))
        # CONVERTS BTU TO kWh
        elif conversion=="btu" :
            return kwh * 3412.14
        # Converts to DOLLARS
        else:
            return kwh * 11.1
    '''
