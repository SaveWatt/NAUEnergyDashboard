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
        bnamelst = ['gamage','B1','blome','B2','1899','B3', 'adel','B26', 'allen hall','B46',
        'athropology','B29', 'aquatic center','B49', 'ardey audit','B37A',
        'ashurst','B11','beaver street school','B93','biology annex','B21B',
        'bookstore','B35','bury','B5','bus barn', 'B83',
        'calderon','B29','campus distribution cntr', 'B98D',
        'campus heights','B50', 'centenial','B91', 'cline','B28',
        'college of business','B81', 'college of engineering','B69',
        'communication','B16', 'conference center','B58', 'cowden','B38',
        'dubois','B64', 'dinning hall expansion','B30C', 'dlc','B16C',
        'eastburn','B27', 'fieldhouse','B30', 'forestry','B82',
        'gabaldon hall','B53', 'gateway','B43','geo annex','B13',
        'geology','B12', 'gillenwaters hall','B31', 'health professions','B66',
        'hilltop','B59', 'hlc','B25', 'honors hall','B41', 'hrm','B33',
        'ihd','B27A', 'isp','B50A', 'its','B54', 'liberal arts','B18',
        'mcconnell hall','B62', 'mcconnell suites','B75', 'mcdonald hall','B40',
        'mckay village','B50B', 'morton hall','B4', 'mountain view hall','B55',
        'nacc','B14', 'old main','B10', 'performing arts','B37',
        'physical science','B19', 'pine ridge village','B95', 'raymond hall','B39',
        'recital hall','B37', 'reilly hall','B48', 'res life warehouse','B98F',
        'riles','B15', 'rosebury','B13A', 'san fran parking garage','B96B',
        'SAS','B60', 'sbs east','B65', 'sbs west','B70', 'science & health','B36',
        'science lab','B17', 'sechrist hall','B42', 'skydome','B73',
        'skywiew','B87', 'south dinning','B64', 'south village apts','B71',
        'student services','B30B', 'studnt servs vav overw','B30A',
        'swing space','B98C', 'talor hall','B9', 'telcomm','B54A',
        'tinsley','B44', 'univ dinning','B30D', 'univ services','B90',
        'wettaw','B88', 'wilson','B45']

        #bnamelst1 = ['adel','B26', 'cline','B28', 'sas','B60',]

        cursor = self.__connection.cursor(as_dict=True)
        # Get list of trendlogs
        cursor.execute('SELECT * FROM tblTrendloglist')
        # Create a dictionary to store log information. Keys logdevnum_loginst
        log_dict = {}
        for row in cursor:
            for name in bnamelst:
                # Searching for any instance of building name in all logdesc
                if name.upper() in row['logdescription']:
                    # Creating key
                    logdevnum = str(row['logdevnum'])
                    loginst = str(row['loginst'])
                    key = logdevnum+"_"+loginst
                    # Storing bname, logdesc, objname, TrendlogID in log_dict
                    log_dict[key] = [name, row['logdescription'],
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

            print(str(lognum) + ": logid: " + key + " logstring: " + logstring)
            lognum +=1

            # Creating dynamic query for trendlog table
            query = ('SELECT * FROM %s' % logstring)
            # Querying for trendlog table
            cursor.execute(query, ())

            count = 0
            for row in cursor:
                if count > 3:
                    break
                print(row)
                count+=1
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
