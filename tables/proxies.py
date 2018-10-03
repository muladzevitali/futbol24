import json

with open('tables/proxies.json', 'r') as _input_file:
    proxies = json.loads(_input_file.read())
