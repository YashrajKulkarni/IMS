import tkinter as tk
import tkinter.font as font
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector


def main_page():


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

        #Right Frame Buttons Function
        #Basic Services Function
        def basic_services_pressed():
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
        p1b=Button(left_main,  image = p1,bg ='#FFFFFF',highlightthickness=3,bd=0)
        #Creating referance of image 'same in all buttons'
        p1b.image=p1
        p1b.grid(row=1,column=0,padx=(0,0),pady=(0,0))
        button_hover(p1b)

        p2 = PhotoImage(file = "Picture3.png")
        p2b=Button(left_main,  image = p2,bg ='#FFFFFF',highlightthickness=3,bd=0)
        p2b.image=p2
        p2b.grid(row=1,column=1,padx=(0,0),pady=(0,0),sticky="w")
        button_hover(p2b)

        p3 = PhotoImage(file = "Picture4.png")
        p3b=Button(left_main,  image = p3,bg ='#FFFFFF',highlightthickness=3,bd=0)
        p3b.image=p3
        p3b.grid(row=2,column=0,padx=(0,0),pady=(0,0))
        button_hover(p3b)

        p4 = PhotoImage(file = "Picture5.png")
        p4b=Button(left_main, image = p4,bg ='#FFFFFF',highlightthickness=3,bd=0)
        p4b.image=p4
        p4b.grid(row=2,column=1,padx=(0,0),pady=(0,0),sticky="w")
        button_hover(p4b)
    #Main Frame Working End

    #Dashboard Button Function
    def dashboard_button_pressed():
        for widgets in main_frame.winfo_children():
     	   widgets.destroy()

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
        da1="""
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
        This is available as a lump-sum or monthly payment after the policyholder retires."""


        da2="""

                                         2. Health Insurance


        Health insurance refers to a type of general insurance, which provides financial assistance
        to policyholders when they are admitted to hospitals for treatment. Additionally, some plans
        also cover the cost of treatment undertaken at home, prior to a hospitalisation or after
        discharge from the same.

        With the rising medical inflation in India, buying health insurance has become a necessity.
        However, before proceeding with your purchase, consider the various types of health insurance
        plans available in India."""


        da3="""

                                            3.Property Insurance


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


        """


        main_frame.columnconfigure(0,weight=20)
        main_frame.columnconfigure(1,weight=1)


        text_box = Text(
            main_frame,
            font=(12)
        )
        #text_box.tag_configure("tag_name", justify='center')
        text_box.insert(END,da1)
        #text_box.config(font=('times new roman',12,'bold'))
        text_box.insert(END,da2)
        text_box.insert(END,da3)



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

    top=tk.Button(top_frame,borderwidth = 0,bg="#40c9f6", text = 'Type of Policies',command=top_button ,font=('Bodoni MT',12, 'bold'),activebackground='#0065FF')
    cal=tk.Button(top_frame,borderwidth = 0,bg="#40c9f6", text = 'Calculator', font=('Bodoni MT',12, 'bold'),activebackground='#0065FF')
    con=tk.Button(top_frame,borderwidth = 0,bg="#40c9f6", text = 'Contact Us', font=('Bodoni MT',12, 'bold'),activebackground='#0065FF')
    abo=tk.Button(top_frame,borderwidth = 0,bg="#40c9f6", text = 'About Us', font=('Bodoni MT',12, 'bold'),activebackground='#0065FF')
    top_frame_buttons_hover(top)
    top_frame_buttons_hover(cal)
    top_frame_buttons_hover(con)
    top_frame_buttons_hover(abo)

    log_out_b=tk.Button(top_frame,borderwidth = 0,bg="#40c9f6", text = 'Log Out',command=top_button ,font=('Bodoni MT',12, 'bold'),activebackground='#0065FF')

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
