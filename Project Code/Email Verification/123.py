import os
import math
import random
import smtplib

#Create a 6 digit OTP
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp

#Use smtp library
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("insurancemanagementsystem@gmail.com", "ims@1234")
emailid = input("Enter your email: ")
s.sendmail("insurancemanagementsystem@gmail.com",emailid,msg)

#Verify OTP
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")

def my_function(fname):
  print(fname + " Refsnes")
