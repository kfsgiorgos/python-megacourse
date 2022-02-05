from audioop import add
import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = list(data.LAT)
lon = list(data.LON)
elev = list(data.ELEV)

def colour_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 2500:
        return "orange"
    else:
        return "red" 

map = folium.Map(location=[38.58, -99.09], zoom_start = 6, tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name=" US map with Volanoes")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup="Elevation is: "+str(el)+ "m", icon=folium.Icon(color=colour_producer(el))))

map.add_child(fg)
map.save("/Users/georgios.kaiafas/Documents/GitHub/python-megacourse/Map1.html")
