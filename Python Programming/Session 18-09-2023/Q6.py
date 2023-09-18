#Q6
number = list(map(int,input("Enter number :").split(" ")))
print(number)

for k in number:
    if k <= 0:
        continue
    print(k , endl= " ")
