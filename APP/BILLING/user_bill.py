from APP.ORDER.cstmr_order import ordered_items,total
from APP.ORDER.cstmr_order import coustomer_data
from APP.AUTH import data_modes

def final_bill():
  while True: 
       try:  
               cus_name=input("Enter the coustomer name: ").strip()
               if  not cus_name:
                    print("input cant't be emapty...........!")
                    continue
               print("******TOTAL_BILL******")
               print("=========================")
               if cus_name  == coustomer_data["name"]:
                    print("Coustomer Name:",coustomer_data["name"])
                    print("Table Number:",coustomer_data["table_number"])
                    print("Seats Number:",coustomer_data["seats_number"])
                    print("\nYour Ordered Items:")
                    if ordered_items:
                         for item in ordered_items:
                              print(item, ordered_items[item])
                              print("===========================")
                              print(f"Total Bill Amount : {total}")
                              print("thank you for ordering! ")
                              print("=========================")
                              payment()
                              pass
                    else:
                         print("No items ordered.")
                         print("=========================") 
                         continue       
               else:
                    print("coustomer name not found.....!")
                    continue
       except Exception as error:
               print( error)
               data_modes.erroer_write(error_message=str(error))
               continue     
 
 
def payment():
     while True:
          try:
               
               print("******PAYMENT******")
               print("=========================")
               print("1.CASH")
               print("2.CARD")
               print("3.MOBILE PAYMENT")
               payment_choice = input("Enter your payment method: ").strip()
               if not payment_choice:
                    print("input cant't be emapty...........!")
                    
                    continue
               if not payment_choice.isdigit():
                    print("invalid input. plese enter a valid choice....!")
                    continue
               if payment_choice.startswith('0'):
                    print("input can't be start with zero.....!")
                    continue
               user_payment= int(payment_choice)
               if user_payment == 1:
                print("You have selected CASH payment.")
          
               elif user_payment == 2:
                    print("You have selected CARD payment.")
    
               elif user_payment == 3:
                    print("You have selected MOBILE PAYMENT.")    
               else:
                    print("Invalid payment method. Please try again.")
                    continue
               print("Payment successful! Thank you for your order.")
               break
          except Exception as error:
               print( error)
               data_modes.erroer_write(error_message=str(error))
               continue   
    
           
# def customer_bill ():

#      print("=========================")
#      print("\n" + "=" * 40)
#      print("YOUR ORDER BILL")
#      print("=" * 40)

#      if ordered_items:
#         for item in ordered_items:
#             print(item)
#         print("-" * 40)
#         print(f"Total Bill Amount : {total}")
#      else:
#         print("No items ordered.")

#      print("=" * 40)
#      print("Thank you for ordering! ")
    