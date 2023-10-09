'''
myfile = open("sample.txt","r")
str1 = " "
size = 0
tsize = 0
while str1:
    str1 = myfile.readline()
    tsize = tsize + len(str1)
    size = size + len(str1.strip())
print("Total size :",tsize)
print("Size :",size)
myfile.close()

'''

'''

myfile = open("sample.txt","r")
contents = myfile.readlines()
print(contents)
print("First line is :", contents[0])
print("Last line is :",contents[len(contents)-1])
'''

myfile = open("sample.txt","r")
str = myfile.read()
size = len(str)
print("Size of file in bytes",size)
myfile.close()

myfile = open("sample.txt","r")
str = myfile.readlines()
size = len(str)
print("Numbers of file line",size)
myfile.close()

# Q. wapp to read the content of file and count how many times lette 'a' comes in file
# Wapp to read the content of a file and display capital I in place of 'E' while displaying content of file all other charcters should appear as it is.

