import hashlib
from db_connect import get_signatures
import scanner
def hash(file_path):
 try :
  md5 = hashlib.md5()
  with open(file_path,'rb') as f :

      chunk = f.read(4096)
      while chunk:
         md5.update(chunk)
         chunk = f.read(4096)
      
      return md5.hexdigest()
 except:
   print("Error in hash converion")
 

if __name__ == "__main__":
    file_path = input("Enter the file path: ").strip()
    signatures = get_signatures()
    result = scanner.scan_file(file_path, signatures)
    print(result)
