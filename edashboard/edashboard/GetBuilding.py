from django import forms

class ExportBuilding:

    def __init__(self):
        self.building = ""
        self.util = ""
        self.sensor = ""
        self.timestart = ""
        self.timeend = ""

    def createQuery(searchobj):
        return searchobj.building
