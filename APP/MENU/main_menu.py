
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




def show_menu():
    print("\n------ MENU ------")
    for category, items in user_menu.items():
        print("\n",category)
        for item, price in items.items():
            print(item,":",price)


def add_item():
    category=input("Enter category: ")
    item=input("Enter item name: ")
    price=int(input("Enter price: "))

    user_menu[category][item]=price
    print("Item Added")


def delete_item():
    category=input("Enter category: ")
    item=input("Enter item name: ")

    del user_menu[category][item]
    print("Item Deleted")


def update_item():
    category=input("Enter category: ")
    item=input("Enter item name: ")
    price=int(input("Enter new price: "))

    user_menu[category][item]=price
    print("Item Updated")


def search_item():
    item_name=input("Enter item name to search: ")

    for category, items in user_menu.items():
        if item_name in items:
            print("Item Found")
            print("Category:",category)
            print("Price:",items[item_name])
            return

    print("Item Not Found")




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


        if choice=="1":
            show_menu()

        elif choice=="2":
            add_item()

        elif choice=="3":
            delete_item()

        elif choice=="4":
            update_item()

        elif choice=="5":
            print("Exit Program")
            break
        else:
            print("enter the valid input....!")
            continue

