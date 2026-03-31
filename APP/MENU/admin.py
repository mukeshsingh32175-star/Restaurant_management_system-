from APP.MENU.main_menu import admin_menu
from APP.BOOKING.booak_seat import custmor_seats
from APP.BOOKING.booak_seat import cousmor_booking_data
from APP.AUTH.data_modes import read_json
import json
from APP.BOOKING.booak_seat import custmor_seats
from APP.ORDER.cstmr_order import customer
from APP.AUTH import data_modes
import pprint



data = data_modes.read_json(r"APP\DATABASE\sign_data.json")
                   

def delete_data():
 while True:
    try:
        if not data:
            print("No staff data available to delete.")
            continue
        print("***DELETE_DATA***")
        delete_name=input("Enter the staff name: ")
        for i in data:
            if i["name"] == delete_name:
                data.remove(i)
                print("Deleted data:",end="")
                pprint.pprint(i,indent=2)
                print("Data deleted successfully.....!")
                print("==========================")
        data_modes.write_json(r"APP\DATABASE\sign_data.json",data)
        break
    except Exception as error:
        print( error)
        data_modes.erroer_write(error_message=str(error))
        continue            
    
def admin_manage():
 while True:
     try: 
            print("<<<<ADMIN_MENU>>>>>")
            print("=====================")
            print("1.MANAGE_MENU")
            print("2.ORDER")
            print("3.BOOKING")
            print("4.REPORT")
            print("5.VEW ALL BOOKING DATA")
            print("6.DELETE STAFF")
    
            admin_input=input("enter your choice(1 to 6):  ")
            if  not admin_input:
                print("input can'tbe emapty.....!")
                continue
            elif not admin_input.isdigit():
                print("only numbers allowed.....!")
                continue
            elif int(admin_input) < 1 or int(admin_input) > 6:
                print("enter the valid value.....!")
                continue
            elif admin_input.startswith("0"):
                print("enter value can't start wit zero.....!")
                continue
            admin_input=int(admin_input)
            if  admin_input == 1:
                admin_menu()   
            elif  admin_input == 2 :
                customer()
            elif admin_input  == 3:
                custmor_seats()
            elif admin_input == 4:
                None
            elif  admin_input == 5:
                print("*****ALL BOOKING DATA****")
                print (cousmor_booking_data)
                print("=======================")     
            elif admin_input  == 6:
                delete_data()
            else :                  
                print ("enter the valid value.....!")  
                continue  
     except Exception as error:
            print( error)
            data_modes.erroer_write(error_message=str(error))
            continue      
            

          
    
    
        