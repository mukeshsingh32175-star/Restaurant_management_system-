from APP.AUTH.valid_name import input_name                   
from APP.AUTH import data_modes
from APP.MENU.main_menu import user_menu
import json
import datetime



coustomer_data = []
    
def write_order():
    with open (r"APP\DATABASE\order_data.json","w") as file:
       order_data= json.dumps(coustomer_data)
       file.write(order_data)


           
read_table=data_modes.write_json(r"APP\DATABASE\order_data.json",coustomer_data)       

def valid_table():
    while True:
        try:
            # data = read_order()
            total_table = 10
        
            table_number =input("enter the table number :  ").strip()
            # for data in read_table:
            #     if data["table_number"] == table_number:
            #         print("table number already booked. please choose  another table.")
            #         continue
            #     if data["table_number"] != table_number:
                    
            #         continue
            # break    
            # if  read_table > total_table:
            #     print("sorry, no more tables available.")
            #     break
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
            # elif data["table_number"] > total_table:
            #     print(" only", table, "tables are available.")
            #     continue
            # for data in read_table:
            #     if data["table_number"] == table_number:
            #         print("table number already booked. please choose  another table.")
            #         continue
            #     # if data["table_number"] > total_table:
            #     #     print("")
            #     #     continue
            # break    
            # if  read_table > total_table:
            #     print("sorry, no more tables available.")
            #     break
           
            else:
                print('remanig tables:', total_table)
                return table
        except Exception as error:  
            print( error)
            error_data=[
                {               "error_message": str(error),                
                    "datetime": data_modes.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
                }
            ]
            data_modes.erroer_write(json.dumps(error_data))
            continue

        
        
def valid_seats():
    while True:
        try:
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
        except Exception as error:
            print( error)
            
            error_data=[
                {
                    "error_message": str(error),
                    "datetime": data_modes.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
            ]
            data_modes.erroer_write(json.dumps(error_data))
            continue       

  

    
    
ordered_items = []   
total = 0
def order():
    
    total = 0
    print("\n****** PLACE YOUR ORDER ******")
    print("=" * 35)

    while True:
        try:
            customer = input("\nEnter the item name (or 'done' to finish): ").strip()
            if not customer:
                print(" Input cannot be empty!")
                continue

            if customer.lower() == 'done':
             break
            found = False

            for category, items in user_menu.items():
             if customer in items:
                found = True
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
                    ordered_items.append(f"{qty}  {customer:<15} {price}")
                    break
                break
            if not found:
                print(f"'{customer}' not found in the menu. Please try again.")
                continue
        except Exception as error:
            print( error)
            error_data=[
                {
                    "error_message": str(error),
                    "datetime": data_modes.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
            ]
            data_modes.erroer_write(json.dumps(error_data))
            continue  

def customer():
   
        
        coustomer={}
        print("******ORDER******")
        print("=========================")
        coustomer["name"]=input_name()
        coustomer["table_number"]=valid_table()
        coustomer["seats_number"]= valid_seats()
        coustomer["order"]= order() 
        coustomer["order_time"]= (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        coustomer_data.append(coustomer)
        write_order()
        print("______________Table booking successful_____________!")
        print("=========================================")
     