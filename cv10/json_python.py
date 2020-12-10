import json

json_str='{"klíč1":"hodnota1","klic2":[1,2,3]}'

json_parsed = json.loads(json_str)
print(json_parsed)
print(json_parsed["klic2"][2])
json_parsed["klíč1"]=None

print(json.dumps(json_parsed, ensure_ascii=False))

with open("out.json","w") as f:
    json.dump(json_parsed,f, indent=2, ensure_ascii=False)

with open("out.json") as f:
    print(json.load(f))