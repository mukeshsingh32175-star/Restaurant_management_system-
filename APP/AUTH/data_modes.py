import json
def read_json(path):
    with open (path,"r") as file:
       save_data= json.loads(file.read())
       return save_data
  
 
def write_json(path,data):
    with open (path,"w") as file:
       data= json.dumps(data,indent=2)
       file.write(data) 
       
def  erroer_write(error_message):
    with open (r"APP\LOGS\error_data.txt","w") as file:
        file.write(error_message)