cars=('supra','fortuner','bmw','ferrai')
print(cars)

#accessing element of tuple by index
print(cars[0])
print(cars[-1])
print(cars[-2])
print(cars[2:])
print(cars[:3])
print(cars[2:-1])
print(cars[-1:-3:-1])

#no insert remove replace

#combine tuple together
superCars = ("GTR","Bugati")
newTuple = cars+superCars
print(newTuple)


mul = cars*2
print(mul)

#length of a tuple
length = len(cars)

print("Length of cars :",length)

#Tuple methods
print(cars.index("ferrai"))
print(mul.count("supra"))

#Tuple packing
myCar = "supra","black",5555


#Tuple unpacking
name,color,num = myCar

#printing the unpacked values
print("Name :",name)
print("Color :",color)
print("Number :",num)


#inp = input("Enter ")

#l = [3,4,6,10,4,8,9,6,0,1,12]

#l = []

#for x in range(0,5):
#    num = int(input("Enter number : "))
#    l.append(num)

l = list(map(int,input("Enter space separeted values:").split(" ")))
print(l)

minimum = l[0]
maximum = l[0]
sum1 = 0

for x in l:
    if(x > maximum):
        maximum = x
    elif(x < minimum):
        minimum = x
    sum1 = sum1 + x

print("Sum is :",sum1)
print("Minimum is :",minimum)
print("Maximum is :",maximum)






















