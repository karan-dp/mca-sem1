tup = (1,2,3,4,5,6)

tup2 = (7,8)

t3 = tup + tup2
print(t3)

#converting tuple to list
print(list(tup))

#method2
l1 = [*tup2] + [*tup]

print(l1)

#method 3

l2 = []
for x in tup:
    l2.append(x)
    
print(l2)

#


