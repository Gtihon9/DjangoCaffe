import os
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
import folium
from folium import plugins, FeatureGroup, elements
from django.urls import reverse
from caffes.models import Caffe


def map(request):
    # Creating map
    m = folium.Map(location=[52.090151991910915, 23.69469500885926], zoom_start=16, zoom_max=40, position='center')

    folium.GeoJson(data='moth_site/belarus.geojson', name='Belarus').add_to(m)
    feature_group = FeatureGroup(name="Coffe")

    cafes = Caffe.objects.all()
    for cafe in cafes:
        feature_group.add_child(folium.Marker(location=[cafe.longtitude, cafe.latitude], popup=cafe_popup(cafe)))

    m.add_child(feature_group)
    m.add_child(folium.map.LayerControl())
    folium.plugins.Fullscreen().add_to(m)

    m = m._repr_html_()

    context = {
        'm': m,
        'cafes': cafes,
    }
    return render(request, 'moth_site/map.html', context)

def cafe_popup(cafe):
    try:
        cafe_template = f"""
            <h1> 
                <a href='{reverse('detail',args=[cafe.id])}' target='_blank' > {cafe.name}</a>
            </h1>
            <h5> {cafe.address}</h2>
            <h1> 
                <img src={cafe.photo.url} style="width:100px; height: 100px;">
            </h1>
            
            <h5>
                <b>Working time</b><br>{ cafe.open_time } - { cafe.close_time } 
            </h5>
            <hr>
            <h5>
                <b>Rate: {cafe.rating}<b/>
            </h5>
            
            """
        popup = folium.Popup(html=cafe_template)
        return popup
    except Exception as e:
        return repr(e)



def home(request):
    return render(request, 'moth_site/hello.html')