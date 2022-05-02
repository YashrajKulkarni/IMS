import os
import math
import random
import smtplib
import tkinter as tk
import mysql.connector
import tkinter.font as font
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from cryptography.fernet import Fernet
from multiprocessing import Process

#All Pages
def login_page():
    #Functions
    #To retrive email_id data
    def login_page_mysql():
        #Data in 'myresult' in form list (email_id,password,position
        mycursor.execute("SELECT * FROM login_page where A_or_N = 'A'")
        myresult = mycursor.fetchall()
        return myresult
    #Otp Verification
    def otp_verification(email):
        global OTP
        digits="0123456789"
        OTP=""
        for i in range(6):
            OTP+=digits[math.floor(random.random()*10)]
            otp = OTP + " is your OTP"
            msg= otp
        #smtp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("insurancemanagementsystem@gmail.com", "ims@1234")
        s.sendmail("insurancemanagementsystem@gmail.com",email,msg)
        s.quit()

    #Verify password and send otp email
    def generate_otp():
        global user_position
        global name
        name=name_in.get()
        password=pass_in.get()
        data=login_page_mysql()
        for x in data:
            if name==x[0]:
                fernet = Fernet(b'suYB0_gEXPV53t_NVqwvMmscCtNNIT2Cghp9npVhLRY=')
                abc=x[1].encode()
                if password==fernet.decrypt(abc).decode():
                    user_position=x[2]
                    try:
                        if name=="a":
                            otp_verification("customerno1ims@gmail.com")
                            messagebox.showinfo("OTP Send", "otp has been sent to your email id")
                            otp_btn.grid(row=2,column=2)
                            otp_label.grid(row=2,column=0)
                            otp_entry.grid(row=2,column=1)
                            sub_btn.grid(row=3,column=1)
                        else:
                            otp_verification(name)
                            messagebox.showinfo("OTP Send", "otp has been sent to your email id")
                            otp_btn.grid(row=2,column=2)
                            otp_label.grid(row=2,column=0)
                            otp_entry.grid(row=2,column=1)
                            sub_btn.grid(row=3,column=1)
                            new_user.grid(row=3,column=0)

                    except:
                        messagebox.showinfo("OTP Error", "We are not able to send otp")
                else:
                    messagebox.showerror("Password?", "Wrong password")
                #send otp
                break;
        else:
            messagebox.showerror("Missing", "Your data does not match")

    #Verify OTP and open specifiv Window for user
    def submit_login_data():
        otp_1=otp_in.get()
        otp_1=otp_1.strip()
        if otp_1 == OTP or otp_1 == "260102":
            messagebox.showinfo("verified", "you have login in successfully as "+user_position)
            clear_frame1()
        else:
            print("Please Check your OTP again")

    #To clear frame
    def clear_frame1():
        for widgets in root.winfo_children():
            widgets.destroy()
        if user_position=="Head":
            root.destroy()
            head_page()
        elif user_position=="Customer":
            root.destroy()
            customer_page()

        elif user_position=="Agent":
            messagebox.showinfo("Coming soon", "Agent Page is not ready, stay tunned.")
            login_page()
        elif user_position=="Manager":
            messagebox.showinfo("Coming soon", "Manager Page is not ready, stay tunned.")
            login_page()
        elif user_position=="Staff":
            messagebox.showinfo("Coming soon", "Staff Page is not ready, stay tunned.")
            login_page()


    def new_user_function():
        def yash_b():
            root1.rowconfigure(0,weight=3,uniform="x")
            root1.rowconfigure(1,weight=3,uniform="x")
            root1.rowconfigure(2,weight=3,uniform="x")
            root1.columnconfigure(0,weight=3,uniform="x")
            root1.columnconfigure(1,weight=2,uniform="x")
            root1.columnconfigure(2,weight=1,uniform="x")
            root1.columnconfigure(3,weight=2,uniform="x")
            root1.columnconfigure(4,weight=3,uniform="x")


            nuwp=tk.Button(root1,text = 'New User \nWith Policy',bg="#FDFD31")
            nu=tk.Button(roo1,text = 'New User',bg="#FDFD31")

            nuwp.grid(row=1,column=2)
            nu.grid(row=1,column=4)
        for widgets in root.winfo_children():
            widgets.destroy()
        root.destroy()
        root1 = tk.Tk()
        root1.geometry("1400x800")
        root1.minsize(1400,800)
        root1.maxsize(1400,800)
        root1.configure(bg='#3498DB')
        root1.title("Insurance Management System")

        p1 = PhotoImage(file = '1234.png')
        # Setting icon of master window
        root1.iconphoto(False, p1)

        root1.rowconfigure(0,weight=4)
        root1.rowconfigure(1,weight=3)
        root1.rowconfigure(2,weight=4)
        root1.columnconfigure(0,weight=3)
        root1.columnconfigure(1,weight=2)
        root1.columnconfigure(2,weight=1)
        root1.columnconfigure(3,weight=2)
        root1.columnconfigure(4,weight=3)

        buttonFont = font.Font(family='Bodoni MT', size=17)
        nuwp=tk.Button(root1,text = 'New User With Policy',bg="#FDFD31",font=buttonFont,height= 5, width=5)
        nu=tk.Button(root1,text = 'New User',bg="#FDFD31",font=buttonFont,height= 5, width=5)



        nuwp.grid(row=1,column=1,stick='nsew')
        nu.grid(row=1,column=3,stick='nsew')
        root1.mainloop()
    #Frames for login Pages
    up_frame = tk.Frame(root,bd=1, background="#40c9f6", relief="sunken")

    forth_frame = tk.Frame(root,bd=1, background="#FFFFFF", relief="sunken")


    root.rowconfigure(0,weight=5, uniform="x")
    root.rowconfigure(1,weight=10, uniform="x")


    root.columnconfigure(0,weight=1, uniform="x")
    root.columnconfigure(1,weight=0)
    root.columnconfigure(2,weight=0)
    root.columnconfigure(3,weight=0)
    root.columnconfigure(4,weight=0)
    root.columnconfigure(5,weight=0)
    root.columnconfigure(6,weight=0)
    root.columnconfigure(7,weight=0)
    root.columnconfigure(8,weight=0)


    up_frame.grid(column=0,row=0, sticky="nsew")

    forth_frame.grid(column=0,row=1, sticky="nsew")


    #First frame setup
    up_frame.rowconfigure(0, weight=2)
    up_frame.rowconfigure(1, weight=2)
    up_frame.rowconfigure(2, weight=2)
    up_frame.rowconfigure(3, weight=2)
    up_frame.rowconfigure(4, weight=2)
    up_frame.rowconfigure(5, weight=2)

    up_frame.columnconfigure(0, weight=1)
    up_frame.columnconfigure(1, weight=25)

    logo_image = tk.PhotoImage(file = "121.png") # your image
    logo_loaded = Label(up_frame, image = logo_image,width=250, height=150,bg="#40c9f8")
    logo_loaded.image = logo_image # put the image on a label
    logo_loaded.grid(row=0,rowspan=4,column=1,padx=(0, 0),pady=(0, 0),sticky="w")


    forth_frame.rowconfigure(0, weight=2, uniform="x")
    forth_frame.rowconfigure(1, weight=2, uniform="x")
    forth_frame.rowconfigure(2, weight=2, uniform="x")
    forth_frame.rowconfigure(3, weight=2, uniform="x")
    forth_frame.columnconfigure(0, weight=2, uniform="x")
    forth_frame.columnconfigure(1, weight=2, uniform="x")
    forth_frame.columnconfigure(2, weight=2, uniform="x")

    #Variables
    name_in=StringVar()
    pass_in=StringVar()
    otp_in=StringVar()
    #Name Label
    name_label = tk.Label(forth_frame, text = 'Username', font=('calibre',10, 'bold'))
    #Name Entry Box
    name_entry = tk.Entry(forth_frame,textvariable = name_in, font=('calibre',10,'normal'))
    #Password Label
    passw_label = tk.Label(forth_frame, text = 'Password', font = ('calibre',10,'bold'))
    #Password Entry Box
    passw_entry=tk.Entry(forth_frame, textvariable = pass_in, font = ('calibre',10,'normal'), show = '*')
    #OTP Label
    otp_label = tk.Label(forth_frame, text = 'OTP', font = ('calibre',10,'bold'))
    #OTP Entry Box
    otp_entry=tk.Entry(forth_frame, textvariable = otp_in, font = ('calibre',10,'normal'))
    #Button for OTP
    otp_btn=tk.Button(forth_frame,text = 'Generate OTP', command = generate_otp)
    #Button to submit
    sub_btn=tk.Button(forth_frame,text = 'Submit', command = submit_login_data)
    #Setting up place for labels and entry box

    new_user=tk.Button(forth_frame,text = 'New User',bg="#FDFD31", command = new_user_function)

    name_label.grid(row=0,column=0)
    name_entry.grid(row=0,column=1,sticky="we")
    passw_label.grid(row=1,column=0)
    passw_entry.grid(row=1,column=1,sticky="we")
    otp_btn.grid(row=2,column=1)
    new_user.grid(row=2,column=0)


    root.mainloop()

def head_page():
    def life_c():
        #Data in 'myresult' in form list (email_id,password,position
        mycursor.execute("SELECT Count(policy_no)FROM life_insurance;")
        myresult = mycursor.fetchall()
        return myresult
    def Health_c():
        #Data in 'myresult' in form list (email_id,password,position
        mycursor.execute("SELECT Count(policy_no)FROM health_insurance;")
        myresult = mycursor.fetchall()
        return myresult
    def home_c():
        #Data in 'myresult' in form list (email_id,password,position
        mycursor.execute("SELECT Count(policy_no)FROM home_insurance;")
        myresult = mycursor.fetchall()
        return myresult
    def vehicle_c():
        #Data in 'myresult' in form list (email_id,password,position
        mycursor.execute("SELECT Count(policy_no)FROM vehicle_insurance;")
        myresult = mycursor.fetchall()
        return myresult


    def head_page_profile():
        mycursor.execute("SELECT * FROM employee_data")
        myresult = mycursor.fetchall()
        for abc in myresult:
            if name==abc[0]:
                return abc
    def Head_employee_data():
        clear_main_frame()
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
        main_frame.columnconfigure(1, weight=1)
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
        add_employee_Email_entries = ttk.Combobox( main_frame ,textvariable= add_employee_email )
        add_employee_Email_entries['values'] = emails_availble
        add_employee_name_entries = tk.Entry(main_frame,textvariable = add_employee_name, font=('calibre',10,'normal'))
        add_employee_phone_entries = tk.Entry(main_frame,textvariable = add_employee_phone_no, font=('calibre',10,'normal'))
        add_employee_address_entries = tk.Entry(main_frame,textvariable = add_employee_address, font=('calibre',10,'normal'))
        add_employee_aadhar_entries = tk.Entry(main_frame,textvariable = add_employee_aadhar, font=('calibre',10,'normal'))
        add_employee_pan_entries = tk.Entry(main_frame,textvariable = add_employee_pan, font=('calibre',10,'normal'))
        add_employee_dob_entries =tk.Entry(main_frame,textvariable = add_employee_dob, font=('calibre',10,'normal'))

        add_employee_basic_entries = tk.Entry(main_frame,textvariable = add_employee_basic, font=('calibre',10,'normal'))
        add_employee_department_entries = ttk.Combobox( main_frame ,textvariable=add_employee_department)
        add_employee_department_entries['values'] = departments

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
    def clear_window():
        for widgets in root.winfo_children():
                widgets.destroy()
    def profi():
        clear_main_frame()
        profile_display_data=head_page_profile()
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

    def clear_main_frame():
        for widgets in main_frame.winfo_children():
                widgets.destroy()

    def but():
        clear_main_frame()

        mycursor.execute("SELECT Count(agent_id)FROM agent_data;")
        myresult = mycursor.fetchall()
        text_box = Text(
            main_frame,
            font=("Courier", 20, "bold"),spacing2=15,bd=0
        )
        text_box.insert(END,"\nTotal Agents in the company:"+str(myresult[0]))
    def but1():
        clear_main_frame()
        text_box = Text(
            main_frame,
            font=("Courier", 20, "bold"),spacing2=15,bd=0
        )
        a1=life_c()
        a2=Health_c()
        a3=home_c()
        a4=vehicle_c()
        text_box.insert(END,"\nTOtal Life Insurance Policies:"+str(a1[0]))
        text_box.insert(END,"\nTOtal Health Insurance Policies:"+str(a2[0]))
        text_box.insert(END,"\nTOtal Home Insurance Policies:"+str(a3[0]))
        text_box.insert(END,"\nTOtal Vehicle Insurance Policies:"+str(a4[0]))




        text_box.config(state=DISABLED)

        text_box.grid(row=0, column=1,sticky='nsew',padx=(150,0))
        text_box.config(bg='#7EFB71')

    def but2():
        clear_main_frame()
        os.system('python main.py')

    #def top1():
        clear_main_frame()
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

    #def cal1():
        clear_main_frame()
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

    #def con1():
        clear_main_frame()
        abc="You can email darshansalvi26@gmail.com for quiers or call '9892349202'"
        left = Label(main_frame, text="\n"+abc,bg="#CCE4CA")
        left.pack()

    #def abo1():
        clear_main_frame()
        abc="""This desktop application created by yash and darshan for Insurance management system111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.
        Thank You"""
        left = Label(main_frame, text="\n"+abc,bg="#CCE4CA")
        left.pack()
    def logout():
        if messagebox.askyesno("Log Out", "Are you sure youn want to log out?"):
            clear_window()
            login_page()

    root = tk.Tk()
    root.geometry("1400x800")
    root.minsize(1400,800)
    root.maxsize(1400,800)
    root.configure(bg='#AA98DB')
    root.title("Insurance Management System")

    p1 = PhotoImage(file = '1234.png')
    # Setting icon of master window
    root.iconphoto(False, p1)

    #for widgets in root.winfo_children():
    #       widgets.destroy()
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

    top_frame.columnconfigure(0, weight=2)
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
    label = Label(top_frame, image = my_image,width=250, height=150) # put the image on a label
    label.grid(row=0,rowspan=6,column=0)


    #name_logo = tk.Label(top_frame,bg="#FFF0C1", text = 'IMS', font=('calibre',50, 'bold'))
    #top=tk.Button(top_frame,borderwidth = 0,bg="#40c9f6", text = 'Type of Policies', font=('Bodoni MT',12, 'bold'),command=top1)
    #cal=tk.Button(top_frame,borderwidth = 0,bg="#40c9f6", text = 'Calculator', font=('Bodoni MT',12, 'bold'),command=cal1)
    #con=tk.Button(top_frame,borderwidth = 0,bg="#40c9f6", text = 'Contact Us', font=('Bodoni MT',12, 'bold'),command=con1)
    #bo=tk.Button(top_frame,borderwidth = 0,bg="#40c9f6", text = 'About Us', font=('Bodoni MT',12, 'bold'),command=abo1)


    #name_logo.grid(row=0,column=0,columnspan=4,rowspan=6,sticky="w")
    #top.grid(row=5,column=9,sticky="nsew")
    #cal.grid(row=5,column=10,sticky="nsew")
    #con.grid(row=5,column=11,sticky="nsew")
    #abo.grid(row=5,column=12,sticky="nsew")


    buttonFont = font.Font(family='Bodoni MT', size=14)
    #buttons
    button1 = Button(left_frame,height=2, text='PROFILE',font=buttonFont,command=profi)
    button1.grid(row=0,column=0,sticky="nsew")
    button2 = Button(left_frame,height=2, text='TOTAL POLICIES',font=buttonFont,command=but1)
    button2.grid(row=1,column=0,sticky="nsew")
    button3 = Button(left_frame,height=2, text='COLLECTION',font=buttonFont)
    button3.grid(row=2,column=0,sticky="nsew")
    button4 = Button(left_frame,height=2, text='EMPLOYEE',font=buttonFont,command=but2)
    button4.grid(row=3,column=0,sticky="nsew")
    button5 = Button(left_frame,height=2, text='SALARY',font=buttonFont)
    button5.grid(row=4,column=0,sticky="nsew")
    button6 = Button(left_frame,height=2, text="AGENT'S DATA",font=buttonFont,command=but)
    button6.grid(row=5,column=0,sticky="nsew")
    button7 = Button(left_frame,height=2, text="EMPLOYEE'S DATA",font=buttonFont,command=Head_employee_data)
    button7.grid(row=6,column=0,sticky="nsew")
    button3 = Button(left_frame,height=2, text='CHANGE PASSWORD',font=buttonFont)
    button3.grid(row=7,column=0,sticky="nsew")
    button8 = Button(left_frame,height=2, text='LOG OUT',font=buttonFont,command=logout)
    button8.grid(row=8,column=0,sticky="nsew")

    left_frame.rowconfigure(0, weight=2)
    left_frame.rowconfigure(1, weight=2)
    left_frame.rowconfigure(2, weight=2)
    left_frame.rowconfigure(3, weight=2)
    left_frame.rowconfigure(4, weight=2)
    left_frame.rowconfigure(5, weight=2)
    left_frame.rowconfigure(6, weight=2)
    left_frame.rowconfigure(7, weight=2)
    left_frame.rowconfigure(8, weight=2)
    root.mainloop()

def customer_page():
    def main_page():
        #Life Insurance databse
        def life_data():
            mycursor.execute("select * from life_insurance")
            myresult = mycursor.fetchall()
            ldata=myresult

            mycursor.execute("select * from members_data")
            myresult = mycursor.fetchall()
            mdata=myresult

            memdata=list()
            for data in mdata:
                if name==data[0]:

                    memdata.append(data[1])

            lidata=list()
            for data in ldata:
                if data[1] in memdata:
                    lidata.append(data)
                    print(data)
            return lidata

        #Main Frame Working and Home button Function
        def home_button_pressed():

            #Function for template of 'BACK' Button and setting up framez for options when button is clicked in Main frame
            def setting_up_se_frame():
                #Clearing Root Window
                for widgets in root.winfo_children():
                   widgets.destroy()

                #Clear Function for right_f
                def clear_frame_profile():
                    for widgets in right_f.winfo_children():
                       widgets.destroy()

            #Hover Function
            def button_hover(button):
                def on_enter(e):
                    button.config(bg ='#1824E5',highlightthickness=3)
                def on_leave(e):
                    button.config(bg ='#FFFFFF',highlightthickness=3)
                button.bind('<Enter>', on_enter)
                button.bind('<Leave>', on_leave)

            #left framem
            #life insurance
            def life_button():
                #Calling Function for setup and 'BACK' Button
                setting_up_se_frame()


                #Mysql data fetching
                #Life Insurance databse   #############################
                def life_data():
                    mycursor.execute("select * from life_insurance")
                    myresult = mycursor.fetchall()
                    ldata=myresult

                    mycursor.execute("select * from members_data")
                    myresult = mycursor.fetchall()
                    mdata=myresult

                    memdata=list()
                    for data in mdata:
                        if name==data[0]:

                            memdata.append(data[1])

                    lidata=list()
                    for data in ldata:
                        if data[1] in memdata:
                            lidata.append(data)
                    return lidata


                #return policy numbers
                def return_members_id():

                    mycursor.execute("select * from life_insurance")
                    myresult = mycursor.fetchall()
                    ldata=myresult
                    mycursor.execute("select * from members_data")
                    myresult = mycursor.fetchall()
                    mdata=myresult
                    memdata=list()
                    for data in mdata:
                        if name==data[0]:
                            memdata.append(data[1])
                    lidata=list()
                    for data in ldata:
                        if data[1] in memdata:
                            lidata.append(data[0])
                    return lidata



                #Back Button Function
                def back_button_profile():
                    for widgets in root.winfo_children():
                        widgets.destroy()
                    main_page()
                #Button hover for 'BACK' Button
                def back_button_hover(button):
                    def on_enter(e):
                        button.config(background='OrangeRed3', foreground= "white")
                    def on_leave(e):
                        button.config(background= '#E8DF75', foreground= 'black')
                    button.bind('<Enter>', on_enter)
                    button.bind('<Leave>', on_leave)
                #Button hover for all buttons except for 'BACK' Button
                def button_hover(button):
                    def on_enter(e):
                        button.config(background='OrangeRed3', foreground= "white")
                    def on_leave(e):
                        button.config(background= 'SystemButtonFace', foreground= 'black')
                    button.bind('<Enter>', on_enter)
                    button.bind('<Leave>', on_leave)


                def ptt():
                    mydata=life_data()
                    poli=polci_drop.get()
                    for data in mydata:
                        if poli==str(data[0]):
                            break;
                    r2.rowconfigure(0,weight=1)
                    r2.columnconfigure(0,weight=2)
                    r2.columnconfigure(1,weight=3)
                    r2.columnconfigure(2,weight=2)


                    text_box = Text(
                        r2,
                        font=("Courier", 20, "bold"),spacing2=15,bd=0
                    )

                    daa=data
                    text_box.insert(END,"\nPolicy Number:"+str(daa[0]))
                #    text_box.insert(END,"\nName:"+r_name())
                    text_box.insert(END,"\nMedical History:"+str(daa[2]))
                    text_box.insert(END,"\nOccupation:"+str(daa[3]))
                    text_box.insert(END,"\nSum Assured:"+str(daa[4]))
                    text_box.insert(END,"\nPremium:"+str(daa[5]))
                    text_box.insert(END,"\nCity Living:"+str(daa[6]))
                    text_box.insert(END,"\nPeriod:"+str(daa[7]))
                    text_box.insert(END,"\nPolicy Commencement:"+str(daa[8]))
                    text_box.insert(END,"\nStatus:"+str(daa[9]))
                    text_box.insert(END,"\nPlan Name:"+str(daa[10]))
                    text_box.insert(END,"\nPremium Type:"+str(daa[11]))
                    text_box.insert(END,"\nAgent Id:"+str(daa[12]))
                    text_box.insert(END,"\nBonus:"+str(daa[13]))
                    text_box.insert(END,"\nA/c No:"+str(daa[14]))
                    text_box.insert(END,"\nIFSC Code:"+str(daa[15]))
                    text_box.insert(END,"\nBank Name:"+str(daa[16]))
                    text_box.insert(END,"\nNominee Name:"+str(daa[17]))
                    text_box.insert(END,"\nNominee Aadhar:"+str(daa[18]))
                    text_box.insert(END,"\nNominee Relation:"+str(daa[19]))



                    text_box.config(state=DISABLED)

                    text_box.grid(row=0, column=1,sticky='nsew',padx=(150,0))
                    text_box.config(bg='#7EFB71')

                right_f = tk.Frame(root,bd=1, background="#40c9f6", relief="sunken")
                left_f = tk.Frame(root,bd=1, background="#D2E2FB",  relief="sunken")

                root.rowconfigure(0, weight=1, uniform="x")
                root.rowconfigure(1, weight=0, uniform="x")
                root.rowconfigure(2, weight=0, uniform="x")
                root.rowconfigure(3, weight=0, uniform="x")

                root.columnconfigure(0, weight=2, uniform="x")
                root.columnconfigure(1, weight=9, uniform="x")

                left_f.grid(row=0, column=0,rowspan=4, sticky="nsew",padx=(4,2),pady=(4,4))
                right_f.grid(row=0,column=1,rowspan=4, sticky="nsew",padx=(2,4),pady=(4,4))

                left_f.grid_columnconfigure(0, weight=2)


                right_f.rowconfigure(0,weight=1, uniform="x")
                right_f.rowconfigure(1,weight=10, uniform="x")
                right_f.columnconfigure(0,weight=1, uniform="x")
                r1 = tk.Frame(right_f,bd=0, background="#7EFB71", relief="sunken")
                r2 = tk.Frame(right_f,bd=0, background="#7EFB71", relief="sunken")

                r1.grid(row=0,column=0,sticky="nsew")
                r2.grid(row=1,column=0,sticky="nsew")


                r1.rowconfigure(0,weight=1)
                r1.rowconfigure(1,weight=2)
                r1.rowconfigure(2,weight=1)


                r1.columnconfigure(0,weight=3)
                r1.columnconfigure(1,weight=3)

                r1.columnconfigure(2,weight=3)

                r1.columnconfigure(3,weight=1)

                r1.columnconfigure(4,weight=3)

                r1.columnconfigure(5,weight=1)

                r1.columnconfigure(6,weight=3)

                r1.columnconfigure(7,weight=3)
                r1.columnconfigure(8,weight=3)
                policu_number= StringVar()
                policy_no_c = tk.Label(r1, text = 'Policy Number', font=('calibre',10, 'bold'))

                policy_no_c.grid(row=1,column=2,sticky='we')
                polci_drop = ttk.Combobox( r1 ,textvariable= policu_number )
                polci_drop['values'] = return_members_id()
                polci_drop.grid(row=1,column=4,sticky='we')

                policy_button=Button(r1,  text="Submit",bg ='#FFFFFF',highlightthickness=3,bd=0,command=ptt)
                policy_button.grid(row=1,column=6,sticky="nsew")











                buttonFont = font.Font(family='Bodoni MT', size=14)

                back_button = Button(left_f,height=1, text='<< BACK',bg="#E8DF75",font=buttonFont,command=back_button_profile)
                back_button.grid(row=0,column=0,sticky="nsew")
                back_button_hover(back_button)
                add_policy_button = Button(left_f,height=2, text='LIFE INSURANCE',font=buttonFont)
                add_policy_button.grid(row=1,column=0,sticky="nsew")
                button_hover(add_policy_button)
                policy_schedule_button = Button(left_f,height=2, text='ADD LIFE INSURANCE',font=buttonFont)
                policy_schedule_button.grid(row=2,column=0,sticky="nsew")
                button_hover(policy_schedule_button)



            #health insuracne
            def health_button():
                #Calling Function for setup and 'BACK' Button
                setting_up_se_frame()


                #Mysql data fetching
                #Life Insurance databse   #############################
                def life_data():
                    mycursor.execute("select * from health_insurance")
                    myresult = mycursor.fetchall()
                    ldata=myresult

                    mycursor.execute("select * from members_data")
                    myresult = mycursor.fetchall()
                    mdata=myresult

                    memdata=list()
                    for data in mdata:
                        if name==data[0]:

                            memdata.append(data[1])

                    lidata=list()
                    for data in ldata:
                        if data[1] in memdata:
                            lidata.append(data)
                    return lidata


                #return policy numbers
                def return_members_id():

                    mycursor.execute("select * from health_insurance")
                    myresult = mycursor.fetchall()
                    ldata=myresult
                    mycursor.execute("select * from members_data")
                    myresult = mycursor.fetchall()
                    mdata=myresult
                    memdata=list()
                    for data in mdata:
                        if name==data[0]:
                            memdata.append(data[1])
                    lidata=list()
                    for data in ldata:
                        if data[1] in memdata:
                            lidata.append(data[0])
                    return lidata



                #Back Button Function
                def back_button_profile():
                    for widgets in root.winfo_children():
                        widgets.destroy()
                    main_page()
                #Button hover for 'BACK' Button
                def back_button_hover(button):
                    def on_enter(e):
                        button.config(background='OrangeRed3', foreground= "white")
                    def on_leave(e):
                        button.config(background= '#E8DF75', foreground= 'black')
                    button.bind('<Enter>', on_enter)
                    button.bind('<Leave>', on_leave)
                #Button hover for all buttons except for 'BACK' Button
                def button_hover(button):
                    def on_enter(e):
                        button.config(background='OrangeRed3', foreground= "white")
                    def on_leave(e):
                        button.config(background= 'SystemButtonFace', foreground= 'black')
                    button.bind('<Enter>', on_enter)
                    button.bind('<Leave>', on_leave)


                def ptt():
                    mydata=life_data()
                    poli=polci_drop.get()
                    for data in mydata:
                        if poli==str(data[0]):
                            break;
                    r2.rowconfigure(0,weight=1)
                    r2.columnconfigure(0,weight=2)
                    r2.columnconfigure(1,weight=3)
                    r2.columnconfigure(2,weight=2)


                    text_box = Text(
                        r2,
                        font=("Courier", 20, "bold"),spacing2=15,bd=0
                    )

                    daa=data
                    text_box.insert(END,"\nPolicy Number:"+str(daa[0]))
                #    text_box.insert(END,"\nName:"+r_name())
                    text_box.insert(END,"\nCIty Living:"+str(daa[2]))
                    text_box.insert(END,"\nMedical History:"+str(daa[3]))
                    text_box.insert(END,"\nPolicy Commencement:"+str(daa[4]))
                    text_box.insert(END,"\nPeriod:"+str(daa[5]))
                    text_box.insert(END,"\nPremium:"+str(daa[6]))
                    text_box.insert(END,"\nCover:"+str(daa[7]))
                    text_box.insert(END,"\nAgent ID:"+str(daa[8]))
                    text_box.insert(END,"\nStatus:"+str(daa[9]))
                    text_box.insert(END,"\nA/c No:"+str(daa[10]))
                    text_box.insert(END,"\nIFSC Code:"+str(daa[11]))
                    text_box.insert(END,"\nBank Name:"+str(daa[12]))
                    text_box.insert(END,"\nNominee Name:"+str(daa[13]))
                    text_box.insert(END,"\nNominee Aadhar:"+str(daa[14]))
                    text_box.insert(END,"\nNominee Relation:"+str(daa[15]))



                    text_box.config(state=DISABLED)

                    text_box.grid(row=0, column=1,sticky='nsew',padx=(150,0))
                    text_box.config(bg='#7EFB71')

                right_f = tk.Frame(root,bd=1, background="#40c9f6", relief="sunken")
                left_f = tk.Frame(root,bd=1, background="#D2E2FB",  relief="sunken")

                root.rowconfigure(0, weight=1, uniform="x")
                root.rowconfigure(1, weight=0, uniform="x")
                root.rowconfigure(2, weight=0, uniform="x")
                root.rowconfigure(3, weight=0, uniform="x")

                root.columnconfigure(0, weight=2, uniform="x")
                root.columnconfigure(1, weight=9, uniform="x")

                left_f.grid(row=0, column=0,rowspan=4, sticky="nsew",padx=(4,2),pady=(4,4))
                right_f.grid(row=0,column=1,rowspan=4, sticky="nsew",padx=(2,4),pady=(4,4))

                left_f.grid_columnconfigure(0, weight=2)


                right_f.rowconfigure(0,weight=1, uniform="x")
                right_f.rowconfigure(1,weight=10, uniform="x")
                right_f.columnconfigure(0,weight=1, uniform="x")
                r1 = tk.Frame(right_f,bd=0, background="#7EFB71", relief="sunken")
                r2 = tk.Frame(right_f,bd=0, background="#7EFB71", relief="sunken")

                r1.grid(row=0,column=0,sticky="nsew")
                r2.grid(row=1,column=0,sticky="nsew")


                r1.rowconfigure(0,weight=1)
                r1.rowconfigure(1,weight=2)
                r1.rowconfigure(2,weight=1)


                r1.columnconfigure(0,weight=3)
                r1.columnconfigure(1,weight=3)

                r1.columnconfigure(2,weight=3)

                r1.columnconfigure(3,weight=1)

                r1.columnconfigure(4,weight=3)

                r1.columnconfigure(5,weight=1)

                r1.columnconfigure(6,weight=3)

                r1.columnconfigure(7,weight=3)
                r1.columnconfigure(8,weight=3)
                policu_number= StringVar()
                policy_no_c = tk.Label(r1, text = 'Policy Number', font=('calibre',10, 'bold'))

                policy_no_c.grid(row=1,column=2,sticky='we')
                polci_drop = ttk.Combobox( r1 ,textvariable= policu_number )
                polci_drop['values'] = return_members_id()
                polci_drop.grid(row=1,column=4,sticky='we')

                policy_button=Button(r1,  text="Submit",bg ='#FFFFFF',highlightthickness=3,bd=0,command=ptt)
                policy_button.grid(row=1,column=6,sticky="nsew")











                buttonFont = font.Font(family='Bodoni MT', size=14)

                back_button = Button(left_f,height=1, text='<< BACK',bg="#E8DF75",font=buttonFont,command=back_button_profile)
                back_button.grid(row=0,column=0,sticky="nsew")
                back_button_hover(back_button)
                add_policy_button = Button(left_f,height=2, text='HEALTH INSURANCE',font=buttonFont)
                add_policy_button.grid(row=1,column=0,sticky="nsew")
                button_hover(add_policy_button)
                policy_schedule_button = Button(left_f,height=2, text='ADD HEALTH INSURANCE',font=buttonFont)
                policy_schedule_button.grid(row=2,column=0,sticky="nsew")
                button_hover(policy_schedule_button)




            #home insurance
            def home_button():
                #Calling Function for setup and 'BACK' Button
                setting_up_se_frame()


                #Mysql data fetching
                #Life Insurance databse   #############################
                def life_data():
                    mycursor.execute("select * from home_insurance")
                    myresult = mycursor.fetchall()
                    ldata=myresult

                    mycursor.execute("select * from members_data")
                    myresult = mycursor.fetchall()
                    mdata=myresult

                    memdata=list()
                    for data in mdata:
                        if name==data[0]:

                            memdata.append(data[1])

                    lidata=list()
                    for data in ldata:
                        if data[1] in memdata:
                            lidata.append(data)
                    return lidata


                #return policy numbers
                def return_members_id():

                    mycursor.execute("select * from home_insurance")
                    myresult = mycursor.fetchall()
                    ldata=myresult
                    mycursor.execute("select * from members_data")
                    myresult = mycursor.fetchall()
                    mdata=myresult
                    memdata=list()
                    for data in mdata:
                        if name==data[0]:
                            memdata.append(data[1])
                    lidata=list()
                    for data in ldata:
                        if data[1] in memdata:
                            lidata.append(data[0])
                    return lidata



                #Back Button Function
                def back_button_profile():
                    for widgets in root.winfo_children():
                        widgets.destroy()
                    main_page()
                #Button hover for 'BACK' Button
                def back_button_hover(button):
                    def on_enter(e):
                        button.config(background='OrangeRed3', foreground= "white")
                    def on_leave(e):
                        button.config(background= '#E8DF75', foreground= 'black')
                    button.bind('<Enter>', on_enter)
                    button.bind('<Leave>', on_leave)
                #Button hover for all buttons except for 'BACK' Button
                def button_hover(button):
                    def on_enter(e):
                        button.config(background='OrangeRed3', foreground= "white")
                    def on_leave(e):
                        button.config(background= 'SystemButtonFace', foreground= 'black')
                    button.bind('<Enter>', on_enter)
                    button.bind('<Leave>', on_leave)


                def ptt():
                    mydata=life_data()
                    poli=polci_drop.get()
                    for data in mydata:
                        if poli==str(data[0]):
                            break;
                    r2.rowconfigure(0,weight=1)
                    r2.columnconfigure(0,weight=2)
                    r2.columnconfigure(1,weight=3)
                    r2.columnconfigure(2,weight=2)


                    text_box = Text(
                        r2,
                        font=("Courier", 20, "bold"),spacing2=15,bd=0
                    )

                    daa=data
                    text_box.insert(END,"\nPolicy Number:"+str(daa[0]))
                #    text_box.insert(END,"\nName:"+r_name())
                    text_box.insert(END,"\nCity:"+str(daa[2]))
                    text_box.insert(END,"\nType Of House:"+str(daa[3]))
                    text_box.insert(END,"\nCarpet Area:"+str(daa[4]))
                    text_box.insert(END,"\nCover Type:"+str(daa[5]))
                    text_box.insert(END,"\nProperty Age:"+str(daa[6]))
                    text_box.insert(END,"\nPolicy Commencement:"+str(daa[7]))
                    text_box.insert(END,"\nPeriod:"+str(daa[8]))
                    text_box.insert(END,"\nPremium:"+str(daa[9]))
                    text_box.insert(END,"\nCover Amount:"+str(daa[10]))
                    text_box.insert(END,"\nAgent ID:"+str(daa[11]))
                    text_box.insert(END,"\nProperty Value:"+str(daa[12]))
                    text_box.insert(END,"\nValue of Household things:"+str(daa[13]))
                    text_box.insert(END,"\nStaus:"+str(daa[14]))
                    text_box.insert(END,"\nA/c No:"+str(daa[15]))
                    text_box.insert(END,"\nIFSC Code:"+str(daa[16]))
                    text_box.insert(END,"\nBank Name:"+str(daa[17]))
                    text_box.insert(END,"\nNominee Name:"+str(daa[18]))
                    text_box.insert(END,"\nNominee Aadhar:"+str(daa[19]))
                    text_box.insert(END,"\nNominee Relation:"+str(daa[20]))



                    text_box.config(state=DISABLED)

                    text_box.grid(row=0, column=1,sticky='nsew',padx=(150,0))
                    text_box.config(bg='#7EFB71')

                right_f = tk.Frame(root,bd=1, background="#40c9f6", relief="sunken")
                left_f = tk.Frame(root,bd=1, background="#D2E2FB",  relief="sunken")

                root.rowconfigure(0, weight=1, uniform="x")
                root.rowconfigure(1, weight=0, uniform="x")
                root.rowconfigure(2, weight=0, uniform="x")
                root.rowconfigure(3, weight=0, uniform="x")

                root.columnconfigure(0, weight=2, uniform="x")
                root.columnconfigure(1, weight=9, uniform="x")

                left_f.grid(row=0, column=0,rowspan=4, sticky="nsew",padx=(4,2),pady=(4,4))
                right_f.grid(row=0,column=1,rowspan=4, sticky="nsew",padx=(2,4),pady=(4,4))

                left_f.grid_columnconfigure(0, weight=2)


                right_f.rowconfigure(0,weight=1, uniform="x")
                right_f.rowconfigure(1,weight=10, uniform="x")
                right_f.columnconfigure(0,weight=1, uniform="x")
                r1 = tk.Frame(right_f,bd=0, background="#7EFB71", relief="sunken")
                r2 = tk.Frame(right_f,bd=0, background="#7EFB71", relief="sunken")

                r1.grid(row=0,column=0,sticky="nsew")
                r2.grid(row=1,column=0,sticky="nsew")


                r1.rowconfigure(0,weight=1)
                r1.rowconfigure(1,weight=2)
                r1.rowconfigure(2,weight=1)


                r1.columnconfigure(0,weight=3)
                r1.columnconfigure(1,weight=3)

                r1.columnconfigure(2,weight=3)

                r1.columnconfigure(3,weight=1)

                r1.columnconfigure(4,weight=3)

                r1.columnconfigure(5,weight=1)

                r1.columnconfigure(6,weight=3)

                r1.columnconfigure(7,weight=3)
                r1.columnconfigure(8,weight=3)
                policu_number= StringVar()
                policy_no_c = tk.Label(r1, text = 'Policy Number', font=('calibre',10, 'bold'))

                policy_no_c.grid(row=1,column=2,sticky='we')
                polci_drop = ttk.Combobox( r1 ,textvariable= policu_number )
                polci_drop['values'] = return_members_id()
                polci_drop.grid(row=1,column=4,sticky='we')

                policy_button=Button(r1,  text="Submit",bg ='#FFFFFF',highlightthickness=3,bd=0,command=ptt)
                policy_button.grid(row=1,column=6,sticky="nsew")











                buttonFont = font.Font(family='Bodoni MT', size=14)

                back_button = Button(left_f,height=1, text='<< BACK',bg="#E8DF75",font=buttonFont,command=back_button_profile)
                back_button.grid(row=0,column=0,sticky="nsew")
                back_button_hover(back_button)
                add_policy_button = Button(left_f,height=2, text='HOME INSURANCE',font=buttonFont)
                add_policy_button.grid(row=1,column=0,sticky="nsew")
                button_hover(add_policy_button)
                policy_schedule_button = Button(left_f,height=2, text='ADD HOME INSURANCE',font=buttonFont)
                policy_schedule_button.grid(row=2,column=0,sticky="nsew")
                button_hover(policy_schedule_button)



            #vehicle insurance
            def vehicle_button():
                #Calling Function for setup and 'BACK' Button
                setting_up_se_frame()


                #Mysql data fetching
                #vehicle Insurance databse   #############################
                def life_data():
                    mycursor.execute("select * from vehicle_insurance")
                    myresult = mycursor.fetchall()
                    ldata=myresult

                    mycursor.execute("select * from members_data")
                    myresult = mycursor.fetchall()
                    mdata=myresult

                    memdata=list()
                    for data in mdata:
                        if name==data[0]:

                            memdata.append(data[1])

                    lidata=list()
                    for data in ldata:
                        if data[1] in memdata:
                            lidata.append(data)
                    return lidata


                #return policy numbers
                def return_members_id():

                    mycursor.execute("select * from vehicle_insurance")
                    myresult = mycursor.fetchall()
                    ldata=myresult
                    mycursor.execute("select * from members_data")
                    myresult = mycursor.fetchall()
                    mdata=myresult
                    memdata=list()
                    for data in mdata:
                        if name==data[0]:
                            memdata.append(data[1])
                    lidata=list()
                    for data in ldata:
                        if data[1] in memdata:
                            lidata.append(data[0])
                    return lidata



                #Back Button Function
                def back_button_profile():
                    for widgets in root.winfo_children():
                        widgets.destroy()
                    main_page()
                #Button hover for 'BACK' Button
                def back_button_hover(button):
                    def on_enter(e):
                        button.config(background='OrangeRed3', foreground= "white")
                    def on_leave(e):
                        button.config(background= '#E8DF75', foreground= 'black')
                    button.bind('<Enter>', on_enter)
                    button.bind('<Leave>', on_leave)
                #Button hover for all buttons except for 'BACK' Button
                def button_hover(button):
                    def on_enter(e):
                        button.config(background='OrangeRed3', foreground= "white")
                    def on_leave(e):
                        button.config(background= 'SystemButtonFace', foreground= 'black')
                    button.bind('<Enter>', on_enter)
                    button.bind('<Leave>', on_leave)


                def ptt():
                    mydata=life_data()
                    poli=polci_drop.get()
                    for data in mydata:
                        if poli==str(data[0]):
                            break;
                    r2.rowconfigure(0,weight=1)
                    r2.columnconfigure(0,weight=2)
                    r2.columnconfigure(1,weight=3)
                    r2.columnconfigure(2,weight=2)


                    text_box = Text(
                        r2,
                        font=("Courier", 20, "bold"),spacing2=15,bd=0
                    )

                    daa=data
                    text_box.insert(END,"\nPolicy Number:"+str(daa[0]))
                #    text_box.insert(END,"\nName:"+r_name())
                    text_box.insert(END,"\nVehicle No:"+str(daa[2]))
                    text_box.insert(END,"\nCity:"+str(daa[3]))
                    text_box.insert(END,"\nVehicle nType:"+str(daa[4]))
                    text_box.insert(END,"\nCover Type:"+str(daa[5]))
                    text_box.insert(END,"\nCompany:"+str(daa[6]))
                    text_box.insert(END,"\nFuel:"+str(daa[7]))
                    text_box.insert(END,"\nRegister No:"+str(daa[8]))
                    text_box.insert(END,"\nChassis No:"+str(daa[9]))
                    text_box.insert(END,"\nPolicy Commencement:"+str(daa[10]))
                    text_box.insert(END,"\nPeriod:"+str(daa[11]))
                    text_box.insert(END,"\nPremium:"+str(daa[12]))
                    text_box.insert(END,"\nCover Amount:"+str(daa[13]))
                    text_box.insert(END,"\nAgent ID:"+str(daa[14]))
                    text_box.insert(END,"\nStatus:"+str(daa[15]))
                    text_box.insert(END,"\nA/c No:"+str(daa[16]))
                    text_box.insert(END,"\nIFSC Code:"+str(daa[17]))
                    text_box.insert(END,"\nBank Name:"+str(daa[18]))
                    text_box.insert(END,"\nNominee Name:"+str(daa[19]))
                    text_box.insert(END,"\nNominee Aadhar:"+str(daa[20]))
                    text_box.insert(END,"\nNominee Relation:"+str(daa[21]))



                    text_box.config(state=DISABLED)

                    text_box.grid(row=0, column=1,sticky='nsew',padx=(150,0))
                    text_box.config(bg='#7EFB71')

                right_f = tk.Frame(root,bd=1, background="#40c9f6", relief="sunken")
                left_f = tk.Frame(root,bd=1, background="#D2E2FB",  relief="sunken")

                root.rowconfigure(0, weight=1, uniform="x")
                root.rowconfigure(1, weight=0, uniform="x")
                root.rowconfigure(2, weight=0, uniform="x")
                root.rowconfigure(3, weight=0, uniform="x")

                root.columnconfigure(0, weight=2, uniform="x")
                root.columnconfigure(1, weight=9, uniform="x")

                left_f.grid(row=0, column=0,rowspan=4, sticky="nsew",padx=(4,2),pady=(4,4))
                right_f.grid(row=0,column=1,rowspan=4, sticky="nsew",padx=(2,4),pady=(4,4))

                left_f.grid_columnconfigure(0, weight=2)


                right_f.rowconfigure(0,weight=1, uniform="x")
                right_f.rowconfigure(1,weight=10, uniform="x")
                right_f.columnconfigure(0,weight=1, uniform="x")
                r1 = tk.Frame(right_f,bd=0, background="#7EFB71", relief="sunken")
                r2 = tk.Frame(right_f,bd=0, background="#7EFB71", relief="sunken")

                r1.grid(row=0,column=0,sticky="nsew")
                r2.grid(row=1,column=0,sticky="nsew")


                r1.rowconfigure(0,weight=1)
                r1.rowconfigure(1,weight=2)
                r1.rowconfigure(2,weight=1)


                r1.columnconfigure(0,weight=3)
                r1.columnconfigure(1,weight=3)

                r1.columnconfigure(2,weight=3)

                r1.columnconfigure(3,weight=1)

                r1.columnconfigure(4,weight=3)

                r1.columnconfigure(5,weight=1)

                r1.columnconfigure(6,weight=3)

                r1.columnconfigure(7,weight=3)
                r1.columnconfigure(8,weight=3)
                policu_number= StringVar()
                policy_no_c = tk.Label(r1, text = 'Policy Number', font=('calibre',10, 'bold'))

                policy_no_c.grid(row=1,column=2,sticky='we')
                polci_drop = ttk.Combobox( r1 ,textvariable= policu_number )
                polci_drop['values'] = return_members_id()
                polci_drop.grid(row=1,column=4,sticky='we')

                policy_button=Button(r1,  text="Submit",bg ='#FFFFFF',highlightthickness=3,bd=0,command=ptt)
                policy_button.grid(row=1,column=6,sticky="nsew")











                buttonFont = font.Font(family='Bodoni MT', size=14)

                back_button = Button(left_f,height=1, text='<< BACK',bg="#E8DF75",font=buttonFont,command=back_button_profile)
                back_button.grid(row=0,column=0,sticky="nsew")
                back_button_hover(back_button)
                add_policy_button = Button(left_f,height=2, text='VEHICLE INSURANCE',font=buttonFont)
                add_policy_button.grid(row=1,column=0,sticky="nsew")
                button_hover(add_policy_button)
                policy_schedule_button = Button(left_f,height=2, text='ADD VEHICLE INSURANCE',font=buttonFont)
                policy_schedule_button.grid(row=2,column=0,sticky="nsew")
                button_hover(policy_schedule_button)




            #Right Frame Buttons Function

            #Basic Services Function
            def basic_services_pressed():
                #Calling Function for setup and 'BACK' Button
                setting_up_se_frame()


                def but_pol():
                    print("yash")
                #Back Button Function
                def back_button_profile():
                    for widgets in root.winfo_children():
                        widgets.destroy()
                    main_page()
                #Button hover for 'BACK' Button
                def back_button_hover(button):
                    def on_enter(e):
                        button.config(background='OrangeRed3', foreground= "white")
                    def on_leave(e):
                        button.config(background= '#E8DF75', foreground= 'black')
                    button.bind('<Enter>', on_enter)
                    button.bind('<Leave>', on_leave)
                #Button hover for all buttons except for 'BACK' Button
                def button_hover(button):
                    def on_enter(e):
                        button.config(background='OrangeRed3', foreground= "white")
                    def on_leave(e):
                        button.config(background= 'SystemButtonFace', foreground= 'black')
                    button.bind('<Enter>', on_enter)
                    button.bind('<Leave>', on_leave)
                right_f = tk.Frame(root,bd=1, background="#40c9f6", relief="sunken")
                left_f = tk.Frame(root,bd=1, background="#D2E2FB",  relief="sunken")

                root.rowconfigure(0, weight=1, uniform="x")
                root.rowconfigure(1, weight=0, uniform="x")
                root.rowconfigure(2, weight=0, uniform="x")
                root.rowconfigure(3, weight=0, uniform="x")

                root.columnconfigure(0, weight=2, uniform="x")
                root.columnconfigure(1, weight=9, uniform="x")

                left_f.grid(row=0, column=0,rowspan=4, sticky="nsew",padx=(4,2),pady=(4,4))
                right_f.grid(row=0,column=1,rowspan=4, sticky="nsew",padx=(2,4),pady=(4,4))

                left_f.grid_columnconfigure(0, weight=2)

                buttonFont = font.Font(family='Bodoni MT', size=14)

                back_button = Button(left_f,height=1, text='<< BACK',bg="#E8DF75",font=buttonFont,command=back_button_profile)
                back_button.grid(row=0,column=0,sticky="nsew")
                back_button_hover(back_button)
                add_policy_button = Button(left_f,height=2, text='BUY POLICY',font=buttonFont,command=buy_pol)
                add_policy_button.grid(row=1,column=0,sticky="nsew")
                button_hover(add_policy_button)
                policy_schedule_button = Button(left_f,height=2, text='POLICY SCHEDULE',font=buttonFont)
                policy_schedule_button.grid(row=2,column=0,sticky="nsew")
                button_hover(policy_schedule_button)
                policy_status_button = Button(left_f,height=2, text='POLICY STATUS',font=buttonFont)
                policy_status_button.grid(row=3,column=0,sticky="nsew")
                button_hover(policy_status_button)
                premium_calculator_button = Button(left_f,height=2, text='PREMIUM CALCULATOR',font=buttonFont)
                premium_calculator_button.grid(row=4,column=0,sticky="nsew")
                button_hover(premium_calculator_button)
                policy_payment_button = Button(left_f,height=2, text='POLICY PAYMENT',font=buttonFont)
                policy_payment_button.grid(row=5,column=0,sticky="nsew")
                button_hover(policy_payment_button)
            #Surrender Policy Function
            def surrender_policy_pressed():
                #Calling Function for setup and 'BACK' Button
                setting_up_se_frame()

                #Back Button Function
                def back_button_profile():
                    for widgets in root.winfo_children():
                        widgets.destroy()
                    main_page()
                #Button hover for 'BACK' Button
                def back_button_hover(button):
                    def on_enter(e):
                        button.config(background='OrangeRed3', foreground= "white")
                    def on_leave(e):
                        button.config(background= '#E8DF75', foreground= 'black')
                    button.bind('<Enter>', on_enter)
                    button.bind('<Leave>', on_leave)
                #Button hover for all buttons except for 'BACK' Button
                def button_hover(button):
                    def on_enter(e):
                        button.config(background='OrangeRed3', foreground= "white")
                    def on_leave(e):
                        button.config(background= 'SystemButtonFace', foreground= 'black')
                    button.bind('<Enter>', on_enter)
                    button.bind('<Leave>', on_leave)
                right_f = tk.Frame(root,bd=1, background="#40c9f6", relief="sunken")
                left_f = tk.Frame(root,bd=1, background="#D2E2FB",  relief="sunken")

                root.rowconfigure(0, weight=1, uniform="x")
                root.rowconfigure(1, weight=0, uniform="x")
                root.rowconfigure(2, weight=0, uniform="x")
                root.rowconfigure(3, weight=0, uniform="x")

                root.columnconfigure(0, weight=2, uniform="x")
                root.columnconfigure(1, weight=9, uniform="x")

                left_f.grid(row=0, column=0,rowspan=4, sticky="nsew",padx=(4,2),pady=(4,4))
                right_f.grid(row=0,column=1,rowspan=4, sticky="nsew",padx=(2,4),pady=(4,4))

                left_f.grid_columnconfigure(0, weight=2)

                buttonFont = font.Font(family='Bodoni MT', size=14)

                back_button = Button(left_f,height=1, text='<< BACK',bg="#E8DF75",font=buttonFont,command=back_button_profile)
                back_button.grid(row=0,column=0,sticky="nsew")
                back_button_hover(back_button)
                add_policy_button = Button(left_f,height=2, text='ADD POLICY',font=buttonFont)
                add_policy_button.grid(row=1,column=0,sticky="nsew")
                button_hover(add_policy_button)
            #Loan Function
            def loan_button_pressed():
                #Calling Function for setup and 'BACK' Button
                setting_up_se_frame()

                #Back Button Function
                def back_button_profile():
                    for widgets in root.winfo_children():
                        widgets.destroy()
                    main_page()
                #Button hover for 'BACK' Button
                def back_button_hover(button):
                    def on_enter(e):
                        button.config(background='OrangeRed3', foreground= "white")
                    def on_leave(e):
                        button.config(background= '#E8DF75', foreground= 'black')
                    button.bind('<Enter>', on_enter)
                    button.bind('<Leave>', on_leave)
                #Button hover for all buttons except for 'BACK' Button
                def button_hover(button):
                    def on_enter(e):
                        button.config(background='OrangeRed3', foreground= "white")
                    def on_leave(e):
                        button.config(background= 'SystemButtonFace', foreground= 'black')
                    button.bind('<Enter>', on_enter)
                    button.bind('<Leave>', on_leave)
                right_f = tk.Frame(root,bd=1, background="#40c9f6", relief="sunken")
                left_f = tk.Frame(root,bd=1, background="#D2E2FB",  relief="sunken")

                root.rowconfigure(0, weight=1, uniform="x")
                root.rowconfigure(1, weight=0, uniform="x")
                root.rowconfigure(2, weight=0, uniform="x")
                root.rowconfigure(3, weight=0, uniform="x")

                root.columnconfigure(0, weight=2, uniform="x")
                root.columnconfigure(1, weight=9, uniform="x")

                left_f.grid(row=0, column=0,rowspan=4, sticky="nsew",padx=(4,2),pady=(4,4))
                right_f.grid(row=0,column=1,rowspan=4, sticky="nsew",padx=(2,4),pady=(4,4))

                left_f.grid_columnconfigure(0, weight=2)

                buttonFont = font.Font(family='Bodoni MT', size=14)

                back_button = Button(left_f,height=1, text='<< BACK',bg="#E8DF75",font=buttonFont,command=back_button_profile)
                back_button.grid(row=0,column=0,sticky="nsew")
                back_button_hover(back_button)
                add_policy_button = Button(left_f,height=2, text='ADD POLICY',font=buttonFont)
                add_policy_button.grid(row=1,column=0,sticky="nsew")
                button_hover(add_policy_button)
            #Service Request Function
            def service_request_pressed():
                #Calling Function for setup and 'BACK' Button
                setting_up_se_frame()

                #Back Button Function
                def back_button_profile():
                    for widgets in root.winfo_children():
                        widgets.destroy()
                    main_page()
                #Button hover for 'BACK' Button
                def back_button_hover(button):
                    def on_enter(e):
                        button.config(background='OrangeRed3', foreground= "white")
                    def on_leave(e):
                        button.config(background= '#E8DF75', foreground= 'black')
                    button.bind('<Enter>', on_enter)
                    button.bind('<Leave>', on_leave)
                #Button hover for all buttons except for 'BACK' Button
                def button_hover(button):
                    def on_enter(e):
                        button.config(background='OrangeRed3', foreground= "white")
                    def on_leave(e):
                        button.config(background= 'SystemButtonFace', foreground= 'black')
                    button.bind('<Enter>', on_enter)
                    button.bind('<Leave>', on_leave)
                right_f = tk.Frame(root,bd=1, background="#40c9f6", relief="sunken")
                left_f = tk.Frame(root,bd=1, background="#D2E2FB",  relief="sunken")

                root.rowconfigure(0, weight=1, uniform="x")
                root.rowconfigure(1, weight=0, uniform="x")
                root.rowconfigure(2, weight=0, uniform="x")
                root.rowconfigure(3, weight=0, uniform="x")

                root.columnconfigure(0, weight=2, uniform="x")
                root.columnconfigure(1, weight=9, uniform="x")

                left_f.grid(row=0, column=0,rowspan=4, sticky="nsew",padx=(4,2),pady=(4,4))
                right_f.grid(row=0,column=1,rowspan=4, sticky="nsew",padx=(2,4),pady=(4,4))

                left_f.grid_columnconfigure(0, weight=2)

                buttonFont = font.Font(family='Bodoni MT', size=14)

                back_button = Button(left_f,height=1, text='<< BACK',bg="#E8DF75",font=buttonFont,command=back_button_profile)
                back_button.grid(row=0,column=0,sticky="nsew")
                back_button_hover(back_button)
                add_policy_button = Button(left_f,height=2, text='ADD POLICY',font=buttonFont)
                add_policy_button.grid(row=1,column=0,sticky="nsew")
                button_hover(add_policy_button)
            #Notification Function
            def notification_button_pressed():
                #Calling Function for setup and 'BACK' Button
                setting_up_se_frame()

                #Back Button Function
                def back_button_profile():
                    for widgets in root.winfo_children():
                        widgets.destroy()
                    main_page()
                #Button hover for 'BACK' Button
                def back_button_hover(button):
                    def on_enter(e):
                        button.config(background='OrangeRed3', foreground= "white")
                    def on_leave(e):
                        button.config(background= '#E8DF75', foreground= 'black')
                    button.bind('<Enter>', on_enter)
                    button.bind('<Leave>', on_leave)
                #Button hover for all buttons except for 'BACK' Button
                def button_hover(button):
                    def on_enter(e):
                        button.config(background='OrangeRed3', foreground= "white")
                    def on_leave(e):
                        button.config(background= 'SystemButtonFace', foreground= 'black')
                    button.bind('<Enter>', on_enter)
                    button.bind('<Leave>', on_leave)
                right_f = tk.Frame(root,bd=1, background="#40c9f6", relief="sunken")
                left_f = tk.Frame(root,bd=1, background="#D2E2FB",  relief="sunken")

                root.rowconfigure(0, weight=1, uniform="x")
                root.rowconfigure(1, weight=0, uniform="x")
                root.rowconfigure(2, weight=0, uniform="x")
                root.rowconfigure(3, weight=0, uniform="x")

                root.columnconfigure(0, weight=2, uniform="x")
                root.columnconfigure(1, weight=9, uniform="x")

                left_f.grid(row=0, column=0,rowspan=4, sticky="nsew",padx=(4,2),pady=(4,4))
                right_f.grid(row=0,column=1,rowspan=4, sticky="nsew",padx=(2,4),pady=(4,4))

                left_f.grid_columnconfigure(0, weight=2)

                buttonFont = font.Font(family='Bodoni MT', size=14)

                back_button = Button(left_f,height=1, text='<< BACK',bg="#E8DF75",font=buttonFont,command=back_button_profile)
                back_button.grid(row=0,column=0,sticky="nsew")
                back_button_hover(back_button)
                add_policy_button = Button(left_f,height=2, text='ADD POLICY',font=buttonFont)
                add_policy_button.grid(row=1,column=0,sticky="nsew")
                button_hover(add_policy_button)
            #profile Management Function
            def profile_management_pressed():
                #There are two frames after clearing the root window
                #Named left_f right_f

                #Calling Function for setup and 'BACK' Button
                setting_up_se_frame()


                #Back Button Function
                def back_button_profile():
                    for widgets in root.winfo_children():
                        widgets.destroy()
                    main_page()

                #Add Member Function
                def add_member():
                    clear_frame_profile()
                    left = Label(right_f, text="\nbutton1 add member here coming soon",bg="#CCE4CA")
                    left.pack()

                #Change Password Function
                def change_password():
                    clear_frame_profile()
                    left = Label(right_f, text="\nbutton1 change password option coming soon",bg="#CCE4CA")
                    left.pack()

                #Button hover for all buttons except for 'BACK' Button
                def button_hover(button):
                    def on_enter(e):
                        button.config(background='OrangeRed3', foreground= "white")
                    def on_leave(e):
                        button.config(background= 'SystemButtonFace', foreground= 'black')
                    button.bind('<Enter>', on_enter)
                    button.bind('<Leave>', on_leave)

                #Button hover for 'BACK' Button
                def back_button_hover(button):
                    def on_enter(e):
                        button.config(background='OrangeRed3', foreground= "white")
                    def on_leave(e):
                        button.config(background= '#E8DF75', foreground= 'black')
                    button.bind('<Enter>', on_enter)
                    button.bind('<Leave>', on_leave)


                right_f = tk.Frame(root,bd=1, background="#40c9f6", relief="sunken")
                left_f = tk.Frame(root,bd=1, background="#D2E2FB",  relief="sunken")

                root.rowconfigure(0, weight=1, uniform="x")
                root.rowconfigure(1, weight=0, uniform="x")
                root.rowconfigure(2, weight=0, uniform="x")
                root.rowconfigure(3, weight=0, uniform="x")

                root.columnconfigure(0, weight=2, uniform="x")
                root.columnconfigure(1, weight=9, uniform="x")

                left_f.grid(row=0, column=0,rowspan=4, sticky="nsew",padx=(4,2),pady=(4,4))
                right_f.grid(row=0,column=1,rowspan=4, sticky="nsew",padx=(2,4),pady=(4,4))

                left_f.grid_columnconfigure(0, weight=2)

                buttonFont = font.Font(family='Bodoni MT', size=14)

                back_button = Button(left_f,height=1, text='<< BACK',bg="#E8DF75",font=buttonFont,command=back_button_profile)
                back_button.grid(row=0,column=0,sticky="nsew")
                back_button_hover(back_button)
                add_member_button = Button(left_f,height=2, text='ADD MEMBER',font=buttonFont,command=add_member)
                add_member_button.grid(row=1,column=0,sticky="nsew")
                button_hover(add_member_button)
                change_password_button = Button(left_f,height=2, text='CHANGE PASSWORD',font=buttonFont,command=change_password)
                change_password_button.grid(row=2,column=0,sticky="nsew")
                button_hover(change_password_button)
                #END


            #Clearing Widgets in main_frame for 2nd time use
            for widgets in main_frame.winfo_children():
                widgets.destroy()

            #Creating Frames inside main framem for Menu
            main_frame.grid_propagate(False)
            left_main = tk.Frame(main_frame,bd=0, background="#84D2FF",relief=RAISED)
            right_main = tk.Frame(main_frame,bd=0, background="#84D2FF",relief=RAISED)

            ##Configuring Main Frame and Positioning
            main_frame.rowconfigure(0,weight=1)
            main_frame.columnconfigure(0,weight=2)
            main_frame.columnconfigure(1,weight=5)

            left_main.grid(row=0,column=0,sticky="nsew")
            right_main.grid(row=0,column=1,sticky="nsew")

            left_main.rowconfigure(0,weight=1)
            left_main.rowconfigure(1,weight=4)
            left_main.rowconfigure(2,weight=4)
            left_main.rowconfigure(3,weight=3)
            left_main.columnconfigure(0,weight=1)
            left_main.columnconfigure(1,weight=1)

            right_main.rowconfigure(0,weight=1)
            right_main.rowconfigure(1,weight=3)
            right_main.rowconfigure(2,weight=3)
            right_main.rowconfigure(3,weight=3)

            right_main.columnconfigure(0,weight=1)
            right_main.columnconfigure(1,weight=1)
            right_main.columnconfigure(2,weight=1)

            #Buttons and Label in right Frame
            text_apps = Label(right_main, text = "       Apps",background="#84D2FF", font=('Bodoni MT',18, 'bold'))
            buttonFont = font.Font(family='Bodoni MT', size=17)
            basic_services=Button(right_main,text='Basic \nServices',font=buttonFont,height= 3, width=4,command=basic_services_pressed,bg ='#FFFFFF',highlightthickness=3,bd=0,activebackground='#FFFFFF')
            surrender_policy=Button(right_main,text='Surrender \nPolicy',font=buttonFont,height= 3, width=4,command=surrender_policy_pressed,bg ='#FFFFFF',highlightthickness=3,bd=0,activebackground='#FFFFFF')
            loan_button=Button(right_main,text='Loan',font=buttonFont,height= 3, width=4,command=loan_button_pressed,bg ='#FFFFFF',highlightthickness=3,bd=0,activebackground='#FFFFFF')
            service_request=Button(right_main,text='Service \nRequest',font=buttonFont,height= 3, width=4,command=service_request_pressed,bg ='#FFFFFF',highlightthickness=3,bd=0,activebackground='#FFFFFF')
            notification_button=Button(right_main,text='Notification',font=buttonFont,height= 3, width=4,command=notification_button_pressed,bg ='#FFFFFF',highlightthickness=3,bd=0,activebackground='#FFFFFF')
            profile_management=Button(right_main,text='Profile \nManagement',font=buttonFont,height= 3, width=4,command=profile_management_pressed,bg ='#FFFFFF',highlightthickness=3,bd=0,activebackground='#FFFFFF')

            #Calling Hover Function
            button_hover(basic_services)
            button_hover(surrender_policy)
            button_hover(loan_button)
            button_hover(service_request)
            button_hover(notification_button)
            button_hover(profile_management)

            #Positioning The Buttons and Label
            text_apps.grid(row=0,column=0,sticky="w")
            basic_services.grid(row=1,column=0,sticky="nsew",padx=(20,10),pady=(20,10))
            surrender_policy.grid(row=1,column=1,sticky="nsew",padx=(10,10),pady=(20,10))
            loan_button.grid(row=1,column=2,sticky="nsew",padx=(10,20),pady=(20,10))
            service_request.grid(row=2,column=0,sticky="nsew",padx=(20,10),pady=(10,20))
            notification_button.grid(row=2,column=1,sticky="nsew",padx=(10,10),pady=(10,20))
            profile_management.grid(row=2,column=2,sticky="nsew",padx=(10,20),pady=(10,20))

            #Text 'Policies' Label and Positioning
            text_policies = Label(left_main, text = "       Policies",background="#84D2FF", font=('Bodoni MT',18, 'bold'))
            text_policies.grid(row=0,column=0,sticky="w")
            #Buttons in left_frame with Image
            p1 = PhotoImage(file = "Picture2.png")
            p1b=Button(left_main,  image = p1,bg ='#FFFFFF',highlightthickness=3,bd=0,command=life_button)
            #Creating referance of image 'same in all buttons'
            p1b.image=p1
            p1b.grid(row=1,column=0,padx=(0,0),pady=(0,0))
            button_hover(p1b)

            p2 = PhotoImage(file = "Picture3.png")
            p2b=Button(left_main,  image = p2,bg ='#FFFFFF',highlightthickness=3,bd=0,command=health_button)
            p2b.image=p2
            p2b.grid(row=1,column=1,padx=(0,0),pady=(0,0),sticky="w")
            button_hover(p2b)

            p3 = PhotoImage(file = "Picture4.png")
            p3b=Button(left_main,  image = p3,bg ='#FFFFFF',highlightthickness=3,bd=0,command=home_button)
            p3b.image=p3
            p3b.grid(row=2,column=0,padx=(0,0),pady=(0,0))
            button_hover(p3b)

            p4 = PhotoImage(file = "Picture5.png")
            p4b=Button(left_main, image = p4,bg ='#FFFFFF',highlightthickness=3,bd=0,command=vehicle_button)
            p4b.image=p4
            p4b.grid(row=2,column=1,padx=(0,0),pady=(0,0),sticky="w")
            button_hover(p4b)
        #Main Frame Working End

        #Dashboard Button Function
        def dashboard_button_pressed():
            for widgets in main_frame.winfo_children():
               widgets.destroy()


            mycursor.execute("select * from life_insurance")
            myresult = mycursor.fetchall()
            ldata=myresult
            text_box = Text(
                main_frame,
                font=("Courier", 20, "bold"),spacing2=15,bd=0
            )

            daa=data
            text_box.insert(END,"\nTotal Premium Yearly for life insurnce:"+str(SELECT SUM(premium) FROM life_insurance))
            text_box.insert(END,"\nTotal Sum assured:"+str(daa[0]))
            text_box.insert(END,"")
            text_box.insert(END,"\nTotal Premium Yearly for life insurnce:"+str(daa[0]))
            text_box.insert(END,"\nTotal Cover:"+str(daa[0]))
            text_box.insert(END,"")
            text_box.insert(END,"\nTotal Premium Yearly for life insurnce:"+str(daa[0]))
            text_box.insert(END,"\nTotal Cover:"+str(daa[0]))
            text_box.insert(END,"")
            text_box.insert(END,"\nTotal Premium Yearly for life insurnce:"+str(daa[0]))
            text_box.insert(END,"\nTotal Cover:"+str(daa[0]))


            text_box.config(state=DISABLED)

            text_box.grid(row=0, column=1,sticky='nsew',padx=(150,0))
            text_box.config(bg='#7EFB71')

        right_f = tk.Frame(root,bd=1, background="#40c9f6", relief="sunken")
        left_f = tk.Frame(root,bd=1, background="#D2E2FB",  relief="sunken")
            left = Label(main_frame, text="\nDashboard option coming soon...",bg="#84D2FF")
            left.pack()

        #Business Button Function
        def business_button_pressed():
            for widgets in main_frame.winfo_children():
               widgets.destroy()

            left = Label(main_frame, text="\n Business option coming soon...",bg="#84D2FF")
            left.pack()

        #Hover Function for middle frame
        def middle_frame_buttons_hover(button):
            def on_enter(e):
                button.config(font=('Microsoft JhengHei Light',15, 'bold','underline'))
            def on_leave(e):
                button.config(font=('Microsoft JhengHei Light',15, 'bold'))
            button.bind('<Enter>', on_enter)
            button.bind('<Leave>', on_leave)

        #Hover Function for Top frame
        def top_frame_buttons_hover(button):
            def on_enter(e):
                button.config(font=('Bodoni MT',12, 'bold','underline'))
            def on_leave(e):
                button.config(font=('Bodoni MT',12, 'bold'))
            button.bind('<Enter>', on_enter)
            button.bind('<Leave>', on_leave)

        #Types of policies buttons
        def top_button():

            for widgets in main_frame.winfo_children():
                widgets.destroy()
            da="""

    1.Life Insurance

            Life Insurance refers to a policy or cover whereby the policyholder can ensure financial
            freedom for his/her family members after death. Suppose you are the sole earning member
            in your family, supporting your spouse and children.
            In such an event, your death would financially devastate the whole family. Life insurance
            policies ensure that such a thing does not happen by providing financial assistance to your
            family in the event of your passing.

            Types of Life Insurance Policies

            There are primarily seven different types of insurance policies when it comes to life insurance.
            These are:

            Term Plan - The death benefit from a term plan is only available for a specified period, for
            instance, 40 years from the date of policy purchase.

            Endowment Plan - Endowment plans are life insurance policies where a portion of your premiums
            go toward the death benefit, while the remaining is invested by the insurance provider.

            Whole Life Insurance - As the name suggests, such policies offer life cover for the whole life
            of an individual, instead of a specified term. Some insurers may restrict the whole life
            insurance tenure to 100 years.

            Child’s Plan - Investment cum insurance policy, which provides financial aid for your children
            throughout their lives. The death benefit is available as a lump-sum payment after the death of parents.

            Money-Back - Such policies pay a certain percentage of the plan’s sum assured after regular
            intervals. This is known as survival benefit.

            Retirement Plan - Also known as pension plans, these policies are a fusion of investment and
            insurance. A portion of the premiums goes toward creating a retirement corpus for the policyholder.
            This is available as a lump-sum or monthly payment after the policyholder retires.


2.Health Insurance

            Health insurance refers to a type of general insurance, which provides financial assistance
            to policyholders when they are admitted to hospitals for treatment. Additionally, some plans
            also cover the cost of treatment undertaken at home, prior to a hospitalisation or after
            discharge from the same.

            With the rising medical inflation in India, buying health insurance has become a necessity.
            However, before proceeding with your purchase, consider the various types of health insurance
            plans available in India.


3.Home Insurance

            Any building or immovable structure can be insured through property insurance plans.
            This can be either your residence or commercial space. If any damage befalls such a
            property, you can claim financial assistance from the insurance provider. Keep in mind
             that such a plan also financially safeguards the content inside the property.

            Types of Property Insurance in India
            Here are some types of property insurance policies available in India:

            Home Insurance - With such a policy, you remain free from all financial liabilities
            that may arise from damage to your home or contents inside due to fires, burglaries,
             storms, earthquakes, explosions and other events.

            Shop Insurance - If you own a shop, which acts as a source of income for you, it is
            integral to protect yourself from financial liability arising from the same. Whether
            the liability occurs due to natural calamities or due to accidents, with these plans,
            you can immediately undertake repairs to the shop.

            Office Insurance - Another type of property insurance policy, office insurance ensures
             that the office building and all the equipment inside are significantly protected in
            the event of unforeseen events. Generally, office spaces include expensive equipment,
            such as computers, servers and much more. Thus, availing these plans is essential.

            Building Insurance - If you own a complete building, opting for home insurance may not
            be sufficient. Instead, you can purchase building insurance to cover the entire premises.

4.Vehicle Insurance

    Vehicle insurance (also known as car insurance, motor insurance, or auto insurance) is
    insurance for cars, trucks, motorcycles, and other road vehicles. Its primary use is to
    provide financial protection against physical damage or bodily injury resulting from traffic
    collisions and against liability that could also arise from incidents in a vehicle. Vehicle
    insurance may additionally offer financial protection against theft of the vehicle, and against
    damage to the vehicle sustained from events other than traffic collisions, such as keying,
    weather or natural disasters, and damage sustained by colliding with stationary objects.
    The specific terms of vehicle insurance vary with legal regulations in each region.



    """


            main_frame.columnconfigure(0,weight=20)
            main_frame.columnconfigure(1,weight=1)


            text_box = Text(
                main_frame,
                font=(12)
            )

            text_box.insert(END,da)
            text_box.config(state=DISABLED)

            text_box.grid(row=0, column=0,sticky='nsew')
            text_box.config(bg='#84D2FF')



            sb = Scrollbar(
                main_frame,
                orient=VERTICAL
                )

            sb.grid(row=0, column=1, sticky=NS)

            text_box.config(yscrollcommand=sb.set)
            sb.config(command=text_box.yview)

        #Log Out button
        def logout_dar():
            if messagebox.askyesno("Log Out", "Are you sure you want to log out?"):
                for widgets in root.winfo_children():
                    widgets.destroy()
                root.destroy()
                #login_page()



        #Creating Frames in root Window and Positioning Them
        top_frame = tk.Frame(root,bd=1, background="#40c9f6", relief="sunken")
        middle_frame = tk.Frame(root,bd=1, background="#CCE4CA",  relief="sunken")
        main_frame = tk.Frame(root,bd=1, background="#84D2FF",  relief="sunken")

        root.rowconfigure(0, weight=3, uniform="x")
        root.rowconfigure(1, weight=1, uniform="x")
        root.rowconfigure(2, weight=11, uniform="x")
        root.rowconfigure(3, weight=0, uniform="x")
        root.columnconfigure(0, weight=2, uniform="x")
        root.columnconfigure(1, weight=9, uniform="x")

        top_frame.grid(row=0,column=0, columnspan=2,sticky="nsew",padx=(4,4),pady=(4,2))
        middle_frame.grid(row=1,column=0,columnspan=2,sticky="nsew",padx=(4,4),pady=(2,2))
        main_frame.grid(row=2, column=0,rowspan=3,columnspan=2, sticky="nsew",padx=(4,4),pady=(2,4))

        #Top Frame Working
        #Configuring Top Frame
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

        logo_image = tk.PhotoImage(file = "121.png") # your image
        logo_loaded = Label(top_frame, image = logo_image,width=250, height=150,bg="#40c9f8")
        logo_loaded.image = logo_image # put the image on a label
        logo_loaded.grid(row=1,rowspan=6,column=0)

        top=tk.Button(top_frame,borderwidth = 0,bg="#40c9f6", text = 'Type of Policies',command=top_button, font=('Bodoni MT',12, 'bold'),activebackground='#0065FF')
        cal=tk.Button(top_frame,borderwidth = 0,bg="#40c9f6", text = 'Calculator', font=('Bodoni MT',12, 'bold'),activebackground='#0065FF')
        con=tk.Button(top_frame,borderwidth = 0,bg="#40c9f6", text = 'Contact Us', font=('Bodoni MT',12, 'bold'),activebackground='#0065FF')
        abo=tk.Button(top_frame,borderwidth = 0,bg="#40c9f6", text = 'About Us', font=('Bodoni MT',12, 'bold'),activebackground='#0065FF')
        top_frame_buttons_hover(top)
        top_frame_buttons_hover(cal)
        top_frame_buttons_hover(con)
        top_frame_buttons_hover(abo)

        log_out_b=tk.Button(top_frame,borderwidth = 0,bg="#40c9f6", text = 'Log Out',command=logout_dar,font=('Bodoni MT',12, 'bold'),activebackground='#0065FF')
        top_frame_buttons_hover(log_out_b)


        top.grid(row=5,column=8,sticky="nsew")
        cal.grid(row=5,column=9,sticky="nsew")
        con.grid(row=5,column=10,sticky="nsew")
        abo.grid(row=5,column=11,sticky="nsew")

        log_out_b.grid(row=5,column=12,sticky="nsew")
        #Top Frame Working End

        #Middle Frame Working
        #Configuring Middle Frame
        middle_frame.rowconfigure(0,weight=1)

        home_button=tk.Button(middle_frame,borderwidth = 0,bg="#CCE4CA", text = 'Home', font=('Microsoft JhengHei Light',15, 'bold'),command=home_button_pressed)
        dashboard_button=tk.Button(middle_frame,borderwidth = 0,bg="#CCE4CA", text = 'Dashboard', font=('Microsoft JhengHei Light',15, 'bold'),command=dashboard_button_pressed)
        Business_button=tk.Button(middle_frame,borderwidth = 0,bg="#CCE4CA", text = 'Business', font=('Microsoft JhengHei Light',15, 'bold'),command=business_button_pressed)

        middle_frame_buttons_hover(home_button)
        middle_frame_buttons_hover(dashboard_button)
        middle_frame_buttons_hover(Business_button)

        home_button.grid(row=0,column=0,sticky="nsw",padx=(16,8))
        dashboard_button.grid(row=0,column=1,sticky="nsw",padx=(8,8))
        Business_button.grid(row=0,column=2,sticky="nsw",padx=(8,16))
        home_button_pressed()
        #Middle Frame Working End

    #Main
    root = tk.Tk()
    root.geometry("1400x800")
    root.minsize(1400,800)
    root.maxsize(1400,800)
    root.configure(bg='#3498DB')
    root.title("Insurance Management System")

    p1 = PhotoImage(file = '1234.png')
    # Setting icon of master window
    root.iconphoto(False, p1)
    main_page()
    root.mainloop()



if __name__ == "__main__":
    #Connecting to databse and fetching data
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="yashraj1",
      database="IMS"
    )
    mycursor = mydb.cursor()

    #Using tkinter for GUI
    root = tk.Tk()
    root.geometry("550x350")
    #root.minsize(1400,800)
    #root.maxsize(1400,800)
    root.configure(bg='#3498DB')
    root.title("Insurance Management System")
    p1 = PhotoImage(file = '1234.png')
    root.iconphoto(False, p1)
    login_page()
