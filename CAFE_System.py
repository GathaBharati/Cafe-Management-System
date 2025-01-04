print(f"Welcome to  Gelhi's cafe!\n Stressed, blessed, and coffee-obsessed \n Here's the menu for you: \n")
menu={
    "Cappucino": 98,
    "Americano": 70,
    "Espresso": 80,
    "Margherita": 180,
    "Farmhouse pizza": 209,
    "Barbeque chicken pizza": 320,
    "Chicken tikka pizza": 299,
    "Mac n cheese burger": 250,
    "The upsidedown burger": 240,
    "Arabita pasta": 200,
    "Cheese chicken penne pasta": 299,
    "Brownie": 120,
    "Blueberry cheesecake": 150,
    "Pinacolada": 120,
    "Blue lagoon": 120,
}
print("Cappucino: 9")
print("Espresso: 80")
print("Americano: 70")
print("Margherita: 180")
print("Farmhouse pizza: 209")
print("Barbeque chicken pizza: 320")
print("Chicken tikka pizza: 299")
print("Mac n cheese burger: 250")
print("The upsidedown burger: 240")
print("Arabita pasta: 200")
print("Cheese chicken penne pasta: 299")
print("Brownie: 120")
print("Blueberry cheesecake: 150")
print("Pinacolada: 120")
print("Blue lagoon: 120 \n")

order=input("What would you like to order?\n")
item=0
if order in menu:
    item+=menu[order]
else:
    print("Sry! we don't serve",order)

order2=input("Anything else you would like to order? yes/no ")

if (order2=="yes"): 
  i=1
  while (order2!="no"): 
     item2=input("What would you like to order? ")

     if item2 in menu:
         item+=menu[item2]
     else:
        print("Sry! we don't serve",order)  
     order2=input("Anything else you would like to order? yes/no \n")       
  i+=1
else:
   exit

print("Here's your bill. Have a nice gossip with your food!\n",)
print("Total amount: Rs.",item,"\n"
         "  Come with your friends next time!")

