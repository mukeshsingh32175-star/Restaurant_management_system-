from APP.MENU.main_menu import show_menu,search_item
from APP.BOOKING.booak_seat import custmor_seats
from APP.BOOKING.booak_seat import data_vew
from APP.BOOKING.booak_seat import custmor_seats
def user_menu():
    while True:
        print("<<<<USER_MENU>>>>>")     
        print("=================")
        print("1.VEW MENU")
        print("2.ORDER")
        print("3.BOOKING")
        print("4.GENERATE BILL")
        print("5.SEARCH ITEMS ")
        print("6.BOOKING VIEW")
        user_input =input("enter your choice:   ")
        print("=================")
        
        
        if user_input == "1":
             show_menu()
        elif user_input =="2":
              None
        elif  user_input == "3":
              custmor_seats()
        elif user_input == "4":
               None
        elif user_input == "5" :
            search_item()   
        elif user_input =="6":
             data_vew()
                 
        else:
            print("enter_the_valid_input.....!")
            print (" ....................")   
            
         
          