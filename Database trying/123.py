#Working to insert data

import mysql.connector
from cryptography.fernet import Fernet

def password_encrypt(p):
	fernet = Fernet(b'suYB0_gEXPV53t_NVqwvMmscCtNNIT2Cghp9npVhLRY=')
	encMessage = fernet.encrypt(p.encode())
	#print("original string: ",p)
	#print("encrypted string: ", encMessage)
	decMessage = fernet.decrypt(encMessage)
	print("decrypted string: ", decMessage)
	decMessage = fernet.decrypt(encMessage).decode()
	print(decMessage)
	return encMessage 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="yashraj1",
  database="IMS"
)

na=input("enter your email")
mycursor = mydb.cursor()
pass_1=input("enter password:")
em=password_encrypt(pass_1)
posi=input("enter your position")
mycursor.execute("INSERT INTO login_page (email_id,login_password,category) VALUES (%s, %s, %s)", (na,em,posi))
mydb.commit()
#a=input("Enter a name:")

'''for x in myresult:
 if a in x:
  print(a,"your Position is",x[2],"and password is",x[1])
  break;
else:
 print(a,"your Data Is Missing")'''

