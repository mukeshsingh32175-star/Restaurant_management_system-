from APP.AUTH.valid_name import input_name
from APP.MENU.main_menu import user_menu
import json
import datetime

def vlaid_table():
    while True:
        total_table =10
        
        table_number =input("enter the table number :  ").strip()
        if not table_number:
            print("input cant't be emapty....!")
            continue
        elif not table_number.isdigit():
            print("invalid input. please enter a valid table number.")
            continue
        elif table_number.startswith('0'):
            print("input can't be start with zero.....!")
            continue
        table  =int(table_number)
        if table < 1 or table > total_table:
            print("invalid table number. please enter a number between 1 and", total_table)
            continue
        total_table -=  table
        if total_table < 0:
            print("sorry, no more tables available.")
            continue
        elif table > total_table:
            print(" only", table, "tables are available.")
            continue
           
        else:
            print('remanig tables:', total_table)
            return table
        
        
def valid_seats():
    while True:
        total_seats =50
        seats_number =input("enter the number of seats :  ").strip()
        if not seats_number:
            print("input cant't be emapty....!")
            continue
        elif not seats_number.isdigit():
            print("invalid input. please enter a valid number of seats.")
            continue
        elif seats_number.startswith('0'):
            print("input can't be start with zero.....!")
            continue
        seats  =int(seats_number)
        if seats < 1 or seats > total_seats:
            print("invalid number of seats. please enter a number between 1 and", total_seats)
            continue
        
        total_seats -=  seats
        if total_seats < 0:
            print("sorry, no more seats available.")
            continue
        elif seats > total_seats:
            print(" only", total_seats, "seats are available.")
            continue
        else:
            print('remanig seats:', total_seats)
            return seats_number        

def read_order():
    with open (r"APP\DATABASE\order_data.json","r") as file:
       order_data= json.loads(file.read())
    
    
def write_order():
    with open (r"APP\DATABASE\order_data.json","w") as file:
       order_data= json.dumps(coustomer_data)
       file.write(order_data)

# def order():
#     while True:
#         print("******ORDER******")
#         print('=========================')
#         total= 0
#         customer=input("enter the item name:  ").strip()
#         if not customer:
#             print("input can't be emapty....!") 
#             continue
        
#         if not  customer.isalpha():
#             print("invalid input. please enter a valid input......!") 
#             continue  
#         for item in user_menu:
#             if customer in item[category]:
#                 qantity=input("enter the quantity:  ").strip()
#                 if not qantity:
#                     print("input can't be emapty....!") 
#                     continue
#                 if not qantity.isdigit():
#                     print("invalid input. please enter a valid quantity......!") 
#                     continue
#                 if qantity.startswith('0'):
#                     print("input can't be start with zero.....!")
#                     continue
#                 Qantities =int(qantity)
#                 if Qantities < 1:
#                     print("invalid quantity. please enter a number greater than 0.")
#                     continue
#                 price = user_menu[category][customer] * Qantities
#                 total += price
#                 # print("Price:", price)
#                 break
#             else:
#                 print("item not found in the menu. please enter a valid item name.")
#                 continue
   
    
    
ordered_items = []   
total = 0
def order():

    print("\n****** PLACE YOUR ORDER ******")
    print("=" * 35)

    while True:
        customer = input("\nEnter the item name (or 'done' to finish): ").strip().title()

        if not customer:
            print(" Input cannot be empty!")
            continue

        if customer.lower() == 'done':
            break

        for item in user_menu:
         if customer in user_menu[category]:
            while True:   
                quantity = input(f"Enter quantity for {customer}: ").strip()

                if not quantity:
                    print(" Quantity cannot be empty!")
                    continue
                    
                if not quantity.isdigit():
                    print(" Please enter a valid number!")
                    continue

                if quantity.startswith('0') and len(quantity) > 1: 
                    print(" Quantity cannot start with zero!")
                    continue

                qty = int(quantity)
                if qty == 0:
                    print(" Quantity cannot be zero!")
                    continue

           
                price = user_menu[category][customer] * qty
                total += price

                ordered_items.append(f"{qty} x {customer:<15} {price}")
                # print(f" Added: {qty} x {customer} = ₹{price}")
                break

        else:
            print(f"'{customer}' not found in the menu. Please try again.")

coustomer_data={}
def customer():
    while True:
        
        print("******ORDER******")
        print("=========================")
        coustomer_data["name"]=input_name()
        coustomer_data["table_number"]=vlaid_table(),
        coustomer_data["seats_number"]= valid_seats()
        coustomer_data["order"]= order() 
        coustomer_data["order_time"]= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        write_order()
        print("______________Table booking successful_____________!")
     