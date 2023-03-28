# Importations

from geopy.geocoders import Nominatim
import plotly_express as px
from preprocessing import *

# Fonctionnement du module

geocoder = Nominatim()
adresse = "191 rue Saint-Jacques, Paris, France"
location = geocoder.geocode(adresse, True, 30)
print((location.latitude, location.longitude))

# In progress: modification du dataset


# Visualisation avec plotly

fig = px.choropleth_mapbox(df, geojson=colonne_ajoutee, locations='Voie', color='Surface bati',
                           color_continuous_scale="year",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5)

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()