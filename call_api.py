import requests
import json
from dotenv import load_dotenv
load_dotenv()
import os

SUBSCRIPTION_KEY = 'efcd73199e6f4c1d82f1015725ed071e'
SUBSCRIPTION_KEY = os.getenv('PASSWORD')
vision_service_address = 'https://imagereco.cognitiveservices.azure.com/vision/v1.0/'
address = vision_service_address + 'analyze'

parameters  = {'visualFeatures':'Description,Color',
               'language':'en'}

image_path = "./img/bear.jpg"
image_data = open(image_path, "rb").read()

headers    = {'Content-Type': 'application/octet-stream',
              'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

response = requests.post(address, headers=headers, params=parameters, data=image_data)

# Raise an exception if the call returns an error code
response.raise_for_status()

# Display the JSON results returned
results = response.json()
print(json.dumps(results))
print('requestId')
print(results['requestId'])
print(results['color']['dominantColorForeground'])
for tag in results['description']['tags']:
    print(tag)
# 