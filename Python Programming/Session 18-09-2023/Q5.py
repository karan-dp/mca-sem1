
#Q5
for num in range(1, 51):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

#Q8
number = list(map(int,input("Enter number for list :").split(" ")))
limit = 100
total = 0
for x in number:
    if total > limit:
        break
    newTotal = total + x
    if newTotal < 100:
       total = newTotal
print(total)

#Q9
li = list(map(int,input("Enter number for list :").split(" ")))
l2 = []
for x in li:
    if x in l2:
        #print("exist")
        continue
    else:
        l2.append(x)
        print(x, end= " ")


#Q7
#password code
while True:
    password = input("Enter a password: ")
    if len(password) < 8:
        print("Weak: Password is too short.")
    elif not any(char.isdigit() for char in password):
        print("Moderate: Password contains no digits.")
    elif len(password) >= 12 and any(char.isdigit() or not char.isalnum() for char in password):
        print("Very Strong: Password is strong with special characters.")
    else:
        print("Strong: Password is strong.")
    break
    
