#1.create a string
str1 = "Hello"
str2 = " Welcome to MCA - K J Somaiya Institue of Mangement"

#2.concat string 
str = str1 + str2
print(str)


#3.slicing of a string
substr = str[2:10]
print(str,substr)

print()
substr3 = str[-6:]
substr2 = str[-1:-6:-1]
print(substr3 ,"\n",substr2)

#4.string length
length = len(str)
print("Length of string is :",length)


#5.string methods - converting to lower and upper case
upper = str.upper()
lower = str.lower()

print(upper)
print(lower)


str_space = "       this is dummy          text          "

#only remove space from left and right not from middle of text
print(str_space.strip())

#spliting string

#default value for split is space
print(str.split())

#spliting on letter/character
print(str.split("o"))


#6.string formatting
print("\nFirst String =", str1)
print("\tFirst String =", str1 , "and second string",str2)
print("new string = ", str ,end = "#")

print()
#7.Searching in a string // case-sensitive
searchStr = "k j"

if searchStr in str.lower():
    print(searchStr,"is present in")
else:
    print(searchStr,"is not present in")


#8.replacing a keyword in a given string
#replcae only the word specificed in parameter
originalStr = "Hello world!!!"
rstr = originalStr.replace("world","karan")

print(rstr)
