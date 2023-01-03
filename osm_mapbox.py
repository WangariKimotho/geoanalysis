import osmnx as ox
import mapbox
import pydeck as pdk
import plotly.express as px
mapbox_access_token = 'pk.eyJ1Ijoia2ltb3Nob25zIiwiYSI6ImNsYzkwcW9yazBpdjkzcHBjbWtlNW1iZHIifQ.Na_6glvmkjBpCFLJ7x1lYA'

# download the street network for a city
city_name = 'Nairobi, Kenya'
city_geocode = ox.geocode(city_name)
G = ox.graph_from_point(city_geocode,network_type='drive')
# plot the street network
#ox.plot_graph(G)
# convert graph to geojson file 
geojson = ox.graph_to_gdfs(G,

    nodes=False,edges=True)
geojson = geojson.to_json()



# create a Mapbox map using the GeoJSON object
# create a Mapbox map using the GeoJSON object
view_state = pdk.ViewState(latitude=city_geocode[1], longitude=city_geocode[0], zoom=10)
geo_data = pdk.Layer(type='GeoJsonLayer',geojson=geojson, mapbox_style='mapbox://styles/mapbox/streets-v9', opacity=0.8)
r = pdk.Deck(layers=[geo_data], initial_view_state=view_state,api_keys={'mapbox': mapbox_access_token})

# plot the map
# pdk.JupyterDeck(r)
r.to_html('map_2.html')
r.show()
