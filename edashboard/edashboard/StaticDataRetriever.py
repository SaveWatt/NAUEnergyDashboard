import pandas as pd
from pathlib import Path
from edashboard.models import Building, Sensor
import pymssql as sql

class StaticDataRetriever:

    def __init__(self):
        self.__host = r'Sweetleaf.nau.froot.nau.edu\GPDEV'
        self.__user = r'NAU\idd6'
        self.__pass = "Itsuko23272147"
        self.__base = 'EnergyCap'
        self.__b_identifiers = {'B1': ['Gammage','gamage'],
                         'B2': ['Blome', 'blome'],
                         'B3': ['1899 Bar and Grill', 'north union'],
                         'B4': ['Morton Hall', 'morton hall'],
                         'B8': ['Bury', 'bury'],
                         'B9': ['Taylor Hall', 'taylor'],
                         'B10': ['Old Main', 'old main'],
                         'B11': ['Ashurst', 'ashurst'],
                         'B12': ['Geology', 'geology'],
                         'B13': ['Geology Annex', 'geo annex'],
                         'B13A': ['Rosebury Apartments', 'rosebury'],
                         'B14': ['Native American Cultural Center', 'nacc'],
                         'B15': ['Riles', 'riles'],
                         'B16': ['Communication', 'communication'],
                         'B16A': ['University Marketing and Operations', 'dlc'],
                         'B17': ['Science Lab Facility', 'science lab'],
                         'B18': ['Liberal Arts', 'liberal arts'],
                         'B19': ['Physical Sciences', 'physcience'],
                         'B21B': ['Biological Sciences Annex', 'biology annex'],
                         'B25': ['Health and Learning Center', 'hlc'],
                         'B26': ['Adel Mathematics', 'adel'],
                         'B27': ['Eastburn Education Center', 'eastburn'],
                         'B27A': ['Institute for Human Development', 'ihd'],
                         'B28': ['Cline Library', 'cline'],
                         'B29': ['Ernest Calderon Learning Community', 'calderone'],
                         'B30': ['University Union Fieldhouse', 'fieldhouse'],
                         'B30A': ['University Union Dining Services', 'student services vav overview'],
                         'B30B': ['University Union Student Services','student services'],
                         'B30C': ['University Union Food Court', 'dining hall expansion'],
                         'B30D': ['University Union Dining Expansion', 'university dining'],
                         'B31': ['Gillenwater Hall', 'gillenwates hall'],
                         'B33': ['Hotel and Restaurant Management', 'hrm'],
                         'B35': ['NAU Bookstore', 'bookstore'],
                         'B36': ['Science and Health Building', 'shb'],
                         'B37': ['Performing and Fine Arts', 'performing arts'],
                         'B37A': ['Ardrey Auditorium', 'ardrey'],
                         'B38': ['Cowden Hall', 'cowden'],
                         'B39': ['Raymond Hall', 'raymond'],
                         'B40': ['McDonald Hall', 'mcdonald'],
                         'B41': ['Honors Living and Learning Community', 'honors'],
                         'B42': ['Sechrist Hall', 'sechrist'],
                         'B43': ['Gateway Student Success Center', 'gateway'],
                         'B44': ['Tinsley Hall', 'tinsley'],
                         'B45': ['Wilson Hall', 'wilson'],
                         'B46': ['Allen Hall', 'allen'],
                         'B48': ['Reilly Hall', 'reilly'],
                         'B49': ['Anthropology Laboratory', 'anthropology'],
                         'B50': ['Campus Heights Apartments', 'campus heights'],
                         'B50A': ['International Pavillion', 'isp'],
                         'B50B': ['McKay Village', 'mckay'],
                         'B53': ['Gabaldon Hall', 'gabaldon'],
                         'B54': ['Information Technology Services', 'its'],
                         'B54A': ['Information Technology Telecomm', 'telcomm'],
                         'B55': ['Moiuntain View Hall', 'mountain view'],
                         'B58': ['High Country Conference Center', 'conference'],
                         'B59': ['Hilltop Townhomes', 'hilltop'],
                         'B60': ['Student and Academic Services', 'sas'],
                         'B62': ['McConnell Hall', 'mcconnell'],
                         'B64': ['DuBois South Union', 'dubois'],
                         'B65': ['Social and Behavioral Sciences (Castro)', 'sbs east'],
                         'B66': ['Health Professions', 'health professions'],
                         'B69': ['Engineering and Technology', 'engineering'],
                         'B70': ['Social and Behavioral Sciences (West)', 'sbs west'],
                         'B71': ['South Village Apartments', 'south village'],
                         'B73': ['Walkup Skydome', 'skydome'],
                         'B75': ['The Suites', 'suites'],
                         'B81': ['Franke College of Business', 'business'],
                         'B82': ['South West Forestry Science Complex', 'forestry'],
                         'B83': ['KNAU/Mountain Campus Transit', 'bus barn'],
                         'B86': ['Aquatic and Tennis Complex', 'aquatic center'],
                         'B87': ['Skyview Apartments', 'skyview'],
                         'B88': ['Wettaw', 'wettaw'],
                         'B90': ['School of Infomatics, Computing and Cyber Systems', 'nareh'],
                         'B91': ['Centennial', 'parking services'],
                         'B93': ['South Beaver School', 'beaver'],
                         'B95': ['Pine Ridge Village', 'pine ridge village'],
                         'B96B': ['San Francisco Parking Garage', 'san fran paraking garage'],
                         'B98C': ['Engineering Research', 'swing space'],
                         'B98D': ['Extended Campus Operation Center', 'campus distribution center'],
                         'B98F': ['RLSS Warehouse', 'res life warehouse']}
        self.__connection = sql.connect(host=self.__host, user=self.__user,
        password=self.__pass, database=self.__base)
        self.__log_dict = {}

    def update_buildings(self):
        for key in self.__b_identifiers.keys():
            num_results = Building.objects.filter(b_num = key).count()
            if num_results < 1:
                b = Building(b_name=self.__b_identifiers[key][0], b_num=key, b_alias=self.__b_identifiers[key][1])
                b.save()

    def update_sensors(self):
        if not self.__log_dict:
            self.make_log_dict()
        for key in sorted(self.__log_dict.keys()):
            num_results = Sensor.objects.filter(s_log = key).count()
            if num_results < 1:
                b = Building.objects.get(b_num=self.__log_dict[key][0])
                s = b.sensor_set.create(s_name=self.__log_dict[key][1], s_type=self.__log_dict[key][4], s_log=key)
                s.save()

    def make_log_dict(self):
        #bnamelst1 = ['adel','B26 ', 'cline','B28 ', 'sas','B60 ']
        types = ['Current Demand KW', 'Dom Water Gallons',
                 'Reclaimed Water Gallons', 'Steam KBTU']

        cursor = self.__connection.cursor(as_dict=True)
        # Get list of trendlogs
        cursor.execute('SELECT * FROM tblTrendloglist')
        # Create a dictionary to store log information. Keys logdevnum_loginst
        for row in cursor:
            for num in self.__b_identifiers.keys():
                desc = row['logdescription'].upper()
                # Searching for any instance of building name in all logdesc
                #if num+" " in desc or num in desc or num[1:] in desc:
                if num+" " in desc or num in desc or self.__b_identifiers[num][1].upper() in desc:
                    # Creating key
                    logdevnum = str(row['logdevnum'])
                    loginst = str(row['loginst'])
                    key = logdevnum+"_"+loginst
                    # Storing bname, logdesc, objname, TrendlogID in log_dict
                    self.__log_dict[key] = [num, row['logdescription'],
                    row['objname'], row['TrendlogID'], 'None']
                    for t in types:
                        if t.upper() in desc:
                            self.__log_dict[key][4] = t
        #self.dict_printer()

    def update_logs(self):
        # Querying for trendlogs based on log_dict info
        lognum = 1
        for key in sorted(self.__log_dict.keys()):
            # Creating string which identifies trendlog
            logstring = self.__create_trend_string(key)

            print(str(lognum) + ": logid: " + key + " logstring: " + logstring +
            " building: " + log_dict[key][0])
            print("--- " + log_dict[key][1])
            lognum +=1

            num_results = Building.objects.filter(b_num = key).count()
            if num_results < 1:
                b = Building(b_name='lol', b_num=key, b_alias=self.__b_identifiers[key])
                b.save()

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

    def __create_trend_string(self, log_id):
        # Creating string which identifies trendlog
        logstring = 'tblTrendlog_'
        logid = log_id.split("_")
        for i in range(7-len(logid[0])):
            logstring += "0"
        logstring += logid[0]
        logstring += "_"
        for i in range(10 - len(logid[1])):
            logstring += "0"
        logstring += logid[1]
        return logstring

    def get_log(self, log_id):
        # Creating string which identifies trendlog
        logstring = self.__create_trend_string(log_id)
        # Creating cursor to parse database
        cursor = self.__connection.cursor(as_dict=True)
        # Creating dynamic query for trendlog table
        query = ('SELECT * FROM %s' % logstring)
        # Querying for trendlog table
        cursor.execute(query, ())

        ret_dict = {}

        for row in cursor:
            ret_dict[row['Sequence']] = [row['TimeOfSample'], row['SampleValue']]

        return ret_dict

    def dict_printer(self):
        count = 0
        for key in sorted(self.__log_dict.keys()):
            count+=1
            print(str(count) + ": " + key + ": " + str(self.__log_dict[key]))

    def log_printer(self):
        cursor = self.__connection.cursor()
        cursor.execute('SELECT * FROM ')
        self.__table = cursor.fetchall()
        print(self.__table)



#print("Hello from SDR")
sdr = StaticDataRetriever()
#sdr.update_buildings()
sdr.make_log_dict()
#sdr.find_logs()
#sdr.store_table()'''