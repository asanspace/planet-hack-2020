from planet import api
from planet.api import filters
import sys
import os
import requests
import time
from sys import stdout
import json 
import numpy as np
from pythonosc import udp_client

oscclient = udp_client.SimpleUDPClient("127.0.0.1", 4559) # port Sonic Pi is listening on


apikey = "edc98de4edd14e0c9cc393a6994876f4"

ddir = "/"
sdate = "2020-10-05"
edate = "2020-10-07"
limit = 16

f = open('explorer-aoi.geojson',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
coords = data['features'][0]['geometry']['coordinates']
aoi = {
  "type": "Polygon",
  "coordinates": coords
}

client = api.ClientV1(api_key= "edc98de4edd14e0c9cc393a6994876f4")

# build a query using the AOI and
# a cloud_cover filter that excludes 'cloud free' scenes
query = filters.and_filter(
    filters.geom_filter(aoi),
    filters.range_filter('cloud_cover', gt=0),
)

# build a request for only PlanetScope imagery
request = filters.build_search_request(
    query, item_types=['PSScene3Band', 'PSScene4Band']
)

results = client.quick_search(request)

stdout.write('id,cloud_cover,date\n')
coverVals = []
for item in results.items_iter(limit=limit):
    props = item['properties']
    coverVals.append(item['properties']['cloud_cover'])
    stdout.write('{0},{cloud_cover},{acquired}\n'.format(item['id'], **props))

print(coverVals)


arp = (15*(coverVals - np.min(coverVals))/np.ptp(coverVals)).astype(int)  
arp = arp.tolist()
print(arp)

oscclient.send_message("/trigger/prophet", arp)
