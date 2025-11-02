from db_connect import get_signatures
import scanner
import tkinter as tk
from tkinter import filedialog
#For opeaning a file
file_path = filedialog.askopenfilename(
    initialdir="/",  
    title="Select a file for scan")
signature = get_signatures() # for database signature retriving 
sc = scanner.scan_file(file_path,signature) # for sending the file path and signature to the scanner.py 
print(sc) # for printing the o/p 