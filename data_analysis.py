import json

with open('cities.json') as json_file:
    data1   = json.load(json_file)

with open('libraries.json') as json_file:
    data2 = json.load(json_file)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump([data1,data2], f, ensure_ascii=False, indent=4)