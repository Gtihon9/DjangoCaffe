import branca
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import folium
from folium import plugins, FeatureGroup, elements
from folium.plugins import MousePosition, MiniMap
from caffes.models import Caffe


def map(request):
    # Creating map
    m = folium.Map(location=[52.090151991910915, 23.69469500885926], zoom_start=16, zoom_max=40, height=800, width=1400)
    folium.Map()

    folium.GeoJson(data='D:\Apps\PycharmProjects\DjangoCaffesApp\CaffesApp\moth_site\\belarus.geojson',name='Belarus').add_to(m)
    # # Adding tile layers
    # folium.raster_layers.TileLayer('CartoDB Dark_Matter', name="CartoDB(Dark)").add_to(m)
    # folium.raster_layers.TileLayer('Stamen Terrain', name="Stamen Terrain").add_to(m)
    # folium.raster_layers.TileLayer('Stamen Toner', name="Stamen Toner").add_to(m)
    # folium.raster_layers.TileLayer('Stamen Watercolor', name="Stamen Watercolor").add_to(m)
    # folium.raster_layers.TileLayer('CartoDB positron', name="CartoDB Positron").add_to(m)
    # folium.raster_layers.TileLayer(
    #     'https://tile.jawg.io/jawg-matrix/{z}/{x}/{y}.png?access-token=DdeoPv8NeLv4t0IB7ZXdH6Js9CS1WwIPRHxDmVtOsPLw0nfMZ6NQeXW6Dk4SUtiF',
    #     name="Jawg Matrix",
    #     attr='<a href="http://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank" class="jawg-attrib" >&copy; <b>Jawg</b>Maps</a> | <a href="https://www.openstreetmap.org/copyright" title="OpenStreetMap is open data licensed under ODbL" target="_blank" class="osm-attrib" >&copy; OSM contributors</a>').add_to(
    #     m
    # # Adding layer control button to map
    # # Adding Fullscreen button to map
    feature_group = FeatureGroup(name="Coffe")

    caffes_geoposition = Caffe.objects.all()
    for caffe_geoposition in caffes_geoposition:
        caffe_template=f"""
        <h1> {caffe_geoposition.name}</h1><br>
        { caffe_geoposition.open_time } - { caffe_geoposition.close_time }
        <p>
        <code>
            from numpy import *<br>
            exp(-2*pi)
        </code>
        </p>
        """
        feature_group.add_child(folium.Marker(location=[caffe_geoposition.longtitude, caffe_geoposition.latitude], popup=caffe_template))

    m.add_child(feature_group)
    m.add_child(folium.map.LayerControl())
    # folium.plugins.Fullscreen().add_to(m)
    # # Adding marker to map


    #
    # formatter = "function(num) {return L.Util.formatNum(num, 4) + ' º ';};"
    #
    # MousePosition(
    #     position="topright",
    #     separator=" | ",
    #     empty_string="NaN",
    #     lng_first=True,
    #     num_digits=20,
    #     prefix="Coordinates:",
    #     lat_formatter=formatter,
    #     lng_formatter=formatter,
    # ).add_to(m)
    #
    # # MiniMap(tile_layer='Stamen WaterColor', position='bottomleft', toggle_display=True).add_to(m)
    #
    # folium.ClickForMarker().add_to(m)
    #
    # # folium.plugins.LocateControl(auto_start=True).add_to(m)
    m = m._repr_html_()

    caffes = Caffe.objects.all()
    for caffe in caffes:
        print(caffe.longtitude)
    context = {
        'm': m,
        'caffes': caffes,
    }
    return render(request, 'moth_site/map.html', context)

def detail_view(request, pk):
    #comments
    caffe = get_object_or_404(Caffe, id=pk)
    return render(request, 'moth_site/detail.html', {
        'caffe': caffe
    })
