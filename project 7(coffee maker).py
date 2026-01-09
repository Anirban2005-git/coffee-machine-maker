#coffee machine maker
from playsound import playsound
import time
menu={
    "Espresso":{
        " ingredients":{
            "water":40,
            "coffee": 18
        },
        "cost":50
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24
        },
        "cost":70
    },
    "cappuccino":{
        "ingredients":{
            "water":200,
            "milk":100,
            "coffee":40
        },
        "cost":90
    }
}


resources={
    "water":500,
    "milk":300,
    "coffee":100
}

profit=0

def check_esources_sufficient(order_ingredients):
  for item in order_ingredients:
    if order_ingredients[item]>resources[item]:
      print(f"sorry not enough {item} ")
      return False
  return True

def process_coin():
  print("please insert the coin")
  total=0
  coins_one=int(input("how many 1 rs coin?"))
  coins_two=int(input("how many 2 rs coin?"))
  coins_five=int(input("how many 5 rs coin?"))
  coins_ten=int(input("how many 10 rs coin?"))
  total= coins_one*1 + coins_two*2 + coins_five*5 + coins_ten*10
  return total


def make_coffee(drink_name,order_ingredients,sugar):
  for item in order_ingredients:
    resources[item]-= order_ingredients[item]

  print("☕ Brewing your coffee...")
  time.sleep(2)

  playsound("brewing-coffee-56459.mp3")


  print(f"Here is your {drink_name} with extra {sugar} spoons of sugar.☕Enjoy!")



while True:
 choice=input("what do you want to like? (Espresso/latte/cappuccino)").lower()
 if choice=="off":
    print("thanks for order...")
    break
 elif choice=="report":
   print(f"water: {resources['water']}ml")
   print(f"milk: {resources['milk']}ml")
   print(f"coffee: {resources['coffee']}ml")
   print(f"money: rs.{profit}")
 elif choice in menu:
   drink=menu[choice]
   if check_esources_sufficient(drink['ingredients']):
     payment = process_coin()
     if payment>=drink['cost']:
       change=payment-drink['cost']
       print(f"this is your {change} in change")
       profit+=drink['cost']
       sugar=int(input("how many spoons of sugar do you ike?(0-3): "))
       if sugar>0:
         print(0)
       elif sugar>3:
         print(3)
       make_coffee(choice,drink["ingredients"],sugar)
     else:
       print(f"sorry not enough money, refund money and your order is canceled")
 else:
   print("invalid input...")

     

