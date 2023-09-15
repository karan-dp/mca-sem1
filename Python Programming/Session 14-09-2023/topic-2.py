#creating nested dictionary

student = {"name":"karan",
           "age":21,
           "courses": { "math": 50 ,"science":90, "history":60}
           }

#accessing the element of nested dictionary values
data = student["courses"]["math"]

print(student)
print(data)

#dictionary methods

k = student.keys()

print(k)


v = student.values()

print(v)

d = student.items()

print(d)


i = student.get("city" "this key is not present in current dictionary")

print(i)

student.pop("age")

print(student)

#handling key errors
person = {
    "name":"karan",
    "age": 18
}

try:
    print(person["city"])
except KeyError:
    print("Error")

#merge

    d1 = {"a":1,"b":2}
    d2 = {"c":3,"d":4}
    d1.update(d2)
    print(d1)



