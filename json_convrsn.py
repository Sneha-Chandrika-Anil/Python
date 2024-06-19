import json

x = '{"name":"urmila","age" : "23"}'
y = json.loads(x)
print(type(x))
print(type(y))
z = json.dumps(y)
print(type(z))
print(y)