from operator import concat
from cryptography.fernet import Fernet
import os
import time
key = 'z4PH1i1lqp1sxUZmSYc7bNwvF72U3VSNHOn8LpyJ45k='
files = []
#files = os.listdir()
for file in os.listdir():
    if file == "enc.py" or file == "dec.py":
        continue
    if os.path.isfile(file):
        files.append(file)
        
print("The Files That Can be encrypted : \n")
print(files)
file_enc = input("Please Enter a filename from the list : \n")

with open(file_enc, "rb") as file_nd:
    contents = file_nd.read()
contents_enc = Fernet(key).encrypt(contents)
with open(file_enc, "wb") as file_nd:
    file_nd.write(contents_enc)

print("the file " + file_enc + " Has Been Encrypted.. Enjoy Your Coffee.")
time.sleep(2)

