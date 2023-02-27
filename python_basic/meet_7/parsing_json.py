import json

# string JSON
data_str = '{"name": "John", "age": 30}'

# parsing string JSON
data = json.loads(data_str)

# memperoleh nilai dari kunci 'name'
name = data['name']
print(name)