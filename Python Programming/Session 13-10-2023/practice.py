'''
myfile = open("book.txt","r")
myfile_backup = open("book_backup.txt","w")

str1 = " "
while str1:
    str1= myfile.readline()
    myfile_backup.write(str1)
myfile.close()
myfile_backup.close()


'''
#data is stored in buffer on close its stored in harddrive
'''
print("copied successfully")

'''

'''

myfile = open("book.txt","w+")
myfile.write("Hello")
myfile.write("Welcome to Disneyland")
#save buffer data to file 
myfile.flush()   

# flush the earlier content in buffer
n = input("presss any key")
myfile.write("Go to counter")
myfile.close()
'''

myfile = open("book.txt")
line1 = myfile.readline()
print("length of line is :",len(line1))
line1 = line1.rstrip("\n")
print("length of line is :",len(line1))
line2 = myfile.readline()
print("length of line is :",len(line2))
line2 = line2.lstrip()
print("length of line is :",len(line2))
