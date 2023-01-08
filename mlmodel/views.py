from django.shortcuts import render,HttpResponse,HttpResponseRedirect

from .forms import MyGeoForm

import xgboost
import pickle
import numpy as np
import json

import utm
from django.contrib.gis.geos import Point

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
        print(prediction)
        
       
    form = MyGeoForm()

    return render(request, 'index.html', {'form': form, "price":prediction})