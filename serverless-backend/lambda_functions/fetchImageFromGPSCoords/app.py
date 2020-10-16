from planet import api
from planet.api import filters
from sys import stdout

import os
import json, decimal
import boto3

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
apiKey = os.environ.get('PLANET_API_KEY')

client = api.ClientV1(api_key=apiKey)
def lambda_handler(event, context):
  print(event)
  print(context)
  query = filters.and_filter(
    filters.geom_filter(aoi),
    filters.range_filter('cloud_cover', gt=0),
  )
  
  request = filters.build_search_request(
    query, item_types=['PSScene3Band', 'PSScene4Band']
  )
  
  result = client.quick_search(request)

  stdout.write('id,cloud_cover,date\n')
  
  for item in result.items_iter(limit=5):
    props = item['properties']
    stdout.write('{0},{cloud_cover},{acquired}\n'.format(item['id'], **props))
    
  response = {
    "statusCode": 200,
    "body": json.dumps({
            "something": 5,
            "somethingelse": 5
        })
  }
    
  print(response)
  return response
