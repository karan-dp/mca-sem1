#creating a list
shopping_list = [("tshirt",5),("pants",2),("suit",7)]

print(shopping_list)
item = input("Enter Item name : ")
qty = int(input("Enter Qty : "))
tup = (item,qty)
operation = input("choose operation : ")
print("New item :",tup)


def addList(data):
    shopping_list.append(data)
    return

def removeList(item):
    for x in shopping_list:
        item_name,quantity = x
        if(item_name == item):
            shopping_list.remove(x)
    return

def updateList(item,data):
    for x in shopping_list:
        item_name,quantity = x
        if(item_name == item):
            shopping_list.remove(x)
            shopping_list.append(data)
    return

if(operation == "add"):
    addList(tup)
elif(operation == "remove"):
    removeList(item)
elif(operation == "update"):
    updateList(item,tup)
else:
    print("something went wrong")


print("Updated List :",shopping_list)


