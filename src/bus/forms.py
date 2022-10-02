from django import forms

class Busform(forms.Form):
    bus_name = forms.CharField(max_length=30)
    bus_no = forms.CharField(max_length=15)
    bus_img = forms.FileField()