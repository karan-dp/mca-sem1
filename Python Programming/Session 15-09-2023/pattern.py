#pattern


for x in range(0,5):
    for y in range(0,x+1):
        print("* ", end = " ")
    print()


#pattern pyramind
print()
n = 5
for x in range(0,n):
    for s in range(0, 5-n-1):
        print("  ", end= " ")
    for y in range(0,x+1):
        print("* ", end = " ")
    print()    
