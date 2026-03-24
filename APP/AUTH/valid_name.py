def input_name():
    while True: 
        user_name=input("ENTER YOUR NAME: ") .strip()
        if len(user_name)< 2:
            print("short_name_not_allow......!")
            continue 
        elif not  user_name :
            print("space not allow ")  
            continue
        elif user_name.isdigit():
             print("NAME_CONTAIN_ONLY_ALPHABET ")
             continue
         
        return user_name
    




 


        
        
 
# total_seat=25       

# def user_input():
#     while True:
       
#        User_staff=input("Enter the nuber of seat you want to book: ")
      
#        if not User_staff:
#          print("input can't be empty....!")
#          continue
#        elif  not User_staff.isdigit():
#             print("alphabet is not allow...!")
#             continue
#        elif User_staff.startwith("0"):
#             print("input can't be  0...!")           
#             continue
        
#        change=int(User_staff)
#        total_seat -= User_staff
       
#        if User_staff > total_seat:
#            print("........!")
#     else:
#             print("enter the valid input......!")
#             continue
             
total_seat = 25   # Available seats (this will decrease when you book)

def user_input():
    global total_seat   # This allows us to modify total_seat inside the function
    
    while True:
        # Get input from user
        User_staff = input("Enter the number of seats you want to book: ").strip()
        
        # Validation checks
        if not User_staff:
            print("Input can't be empty....!")
            continue
            
        elif not User_staff.isdigit():
            print("Alphabet is not allowed...!")
            continue
            
        elif User_staff.startswith("0"):
            print("Input can't be 0 or start with zero...!")
            continue
        
        # If all checks passed → convert to integer
        booked = int(User_staff)          # renamed for clarity (was 'change')
        
        # Now check if enough seats are available
        if booked > total_seat:
            print(f"........! Only {total_seat} seats left. Please book fewer seats.")
            continue                     # ask again
        
        else:
            # Book the seats
            total_seat -= booked             # Correct subtraction (this is what you wanted)
            print(f"**********Seats booked successfully*********!")
            print(f"   Remaining seats: {total_seat}")
            return User_staff
            break                        # exit loop after successful booking


# Run the function
