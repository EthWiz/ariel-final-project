import json

with open('filename.json') as f:
    data = f.read().replace("'", '"')
    json_data = json.loads(data)