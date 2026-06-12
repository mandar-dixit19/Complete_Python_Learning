import json


# this is the python data
data = {
 "name": "mandar",
 "isTeacher": True,
 "age": 57
}

# this is a json strig
json_str = '{"name": "mandar", "isTeacher": null}'
# this is the way that conver the data into the python object -=> dictionary
py_obj = json.loads(json_str)
print(type(py_obj),py_obj) # dict
print(type(json_str))

# convert the python object into the json string
py_obj = {"name": "mandar", "isTeacher": True}
json_str = json.dumps(py_obj)
print(type(json_str), json_str)


#in  the json file se data kko load (read arna chahte he to use json.load() method)
# 
# in the json file me data ko write karna chahte he to use json.dump() method 


# convert the data  into the py obj 
with open("data.json", "r") as f:
 py_obj = json.load(f)
 print(type(py_obj), py_obj)




 # convert the py data into the json str
 with open("data.json", "w") as f:
  json.dump(data, f, indent=4,  sort_keys=True)