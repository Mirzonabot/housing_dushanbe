from django.shortcuts import render,HttpResponse,HttpResponseRedirect

from .forms import MyGeoForm

from .models import Prediction

import xgboost
import pickle
import numpy as np
import json

from django.contrib.gis.geos import Point

import folium

filename = "xgboost_model.sav"
model = pickle.load(open(filename, 'rb'))

# Create your views here.
def index(request):
    # if this is a POST request we need to process the form data

    prediction = None

    if request.method == 'POST':
        response = request.POST
        floor = response["floor"]
        rooms = response["rooms"]
        area = response["area_m_sqrd"]
        location = response["point"]
        location = json.loads(location)
        lc = location["coordinates"]
        point = Point(lc[0], lc[1], srid=3857)
        point.transform(4326)
        long = float(point.x)
        lat  = float(point.y)
        parameters = np.array([[rooms,floor,area,lat,long]], dtype=object)
        prediction = model.predict(parameters)[0] 
        pred = Prediction.objects.create(floor = floor,rooms = rooms,area = area,latitude = lat,longitude = long,price = prediction)
        # print(pred)
        print(prediction)
        
       
    form = MyGeoForm()

    return render(request, 'index.html', {'form': form, "price":prediction})

def prediction_history(request):
    predictions = Prediction.objects.all()
    print(predictions)
    m = folium.Map(location=[38.559772,68.787038],zoom_start=12)

    for row in predictions:
        iframe = folium.IFrame("Date and time " + str(row.created_on)
                                + " </br> Floor " + str(row.floor)
                                + " </br> Rooms " + str(row.rooms)
                                + " </br> Area(in m^2) " + str(row.area)
                                + " </br> Price " + str(row.price))
        popup = folium.Popup(iframe, min_width = 200, max_width=300)

        folium.Marker(location=[row.latitude,row.longitude],
                        popup=popup,c = row.price).add_to(m)

    m = m._repr_html_()
    
    return render(request, 'predictions.html', {'predictions':predictions, 'map':m})