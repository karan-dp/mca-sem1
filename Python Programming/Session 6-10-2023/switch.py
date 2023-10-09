#implementing a "Switch" using dictio

#define functions for each case

def case1():
    print("Case 1 is selected")
def case2():
    print("Case 2 is selected")
def case3():
    print("Case 3 is selected")
def case4():
    print("Case 4 is selected")
switch = {
    1:case1,
    2:case2,
    3:case3,
    }
try:
    selected_case = int(input("Enter a case(1,2 or 3):"))

    selected_function = switch.get(selected_case)
    if selected_function:
        selected_function()
    else:
        print("Invalid Case")
except ValueError:
    print("Invalid input. Please enter a number (1,2 or 3).")
