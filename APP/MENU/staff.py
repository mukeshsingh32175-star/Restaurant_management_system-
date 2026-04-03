from APP.MENU.main_menu import show_menu,search_item
from APP.BOOKING.booak_seat import custmor_seats
from APP.BOOKING.booak_seat import data_vew
from APP.BOOKING.booak_seat import custmor_seats
from APP.ORDER.cstmr_order import customer
from  APP.BILLING.user_bill import final_bill 
from APP.AUTH import data_modes
def user_menu():
    while True:
        try:
            print("<<<<USER_MENU>>>>>")     
            print("=================")
            print("1.VEW MENU")
            print("2.ORDER")
            print("3.BOOKING")
            print("4.GENERATE BILL")
            print("5.SEARCH ITEMS ")
            print("6.BOOKING VIEW")
            user_input =input("enter your choice(1 to 6):   ")
            print("=" * 30)
            if not user_input:
                print("Input can't be empaty....!")
                continue
            if user_input.startswith("0"):
                print("Input must be grater then 0......!")
                continue
            if not user_input.isdigit:
                print("Enter the numbers alphabet is not allowed....!")
                continue
         
            staff_user=int(user_input)
        
            if staff_user == 1:
                show_menu()
            elif staff_user == 2:
                customer()
            elif  staff_user == 3:
                custmor_seats()
            elif staff_user == 4:
                final_bill ()
            elif staff_user == 5 :
                search_item()   
            elif staff_user == 6:
                data_vew()
                 
            else:
                print("enter_the_valid_input(1 to 6).....!")
                print (" ....................") 
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
            
         
          