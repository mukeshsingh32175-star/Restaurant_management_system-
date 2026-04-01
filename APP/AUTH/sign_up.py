from APP.AUTH.valid_email import input_email
from APP.AUTH.valid_name import input_name
from APP.AUTH.valid_password import input_password
import json
import uuid
from datetime import datetime 
from  APP.MENU.staff import user_menu
from APP.MENU.admin import admin_manage
from APP.AUTH import data_modes

data=[]

user_data = data_modes.read_json(r"APP\DATABASE\sign_data.json") 
             
data_modes.write_json(r"APP\DATABASE\sign_data.json",user_data)

def user_login(): 
    data =True
    while True:
      try:       
            print("******LOGIN*****")
            print("=====================")
            user_name = input_name()
            user_password = input_password()
            for i in user_data:
                if i["name"]!= user_name or i["password"] != user_password: 
                    data = False
                    continue
                if      i["name"] == user_name  and  i["password"] == user_password and i["role"] == "admin":
                    print("*****LOGIN____SUCCESSFULY****",user_name.title(),"___SIR***")
                    admin_manage()
               
                elif i["role"] == "staff":
                    user_menu()
                    break
            else:       
                print("****USER_NOT_FOUND****")
                continue     
      except Exception as error:
            print( error)
            data_modes.erroer_write(error_message=str(error))
            continue               


def user_sign_up():
   while True: 
        try:   
            print("<<<<<MENU>>>>>")
            print("=============================")
            print("1.LOGIN")
            print("2.SIGN_UP")
            print("3>EXIT...>")
            user_choice=input("enter your choice: ")
            print("==============================")
            if user_choice.startswith('0'):
                print("input can't be start with zero.....!")
                continue
            if not user_choice:
                print("input cant't be emapty....!")
                continue
            if not user_choice.isdigit():
                print("invalid input. plese enter a valid choice....!")
                continue
            choice =int(user_choice)
            if choice == 2:
             print("******SIGN_UP****")
             user_data={}
             user_data["ID"]=(uuid.uuid4().hex[:4])
             user_data["name"]= input_name()
             user_data["email"]= input_email()
             user_data["password"]=input_password()
             user_data["role"]=None
             user_data["sign_up_datetime"]=(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
             data.append(user_data) 
             write_json()
             print("......SIGN_UP_SCUSSFUL.....",)
             print("============================")
             user_menu()
        
            elif choice == 1:
                user_login()
      
         
            elif choice == 3:
                print("EXITING........!") 
                break 
            else:
                print("ENTER_THE_VALID_INPUT....!")  
                continue
        except Exception as error:
            print( error)
            data_modes.erroer_write(error_message=str(error))
            continue
