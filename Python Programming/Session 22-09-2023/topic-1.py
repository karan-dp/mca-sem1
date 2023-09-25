#1
"""
str1 = "hello"
str2 = "world"
str = str1+ " "+str2
print(str.upper())


user_input = input("Enter any word :")
user_len = len(user_input)

print("Original length of string is :",user_len)

print("After removing white spaces :",user_input.strip()
      ,"New length is :",len(user_input.strip()))
"""

#2.
'''
string = "hello world!!!"
print("first occurence of string is :",string.find("l"))


str = "welcome to mca - python programming - kj somaiya management"
print(string)
def fnc():
    replace_inp = input("Enter the word u want to replace :")
    new_word = input("Enter the new word :")

    new_string = str.replace(replace_inp,new_word)
    print("new string is :\n",new_string)
    
fnc()
'''


#3
email = "karan.dp@somaiya.edu"
a=email.find("@")
print(a)
slicing=email[a:]
print("Username:",email[:a])
print("Domain name:",email[a:])

string = "welcome to mca karan darshan"
string = string.split()
print("No of words are :",len(string))


#4
user_name = input("Enter name :")
user_age =  input("Enter age :")
string = "my name is "+ user_name+" and I am "+user_age+" years old"
print("Original string :",string)
print("TitleCase :", string.title()) 
print("Capitalize :",string.capitalize())
print("--------------------5--------------------")
#5
string = "la la laa la lala lalal lllaaaaaa"

print("count of l letter :",string.count('l'))

para = "Peter Piper picked a peck of pickled peppers.A peck of pickled peppers Peter Piper picked.If Peter Piper picked a peck of pickled peppers,Where’s the peck of pickled peppers Peter Piper picked?"
print(para.lower().count("peter"))

print("--------------------6--------------------")
#6.
og_string = "madam"
reverse_string = ""
og_len = len(og_string)

for i in range(og_len-1,-1,-1):
    reverse_string = reverse_string + og_string[i]

if reverse_string == og_string:
    print("its a palindrome")
else:
    print("not a palindrome")

string = "string. with, punctuation!!"
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for i in string:
    if i in punc:
        string = string.replace(i, "")
print("The string after punctuation filter :",string)

print("-------------------7---------------------")
#7.
word_list = ["hello","world","welcome","to","mca"]
new_string = ""
for i in word_list:
    new_string += i +", "
print(new_string)

para = "this is para1. this is para2. this is para3. this is para4" 
para = para.split(".")
print("New sentence :",para)

print("---------------------8------------------")
#8.
string = "This string start with uppercase"
if string[0].isupper():
    print("string starts with uppercase")
else:
    print("does not starts with uppercase")

user_input = input("Enter any word")
end_word_check =  input("Enter end word to check")
if user_input.endswith(end_word_check):
    print("ends with this word")
else:
    print("does not ends with this word")

print("---------------------9------------------")
#9
user_input = input("Please with 0 in start and end")
user_input = user_input.lstrip("0")
user_input = user_input.rstrip("0")
print(user_input)

user_input = input("Please enter any word")
remove_input = input("enter letter to remove from start and end")
change = user_input.lstrip(remove_input)
change = change.rstrip(remove_input)
print("original string :", user_input)
print("after strip :",change)


print("---------------------10------------------")
#10
user_input1 = input("Please enter first word")
user_input2 = input("Please enter second word")

if user_input1 == user_input2:
    print("Both strings are identical")
else:
    print("Strings are not identical")

print("first occurence of letter in user_input :",user_input1.find("k"))
