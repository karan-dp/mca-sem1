#finding the first even number
myList = [1,23,5,3,4,7]
for i in myList:
    if i%2 == 0:
        print("First even number for list is :",i)
        break

#continue
for i in range(1,10):
    if i%3 == 0:
        continue
    print(i, end=" ")

print()

#question loop till user enter "exit" keyword
while True:
    txt = input("enter any word")
    if txt.lower() == "exit":
        break

print("program closed")

#find element in list and break the loop
num = [1,-3,-3,4,8,0,-1,-4,6,2,10]
for i in num:
    if i <= 0:
        continue
    print(i, end = " ")

"""
while True:
     txt = int(input("enter any num"))
     if txt < 100 and txt >= 0:
         print(txt, end= " ")
         continue
     elif txt >= 100:
         break
"""





    
