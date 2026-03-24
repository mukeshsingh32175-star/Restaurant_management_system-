from APP.AUTH.valid_email import input_email
from APP.AUTH.valid_name import input_name
from APP.AUTH.valid_password import input_password
import json
import uuid
from datetime import datetime 
from  APP.MENU.staff import user_menu
from APP.MENU.admin import admin_manage


def read_json():
    with open (r"APP\DATABASE\sign_data.json","r") as file:
       save_data= json.loads(file.read())
       return save_data
  
user_data = read_json()
 
def write_json():
    with open (r"APP\DATABASE\sign_data.json","w") as file:
       data= json.dumps(user_data)
       file.write(data) 
             

def user_login():
    while True:
        print("******LOGIN*****")
        print("=====================")
        user_name = input_name()
        user_password = input_password()
        for i in user_data:
            if  i["name"] == user_name and  i["password"] == user_password and i["role"] == "admin":
                print("*****LOGIN_SCUSSFUL****",user_name.title())
                admin_manage()
                break
            elif i["role"] == "staff":
                user_menu()
                break
            else:       
                print("****USER_NOT_FOUND****")
                continue                





def user_sign_up():
   while True: 
       
    
    print("<<<<<MENU>>>>>")
    print("=============================")
    print("1.LOGIN")
    print("2.SIGN_UP")
    print("3>EXIT...>")
    user_choice=input("enter your choice: ")
    print("==============================")
    
    
    if user_choice == "2":
        print("******SIGN_UP****")
        Data={}
        Data["ID"]=(uuid.uuid4().hex[:4])
        Data["name"]= input_name()
        Data["email"]= input_email()
        Data["password"]=input_password()
        Data["role"]=None
        Data["datetime"]=(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        user_data.append(Data) 
        write_json()
        print("......SIGN_UP_SCUSSFUL.....",)
        print("============================")
        user_menu()
        
    elif user_choice == '1':
        user_login()
      
         
    elif user_choice == '3':
        print("EXITING........!") 
        break 
    else:
        print("ENTER_THE_VALID_INPUT....!")  
        continue


           
            
        
        
