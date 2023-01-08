from django import forms

from django.contrib.gis import forms as gforms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class MyGeoForm(gforms.Form):
    floor = forms.IntegerField(max_value=20)
    rooms = forms.IntegerField(max_value=20)
    area_m_sqrd = forms.FloatField(max_value=300)
    point = gforms.PointField(
        widget=gforms.OSMWidget(attrs={'map_width': 400, 
                                'map_height': 500, 
                                'default_lat':38.559772,
                                'default_lon':68.787038,
                                'default_zoom': 12}),
                                )


