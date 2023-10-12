'''
theory
syntax
example
application
usage/adv/disadv
'''
'''
myfile = open("sample.txt","a")
for i in range(3):
    name = input("Enter name to store :")
    myfile.write(name)
    myfile.write('\n')
myfile.close()
print("data saved successfully")


myfile = open("sample.txt","r")
read = myfile.readlines()
print(read)
myfile.close()

#example 3 using writelines()
myfile = open("sample.txt","a")
mylist = []
for i in range(3):
    name = input("Enter Employee name : ")
    mylist.append(name+'\n')
myfile.writelines(mylist)
myfile.close()
print("Data Saved..")

'''
myfile = open("sample.txt","a")
ans ='y'
while ans == 'y':
    bno = int(input("Enter book no"))
    bname = input("Enter Book Name ")
    author = input("Enter Author name")
    bprice = int(input("Enter book price"))
    brec = str(bno) + ","+ bname + ","+author
    myfile.write(brec)
    ans = input("add more ?")
myfile.close()


