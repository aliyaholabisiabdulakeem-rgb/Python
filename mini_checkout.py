name = input("Enter your name: ")
product_name = input("Enter product name: ")
quantity1 = int(input("Enter quantity of product: "))
total_price1 = float(input("Enter price of product: "))
proceed = input("Do you want to contiue?: ")
option = input(("yes/no: "))
product1 = quantity1 * total_price1
print(name)
print(product_name)
print(quantity1)
print(total_price1)
print(product1)

for i in range(5):
    if(option == "yes"):
        product_name = input("Enter product name: ")
        quantity2 = int(input("Enter quantity of product: "))
        total_price2 = float(input("Enter price of product: "))
        product2 = quantity2 * total_price2
           
        print(name)
        print(product_name)
        print(quantity2)
        print(total_price2)
        print(product2)
        

        print("totalbill =" , (product1+ product2))  
        
        proceed = input("Do you want to contiue?: ")
        option = input("yes/no")   
    if(option == "no"):
        break;
    
