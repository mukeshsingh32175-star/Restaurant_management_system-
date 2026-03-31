def input_email():   
 while True:
    user=input("enter your email: ").strip()
     
    if "@gmail.com" not  in user:
        print("this is not valid email..")
        continue
    elif len(user)<15:
        print("insert the more char" )
        continue
    elif not user:
       print("only space not allow ")
       continue 
    elif user.isdigit():
        print("only digit not allow ")
        continue
    elif user.isalpha():
        print("only alphabet not allow") 
        continue
    return user  
    




