from db_connect import get_signatures
import scanner
from engine import hash 
file_path =input("Enter the file path :- ").strip()
signature = get_signatures()
ha = hash(file_path)
sc = scanner.scan_file(file_path,signature)
print(sc)