# Mastering Tuple Packing and Unpacking in Python
#Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders
#You are given a list of tuples, each representing a customer's order. #
# Each tuple contains the customer's name, the product ordered, and the quantity. 
# #Your task is to unpack each tuple and print the order details in a user-friendly format.


orders = [("Alice", "Laptop", "1"),("Bob", "Camera", "2"),("Sara", "Charger", "8")]
   
print("\nWelcome to the Customer Order System ")

for item in orders:
        print( "Order: "   + item[0] +" ordered " + item[2] +" " +item[1])
       
    
    

        
        
    





 