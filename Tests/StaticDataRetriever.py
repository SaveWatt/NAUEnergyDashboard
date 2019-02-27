import pandas as pd
from pathlib import Path
import pymssql as sql

HOST = r'Sweetleaf.nau.froot.nau.edu\GPDEV'
USER = r'NAU\idd6'
PASS = "Itsuko23272147"
BASE = 'EnergyCap'

class StaticDataRetriever:

    def __init__(self):
        self.__connection = sql.connect(host=HOST, user=USER,
        password=PASS, database=BASE)
        self.__table = None

    def print_rows(self):
        cursor = self.__connection.cursor()
        cursor.execute('SELECT * FROM tblTrendlog_0000601_0000000000')
        count = 0
        for row in cursor:
            if count > 24:
                break
            print("Row %d: %r" % (count+1, row))
            count += 1

    def store_table(self):
        cursor = self.__connection.cursor(as_dict=True)
        cursor.execute('SELECT * FROM tblTrendlog_0000601_0000000000')
        self.__table = cursor.fetchall()
        print(self.__table)




sdr = StaticDataRetriever()
sdr.print_rows()
sdr.store_table()
