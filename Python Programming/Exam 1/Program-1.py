# 33_Karan_Panchal

# Task 1.1
print("--------------Task 1---------------------")
products = [(101,"shirt",200.00,5),
            (102,"pant",350.00,3),
            (103,"belt",100.00,7),
            (104,"suit",1200.00,0),
            (105,"watch",300.00,0)]
print(products)

# Task 1.2
cart_list = []
"""
while True:
    user_items = input("Enter Item you want : ")
    cart_list.append(user_items)
    print(cart_list)
    add_more = input("want to add more yes or no: ")
    if add_more.lower() != "yes":
        break
print("List of items you want are :",cart_list)
"""
print("----------------Task 2---------------------")
#Task 2

discounted_products = {"shirt","pant"}
print("Products that are on sale are :")
for x in discounted_products:
    print(x, end =" ")

print("\n---------------Task 3----------------------")
#Task 3

customer_info = {
    "name" : "Karan Panchal",
    "email": "karan.dp@somaiya.edu",
    "loyalty_points": 100
    }
print("Customer Details :")
print("Customer Name :",customer_info["name"])
print("Customer Email :",customer_info["email"])
print("Customer Points :",customer_info["loyalty_points"])

print("\n---------------Task 4----------------------")
# Task 4
print("\n***********MENU***********")
for x in products:
    product_id,product_name,price,qty = x
    print(product_id,product_name,price,qty)


user_input = int(input("Enter product id you want to add : "))
for x in products:
    product_id,product_name,price,qty = x
    if user_input == product_id :
        print(product_id,product_name,price,qty)
        if qty > 0:
            print(product_name,"is added to cart")
            cart_list.append((product_name,price))
        else:
            print(product_name,"is out of stock")
print("Your cart contain this items:",cart_list)        

print("\n----------------task 5--------------------\n")
# Task 5
while True:
    user_item = int(input("Enter product id :"))
    for x in products:
        product_id,product_name,price,qty = x
        if user_item == product_id and qty > 0:
            #print(user_item)
            cart_list.append((product_name,price))
        elif user_item == product_id and qty <= 0:
            print("out of stocksss...")
    add_more = input("want to buy more yes or no: ")
    if add_more.lower() != "yes":
        break
print(cart_list)
print("checkout is in progress......")

#calculating total cost of items
total_cost = 0
for x in cart_list:
    pname,pprice = x
    if pname in discounted_products:
        discount_price = pprice - (pprice * 10/100)
        total_cost +=discount_price
    else:
        total_cost +=pprice

print("Price after 10% discount :",total_cost)
#deduct from loyalty
points = float(customer_info["loyalty_points"])
print("Available loyalty points :",points )

final_amount = total_cost - points
if final_amount < 0:
    print("your order will be delivered sooonn....")
else:
    print("After reedeming loyal points amount to be paid is:",final_amount)







