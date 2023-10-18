#exception handling
'''
a = 10
b = 0
try:
    c = a/b
    print(c)
except:
    print("exception occurs")
'''
'''
a = 10
b = 0
try:
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
print("End of program")
'''
'''
try:
    num1 = int(input("Enter num 1"))
    num2 = int(input("Enter num 2"))

    ans = num1 * num2
except (ZeroDivisionError, ValueError):
    print("Unexpected error occured, we will get back to you soon")
else:
    #only execute on no error
    print("else part")
finally:
    #execute every time
    print("this is print every time")
print("End of the programm")

'''
'''
my_list = [1,2,3]
try:
    c= my_list[4]
except:
    print("IndexOutOfBound : ")
'''
#wapp to read a file using exception handling technique

def calling():
    try:
        file_name = input("Ente file name to check")
        my_file = open(file_name,"r")
        data = my_file.read()
        my_file.close()
    except:
        print("file does not exist")
        calling()


calling()

