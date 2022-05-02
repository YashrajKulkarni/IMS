import mysql.connector
import random

import string
string.ascii_letters

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="yashraj1",
  database="IMS"
)

mycursor = mydb.cursor()

for x in range (101,193,1):
	abc="MEM"+str(x)
	data=str((random.randint(7456235845,9999999999)))
	q="update members_data set phone = '"+data+"' where "+"member_id "+"= '"+abc+"';"
	print(q)
	mycursor.execute(q)


#mycursor.execute("update members_data set pan ='PASFJ7314Y' WHERE member_id = 'MEM101';") 
mydb.commit()