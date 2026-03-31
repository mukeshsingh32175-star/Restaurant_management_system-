import json
from datetime import datetime
from APP.AUTH.valid_name import input_name
from APP.AUTH import data_modes
cousmor_booking_data=[]

def write_data():
    with open (r"APP\DATABASE\boking_data.json","w") as file:
     json_data=json.dumps(cousmor_booking_data) 
     file.write(json_data)
  
def read_data():
  with open (r"APP\DATABASE\boking_data.json","r") as file :
    data=json.loads(file)
    file.read(data)
 

def user_input():
  total_seat = 50  
  while True:
      try:
            User_staff = input("Enter the number of seats you want to book: ").strip()
            if not User_staff:
                print("Input can't be empty....!")
                continue
            
            if not User_staff.isdigit():
                print("Alphabet is not allowed...!")
                continue
            
            if User_staff.startswith("0"):
                print("Input can't be 0 or start with zero...!")
                continue
       
        
            booked = int(User_staff)      
    
        
            if booked > total_seat:
                print(f"........! Only {total_seat} seats left. ")
                continue
            if user_table == 1 and User_staff > 5:
                print("Per table have only 5 seat,tou have to book extra tbale.......!   ")
                continue                    
        
            else:
            
                total_seat -= booked            
                print(f"Seats booked successfully!")
                print(f"   Remaining seats: {total_seat}")
                print("=================================")
                return User_staff
                break  
      except Exception as error:
            print( error) 
            data_modes.erroer_write(error_message=str(error))
            continue      



def user_time():
    while True:
       try:
            seat_hour = input("How many hours do you want to reserve the table: ").strip()
            if not seat_hour:
                print("Input can't be empty!")
                continue
    
            elif seat_hour.isalpha():
                print("Input can't be alphabet...!")
                continue
    
            if not seat_hour.isdigit():
                print("Only numbers allowed...!")
                continue
    
    
            if seat_hour.startswith("0"):
                print("Input can't start with 0...!")
                continue
    
    
            hour = int(seat_hour)
    
            if hour < 1 or hour > 2:
                print("Invalid input. Please enter a valid number of hours (1 or 2).")
                continue
            elif hour == 1:
                one_hour()
                break
            elif hour == 2:
                two_hour()
                break
            else:
                print("Invalid input. Please enter a valid number of hours (1 / 2).")
                continue
            return seat_hour,"hr"
       except Exception as error:
            print( error)
            data_modes.erroer_write(error_message=str(error))
            continue
     
                
def data_vew():
    while True:
        try:
        
            print("*******8BOOKING_DATA******") 
            print("=============================")
            print("1.SEARCH BOOKING ")
            print("2. VIEW ALL BOOKING ")
            print("3.EXIT")
            staf_input=input("Enter your choice: ").strip()
            print("===============================")
            if staff_input == chr:
                print("Char not allow in input....!")
                continue
            staff_input = int(staf_input)
            if staff_input == 1:
                user_name=input("Enter the custmor name:  ")
                for booking in cousmor_booking_data:
                    if booking["name"] == user_name:
                        print("*****Booking found****")
                        print("======================")
                        print(Booking,indent=2)
                        print("==================")
                        break
                    else:
                        print("****Booking_not_found****")
                        continue
                
            elif staff_input == 2:
                print("***All booking data*****")
                print("=====================")
                print(cousmor_booking_data) 
                print("=========================")
                break          
            elif staff_input == 3:
                print("Exitting..!")
                break
            else:
                print("Invalid input...!")
                continue
        except Exception as error:
            print( error)
            data_modes.erroer_write(error_message=str(error))
            continue    
                               
def one_hour():
    while True:
        try:
            print("<<ONE HOUR BOOKING TIMINGS.>>")
            print("=================================")
            print("1. 7:00 AM - 8:00 AM")
            print("2. 8:00 AM - 9:00 AM")
            print("3. 9:00 AM - 10:00 AM")
            print("4. 10:00 AM - 11:00 AM")
            print("5. 11:00 AM - 12:00 PM")
            print("6. 12:00 PM - 1:00 PM")
            print("7. 1:00 PM - 2:00 PM")
            print("8. 2:00 PM - 3:00 PM")
            print("9. 3:00 PM - 4:00 PM")
            print("10. 4:00 PM - 5:00 PM")
            print("11. 5:00 PM - 6:00 PM")
            print("12. 6:00 PM - 7:00 PM")
            print("13. 7:00 PM - 8:00 PM")
            print("14. 8:00 PM - 9:00 PM")
            print("=================================")
            one=input("Enter your choice (1-14): ")
    
            if not one.isdigit():
                print("input can't be alphabet....!")
                continue
            elif not one:
                print("input can't be emapty....!")
                continue
            elif one.startswith("0"):
                print("input can't start with 0....!")
                continue
            one_value =int(one)
            if one_value == 1:
                print("****Booking timing  7:00 AM - 8:00 AM****")
                print("-----------BOOKING CONFIRMED!---------")
                print("=====================================")
                break
            elif one_value == 2:
                print("****Booking timing  8:00 AM - 9:00 AM****")
                print("-----------BOOKING CONFIRMED!---------")
                print("=====================================")
                break
            elif one_value  == 3:
                print("****Booking timing  9:00 AM - 10:00 AM****")
                print("-----------BOOKING CONFIRMED!---------")
                print("=====================================")
                break
            elif one_value == 4:
                print("****Booking timing  10:00 AM - 11:00 AM****")
                print("-----------BOOKING CONFIRMED!---------")
                print("=====================================")
                break
        
            elif one_value == 6:
                print("")
                print("****Booking timing  12:00 PM - 1:00 PM****")
                print("-----------BOOKING CONFIRMED!---------")
                print("=====================================")
                break
            elif one_value == 7:
                print("****Booking timing  1:00 PM - 2:00 PM****")
                print("-----------BOOKING CONFIRMED!---------")
                print("=====================================")
                break
            elif one_value == 8:
                print("****Booking timing  2:00 PM - 3:00 PM****")
                print("-----------BOOKING CONFIRMED!---------")
                print("=====================================")
                break
            elif one_value == 9:
                print("****Booking timing  3:00 PM - 4:00 PM****")
                print("-----------BOOKING CONFIRMED!---------")
                print("=====================================")
                break
            elif one_value == 10:
                print("****Booking timing  4:00 PM - 5:00 PM****")
                print("-----------BOOKING CONFIRMED!---------")
                print("=====================================")
                break
        
            elif one_value == 11:
                print("****Booking timing  5:00 PM - 6:00 PM****")
                print("-----------BOOKING CONFIRMED!---------")
                print("=====================================")
                break 
            elif one_value == 12:
                print("****Booking timing  6:00 PM - 7:00 PM****")
                print("-----------BOOKING CONFIRMED!---------")
                print("=====================================")
                break  
            elif one_value == 13:
                print("****Booking timing  7:00 PM - 8:00 PM****")
                print("-----------BOOKING CONFIRMED!---------")
                print("=====================================")
                break
            elif one_value == 14:
                print("****Booking timing  8:00 PM - 9:00 PM****")
                print("-----------BOOKING CONFIRMED!---------")
                print("=====================================")
                break
            else:
                print("Invalid input....!,After - 9:00 PM booking is not allowed...!")
                print("resturant is closing time...!")
                continue
        except Exception as error:
            print( error)
            data_modes.erroer_write(error_message=str(error))
            continue    
                
def two_hour(): 
    while True:
        try:
            print("<<TWO HOUR BOOKING TIMINGS.>>")
            print("=================================")
            print("1. 7:00 AM - 9:00 AM")
            print("2. 9:00 AM - 11:00 AM")
            print("3. 11:00 AM - 1:00 PM")
            print("4. 1:00 PM - 3:00 PM")
            print("5. 3:00 PM - 5:00 PM")
            print("6. 5:00 PM - 7:00 PM")
            print("7. 7:00 PM - 9:00 PM")
            print("=================================")
            two=input("Enter your choice (1-7): ")
    
            if not two.isdigit():
                print("input can't be alphabet....!")
                continue
            elif not two:
                print("input can't be emapty....!")
                continue
            elif two.startswith("0"):
                print("input can't start with 0....!")
                continue
            two_value =int(two)
        
            if two_value == 1:
                print("****Booking timing  7:00 AM - 9:00 AM****")
                print("-----------BOOKING CONFIRMED!---------")
                print("=====================================")
                break
            elif two_value == 2:
                print("****Booking timing  9:00 AM - 11:00 AM****")
                print("-----------BOOKING CONFIRMED!---------")
                print("=====================================")
                break
            elif two_value == 3:
                print("****Booking timing  11:00 AM - 1:00 PM****")
                print("-----------BOOKING CONFIRMED!---------")
                print("=====================================")
                break
            elif two_value == 4:
                print("****Booking timing   1:00 PM - 3:00 PM****")
                print("-----------BOOKING CONFIRMED!---------")
                print("=====================================")
                break
        
            elif two_value == 5:
                print("")
                print("****Booking timing   3:00 PM - 5:00 PM****")
                print("-----------BOOKING CONFIRMED!---------")
                print("=====================================")
                break
            elif two_value == 6:
                print("****Booking timing   5:00 PM - 7:00 PM****")
                print("-----------BOOKING CONFIRMED!---------")
                print("=====================================")
                break
            elif two_value == 7:
                print("****Booking timing   7:00 PM - 9:00 PM****")
                print("-----------BOOKING CONFIRMED!---------")
                print("=====================================")
                break
            else:
                print("Invalid input....!,After - 9:00 PM booking is not allowed...!")
                print("resturant is closing time...!")
                continue
        except Exception as error:
            print( error)
            data_modes.erroer_write(error_message=str(error))
            continue    

user_table=0        
def booking_table():
    total_table = 10
    while True:
        try:    
        
            user_table = input("Enter the number of tables you want to book: ").strip()
        
            if not user_table:
                print("Input can't be empty....!")
                continue
            
            elif not user_table.isdigit():
                print("Alphabet is not allowed...!")
                continue
            
            elif user_table.startswith("0"):
                print("Input can't be 0 or start with zero...!")
                continue
            # if user_staff > 5 and user_table == 1 :
            #     print("1 table have only ")
        
        
            booked = int(user_table)           
            if booked > total_table:
                print(f"........!only {total_table} tables left....!")
                continue
        
            else:
            
                total_table -= booked            
                print(f"Tables booked successfully!")
                print(f"   Remaining tables: {total_table}")
                print("=================================")
                return user_table
            
        except Exception as error:
            print( error)
            data_modes.erroer_write(error_message=str(error))
            continue
         
def custmor_seats():
  print("........<<SEAT_BOOKING>>.......")
  book_data={}
  book_data["name"]=input_name()
  book_data["table "] = booking_table()
  book_data["seats"]= user_input()
  book_data["user_time"] =user_time()
  book_data["date_time"]= (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
  cousmor_booking_data.append(book_data)
  write_data()
  print("*******Seat_booking_scussfully******")
  print("==================================")
        
 