from planet import api
from planet.api import filters
import sys
import os
import requests
import time
from sys import stdout

apikey = "edc98de4edd14e0c9cc393a6994876f4"

ddir = "/"
sdate = "2020-10-05"
edate = "2020-10-07"
limit = 16

aoi = {
  "type": "Polygon",
  "coordinates": [
    [
      [-122.54, 37.81],
      [-122.38, 37.84],
      [-122.35, 37.71],
      [-122.53, 37.70],
      [-122.54, 37.81]
    ]
  ]
}

# will pick up api_key via environment variable PL_API_KEY
# but can be specified using `api_key` named argument
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

# if you don't have an API key configured, this will raise an exception
results = client.quick_search(request)

stdout.write('id,cloud_cover,date\n')

session = requests.Session()
session.auth = ("edc98de4edd14e0c9cc393a6994876f4", '')
# items_iter returns a limited iterator of all results. behind the scenes,
# the client is paging responses from the API
for item in results.items_iter(limit):
        print(item['id'])
        dataset = \
            session.get(
                ("https://api.planet.com/data/v1/item-types/" +
                "{}/items/{}/assets/").format("PSScene4Band", item['id']))
        # extract the activation url from the item for the desired asset
        print(dataset.json())
        item_activation_url = dataset.json()["udm"]["_links"]["activate"]
        # request activation
        response = session.post(item_activation_url)
        print(response.status_code)
        while response.status_code!=204:
            time.sleep(30)
            response = session.post(item_activation_url)
            response.status_code = response.status_code
            print(response.status_code)
        assets = client.get_assets(item).get()
        callback = api.write_to_file(directory=ddir, callback= None, overwrite= True)
        body = client.download(assets["udm"], callback=callback)
        body.wait()