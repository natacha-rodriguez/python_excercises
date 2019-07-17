#! /usr/bin/python3
import json

with open('data.json','r') as file:
	data = json.load(file)

for record in data:
	if len(record['friends']) < 2 :
		record['greeting'] = record['greeting'].replace('!', ', the lonely one!')

with open('data.json','w') as file:
	json.dump(data, file, indent=4)

