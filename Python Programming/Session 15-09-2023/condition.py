#if else statments in python

score = float(input("enter your semester 1 score :"))

print(score)

#use conditional statements to check grade based on percentage

if score >= 75:
    print("First Class with Distinction ",score)
elif score >= 65 and score < 75:
    print("Your grade is First Class",score)
elif score >= 50 and score < 65:
    print("Your grade is Second Class",score)
elif score >= 40 and score < 50:
    print("Your grade is Third Class",score)
else:
    print("You are failed",score)

    
#number
num1 = float(input("Enter num1"))
num2 = float(input("Enter num2"))

if num1 > num2:
    print("num1 is greater")
elif num1 < num2:
    print("num2 is greater")
else:
    print("equal")

year = int(input("Enter year :"))
if year%4 == 0:
    print("this is leap year")
else:
    print("not leap year")

age = int(input("enter your age "))
if age < 0:
    print("invalid")
elif age < 18 :
    print("minor")
elif age < 65:
     print("adult")
else:
     print("senior")




     

