#  Create a dictionary of any 7 Indian states and their capitals.
#  Write this into a JSON file.



import json

obj={
    "Maharashtra":"Mumbai",
    "Uttarpradesh":"lucknow",
    "uttarakhand":"Dehradun",
    "Gujrat":"Gandhinagar",
    "Madhaypradesh":"Bhopal",
    "Himachalpradesh":"Shimla",
    "Westbangal":"Kolkata"
}


file=open(r"states.json","w")
data=json.dump(obj,file)


# #for read
# file=open(r"states.json")
# data=json.load(file)
# print(data)

