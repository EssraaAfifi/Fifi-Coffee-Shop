#def order():
#Greetings
print ("Hello! Welcome to FIFI'S COFFEE SHOP!")
name = input ("What is your name?")
print ("Well then "+ name +", What would you like to order. We have...")
#Menu
print (" 1. Cake \n 2. Tea \n 3. Coffee")

co = str (input ("Please enter a number per your order."))

if co == "1":
    print ("Thankyou " + name + "! Here is your slice of cake! Have a wonderful day!")
if co == "2":
    print ("Thankyou " + name + "! Here is your cup of tea! Have a wonderful day!")
if co == "3":
    print ("Thankyou " + name + "! Here is your cup of coffee! Have a wonderful day!")

#To execute; order()
