def input_password():
  while  True: 
    special_char_found = False 
    special_char=["!","@","#","%","$"]
    user_password=input("enter your password: ")
    for char in special_char:
        if char in user_password :
            special_char_found = True
            pass
            return user_password
      
            
    if len(user_password)<8 and len(user_password)<20:
        print("Enter the input more then eigh....! " )
        continue
    
    elif user_password.isalpha():
        print("only alphabet not allow  in password....")
        continue
    elif user_password.startswith("0"):
        print("the first word can't be the zero, 0........!")
        continue
    elif user_password.isdigit():
        print("only digit not allow.....!")
        continue
    
    elif not special_char_found: 
        print("password must have a special character")
        continue
    else:
        print("Enter the valid input...!")
        continue



