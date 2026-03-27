# from collections import defaultdict


# MENU_LIST=[]
user_menu ={
  "starters":{
    "Veg Spring Roll": 120,
    "Paneer Tikka": 180,
    "Veg Manchurian": 150,
    "Chilli Paneer": 170,
    "French Fries": 100
  },

  "main Course": {
    "Butter Paneer Masala": 220,
    "Shahi Paneer": 210,
    "Kadai Paneer": 200,
    "Dal Makhani": 180,
    "Mix Veg": 160
  },

  "breads": {
    "Tandoori Roti": 20,
    "Butter Naan": 40,
    "Garlic Naan": 50,
    "Lachha Paratha": 45
  },

  "rice": {
    "Plain Rice": 90,
    "Jeera Rice": 120,
    "Veg Pulao": 150,
    "Veg Biryani": 180
  },

  "fast Food": {
    "Veg Burger": 80,
    "Cheese Burger": 100,
    "Veg Pizza": 200,
    "Pasta": 150,
    "Noodles": 120
  },

  "drinks": {
    "Cold Drink": 40,
    "Lassi": 60,
    "Mango Shake": 80,
    "Coffee": 50,
    "Tea": 20
  },

  "desserts":{
    "Gulab Jamun": 60,
    "Rasgulla": 60,
    "Ice Cream": 80,
    "Chocolate Cake": 120,
    "Jalebi": 70
  }
  }

# user_menu = defaultdict(dict)
def read_menu():
    with open(r"APP\DATABASE\menu_data.json","r") as file:
        menu_data=json.load(file)
        file.read(menu_data)
        


def write_menu(): 
    with open(r"APP\DATABASE\menu_data.json","w") as file:
        menu_data=json.dumps(user_menu)
        file.write(menu_data)

def show_menu():
    print("\n------ MENU ------")
    for category, items in user_menu.items():
        print("\n",category)
        for item, price in items.items():
            print(item,":",price)


def add_item():
  while True:
    category=input("Enter category: ").strip()
    if not category:
      print("input can't be empty.....!")
      continue
    elif not category.isalpha():
      print("input  must contain only letters.....!") 
      continue
    
    if category in user_menu:
      print("category already exists.....!")
      continue
    item=input("Enter item name: ").strip()
    if not item:
      print("input cant't be emapty........!")
      continue
    elif not item.isalpha():
      print("input must contain only letters.....!")
      continue
   
    price=input("Enter price: ")
    if not price:
      print("input can't be emapty.....!")
      continue
    elif not price.isdigit():
      print("input must be a valid number.....!")
      continue
    elif price.startswith("0"):
      print("input can't be start with zero.....!")
      continue
    
    
      user_menu[category][item]=price
      read_menu()
      write_menu()
      print("........Item Added........")
      pass
  
  


def delete_item():
  while True:
    category=input("Enter category: ").strip()
    if  not category :
      print("input can't be emapty.....!")
      continue
    elif not category.isalpha():
      print("input contain only latters.....!")
      continue
    if category not in user_menu:
      print("categary not found.....!")
      continue
        
    item=input("Enter item name: ").strip()
    if not item:
      print("input can't be emapty.....!")
      continue
    elif not item.isalpha():
      print("input contain only latters.....!")
      continue
    if item in user_menu[category]:
        del user_menu[category][item]
        print([category][item],"Deleted.....!")
        print("Item Deleted.....!")
        read_menu()
        write_menu()
        break
    else:
        print("Item not found")


def update_item():
  while True:
    category=input("Enter category: ")
    if not category:
      print("input can't be emapty.....!")
      continue
    if not category.isalpha():
      print("input must contain only letters.....!")
      continue
    if category not in user_menu:
      print("category not found.....!")
      continue
    
    item=input("Enter item name: ").strip()
    if not item:
      print("input can't be emapty.....!")
      continue
    if not item.isalpha():
      print("input must contain only letters.....!")
      continue
    if item not in user_menu[category]:
      print("item not found in this category.....!")
      continue
    price=input("Enter new price: ").strip()
    if not price:
      print("input cant't be emapty...........!")
      continue
    if not price.isdigit():
      print("input nust be avalid number.....!")
      continue
    if price.startswith("0"):
      print("input can't be start with 0.....!")
      continue
    
    user_menu[category][item]=price
    read_menu()
    write_menu() 
    print("______Item_Updated_______")
    print(f"{item} in {category} updated with new price {price}")
    break

def search_item():
  while True:
    item_name=input("Enter item name to search: ").strip()
    if not itenm_name:
      print("input  cant't be emapty.....!")
      continue
    elif not item_name.isalpha():
      print("input must contain only letters.....!")
      continue
    else:
      print("enter the valid input.....!")
      continue
      
 
  for category, items in user_menu.items():
    if item_name in items:
      print("Item Found")
      print("Category:",category)
      print("Price:",items[item_name])
      break
   
    else:
      print("Item Not Found")
      continue




def admin_menu():
 while True:
        print("<<<<MANAGE_MENU>>>>>")
        print("=======================")
        print("1.Show Menu")
        print("2.Add Item")
        print("3.Delete Item")
        print("4.Update Item")
        print("5.Exit")
      
        choice=input("Enter your choice: ")
        if not choice:
           print("input can't be emapy.....!")
           continue
        elif not choice.isdigit():
          print("input must contain only numbers.....!")
          continue
        elif choice.startswith("0"):
          print("input can't be start with zero.....!")
          continue
       
        user=int(choice)        

        if user == 1:
            show_menu()

        elif user == 2:
            add_item()

        elif user == 3:
            delete_item()

        elif user == 4:
            update_item()

        elif user == 5:
            print("Exit Program")
            break
        else:
            print("enter the valid input....!")
            continue

