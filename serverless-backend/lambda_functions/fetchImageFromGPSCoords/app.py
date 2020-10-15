import os
import json, decimal
import boto3

apiKey = os.environ.get('PLANET_API_KEY')

def lambda_handler(event, context):
  print(event)
  print(context)
  response = {
    "statusCode": 200,
    "body": json.dumps({
            "something": 5,
            "somethingelse": 5
        })
  }

  print(response)
  return response
