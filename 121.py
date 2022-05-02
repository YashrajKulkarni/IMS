import tkinter as tk
import tkinter.font as font
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
import os
from multiprocessing import Process

mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  password="yashraj1",
	  database="IMS"
	)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM employee_data")
myresult = mycursor.fetchall()

a="yashrajkulkarni2001@gmail.com"
for abc in myresult:
	if a==abc[0]:
		profile_display_data=abc


#Functions
def clear_frame():

	for widgets in main_frame.winfo_children():
		widgets.destroy()



def but():
	clear_frame()
	left = Label(main_frame, text="\nbutton1 clicked yash wadndandakndaakndandadnad",bg="#CCE4CA")
	left.pack()
def but1():
	clear_frame()
	left = Label(main_frame, text="\nbutton 2 has been clicked by user",bg="#CCE4CA")
	left.pack()
def but3():
	clear_frame()

	'''
	main_frame.rowconfigure(0,weight=2)
	main_frame.rowconfigure(1,weight=9)
	main_frame.rowconfigure(2, weight=0)
	main_frame.rowconfigure(3, weight=0)
	main_frame.rowconfigure(4, weight=0)
	main_frame.rowconfigure(5, weight=0)
	main_frame.rowconfigure(6, weight=0)
	main_frame.rowconfigure(7, weight=0)
	main_frame.rowconfigure(8, weight=0)
	main_frame.rowconfigure(9, weight=0)
	main_frame.rowconfigure(10, weight=0)
	main_frame.rowconfigure(11, weight=0)
	main_frame.rowconfigure(12, weight=0)
	main_frame.rowconfigure(13, weight=0)
	main_frame.rowconfigure(14, weight=0)
	main_frame.rowconfigure(15, weight=0)
	main_frame.rowconfigure(16, weight=0)
	main_frame.rowconfigure(17, weight=0)
	main_frame.rowconfigure(18, weight=0)
	main_frame.rowconfigure(19, weight=0)
	main_frame.rowconfigure(20, weight=0)
	main_frame.rowconfigure(21, weight=0)
	main_frame.rowconfigure(22, weight=0)
	main_frame.rowconfigure(23, weight=0)
	main_frame.rowconfigure(24, weight=0)
	main_frame.rowconfigure(25, weight=0)
	main_frame.rowconfigure(26, weight=0)
	main_frame.rowconfigure(27, weight=0)
	main_frame.rowconfigure(28, weight=0)


	main_frame.columnconfigure(0,weight=1)
	main_frame.columnconfigure(1,weight=0)
	main_frame.columnconfigure(2,weight=0)
	main_frame.columnconfigure(3,weight=0)
	main_frame.columnconfigure(4,weight=0)
	main_frame.columnconfigure(5,weight=0)
	main_frame.columnconfigure(6,weight=0)
	main_frame.columnconfigure(7,weight=0)

	upper_frame=Frame(main_frame,bg="RED")
	lower_frame=Frame(main_frame,bg="BLACK")

	upper_frame.grid(row=0,column=0,sticky="nsew")
	lower_frame.grid(row=1,column=0,sticky="nsew")
	'''


	canvas = Canvas(main_frame,bg='RED')
	canvas.pack(side=LEFT,expand=YES, fill=BOTH)

	scroll_y = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
	scroll_y.pack(fill=Y,side=RIGHT)

	canvas.configure(yscrollcommand=scroll_y.set)


	s_frame=tk.Frame(canvas,bg="BLACK",padx=10)
	s_frame.pack(side=LEFT,expand=YES, fill=X)
	s_frame.grid_columnconfigure(0,weight=1)
	s_frame.grid_columnconfigure(1,weight=1)
	s_frame.grid_columnconfigure(2,weight=1)
	canvas.create_window((50,50),window=s_frame, anchor="nw")
	for thing in range(100):
		tk.Button(s_frame,text=f"Button {thing}").grid(row=thing,column=1)
	for thing in range(100):
		tk.Button(s_frame,text=f"Button {thing}").grid(row=thing,column=1)
	canvas.bind('<Configure>',lambda e:canvas.configure(scrollregion=s_frame.bbox("all")))

def but2():
	'''def func1():
		os.system('python c.py')
	def func2():
		root.destroy()
	p1 = Process(target = func1)
	p1.start()
	p2 = Process(target = func2)
	p2.start()'''
	root.destroy()
	os.system('python c.py')

def top():
	clear_frame()
	abc="""Life Insurance
	Motor insurance
	Health insurance
	Travel insurance
	Property insurance
	Mobile insurance
	Cycle insurance
	Bite-size insurance"""
	left = Label(main_frame, text="\n"+abc,bg="#CCE4CA")
	left.pack()
def cal():
	clear_frame()
	abc="""Every insurance premium calculator is based on a pre-built
	algorithm defined for various parameters, such as the buyer's age, nkjkjlkjjljljkjljljljljljljljljljljlkjljljljklkkljljljljlk
	type of policy selected, the policy period, and riders.
	While using our online insurance premium calculator, you are asked
	to enter the value of these parameters. Accordingly, it will display
	an estimated quote of premium payable under the plan.
	Disclaimer: - In some cases, the premium shown upfront may change basis
	underwriting decision."""
	left = Label(main_frame, text="\n"+abc,bg="#CCE4CA")
	left.pack()
def con():
	clear_frame()
	abc="You can email darshansalvi26@gmail.com for quiers or call '9892349202'"
	left = Label(main_frame, text="\n"+abc,bg="#CCE4CA")
	left.pack()
def abo():
	clear_frame()
	abc="""This desktop application created by yash and darshan for Insurance management system111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.
	Thank You"""
	left = Label(main_frame, text="\n"+abc,bg="#CCE4CA")
	left.pack()
def Head_employee_data():
	clear_frame()
	def emails_availble_mysql():
		mycursor.execute("SELECT email_id FROM login_page where A_or_N = 'N' ")
		return mycursor.fetchall()
	def departments_mysql():
		mycursor.execute("SELECT DISTINCT department FROM employee_data")
		return mycursor.fetchall()
	##################################
	#Variables
	##################################

	add_employee_email= StringVar()
	add_employee_name= StringVar()
	add_employee_phone_no=StringVar()
	add_employee_aadhar=StringVar()
	add_employee_address= StringVar()
	add_employee_pan= StringVar()
	add_employee_dob= StringVar()
	add_employee_basic=StringVar()
	add_employee_department= StringVar()
	add_employee_bank_name= StringVar()
	add_employee_ac_no=StringVar()
	add_employee_ifsc= StringVar()



	##################################
	#Configure row and column
	##################################

	main_frame.rowconfigure(0, weight=2)
	main_frame.rowconfigure(1, weight=2)
	main_frame.rowconfigure(2, weight=2)
	main_frame.rowconfigure(3, weight=2)
	main_frame.rowconfigure(4, weight=2)
	main_frame.rowconfigure(5, weight=2)
	main_frame.rowconfigure(6, weight=2)
	main_frame.rowconfigure(7, weight=2)
	main_frame.rowconfigure(8, weight=2)
	main_frame.rowconfigure(9, weight=2)
	main_frame.rowconfigure(10, weight=2)
	main_frame.rowconfigure(11, weight=2)
	main_frame.rowconfigure(12, weight=2)
	main_frame.rowconfigure(13, weight=2)
	main_frame.rowconfigure(14, weight=2)
	main_frame.rowconfigure(15, weight=2)
	main_frame.rowconfigure(16, weight=2)
	main_frame.rowconfigure(17, weight=2)
	main_frame.rowconfigure(18, weight=2)
	main_frame.rowconfigure(19, weight=2)
	main_frame.rowconfigure(20, weight=2)
	main_frame.rowconfigure(21, weight=2)
	main_frame.rowconfigure(22, weight=2)
	main_frame.rowconfigure(23, weight=2)
	main_frame.rowconfigure(24, weight=2)
	main_frame.rowconfigure(25, weight=2)
	main_frame.rowconfigure(26, weight=2)
	main_frame.rowconfigure(27, weight=2)
	main_frame.rowconfigure(28, weight=2)


	main_frame.columnconfigure(0, weight=1)
	main_frame.columnconfigure(1, weight=0)
	main_frame.columnconfigure(2, weight=4)
	main_frame.columnconfigure(3, weight=4)
	main_frame.columnconfigure(4, weight=1)
	main_frame.columnconfigure(5, weight=1)



	##################################
	# 1 Create label for text
	##################################

	add_employee_PD_label = tk.Label(main_frame, text = 'Personal Details', font=('calibre',17, 'bold'))
	add_employee_Email_label = tk.Label(main_frame, text = 'Choose Email Id to Assign :', font=('calibre',10, 'bold'))
	add_employee_name_label = tk.Label(main_frame, text = 'Name :', font=('calibre',10, 'bold'))
	add_employee_phone_label = tk.Label(main_frame, text = 'Phone No: :', font=('calibre',10, 'bold'))
	add_employee_address_label = tk.Label(main_frame, text = 'Address :', font=('calibre',10, 'bold'))
	add_employee_aadhar_label = tk.Label(main_frame, text = 'Aadhar No :', font=('calibre',10, 'bold'))
	add_employee_pan_label = tk.Label(main_frame, text = 'PAN :', font=('calibre',10, 'bold'))
	add_employee_dob_label = tk.Label(main_frame, text = 'Date of Birth :', font=('calibre',10, 'bold'))

	add_employee_ORD_label = tk.Label(main_frame, text = 'Office Related Details', font=('calibre',17, 'bold'))
	add_employee_basic_label = tk.Label(main_frame, text = 'Basic Pay :', font=('calibre',10, 'bold'))
	add_employee_department_label = tk.Label(main_frame, text = 'Department :', font=('calibre',10, 'bold'))

	add_employee_BD_label = tk.Label(main_frame, text = 'Bank Details', font=('calibre',17, 'bold'))
	add_employee_bank_name_label = tk.Label(main_frame, text = 'Bank Name :', font=('calibre',10, 'bold'))
	add_employee_ac_no_label = tk.Label(main_frame, text = 'Ac/No :', font=('calibre',10, 'bold'))
	add_employee_ifsc_label = tk.Label(main_frame, text = 'IFSC :', font=('calibre',10, 'bold'))



	##################################
	# 2 Create entries
	##################################
	emails_availble=emails_availble_mysql()
	departments=departments_mysql()
	add_employee_Email_entries = OptionMenu( main_frame , add_employee_email , *emails_availble )
	add_employee_name_entries = tk.Entry(main_frame,textvariable = add_employee_name, font=('calibre',10,'normal'))
	add_employee_phone_entries = tk.Entry(main_frame,textvariable = add_employee_phone_no, font=('calibre',10,'normal'))
	add_employee_address_entries = tk.Entry(main_frame,textvariable = add_employee_address, font=('calibre',10,'normal'))
	add_employee_aadhar_entries = tk.Entry(main_frame,textvariable = add_employee_aadhar, font=('calibre',10,'normal'))
	add_employee_pan_entries = tk.Entry(main_frame,textvariable = add_employee_pan, font=('calibre',10,'normal'))
	add_employee_dob_entries =tk.Entry(main_frame,textvariable = add_employee_dob, font=('calibre',10,'normal'))

	add_employee_basic_entries = tk.Entry(main_frame,textvariable = add_employee_basic, font=('calibre',10,'normal'))
	add_employee_department_entries = OptionMenu( main_frame ,add_employee_department , *departments )

	add_employee_bank_name_entries = tk.Entry(main_frame,textvariable = add_employee_bank_name, font=('calibre',10,'normal'))
	add_employee_ac_no_entries = tk.Entry(main_frame,textvariable = add_employee_ac_no, font=('calibre',10,'normal'))
	add_employee_ifsc_entries = tk.Entry(main_frame,textvariable = add_employee_ifsc, font=('calibre',10,'normal'))



	##################################
	# 3 Grid label for text
	##################################

	add_employee_PD_label.grid(row=3,column=2,columnspan=2,sticky="nsew")
	add_employee_Email_label.grid(row=5,column=2,sticky="nsew")
	add_employee_name_label.grid(row=6,column=2,sticky="nsew")
	add_employee_phone_label.grid(row=7,column=2,sticky="nsew")
	add_employee_address_label.grid(row=8,column=2,sticky="nsew")
	add_employee_aadhar_label.grid(row=9,column=2,sticky="nsew")
	add_employee_pan_label.grid(row=10,column=2,sticky="nsew")
	add_employee_dob_label.grid(row=11,column=2,sticky="nsew")

	add_employee_ORD_label.grid(row=14,column=2,columnspan=2,sticky="nsew")
	add_employee_basic_label.grid(row=15,column=2,sticky="nsew")
	add_employee_department_label.grid(row=16,column=2,sticky="nsew")

	add_employee_BD_label.grid(row=19,column=2,columnspan=2,sticky="nsew")
	add_employee_bank_name_label.grid(row=20,column=2,sticky="nsew")
	add_employee_ac_no_label.grid(row=21,column=2,sticky="nsew")
	add_employee_ifsc_label.grid(row=22,column=2,sticky="nsew")



	##################################
	# 4 Grid label for entries
	##################################

	add_employee_Email_entries.grid(row=5,column=3,sticky="nsew")
	add_employee_name_entries.grid(row=6,column=3,sticky="nsew")
	add_employee_phone_entries.grid(row=7,column=3,sticky="nsew")
	add_employee_address_entries.grid(row=8,column=3,sticky="nsew")
	add_employee_aadhar_entries.grid(row=9,column=3,sticky="nsew")
	add_employee_pan_entries.grid(row=10,column=3,sticky="nsew")
	add_employee_dob_entries.grid(row=11,column=3,sticky="nsew")

	add_employee_basic_entries.grid(row=15,column=3,sticky="nsew")
	add_employee_department_entries.grid(row=16,column=3,sticky="nsew")


	add_employee_bank_name_entries.grid(row=20,column=3,sticky="nsew")
	add_employee_ac_no_entries.grid(row=21,column=3,sticky="nsew")
	add_employee_ifsc_entries.grid(row=22,column=3,sticky="nsew")
def profile_display():
	clear_frame()

	main_frame.rowconfigure(0, weight=2)
	main_frame.rowconfigure(1, weight=2)
	main_frame.rowconfigure(2, weight=2)
	main_frame.rowconfigure(3, weight=2)
	main_frame.rowconfigure(4, weight=2)
	main_frame.rowconfigure(5, weight=2)
	main_frame.rowconfigure(6, weight=2)
	main_frame.rowconfigure(7, weight=2)
	main_frame.rowconfigure(8, weight=2)
	main_frame.rowconfigure(9, weight=2)
	main_frame.rowconfigure(10, weight=2)
	main_frame.rowconfigure(11, weight=2)
	main_frame.rowconfigure(12, weight=2)
	main_frame.rowconfigure(13, weight=2)
	main_frame.rowconfigure(14, weight=2)
	main_frame.rowconfigure(15, weight=2)
	main_frame.rowconfigure(16, weight=2)
	main_frame.rowconfigure(17, weight=2)
	main_frame.rowconfigure(18, weight=2)
	main_frame.rowconfigure(19, weight=2)
	main_frame.rowconfigure(20, weight=2)
	main_frame.rowconfigure(21, weight=2)
	main_frame.rowconfigure(22, weight=2)
	main_frame.rowconfigure(23, weight=2)
	main_frame.rowconfigure(24, weight=2)
	main_frame.rowconfigure(25, weight=2)
	main_frame.rowconfigure(26, weight=2)
	main_frame.rowconfigure(27, weight=2)
	main_frame.rowconfigure(28, weight=2)




	main_frame.columnconfigure(0, weight=3)
	main_frame.columnconfigure(1, weight=2)
	main_frame.columnconfigure(2, weight=2)
	main_frame.columnconfigure(3, weight=2)
	main_frame.columnconfigure(4, weight=2)
	main_frame.columnconfigure(5, weight=3)



	##################################

	profile_PD_label = tk.Label(main_frame, text = 'Personal Details', font=('calibre',17, 'bold'))
	profile_name_label = tk.Label(main_frame, text = 'Name :', font=('calibre',10, 'bold'))
	profile_employee_id_label = tk.Label(main_frame, text = 'Employee ID :', font=('calibre',10, 'bold'))
	profile_email_id_label = tk.Label(main_frame, text = 'Email ID :', font=('calibre',10, 'bold'))
	profile_address_label = tk.Label(main_frame, text = 'Address :', font=('calibre',10, 'bold'))
	profile_phone_label = tk.Label(main_frame, text = 'Phone No :', font=('calibre',10, 'bold'))
	profile_aadhar_label = tk.Label(main_frame, text = 'Aadhar No :', font=('calibre',10, 'bold'))
	profile_pan_label = tk.Label(main_frame, text = 'PAN :', font=('calibre',10, 'bold'))
	profile_dob_label = tk.Label(main_frame, text = 'Date of Birth :', font=('calibre',10, 'bold'))


	profile_ORD_label = tk.Label(main_frame, text = 'Office Related Details', font=('calibre',17, 'bold'))
	profile_basic_label = tk.Label(main_frame, text = 'Basic Pay :', font=('calibre',10, 'bold'))
	profile_working_days_label = tk.Label(main_frame, text = 'Working Day/Week :', font=('calibre',10, 'bold'))
	profile_department_label = tk.Label(main_frame, text = 'Department :', font=('calibre',10, 'bold'))
	profile_report_to_label = tk.Label(main_frame, text = 'Employee ID of Head:', font=('calibre',10, 'bold'))



	profile_BD_label = tk.Label(main_frame, text = 'Bank Details', font=('calibre',17, 'bold'))
	profile_bank_name_label = tk.Label(main_frame, text = 'Bank Name :', font=('calibre',10, 'bold'))
	profile_ac_no_label = tk.Label(main_frame, text = 'Ac/No :', font=('calibre',10, 'bold'))
	profile_ifsc_label = tk.Label(main_frame, text = 'IFSC :', font=('calibre',10, 'bold'))


	#################################


	profile_name_data_label = tk.Label(main_frame, text =profile_display_data[14], font=('calibre',10))
	profile_employee_id_data_label = tk.Label(main_frame, text =profile_display_data[1], font=('calibre',10))
	profile_email_id_data_label = tk.Label(main_frame, text =profile_display_data[0], font=('calibre',10))
	profile_address_data_label = tk.Label(main_frame, text = profile_display_data[2], font=('calibre',10))
	profile_phone_data_label = tk.Label(main_frame, text =profile_display_data[3], font=('calibre',10))
	profile_aadhar_data_label = tk.Label(main_frame, text =profile_display_data[4], font=('calibre',10))
	profile_pan_data_label = tk.Label(main_frame, text =profile_display_data[5], font=('calibre',10))
	profile_dob_data_label = tk.Label(main_frame, text = profile_display_data[6], font=('calibre',10))


	profile_basic_data_label = tk.Label(main_frame, text = "₹"+str(profile_display_data[7])+"/-", font=('calibre',10))
	profile_working_days_data_label = tk.Label(main_frame, text = profile_display_data[11], font=('calibre',10))
	profile_department_data_label = tk.Label(main_frame, text =profile_display_data[12], font=('calibre',10))
	profile_report_to_data_label = tk.Label(main_frame, text =profile_display_data[13], font=('calibre',10))



	profile_bank_name_data_label = tk.Label(main_frame, text = profile_display_data[8], font=('calibre',10))
	profile_ac_no_data_label = tk.Label(main_frame, text =profile_display_data[9], font=('calibre',10))
	profile_ifsc_data_label = tk.Label(main_frame, text =profile_display_data[10], font=('calibre',10))



	profile_PD_label.grid(row=3,column=2,columnspan=2,sticky="nsew")
	profile_name_label.grid(row=5,column=2,sticky="nsew")
	profile_employee_id_label.grid(row=6,column=2,sticky="nsew")
	profile_email_id_label.grid(row=7,column=2,sticky="nsew")
	profile_address_label.grid(row=8,column=2,sticky="nsew")
	profile_phone_label.grid(row=9,column=2,sticky="nsew")
	profile_aadhar_label.grid(row=10,column=2,sticky="nsew")
	profile_pan_label.grid(row=11,column=2,sticky="nsew")
	profile_dob_label.grid(row=12,column=2,sticky="nsew")


	profile_ORD_label.grid(row=15,column=2,columnspan=2,sticky="nsew")
	profile_basic_label.grid(row=17,column=2,sticky="nsew")
	profile_working_days_label.grid(row=18,column=2,sticky="nsew")
	profile_department_label.grid(row=19,column=2,sticky="nsew")
	profile_report_to_label.grid(row=20,column=2,sticky="nsew")


	profile_BD_label.grid(row=23,column=2,columnspan=2,sticky="nsew")
	profile_bank_name_label.grid(row=25,column=2,sticky="nsew")
	profile_ac_no_label.grid(row=26,column=2,sticky="nsew")
	profile_ifsc_label.grid(row=27,column=2,sticky="nsew")



	profile_name_data_label.grid(row=5,column=3,sticky="nsew")
	profile_employee_id_data_label.grid(row=6,column=3,sticky="nsew")
	profile_email_id_data_label.grid(row=7,column=3,sticky="nsew")
	profile_address_data_label.grid(row=8,column=3,sticky="nsew")
	profile_phone_data_label.grid(row=9,column=3,sticky="nsew")
	profile_aadhar_data_label.grid(row=10,column=3,sticky="nsew")
	profile_pan_data_label.grid(row=11,column=3,sticky="nsew")
	profile_dob_data_label.grid(row=12,column=3,sticky="nsew")



	profile_basic_data_label.grid(row=17,column=3,sticky="nsew")
	profile_working_days_data_label.grid(row=18,column=3,sticky="nsew")
	profile_department_data_label.grid(row=19,column=3,sticky="nsew")
	profile_report_to_data_label.grid(row=20,column=3,sticky="nsew")



	profile_bank_name_data_label.grid(row=25,column=3,sticky="nsew")
	profile_ac_no_data_label.grid(row=26,column=3,sticky="nsew")
	profile_ifsc_data_label.grid(row=27,column=3,sticky="nsew")


#Main
root = tk.Tk()
root.geometry("1400x800")
root.configure(bg='#3498DB')
root.title("Insurance Management System")

p1 = PhotoImage(file = '1234.png')
# Setting icon of master window
root.iconphoto(False, p1)


top_frame = tk.Frame(root,bd=1, background="#40c9f6", relief="sunken")
left_frame = tk.Frame(root,bd=1, background="#D2E2FB",  relief="sunken")
main_frame = tk.Frame(root,bd=1, background="#CCE4CA",  relief="sunken")

left_frame.grid_columnconfigure(0, weight=2)


top_frame.grid(row=0,column=0, columnspan=2,sticky="nsew",padx=(4,4),pady=(4,2))
left_frame.grid(row=1, column=0, sticky="nsew",padx=(4,2),pady=(2,4))
main_frame.grid(row=1, column=1, rowspan=2, sticky="nsew",padx=(2,4),pady=(2,4))

root.grid_rowconfigure(0, weight=2, uniform="x")
root.grid_rowconfigure(1, weight=9, uniform="x")
root.grid_columnconfigure(0, weight=2, uniform="x")
root.grid_columnconfigure(1, weight=9, uniform="x")

top_frame.rowconfigure(0, weight=2)
top_frame.rowconfigure(1, weight=2)
top_frame.rowconfigure(2, weight=2)
top_frame.rowconfigure(3, weight=2)
top_frame.rowconfigure(4, weight=2)
top_frame.rowconfigure(5, weight=2)

top_frame.columnconfigure(0, weight=0)
top_frame.columnconfigure(1, weight=2)
top_frame.columnconfigure(2, weight=2)
top_frame.columnconfigure(3, weight=2)
top_frame.columnconfigure(4, weight=2)
top_frame.columnconfigure(5, weight=2)
top_frame.columnconfigure(6, weight=2)
top_frame.columnconfigure(7, weight=2)
top_frame.columnconfigure(8, weight=2)
top_frame.columnconfigure(9, weight=2)
top_frame.columnconfigure(10, weight=2)
top_frame.columnconfigure(11, weight=2)
top_frame.columnconfigure(12, weight=2)

my_image = tk.PhotoImage(file = "121.png") # your image
label = Label(top_frame, image = my_image,width=250, height=150,bg="#40c9f8") # put the image on a label
label.grid(row=0,rowspan=6,column=0)

#name_logo = tk.Label(top_frame,bg="#FFF0C1", text = 'IMS', font=('calibre',50, 'bold'))
top=tk.Button(top_frame,borderwidth = 0,bg="#40c9f6", text = 'Type of Policies', font=('Bodoni MT',12, 'bold'),command=top)
cal=tk.Button(top_frame,borderwidth = 0,bg="#40c9f6", text = 'Calculator', font=('Bodoni MT',12, 'bold'),command=cal)
con=tk.Button(top_frame,borderwidth = 0,bg="#40c9f6", text = 'Contact Us', font=('Bodoni MT',12, 'bold'),command=con)
abo=tk.Button(top_frame,borderwidth = 0,bg="#40c9f6", text = 'About Us', font=('Bodoni MT',12, 'bold'),command=abo)

#name_logo.grid(row=0,column=0,columnspan=4,rowspan=6,sticky="w")
top.grid(row=5,column=9,sticky="nsew")
cal.grid(row=5,column=10,sticky="nsew")
con.grid(row=5,column=11,sticky="nsew")
abo.grid(row=5,column=12,sticky="nsew")

buttonFont = font.Font(family='Bodoni MT', size=14)
#buttons
'''
loadimage = tk.PhotoImage(file="but.png")
button1 = Button(left_frame,image=loadimage)
button1["bg"]="WHITE"
button1["border"]="0"'''
button1 = Button(left_frame,height=2, text='PROFILE',font=buttonFont,command=profile_display, activebackground='#00ff00')
button1.grid(row=0,column=0,sticky="nsew")
button2 = Button(left_frame,height=2, text='TOTAL POLICIES',font=buttonFont,command=but1, activebackground='#00ff00')
button2.grid(row=1,column=0,sticky="nsew")
button3 = Button(left_frame,height=2, text='COLLECTION',font=buttonFont,command=but2)
button3.grid(row=2,column=0,sticky="nsew")
button4 = Button(left_frame,height=2, text='CLAIM',font=buttonFont,command=but3)
button4.grid(row=3,column=0,sticky="nsew")
button5 = Button(left_frame,height=2, text='SALARY',font=buttonFont,command=but2)
button5.grid(row=4,column=0,sticky="nsew")
button6 = Button(left_frame,height=2, text="AGENT'S DATA",font=buttonFont,command=but2)
button6.grid(row=5,column=0,sticky="nsew")
button7 = Button(left_frame,height=2, text="EMPLOYEE'S DATA",font=buttonFont,command=Head_employee_data)
button7.grid(row=6,column=0,sticky="nsew")
button3 = Button(left_frame,height=2, text='CHANGE PASSWORD',font=buttonFont,command=but2)
button3.grid(row=7,column=0,sticky="nsew")
button8 = Button(left_frame,height=2, text='LOG OUT',font=buttonFont,command=but2)
button8.grid(row=8,column=0,sticky="nsew")
'''
left_frame.rowconfigure(0, weight=2)
left_frame.rowconfigure(1, weight=2)
left_frame.rowconfigure(2, weight=2)
left_frame.rowconfigure(3, weight=2)
left_frame.rowconfigure(4, weight=2)
left_frame.rowconfigure(5, weight=2)
left_frame.rowconfigure(6, weight=2)
left_frame.rowconfigure(7, weight=2)
left_frame.rowconfigure(8, weight=2)'''
root.mainloop()
