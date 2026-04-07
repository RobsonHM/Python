import json

with open("/Users/lordcroft/Documents/Git/studies/Semester_02/datadict.json", "r") as file:
    data = json.load(file)

print(data)