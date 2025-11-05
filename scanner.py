from engine import hash
import os
def scan_file(file_path,signature):
  file_name = os.path.basename(file_path)
  try:
    hash_value = hash(file_path) # Sending the file path to the engine 
    if not hash_value : # if hash file is empty or have no hash data then this part runs
      return f"File Not Found: File Name -: {file_name}"
    for sign_type,sign_value in signature : #created 2 new varible signatue type and signature value 
       if sign_type == 'hash' and hash_value == sign_value : #this part runs when the signature and the value of the signature is matched with the database
         return f"!! INFECTED FILE -: The file {file_name} is Infected" #if the signature(MD5 HASH) is matched with he database signature values and type then it runs this part
    with open(file_path, 'r', errors = 'ignore') as f:#use to open a file and read it 
        content = f.read()#reading the file that is selected by the user
        for sign_type , sign_value in signature: #checking the sigature type of the file and match it with the data base if matched then declare the file infected  
                if sign_type == "string" and sign_value in content:#searching in the selected file if 
                   return f'string matched file is infected !! The file {file_name} is Infected'
    return f"{file_name} is safe"
  except Exception as exc:
     return f"Error in scanning {file_path}.{exc}"