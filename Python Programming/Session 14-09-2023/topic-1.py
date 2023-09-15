#dictionary
#key value pair
#key must be unique
#
#dictionary doesnot do sequencial serach
# traversing / accesing is faster in dict - internal working

#custom error exception handling

#compare all data types in python

data = {"name":"Karan",
        "college":"KJSIM",
        "grade":"O+",
        "courses":["Python","Java","Web","DBMS"]}

#printing whole dictionary
print(data)

#printing based on key
print(data["name"])

#changing key value
data["name"] = "kpanchal"
print("Modified name",data["name"])

#changing list in dict
print(data["courses"])
data["courses"].append("new data")
print("Modifed data :",data["courses"])

#adding new element
data["city"] = "Mumbai"
print("Added new element to dict",data)

data["hobbies"] = ["gaming","coding"]
print("After adding hobbies :",data)

data["hobbies"].append("sleeping") 
print("modified hobbies :",data)

#deleting key value
del data["city"]
print("After deleting:",data)

#check if a key exist
if "city" in data:
    print("City", data["city"])
else:
    print("city is not present")

    
