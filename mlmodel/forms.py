from django import forms

from django.contrib.gis import forms as gforms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class MyGeoForm(gforms.Form):
    point = gforms.PointField(widget=
        gforms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))
    # submit = forms.
