from django import forms

class ExportForm(forms.Form):
    building = forms.CharField()
    timestart = forms.CharField(required=True)
    timeend = forms.CharField(required=True)
    util = forms.CharField()
    sensor = forms.CharField()
