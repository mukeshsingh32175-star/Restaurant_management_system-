def input_name():
    while True: 
        user_name=input("ENTER YOUR NAME: ") .strip()
        if len(user_name)< 2:
            print("short_name_not_allow......!")
            continue 
        if not  user_name :
            print("space not allow ")  
            continue
        if not user_name.isalpha():
             print("NAME_CONTAIN_ONLY_ALPHABET ")
             continue
        if user_name.startswith("0") :
            print("name can't start with zero.....!")
            continue 
      
        return user_name
    



