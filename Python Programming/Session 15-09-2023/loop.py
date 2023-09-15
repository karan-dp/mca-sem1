import time
#range
print("Demo of for loop")

# range (start , end , step)
# step is optional by default value is 1
for x in range(1,6,1):
    print(x, end = " ")

print("\n--------------------------")
#while loop
#if condition is match then only works
#when condition fail control come out of while loop
#we 
print("Demo of while loop")

count = 0
while count < 10:
    print(count, end=" ")
    count += 1

print("\n--------------------------")

#nested for loop

print("Demo of nested for loop")

for x in range(1,6):
    for y in range(1,6):
        print(x,y)

print("\n--------------------------")

#question
print("table using while loop")
table = int(input("Enter number"))
count  = 1
while count <= 10:
    print(table,"X",count," = ",table*count)
    count +=1
print("table using for loop")
#for loop
for x in range(1,11):
     print(table,"X",x," = ",table*x)

import time
for x in range(5,-1,-1):
    time.sleep(1)
    print(x)

print("Timeeeee upsssss....!!!!!!!")




