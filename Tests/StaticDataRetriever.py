import pandas as pd
from pathlib import Path

import pymssql as sql

class StaticDataRetriever:

    def __init__(self):
        self.__host = r'Sweetleaf.nau.froot.nau.edu\GPDEV'
        self.__user = r'NAU\idd6'
        self.__pass = "Itsuko23272147"
        self.__base = 'EnergyCap'
        self.__connection = sql.connect(host=self.__host, user=self.__user,
        password=self.__pass, database=self.__base)
        self.__table = None

    def print_rows(self):
        b_identifiers = {'B1': 'gammage',
                         'B2': 'blome',
                         'B3': 'north union',
                         'B4': 'morton hall',
                         'B8': 'bury',
                         'B9': 'taylor hall',
                         'B10': 'old main',
                         'B11': 'ashurst',
                         'B12': 'geology',
                         'B13': 'geology annex',
                         'B13A': 'rosebury appartments',
                         'B14': 'native american cultural center',
                         'B15': 'riles',
                         'B16': 'communication',
                         'B16A': 'distance learning center',
                         'B17': 'nau lab',
                         'B18': 'liberal arts',
                         'B19': 'physical sciences',
                         'B21B': 'biology annex',
                         'B25': 'hlc',
                         'B26': 'adel',
                         'B27': 'eastburn',
                         'B27A': 'ihd',
                         'B28': 'cline',
                         'B29': 'calderon',
                         'B30': 'fieldhouse',
                         'B30A': 'student services vav overview',
                         'B30B': 'student services',
                         'B30C': 'dining hall expansion',
                         'B30D': 'university dining',
                         'B31': 'gillenwater hall',
                         'B33': 'hrm',
                         'B35': 'bookstore',
                         'B36': 'shb',
                         'B37': 'performing arts',
                         'B37A': 'ardrey auditorium',
                         'B38': 'cowden hall',
                         'B39': 'raymond hall',
                         'B40': 'mcdonald hall',
                         'B41': 'honors hall',
                         'B42': 'sechrist hall',
                         'B43': 'gateway',
                         'B44': 'tinsley hall',
                         'B45': 'wilson hall',
                         'B46': 'allen hall',
                         'B48': 'reilly hall',
                         'B49': 'anthropology',
                         'B50': 'campus heights',
                         'B50A': 'isp',
                         'B50B': 'mckay village',
                         'B53': 'gabaldon hall',
                         'B54': 'its',
                         'B54A': 'telcomm',
                         'B55': 'mountain view hall',
                         'B58': 'conference center',
                         'B59': 'hilltop',
                         'B60': 'sas',
                         'B62': 'mcconnell hall',
                         'B64': 'dubois',
                         'B65': 'sbs east',
                         'B66': 'health professions',
                         'B69': 'engineering',
                         'B70': 'sbs west',
                         'B71': 'south village apartments',
                         'B73': 'skydome',
                         'B75': 'mcconnell suites',
                         'B81': 'business',
                         'B82': 'forestry',
                         'B83': 'bus barn',
                         'B86': 'aquatic center',
                         'B87': 'skyview',
                         'B88': 'wettaw',
                         'B90': 'nareh',
                         'B91': 'parking services',
                         'B93': 'beaver street school',
                         'B95': 'pine ridge village',
                         'B96B': 'san fran paraking garage',
                         'B98C': 'swing space',
                         'B98D': 'campus distribution center',
                         'B98F': 'res life warehouse'}

        #bnamelst1 = ['adel','B26 ', 'cline','B28 ', 'sas','B60 ']

        cursor = self.__connection.cursor(as_dict=True)
        # Get list of trendlogs
        cursor.execute('SELECT * FROM tblTrendloglist')
        # Create a dictionary to store log information. Keys logdevnum_loginst
        log_dict = {}
        for row in cursor:
            for num in b_identifiers.keys():
                desc = row['logdescription'].upper()
                # Searching for any instance of building name in all logdesc
                #if num+" " in desc or num in desc or num[1:] in desc:
                if 'B60 ' in desc or 'B60' in desc or 'SAS' in desc:
                    # Creating key
                    logdevnum = str(row['logdevnum'])
                    loginst = str(row['loginst'])
                    key = logdevnum+"_"+loginst
                    # Storing bname, logdesc, objname, TrendlogID in log_dict
                    log_dict[key] = ['B60', row['logdescription'],
                    row['objname'], row['TrendlogID']]

        # Querying for trendlogs based on log_dict info
        lognum = 1
        for key in sorted(log_dict.keys()):
            # Creating string which identifies trendlog
            logstring = 'tblTrendlog_'
            logid = key.split("_")
            for i in range(7-len(logid[0])):
                logstring += "0"
            logstring += logid[0]
            logstring += "_"
            for i in range(10 - len(logid[1])):
                logstring += "0"
            logstring += logid[1]

            print(str(lognum) + ": logid: " + key + " logstring: " + logstring +
            " building: " + log_dict[key][0])
            print("--- " + log_dict[key][1])
            lognum +=1

            # Creating dynamic query for trendlog table
            #query = ('SELECT * FROM %s' % logstring)
            # Querying for trendlog table
            #cursor.execute(query, ())

            #count = 0
            #for row in cursor:
            #    if count > 3:
            #        break
            #    print(row)
            #    count+=1

        #self.dict_printer(log_dict)

    def dict_printer(self, dict):
        count = 0
        for key in sorted(dict.keys()):
            count+=1
            print(str(count) + ": " + key + ": " + str(dict[key]))

    def log_printer(self):
        cursor = self.__connection.cursor()
        cursor.execute('SELECT * FROM ')
        self.__table = cursor.fetchall()
        print(self.__table)




sdr = StaticDataRetriever()
sdr.print_rows()
#sdr.store_table()
