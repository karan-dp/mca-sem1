#create a list with 1 to 10 number
my_list = [1,2,3,0,4,5,4]
print(my_list)

#list append - append an element to end of the list
my_list.append(11)

print("List after append :",my_list)
my_list.append("karan")
print(my_list)

#inserting list at specific location
my_list.insert(1,0);
print("After inserting at position 1 : ",my_list)

#altering list at given index
#my_list[1] = 16;

#print(my_list)

#Remove the element by value
my_list.remove("karan")
print("After remove by value : ",my_list)

#Remove the element based on index
#my_list.pop(-1)
my_list.pop(5)
print("After poping at index 5 ",my_list)

#Find the index of an element
i = my_list.index(4);
print("Index of element 4 is ", i);

#i = my_list.index(100) error

#check if an element is in the list or not
p = 6 in my_list
print("Is 6 available in list : ",p)

#count number of element in the list
c = my_list.count(10)
print("Count of number of element = ",c)

#copying the list
my_List_copied = my_list.copy();
print("original list :" , my_list)
print("Copied list :" , my_List_copied)

#sort the list

my_List_copied.sort()
print("List after sorting ",my_List_copied)
my_List_copied.sort(reverse = True)
print("List after descending sorting ",my_List_copied)

#clear all element from the list
my_List_copied.clear()
print("List after clear :",my_List_copied)



