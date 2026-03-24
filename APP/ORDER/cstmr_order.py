from APP.AUTH.valid_name import input_name

def vlaid_table():
    while True:
        table_number =input("enter the table number :  ").strip()
        if not table_number:
            print("input cant't be emapty....!")
            continue
        elif not table_number.isdigit():
            print("invalid input. please enter a valid table number.")
            continue
        elif table_number.startswith('0'):
            print("input can't be start with zero.....!")
            continue
        else:
            return table_number

def customer():
    while True:
        
        print("******ORDER_MENU******")
        print("=========================")
        coustomer_data={}
        coustomer_data["name"]=input_name()
        coustomer_data["table_number"]=vlaid_table(),
        coustomer_data["seats_number"]= None
     
        
      