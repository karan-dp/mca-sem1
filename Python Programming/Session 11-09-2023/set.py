cars = {"supra","fortuner","defender","bugatti"}
# order is not preserved
# duplicate not allowed
print("Original set :",cars)

print(type(cars))

#adding flowers name using update method
#setName.update(pass whole set here)
cars.update("gtr")

print("After :",cars)

#removing from set
cars.remove("defender")
print(cars)
"""
print("After removing :",cars)
"""

#discard
cars.discard("fortuner")
print(cars)

#check if specific value exist or not
#case sensitive
if "supra" in cars:
    print("Supra is present")
else:
    print("Supra is not present in set")
    
#Iteration through the set of flower names
print("welcome to iteratoin of set")

for x in cars:
    print(x, end=" ")

print()

print("Length of set :",len(cars))

#copy
cars_copy = cars.copy()
print("ORiginal set",cars)
print("Copied set",cars_copy)

#clear
cars.clear()
print(type(cars))
print("Original set ", cars)

#union - store only unique elements after union
print("Set 1 value :",cars_copy)
cars2 = ("bmw","audi")
print("Set 2 Value :",cars2)

intersection_set = cars_copy.union(cars2)
print("Union of two set :",intersection_set)

#difference of two sets
diff_set = cars_copy.differnce(cars2)
print(diff_set)











#union


