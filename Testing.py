#Libraries
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
import random
import sys
from tkinter import messagebox
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PIL import Image, ImageTk
import time
import pymysql
from datetime import datetime
import os
import time
import board
import busio
from digitalio import DigitalInOut, Direction
import adafruit_fingerprint
import serial

# import cv2
# import numpy as np 
# import face_recognition
# import os
# from datetime import datetime
# import pyrebase

uart = serial.Serial("/dev/ttyS0", baudrate=57600, timeout=1)
finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)


#conencting to database
conn = pymysql.connect(host='localhost', user='localuser1', password='rootuser', database='sensordb')
cursor = conn.cursor()


Mainscreen = Tk()
Mainscreen.title("Health Monitoring System")
Mainscreen.configure(background="bisque")

width = 1200
height = 800
screen_width = Mainscreen.winfo_screenwidth()
screen_height = Mainscreen.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
Mainscreen.geometry('%dx%d+%d+%d' % (width, height, x, y))




# ==================================main program functioning===========================================================
def ExistingStudent():
    myvar = c1.get()
    if myvar.isdigit() == True:    
        if len(str((myvar))) <= 10 and len(str((myvar))) > 9 :
            entry = cursor.execute(f"SELECT * from STUDENT where STU_ID = {myvar}")
            conn.commit()
            if entry != 0:
                #fetching data from database
                cursor.execute(f"SELECT STU_NAME from STUDENT where STU_ID = {myvar}")
                fetchname = cursor.fetchone()
                
                cursor.execute(f"SELECT STU_ID from STUDENT where STU_ID = {myvar}")
                fetchid = cursor.fetchone()
                
                cursor.execute(f"SELECT STU_MAIL from STUDENT where STU_ID = {myvar}")
                fetchmail = cursor.fetchone()
            screen1 = Tk()
            screen1.title("Student Data")
            width = 1200
            height = 800
            screen_width = screen1.winfo_screenwidth()
            screen_height = screen1.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            screen1.geometry('%dx%d+%d+%d' % (width, height, x, y))
            main_title = Label(screen1, text='Displaying Student Data', font=('Arial', 50), fg='red', background="bisque")
            main_title.place(x=160, y=0)
            namelabel = Label(screen1, text='Student Name: ', font=('Arial', 40), fg='red')
            namelabel.place(x=50, y=150)
            disp_name = Label(screen1, text=fetchname, font=('Arial', 40), fg='red')
            disp_name.place(x=500, y=150)
            idlabel = Label(screen1, text='Student ID: ', font=('Arial', 40), fg='red')
            idlabel.place(x=50, y=250)
            disp_id = Label(screen1, text=fetchid , font=('Arial', 40), fg='red')
            disp_id.place(x=500, y=250)
            maillabel = Label(screen1, text='Guardian mail: ', font=('Arial', 40), fg='red')
            maillabel.place(x=50, y=350)
            disp_mail = Label(screen1, text=fetchmail, font=('Arial', 40), fg='red')
            disp_mail.place(x=500, y=350)
            
            StartCheck = Label(screen1, text='Start Checkup: ', font=('Arial', 40), fg='red')
            StartCheck.place(x=50, y=450)
    
    
    # ================================================== PREVIOUS RECORD =======================================
    
        def prevrecords():
            screen1 = Tk()
            screen1.title("Student Previous Data")
            width = 1200
            height = 800
            screen_width = screen1.winfo_screenwidth()
            screen_height = screen1.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            screen1.geometry('%dx%d+%d+%d' % (width, height, x, y))
            
            s_name = Label(screen1, text='Student Previous Data', font=('Arial', 50), fg='red')
            s_name.place(x=40, y=0)
            s_name = Label(screen1, text='Student Name: ', font=('Arial', 40), fg='red')
            s_name.place(x=50, y=100)
            name_out = Label(screen1, text=fetchname, font=('Arial', 40), fg='red')
            name_out.place(x=500, y=100)

            s_id = Label(screen1, text='Student ID: ', font=('Arial', 40), fg='red')
            s_id.place(x=50, y=200)
            id_out = Label(screen1, text=fetchid, font=('Arial', 40), fg='red')
            id_out.place(x=500, y=200)

            sen1 = Label(screen1, text='SPO2: ', font=('Arial', 40), fg='red')
            sen1.place(x=50, y=300)
            cursor.execute(f"SELECT SPO2 from SENSORDATA where STU_ID = {myvar}")
            fetchspo2 = cursor.fetchone()
            sen1_out = Label(screen1, text=fetchspo2, font=('Arial', 40), fg='red')
            sen1_out.place(x=500, y=300)

            sen2 = Label(screen1, text='TEMPERATURE: ', font=('Arial', 40), fg='red')
            sen2.place(x=50, y=400)
            cursor.execute(f"SELECT TEMP from SENSORDATA where STU_ID = {myvar}")
            fetchtemp = cursor.fetchone()
            sen2_out = Label(screen1, text=fetchtemp, font=('Arial', 40), fg='red')
            sen2_out.place(x=500, y=400)
            
            sen3 = Label(screen1, text='PULSE: ', font=('Arial', 40), fg='red')
            sen3.place(x=50, y=500)
            cursor.execute(f"SELECT PULSE from SENSORDATA where STU_ID = {myvar}")
            fetchpulse = cursor.fetchone()
            sen3_out = Label(screen1, text=fetchpulse, font=('Arial', 40), fg='red')
            sen3_out.place(x=500, y=500)
            
            sen3 = Label(screen1, text='Time at Checkup: ', font=('Arial', 40), fg='red')
            sen3.place(x=50, y=600)
            cursor.execute(f"SELECT RECORD_DATE from SENSORDATA where STU_ID = {myvar}")
            fetchtime = cursor.fetchone()
            sen3_out = Label(screen1, text=fetchtime, font=('Arial', 40), fg='red')
            sen3_out.place(x=500, y=600)
            entry3 = Button(screen1, text = 'Back', font=('Arial', 40), width=30, command = screen1.destroy)
            entry3.place(x=50, y=700)

        # ==================================== SENSOR's START READING ==============================================
        def StartReading():
            Sensorscreen = Tk()
            Sensorscreen.title("Student Checkup")
            width = 1200
            height = 800
            screen_width = Sensorscreen.winfo_screenwidth()
            screen_height = Sensorscreen.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            Sensorscreen.geometry('%dx%d+%d+%d' % (width, height, x, y))
            tq = Label(Sensorscreen, text='Start Student Checkup', font=('Arial', 50), fg='red', background="bisque")
            tq.place(x=50, y=0)
            tq = Label(Sensorscreen, text='Sensor 1', font=('Arial', 40), fg='red', background="bisque")
            tq.place(x=400, y=150)
            tq = Label(Sensorscreen, text='Sensor Data:', font=('Arial', 40), fg='red', background="bisque")
            tq.place(x=350, y=250)
            tw = Label(Sensorscreen, text='Sensor 2', font=('Arial', 40), fg='red', background="bisque")
            tw.place(x=400, y=450)
            tq = Label(Sensorscreen, text='Sensor Data:', font=('Arial', 40), fg='red', background="bisque")
            tq.place(x=550, y=550)
            tq = Label(Sensorscreen, text='Sensor Data:', font=('Arial', 40), fg='red', background="bisque")
            tq.place(x=200, y=550)
            entry3 = Button(Sensorscreen, text = 'Back', font=('Arial', 40), width=20, command = Sensorscreen.destroy)
            entry3.place(x=250, y=650)
        
        StartButton1 = Button(screen1, text='Start',font=('Arial', 40), fg='red', background="white", width=20, command = StartReading)
        StartButton1.place(x=500, y = 450)
        PreviousData1 = Label(screen1, text='Previous Data: ', font=('Arial', 40), fg='red')
        PreviousData1.place(x=50, y=550)
        PreviousButton1 = Button(screen1, text='Previous record',font=('Arial', 40), width=20, fg='red', background="white", command = prevrecords)
        PreviousButton1.place(x=500, y=550)
        
        entry3 = Button(screen1, text = 'Back', font=('Arial', 40), width=35, command = screen1.destroy)
        entry3.place(x=50, y=650)
                


# ================================== NEW STUDENT ENTRY ====================================================================================================

def Addnew():
    NewStudentscreen = Tk()
    NewStudentscreen.title("New Student Entry")
    width = 1200
    height = 800
    screen_width = NewStudentscreen.winfo_screenwidth()
    screen_height = NewStudentscreen.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    NewStudentscreen.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def submit():
        if len(str(entry2.get())) == 10:
            entry = cursor.execute(f"SELECT * from STUDENT where STU_ID = {entry2.get()}")
            conn.commit()
            if entry == 0:
                path = f"/home/pi/testing/datasets/{str(entry2.get())}"
                os.mkdir(path)
                cursor.execute("INSERT INTO STUDENT(STU_IMAGE, STU_ID, STU_NAME, STU_MAIL) VALUES (%s, %s, %s, %s)", (path, entry2.get(), entry1.get(), entry3.get()))
                conn.commit()
                messagebox.showinfo("Notification", "Student registered successfuly")
            else:
                messagebox.showerror("Error", "Entered ID already exists")
        else:
            messagebox.showerror("Error", "Entered ID is Invalid")
        
    inputname = Label(NewStudentscreen, text='Add new student ', font=('Arial', 50), fg='red', background="bisque")
    inputname.place(x=30, y=0)
    inputname = Label(NewStudentscreen, text='Enter Student Name: ', font=('Arial', 40), fg='red', background="bisque")
    inputname.place(x=50, y=100)
    inputid = Label(NewStudentscreen, text='Enter Student ID: ', font=('Arial', 40), fg='red', background="bisque")
    inputid.place(x=50, y=250)
    inputmail = Label(NewStudentscreen, text='Enter Student Email-ID: ', font=('Arial', 40), fg='red', background="bisque")
    inputmail.place(x=50, y=400)
    entry1 = Entry(NewStudentscreen, font=('Arial', 40), width=10)#, textvariable = e_name)
    entry1.place(x=650, y=100)
    entry1.get()
    entry2 = Entry(NewStudentscreen, font=('Arial', 40), width=10)#textvariable = e_id, )
    entry2.place(x=650, y=250)
    entry2.get()
    entry3 = Entry(NewStudentscreen, font=('Arial', 40), width=10)#, textvariable = e_mail)
    entry3.place(x=650, y=400)
    submitbutton = Button(NewStudentscreen, text='SUBMIT', font=('Arial', 40), fg='red', background="white", width =20, command =lambda: [submit(), Addnewfin()])
    submitbutton.place(x=450, y=500)
    submitbutton = Button(NewStudentscreen, text='BACK', font=('Arial', 40), fg='white', background="red", width =20, command = NewStudentscreen.destroy)
    submitbutton.place(x=380, y=650)
    
    
def Addnewfin():
    NewStudentscreen = Tk()
    NewStudentscreen.title("New Student Entry")
    width = 600
    height = 600
    screen_width = NewStudentscreen.winfo_screenwidth()
    screen_height = NewStudentscreen.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    NewStudentscreen.geometry('%dx%d+%d+%d' % (width, height, x, y))
    inputname = Label(NewStudentscreen, text='Do You Want to Add Finger Print?', font=('Arial', 26), fg='red', background="bisque")
    inputname.place(x=30, y=100)
    submitbutton = Button(NewStudentscreen, text='Yes', font=('Arial', 24), fg='red', background="white", command =lambda: [fun(), NewStudentscreen.destroy()])
    submitbutton.place(x=270, y=320)
    submitbutton1 = Button(NewStudentscreen, text='No', font=('Arial', 24), fg='red', background="white", command = NewStudentscreen.destroy)
    submitbutton1.place(x=350, y=320)
    

def Senddata():
    Print("Send the data to the database")
    spo2 = 0
    temp = 0
    pulse = 0
    
    
def Communicate():
    print("send command to raspberry pi")

def Communicate1():
    print("send command1 to raspberry pi")

def Communicate2():
    print("send command2 to raspberry pi")

def Communicate3():
    print("send command3 to raspberry pi")

def fun():
    def get_fingerprint():
        print("Waiting for image...")
        while finger.get_image() != adafruit_fingerprint.OK:
            pass
        print("Templating...")
        if finger.image_2_tz(1) != adafruit_fingerprint.OK:
            return False
        print("Searching...")
        if finger.finger_search() != adafruit_fingerprint.OK:
            return False
        return True


# pylint: disable=too-many-branches
    def get_fingerprint_detail():
        """Get a finger print image, template it, and see if it matches!
        This time, print out each error instead of just returning on failure"""
        print("Getting image...", end="")
        i = finger.get_image()
        if i == adafruit_fingerprint.OK:
            print("Image taken")
        else:
            if i == adafruit_fingerprint.NOFINGER:
                print("No finger detected")
            elif i == adafruit_fingerprint.IMAGEFAIL:
                print("Imaging error")
            else:
                print("Other error")
            return False

        print("Templating...", end="")
        i = finger.image_2_tz(1)
        if i == adafruit_fingerprint.OK:
            print("Templated")
        else:
            if i == adafruit_fingerprint.IMAGEMESS:
                print("Image too messy")
            elif i == adafruit_fingerprint.FEATUREFAIL:
                print("Could not identify features")
            elif i == adafruit_fingerprint.INVALIDIMAGE:
                print("Image invalid")
            else:
                print("Other error")
            return False

        print("Searching...", end="")
        i = finger.finger_fast_search()
        # pylint: disable=no-else-return
        # This block needs to be refactored when it can be tested.
        if i == adafruit_fingerprint.OK:
            print("Found fingerprint!")
            return True
        else:
            if i == adafruit_fingerprint.NOTFOUND:
                print("No match found")
            else:
                print("Other error")
            return False


# pylint: disable=too-many-statements
    def enroll_finger(location):
        """Take a 2 finger images and template it, then store in 'location'"""
        for fingerimg in range(1, 3):
            if fingerimg == 1:
                print("Place finger on sensor...", end="")
            else:
                print("Place same finger again...", end="")

            while True:
                i = finger.get_image()
                if i == adafruit_fingerprint.OK:
                    print("Image taken")
                    break
                if i == adafruit_fingerprint.NOFINGER:
                    print(".", end="")
                elif i == adafruit_fingerprint.IMAGEFAIL:
                    print("Imaging error")
                    return False
                else:
                    print("Other error")
                    return False

            print("Templating...", end="")
            i = finger.image_2_tz(fingerimg)
            if i == adafruit_fingerprint.OK:
                print("Templated")
            else:
                if i == adafruit_fingerprint.IMAGEMESS:
                    print("Image too messy")
                elif i == adafruit_fingerprint.FEATUREFAIL:
                    print("Could not identify features")
                elif i == adafruit_fingerprint.INVALIDIMAGE:
                    print("Image invalid")
                else:
                    print("Other error")
                return False

            if fingerimg == 1:
                print("Remove finger")
                time.sleep(1)
                while i != adafruit_fingerprint.NOFINGER:
                    i = finger.get_image()

        print("Creating model...", end="")
        i = finger.create_model()
        if i == adafruit_fingerprint.OK:
            print("Created")
        else:
            if i == adafruit_fingerprint.ENROLLMISMATCH:
                print("Prints did not match")
            else:
                print("Other error")
            return False

        print("Storing model #%d..." % location, end="")
        i = finger.store_model(location)
        if i == adafruit_fingerprint.OK:
            print("Stored")
        else:
            if i == adafruit_fingerprint.BADLOCATION:
                print("Bad storage location")
            elif i == adafruit_fingerprint.FLASHERR:
                print("Flash storage error")
            else:
                print("Other error")
            return False

        return True


    ##################################################


    def get_num():
        """Use input() to get a valid number from 1 to 127. Retry till success!"""
        i = 0
        while (i > 127) or (i < 1):
            try:
                i = int(input("Enter ID # from 1-127: "))
            except ValueError:
                pass
        return i


    print("----------------")
    if finger.read_templates() != adafruit_fingerprint.OK:
        raise RuntimeError("Failed to read templates")
    print("Fingerprint templates:", finger.templates)
    print("e) enroll print")
    print("f) find print")
    print("d) delete print")
    print("----------------")
    c = input("> ")

    if c == "e":
        enroll_finger(get_num())
        screen1 = Tk()
        screen1.title("Student Data")
        width = 350
        height = 150
        screen_width = screen1.winfo_screenwidth()
        screen_height = screen1.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        screen1.geometry('%dx%d+%d+%d' % (width, height, x, y))
        t2 = Label(screen1, text='Finger print is Added :', font=('Arial', 22), background="bisque")
        t2.place(x=20, y=0)
        il = Button(screen1, text='OK',font=('Arial', 20), fg='red', background="white", command = screen1.destroy)
        il.place(x=150, y=70)
        screen1.destroy
        
    if c == "f":
        if get_fingerprint():
            print("Detected #", finger.finger_id, "with confidence", finger.confidence)
            screen1 = Tk()
            screen1.title("Student Data")
            width = 350
            height = 150
            screen_width = screen1.winfo_screenwidth()
            screen_height = screen1.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            screen1.geometry('%dx%d+%d+%d' % (width, height, x, y))
            t2 = Label(screen1, text='Finger print is found :', font=('Arial', 22), background="bisque")
            t2.place(x=20, y=0)
            il = Button(screen1, text='OK',font=('Arial', 20), fg='red', background="white", command = screen1.destroy)
            il.place(x=150, y=70)
        else:
            print("Finger not found")
    if c == "d":
        if finger.delete_model(get_num()) == adafruit_fingerprint.OK:
            print("Deleted!")
        else:
            print("Failed to delete")
    

# def searchfinger():
#     
#     
# def Addfinger():
    
# ===============================****** MAIN SCREEN *******================================================
sc1 = StringVar('')
t1 = Label(Mainscreen, text='Health Monitoring System', font=('Arial', 50), fg='red', background="bisque")
t1.place(x=210, y=0)
t2 = Label(Mainscreen, text='Start with Finger print', font=('Arial', 40), background="bisque")
t2.place(x=120, y=200)
il = Button(Mainscreen, text='Start',font=('Arial', 40), fg='red', background="white", command = fun)
il.place(x=700, y=195)
t4 = Label(Mainscreen, text='Enter Student ID: ', font=('Arial', 40),  fg='black', background="bisque")
t4.place(x=120, y=350)
c1 = Entry(Mainscreen, font=('Arial', 40), width=10)
c1.place(x=600, y=350)
b = Button(Mainscreen, text='OK', font=('Arial', 40), fg='red', background="white", command = ExistingStudent)
b.place(x=960, y=350)
t5 = Label(Mainscreen, text='Add New Student ', font=('Arial', 40),  fg='black', background="bisque")
t5.place(x=120, y=500)
b = Button(Mainscreen, text='YES', font=('Arial', 40), fg='red', background="white", command = Addnew)
b.place(x=600, y=500)
b = Button(Mainscreen, text='EXIT', font=('Arial', 40), width=31, fg='white', background="red", command = Mainscreen.destroy)
b.place(x=120, y=650)



Mainscreen.mainloop()


# ======== DATABASE PROGRAM ==========================================================================


# partypopper = chr(0x1f389)

# while True:
	# print("==== Choose an Option ====")
	# print("1. Add a new Student")
	# print("2. Add values")
	# print("3. Show Values")
	# print("PRESS 0 TO EXIT \n")
	# i = int(input("Option: "))

	# #Exiting the program
	# if i == 0:
		# print("\n ==> BYE .......")
		# break

	# #for a new student
	# elif i == 1:
		# print("\n * ====== NEW ENTRY MENU ====== *")
		# rno = input("--> Student ID: ")
		# path = f'/home/pi/testing/{rno}'
		# os.mkdir(path)
		# name = input("--> Student Name: ")
		# mail = input("--> Enter a valid e-mail address: ")
		# try:
			# cursor.execute("INSERT INTO STUDENT (STU_IMAGE, STU_ID, STU_NAME, STU_MAIL) VALUES (%s, %s, %s, %s)", (path, rno, name, mail))
			# conn.commit()
			# print(f"$$ New Entry Added Sucessfully {partypopper} {partypopper} \n")
		# except TypeError:
			# print("==*= Invalid input! Try again =*==")
		# except  FileExistsError:
			# print("==*= File already exists! Try something else =*==")

	# #sensor input based on the above rno
	# elif i == 2:
		# print("\n * ===== VALUES INSERTION ====== *")
		# rno = input("--> Enter an existing roll no.:")
		# try:
			# now = datetime.now()
			# formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
			# time = formatted_date
			# sen1 = input("--> Enter the first value: ")
			# sen2 = input("--> Enter the second value: ")
			# sen3 = input("--> Enter the third value: ")
			# cursor.execute("INSERT INTO SENSORDATA (STU_ID, TEST_TIME, SEN1, SEN2, SEN3) VALUES (%s, %s, %s, %s, %s)", (rno, time, sen1, sen2, sen3))
			# conn.commit()
		# except TypeError:
			# print("==*= Invalid Input! Try again =*==")

	# elif i == 3:
		# print("\n * ====== LAST RECORD ====== *")
		# rno = input("--> Enter the roll no. for the last value: ")
		# cursor.execute("SELECT * FROM SENSORDATA where STU_ID = %s", (rno))
		# output = cursor.fetchone()
		# print(output)
		# conn.commit()

# #exitting
# cursor.close()
# conn.close()

