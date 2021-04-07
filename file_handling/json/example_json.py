
import json

# json.dumps: python dict -> json
# json.loads: json -> python dict

data = {
    'name' : 'Tung''',
    'height' : 179,
    'weight' : 66
}
jsonStr = json.dumps(data, sort_keys=True, indent=1)
print(jsonStr)
print(type(jsonStr))  # <type 'str'>

print("\n===============\n")

pythonDic = json.loads(jsonStr)
print(pythonDic)
print(type(pythonDic))  # <type 'dict'>



with open('test.json', 'w') as jsonfile:
	jsonfile.write(jsonStr)
	# jsonfile.write(pythonDic)  #TypeError: expected a string or other character buffer object