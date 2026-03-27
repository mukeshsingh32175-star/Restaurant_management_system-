from APP.ORDER.cstmr_order import ordered_items,total
from APP.ORDER.cstmr_order import coustomer_data
# def bill_write():
#      with open (r"APP\DATABASE\final_data.json","w") as file:
      
def final_bill():
  while True:   
          Nam=input("Enter the coustomer name: ").strip()
          if  not Nam:
               print("input cant't be emapty...........!")
               continue
          print("******TOTAL_BILL******")
          print("=========================")
          if nam  == coustomer_data["name"]:
               print("Coustomer Name:",coustomer_data["name"])
               print("Table Number:",coustomer_data["table_number"])
               print("Seats Number:",coustomer_data["seats_number"])
               print("\nYour Ordered Items:")
               if ordered_items:
                   for item in ordered_items:
                       print(item, indent=2)
                       print("-" * 40)
                       print(f"Total Bill Amount : {total}")
                       print("thank you for ordering! ")
                       print("=========================")
                       pass
               else:
                    print("No items ordered.")
                    print("=========================") 
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
    