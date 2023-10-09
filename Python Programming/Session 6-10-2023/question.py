'''
that allow user to manage a todo list. Program a menu with following option
add task to list
remove task from list
display the list
sort
quit/exit
'''
l = ["study","office work"]

def add(data):
    l.append(data)
    print(l)
def remove(data):
    l.remove(data)
    print(l)
def printList():
    print(l)
def sort():
    l.sort()
    print(l)
def quit1():
    print("Thank you!!!")

switch = {
    1:add,
    2:remove,
    3 : printList,
    4:sort,
    5:quit1
}

print("**********Menu************")
print("1.Add Task\n2.Remove Task\n3.Print Task")
print("4.Sort Task\n5.Quit Menu")
print("**************************")


try:
    while True:
        user_input = int(input("choose operation to perform form list : "))
        selected_function = switch.get(user_input)
        if user_input == 1:
            user_add_task = input("enter task : ")
            selected_function(user_add_task)
        elif user_input == 2:
            user_remove_task = input("enter task to remove : ")            
            selected_function(user_remove_task)
        elif user_input == 3:
            selected_function()
        elif user_input == 4:
            selected_function()
        elif user_input == 5:
            selected_function()
            break
        else:
            print("Invalid operation")
except ValueError:
    print("Invalid input. Please enter a number (1,2 or 3).")


