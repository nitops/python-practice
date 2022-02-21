# define dictionary below to create json from it.
data_payload = [
    {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
     'follow up': 'But enough talk!'}
]

import json

with open('output_json.json', 'w') as output_json:
    json.dump(data_payload, output_json)
