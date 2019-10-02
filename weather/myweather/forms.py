from django import forms


class CityForm(forms.Form):
    cityname = forms.CharField(label="Enter City", max_length=15)
