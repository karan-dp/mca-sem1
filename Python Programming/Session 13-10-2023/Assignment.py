'''
Q. WAPP that merges content of multiple text file into one.
ensure lines are sorted in alphabetic order
'''

file_list = ["file1.txt","file2.txt","file3.txt","file4.txt"]

str1 = " "

book_file = open("book.txt",'r+')
for x in file_list:
    #reading data of files
    myfile = open(x,"r+")
    data = myfile.read()
    str1 += data + "\n"
    myfile.close()
    
    #writing data of files
    book_file.write(data + "\n")

#save read file data to new file
book_file.flush()

new_list = book_file.readlines();

new_list.sort()
print(new_list)

for x in new_list:
	book_file.write(x+"\n")

book_file.close()
#print(str1)
