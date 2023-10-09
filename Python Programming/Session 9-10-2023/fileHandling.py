
#create a sample.txt file

#data file handling program to read
#myfile = open("sample.txt","r")
"""
str1 = myfile.read(10) # read first 10 characters
str2 = myfile.read(5) # read next 5 characters
str3 = myfile.read() #

print("Output of first read :")
print(str1)
print("Output of seconf read :")
print(str2)
print("Output of third read :")
print(str3)
"""
#program to read line
'''
myfile = open("sample.txt","r")
line1 = myfile.readline()
line2 = myfile.readline()
line3 = myfile.readline(10)

print(line1)
print(line2)
print(line3)
'''
#read whole data and return list separated by lines
'''
line1 = myfile.readlines()
print(line1)
'''
'''
myfile = open("sample.txt","r")
str1 = ""
while str1:
    str1 = myfile.readline()
    print(str1, end = '')
myfile.close()
'''

'''
myfile = open("sample.txt","r")
for str1 in myfile:
    print(str1 , end='')
'''

