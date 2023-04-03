from tkinter import *
from tkinter import ttk

import calendar

import sqlite3


class login():
    def __init__(self, master):
        
          self.master = master
          self.master.title("Welcome to the room booking")
          self.label2=Label(self.master,text='Welcome to the room booking',fg='black', bg='white').grid(row=1,column=0)

          photo = PhotoImage(file='icons/logo.gif')
          label = Label(image=photo)
          label.image = photo
          label.grid(row=0, column=0)
          
          self.label_1 = Label(self.master, text="Member ID", bg='white')
          self.label_2 = Label(self.master, text="Password", bg='white')
          Mem_id = StringVar()
          pasw = StringVar()
          self.entry_1 = Entry(self.master, textvariable=Mem_id)
          
          self.entry_2 = Entry(self.master, textvariable=pasw, show="*")

          self.label_1.grid(row=3, column=0)
          self.label_2.grid(row=5, column=0)
          self.entry_1.grid(row=4, column=0)
          self.entry_2.grid(row=6, column=0)


          self.logbtn = Button(self.master, text="Login", bg='steel blue',fg='white', command = self._login_btn_clickked)
          self.logbtn.grid(row=8,column=0)          

          self.button5= Button(self.master,text="Register",bg='goldenrod',fg='white',command=self.Register).grid(row=9,column=0)
          self.button6= Button(self.master,text="Exit",bg='sky blue',fg='black',command=self.Exit).grid(row=10,column=0)

          self.msg=Label(self.master ,text='', fg='black',bg='white')
          self.msg.grid(row=11, column=0)

    def _login_btn_clickked(self):
            global ID 
            ID = self.entry_1.get()
            
            password = self.entry_2.get()

            if ID == "" or password == "" :
                self.msg["text"] = "Please Enter Login Details"
                return
            
                


            conn = sqlite3.connect('roombookings.db')
            c = conn.cursor()
        

            sql_query1 = ("""SELECT
                     mem_id,
                     password
                     
                     FROM users
                     
                     """)

            c.execute(sql_query1)
            list = c.fetchall()

            for row in range(len(list)):
                if ID in list[row]:
                    if password in list[row]:
                        if "A" in ID:
                                root4=Toplevel(self.master)
                                myGUI=BookingRecords(root4)
                        elif "U" in ID:
                                root5=Toplevel(self.master)
                                root5.configure(background='white')
                                myGUI=UserPage(root5)
                    else:
                        self.msg["text"] = "Invalid Member ID or Password"
                    
            
            c.close()

    def Exit(self):
        self.master.destroy()

    def Register(self):
        root3=Toplevel(self.master)
        myGUI=CreateAccount(root3)



                        
class UserPage:
    def __init__(self, master):

        scrollbar = Scrollbar(master)
        
        fr = LabelFrame(master, text= 'Add New Booking', bg='white')
        fr.grid(row=0, column=0, sticky='nw')

        T = Text(fr, height=5, width=60, bg='white', fg='black', font=('Helvetica', 10))
        T.insert(END, """These facilities are available as follows:
        Indoor Monday - Friday 6.00pm to 10.00pm
        Outdoor Monday - Friday 6.00pm to 9.00pm
        Saturdays 9.00am to 9.00pm
        Sundays 12.30pm to 6.30pm""")
        T.grid(row=0, column=0, sticky=N)

        

        Label(fr, text='Room:', bg='white').grid(row=1, column=0, sticky=W)
        self.room= StringVar()
        self.room.set("Room")
        option = OptionMenu(fr, self.room, "Community Room", "Sports Hall", "Astro Turf (Full Pitch)", "Astro Turf (Half Pitch)", "Main Hall", "Dining Room", "Small Meeting Room")
        option.grid(row=1, column=1, sticky=W)
        
        
        Label(fr, text='Mem_ID:', bg='white').grid(row=2, column=0,sticky=W)

        self.mem_idfield = Entry(fr)
        self.mem_idfield .grid(row=2, column=1, sticky=W)
        self.mem_idfield .insert(0,ID)
        self.mem_idfield .config(state='readonly')

        Label(fr, text='Time:', bg='white').grid(row=3, column=0,sticky=W)
        self.time= StringVar()
        self.timefield = Entry(fr, textvariable= self.time)
        self.timefield.grid(row=3, column=1, sticky=W)

        Label(fr, text='Date:', bg='white').grid(row=4, column=0,sticky=W)
        self.date= StringVar()
        self.datefield = Entry(fr, textvariable= self.date)
        self.datefield.grid(row=4, column=1, sticky=W)

        Label(fr, text='Duration:', bg='white').grid(row=5, column=0,sticky=W)
        self.number= IntVar()
        self.numberfield = Entry(fr, textvariable= self.number)
        self.numberfield.grid(row=5, column=1, sticky=W)
        
        Button(fr, text= 'Add Record',bg='steel blue',fg='white', command=self.add).grid(row=6, column=0, sticky=E)

        self.msg=Label(fr,text='', fg='red')
        self.msg.grid(row=7, column=0, sticky=W)

        fr2 = LabelFrame(master, text= 'Booking Records', bg='white')
        fr2.grid(row=1, column=0, padx=10,pady=8, sticky=W)


        
        button2 = Button(fr2, text="Show Booking",bg='steel blue',fg='white', command = self.View_Booking).grid(row=1, column=0, sticky=W)
        button3 = Button(fr2, text="Delete Booking",bg='steel blue',fg='white', command = self.Delete).grid(row=2, column=0, sticky=W)

        
        self.tree3 = ttk.Treeview(fr2, columns=("Room", "Time", "Date", "Price"), selectmode="browse", height=100)
        self.tree3.grid(row=4, column=1, columnspan=1, sticky=W)
        self.tree3.heading('#0', text='Booking_ID', anchor=CENTER)
        self.tree3.heading('#1', text='Room', anchor=CENTER )
        self.tree3.heading('#2', text='Time', anchor=CENTER)
        self.tree3.heading('#3', text='Date', anchor=CENTER)
        self.tree3.heading('#4', text='Price', anchor=CENTER)

    def add(self):
        Room = self.room.get()
        if Room == "Community room":
            room = "1A"
        elif Room == "Sports hall":
            room = "2A"
        elif Room == "Astro Turf (Full Pitch)":
            room = "3A"
        elif Room == "Astro Turf (Half Pitch)":
            room = "4A"
        elif Room == "Main Hall":
            room = "5A"
        elif Room == "Dining Room":
            room = "6A"
        elif Room == "Small Meeting Room":
            room = "7A"
        else:
            self.msg["text"] = "Please enter room"
            return
                
        mem = self.mem_idfield.get()
        time = self.timefield.get()
        date = self.datefield.get()
        duration = self.numberfield.get()

    
        if mem == "":
            self.msg["text"] = "Please enter member ID"
            return
        if time == "":
            self.msg["text"] = "Please enter time"
            return
        if date == "":
            self.msg["text"] = "Please enter date"
            return
        if duration == "":
            self.msg["text"] = "Please enter the duration of the booking"
            return
        conn = sqlite3.connect('roombookings.db')
        c = conn.cursor()

        sql_query2 = ("""SELECT
                 booking_id,
                 bookings.time,
                 bookings.date,
                 bookings.room_ID
                 
                 FROM bookings

                 """)

        c.execute(sql_query2)
        list = c.fetchall()

        Available = True

        for row in range(len(list)):
            if (date in list[row]) and (time in list[row]) and (room in list[row]):
                self.msg["text"] = "Booking is not available for this time "
                Available = False
                        
        Price = ("SELECT roomprice FROM rooms WHERE room_ID='%s'"%room)
        c.execute(Price)
        SetPrice = c.fetchone()
        setpriceInt = int(SetPrice[0])
        durationInt = int(duration)
        price = setpriceInt * durationInt
        paid = "No"
                    

        if Available == True:
            c.execute("INSERT INTO bookings VALUES(NULL,?, ?, ?,?,?,?)", (room, mem, time, date, price, paid))
            conn.commit()
            
            self.room.set("Room")
            self.timefield.delete(0, END)
            self.datefield.delete(0, END)
            self.numberfield.delete(0, END)
            self.msg["text"] = "Booking of %s Added" %Room


    def View_Booking(self):
         
         Mem_ID = ID 
         conn = sqlite3.connect('roombookings.db')
         c = conn.cursor()
         sql = ("""SELECT
                 booking_id,
                 bookings.time,
                 bookings.date,
                 bookings.price,
                 users.firstname AS name,
                 users.mem_ID AS id,
                 rooms.room_ID,
                 rooms.roomname AS name
                 
                 FROM bookings

                 INNER JOIN users ON users.mem_ID = bookings.mem_ID
                 INNER JOIN rooms ON rooms.room_ID = bookings.room_ID


                  WHERE bookings.mem_ID=?
                 
        
                 """)
        
         list = c.execute(sql, [(ID)])

        
        
         x = self.tree3.get_children()
         for item in x:
              self.tree3.delete(item)

         for row in list:
                  self.tree3.insert("",0,text=row[0], values=(row[7], row[1], row[2], row[3]))
         c.close()


    def Delete(self):
        try:
            conn = sqlite3.connect('roombookings.db')
            c = conn.cursor()
            Booking = self.tree3.item(self.tree3.selection())['text']
            room_ =  self.tree3.item(self.tree3.selection())['values'][1]
            query = ("DELETE FROM bookings WHERE booking_id='%s'" %Booking)
            c.execute(query)
            conn.commit()
            c.close()
            self.msg["text"] = "Booking for %s Deleted" %room_
            self.View_Booking()
        except IndexError as e:
            self.msg["text"] = "Please Select Item to Delete"
class CreateAccount:
    def __init__(self, master):
        self.master = master
        self.master.title("Welcome to the room booking")
        self.label2=Label(self.master,text='Create An Account',fg='black',font=("Helvetica", 16)).grid(row=0,column=1)

        photo = PhotoImage(file='icons/createaccount.gif')
        label = Label(master, image=photo)
        label.image = photo
        label.grid(row=0, column=0)
             
        self.msg=Label(master, text='', fg='red')
        self.msg.grid(row=17, column=1, sticky=W)
        
        Label(master, text='Member ID:').grid(row=1, column=0,sticky=W,  pady=2)
        mem_ID= StringVar()
        mem_IDfield = Entry(master, textvariable= mem_ID).grid(row=1, column=1, sticky=W, padx=3, pady=2)

        Label(master, text='Firstname:').grid(row=2, column=0,sticky=W,  pady=2)
        firstname= StringVar()
        firstnamefield = Entry(master, textvariable= firstname).grid(row=2, column=1, sticky=W, padx=3, pady=2)
            
        Label(master, text='Surname:').grid(row=3, column=0,sticky=W,  pady=2)
        surname= StringVar()
        surnamefield = Entry(master, textvariable= surname).grid(row=3, column=1, sticky=W,padx=3, pady=2)
            
        Label(master, text='Email:').grid(row=4, column=0,sticky=W,  pady=2)
        email= StringVar()
        emailfield = Entry(master, textvariable= email).grid(row=4, column=1, sticky=W,padx=3, pady=2)
            
        Label(master, text='Telephone:').grid(row=5, column=0,sticky=W,  pady=2)
        phone= StringVar()
        phonefield = Entry(master, textvariable= phone).grid(row=5, column=1, sticky=W, padx=3, pady=2)

        Label(master, text='Password:').grid(row=6, column=0,sticky=W,  pady=2)
        password1= StringVar()
        passwordfield = Entry(master, textvariable= password1, show='*').grid(row=6, column=1, sticky=W, padx=3, pady=2)

        Label(master, text='Confirm Password:').grid(row=7, column=0,sticky=W,  pady=2)
        password2= StringVar()
        passwordfield = Entry(master, textvariable= password2, show='*').grid(row=7, column=1, sticky=W, padx=3, pady=2)

        Label(master, text='Type of user:').grid(row=8, column=0,sticky=W)
        user_type= StringVar()

        r1 = Radiobutton(master, text='Admin', variable=user_type, value="Admin")
        r1.grid(row=8, column=1,sticky=W)
        r2 = Radiobutton(master, text='Staff', variable=user_type, value="Staff")
        r2.grid(row=8, column=2,sticky=W)
        r3 = Radiobutton(master, text='Student', variable=user_type, value="Student")
        r3.grid(row=8, column=3,sticky=W)
            
        upbtn = Button(master, text= 'Sign Up', command=lambda:self.SignUp(mem_ID.get(), user_type.get(), firstname.get(), surname.get(), email.get(), phone.get(), password1.get(), password2.get()))
        upbtn.grid(row=9, column=2, sticky=E)
        exitbn = Button(master, text= 'Exit', command=self.Exit).grid(row=9, column=1, sticky=E)
            

    def SignUp(self, mem_ID, user_type, firstname, surname, email, phone, password1, password2):
            if mem_ID == "":
                self.msg["text"] = "Please Enter Member ID"
                return
            if firstname == "":
                self.msg["text"] = "Please Enter Firstname"
                return
            if surname == "":
                self.msg["text"] = "Please Enter Surname"
                return
            if email == "":
                self.msg["text"] = "Please Enter Email"
                return
            if phone == "":
                self.msg["text"] = "Please Enter Phone"
                return
            if password1 == "":
                self.msg["text"] = "Please Enter Password"
                return
            if password2 == "":
                self.msg["text"] = "Please Re-enter Password"
                return
            

            if password1 == password2:
                password = password1
                try:
                    conn = sqlite3.connect('roombookings.db')
                    c = conn.cursor()
                    c.execute("INSERT INTO users VALUES(?,?,?,?,?,?,?)",(mem_ID, user_type, firstname, surname, email, phone, password) )
                    conn.commit()
                    c.close()
                    self.msg["text"] = "Acccount successfully registered"
                    self.msg.grid(row=9, column=0, sticky=W)
                    
                except sqlite3.IntegrityError as e:
                    self.msg["text"] = "Acccount already exists"
                    

            else:
                self.msg["text"] = "The password does not match"
                self.msg.grid(row=9, column=0, sticky=W)
                
            
    def Exit(self):
        self.master.destroy()
        
class BookingRecords:
    def __init__(self, master):

        self.master = master
        fr3 = LabelFrame(master, text= 'Add New Booking')
        fr3.grid(row=0, column=0, sticky=W)


        Label(fr3, text='Room:').grid(row=1, column=1, sticky=W, pady=2)
        self.room= StringVar()
        self.room.set("Room")
        option = OptionMenu(fr3, self.room, "Community Room", "Sports Hall", "Astro Turf (Full Pitch)", "Astro Turf (Half Pitch)", "Main Hall", "Dining Room", "Small Meeting Room")
        option.grid(row=1, column=2, sticky=W, padx=5, pady=2)
        


        Label(fr3, text='Mem_ID:').grid(row=2, column=1,sticky=W,  pady=2)
        self.mem_id= StringVar()
        self.mem_idfield = Entry(fr3, textvariable= self.mem_id)
        self.mem_idfield.grid(row=2, column=2, sticky=W,padx=5, pady=2)
        
        Label(fr3, text='Time:').grid(row=3, column=1,sticky=W,  pady=2)
        self.time= StringVar()
        self.timefield = Entry(fr3, textvariable= self.time)
        self.timefield.grid(row=3, column=2, sticky=W,padx=5, pady=2)

          
        Label(fr3, text='Date:').grid(row=4, column=1,sticky=W,  pady=2)
        self.date= StringVar()
        self.datefield = Entry(fr3, textvariable= self.date)
        self.datefield.grid(row=4, column=2, sticky=W,padx=5, pady=2)

        Label(fr3, text='Duration (hours):').grid(row=5, column=1,sticky=W,  pady=2)
        self.number= IntVar()
        self.numberfield = Entry(fr3, textvariable= self.number)
        self.numberfield.grid(row=5, column=2, sticky=W,padx=5, pady=2)
        
        Label(fr3, text='Have they paid?').grid(row=6, column=1,sticky=W,  pady=2)
        Paid = StringVar()
        r4 = Radiobutton(fr3, text='Yes', variable=Paid, value="Yes")
        r4.grid(row=6, column=2,sticky=W)
        r5 = Radiobutton(fr3, text='No', variable=Paid, value="No")
        r5.grid(row=6, column=3,sticky=W)

        
        ttk.Button(fr3, text= 'Add Booking', command=lambda:self.create_booking(self.room.get(), self.mem_idfield.get(), self.timefield.get(), self.datefield.get(), Paid.get())).grid(row=7, column=2, sticky=E,padx=5, pady=2)

        fr4 = LabelFrame(master, text= 'Search ')
        fr4.grid(row=1, column=0, padx=0,pady=0, sticky=W)
        
        Label(fr4, text='Please enter name or member ID of user:').grid(row=0, column=0,sticky=W,  pady=2)
        self.search= StringVar()
        self.searchfield = Entry(fr4, textvariable= self.search)
        self.searchfield.grid(row=0, column=1, sticky=W,padx=5, pady=2)

        ttk.Button(fr4, text= 'Find user', command=self.finduser).grid(row=1, column=0, sticky=W)



        
        fr5 = LabelFrame(master, text= 'Create New User ')
        fr5.grid(row=0, column=0, sticky=E)

        Label(fr5, text='Member ID :').grid(row=1, column=1, sticky=W, pady=2)
        self.mem= StringVar()
        self.memfield = Entry(fr5, textvariable=self.mem)
        self.memfield.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        Label(fr5, text='First Name:').grid(row=2, column=1,sticky=W,  pady=2)
        self.first= StringVar()
        self.firstfield = Entry(fr5, textvariable=self.first)
        self.firstfield.grid(row=2, column=2, sticky=W,padx=5, pady=2)

        Label(fr5, text='Surname:').grid(row=3, column=1,sticky=W,  pady=2)
        self.sur= StringVar()
        self.surfield = Entry(fr5, textvariable=self.sur)
        self.surfield.grid(row=3, column=2, sticky=W,padx=5, pady=2)

        Label(fr5, text='Email:').grid(row=4, column=1,sticky=W,  pady=2)
        self.email= StringVar()
        self.emailfield = Entry(fr5, textvariable=self.email)
        self.emailfield.grid(row=4, column=2, sticky=W,padx=5, pady=2)

        Label(fr5, text='Telephone:').grid(row=5, column=1,sticky=W,  pady=2)
        self.phe= StringVar()
        self.phefield = Entry(fr5, textvariable=self.phe)
        self.phefield.grid(row=5, column=2, sticky=W,padx=5, pady=2)

        Label(fr5, text='Password:').grid(row=6, column=1,sticky=W,  pady=2)
        self.pasw= StringVar()
        self.paswfield = Entry(fr5, textvariable=self.pasw)
        self.paswfield.grid(row=6, column=2, sticky=W,padx=5, pady=2)

        Label(fr5, text='Type of user:').grid(row=7, column=1,sticky=W,  pady=2)
        user= StringVar()
        r8 = Radiobutton(fr5, text="Admin", variable=user, value="Admin")
        r8.grid(row=7, column=2, sticky=W)
        r9 = Radiobutton(fr5, text="Staff", variable=user, value="Staff")
        r9.grid(row=7, column=3, sticky=W)
        r10 = Radiobutton(fr5, text="Student", variable=user, value="Student")
        r10.grid(row=7, column=4, sticky=W)

        add_user = ttk.Button(fr5, text="Create User", command =lambda:self.create_user(self.memfield.get(), self.firstfield.get(), self.surfield.get(), self.emailfield.get(), self.phefield.get(), self.paswfield.get(), user.get()))
        add_user.grid(row=8, column=0, sticky=W)

        b2 = ttk.Button(fr3, text="Show Booking", command = self.view_booking).grid(row=0, column=0, sticky=W)
        b3 = ttk.Button(fr3, text="Delete Selected", command = self.delete_booking).grid(row=1, column=0, sticky=W)
        

        fr6 = LabelFrame(master, text= 'Booking Records')

        fr6.grid(row=7, column=0, padx=0,pady=0, sticky=E)
        scrollbary = Scrollbar(orient=VERTICAL)
        scrollbarx = Scrollbar(orient=HORIZONTAL)

        b4 = ttk.Button(fr6, text="Modify Selected", command = self.open_modify_window).grid(row=2, column=0, sticky=W)
        b5 = ttk.Button(fr6, text="Show users", command = self.open_users_window).grid(row=3, column=0, sticky=W)

        self.msg=Label(fr3, text='', fg='red')
        self.msg.grid(row=8, column=1)
        
        
        self.tree = ttk.Treeview(fr6, columns=("Time", "Name", "Room", "Date", "Paid"), selectmode="extended", height=10, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.grid(row=4, column=0, columnspan=1, sticky=W)
        self.tree.heading('#0', text='Booking_ID', anchor=CENTER)
        self.tree.heading('#3', text='Room', anchor=CENTER )
        self.tree.heading('#2', text='Name', anchor=CENTER)
        self.tree.heading('#1', text='Time', anchor=CENTER)
        self.tree.heading('#4', text='Date', anchor=CENTER)
        self.tree.heading('#5', text='Paid', anchor=CENTER)

        self.msg1=Label(fr5, text='', fg='red')
        self.msg1.grid(row=9, column=0)


    def create_user(self, mem, firstname, surname, email, phone, password, usertype):

       
        try:
            if mem == "":
                self.msg1["text"] = "Please Enter member ID"
                return
            if firstname == "":
                self.msg1["text"] = "Please Enter firstname"
                return
            if surname == "":
                self.msg1["text"] = "Please Enter surname"
                return
            if email == "":
                self.msg1["text"] = "Please Enter email"
                return
            if phone == "":
                self.msg1["text"] = "Please Enter phone"
                return
            if password == "":
                self.msg1["text"] = "Please Enter password"
                return
            conn = sqlite3.connect('roombookings.db')
            c = conn.cursor()
            c.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?)",(mem, usertype, firstname, surname, email, phone, password)) 
            conn.commit()

            self.memfield.delete(0, END)
            self.firstfield.delete(0, END)
            self.surfield.delete(0, END)
            self.emailfield.delete(0, END)
            self.phefield.delete(0, END)
            self.paswfield.delete(0, END)
            
            self.msg1["text"] = "Account for %s Added" %firstname

        except sqlite3.IntegrityError as e:
                    self.msg1["text"] = "Member ID already exists"




    def view_booking(self):
        conn = sqlite3.connect('roombookings.db')
        c = conn.cursor()
        sql_query3 = ("""SELECT
                 booking_id,
                 bookings.time,
                 bookings.date,
                 bookings.paid,
                 users.firstname AS name,
                 users.mem_ID AS id,
                 rooms.room_ID,
                 rooms.roomname AS name
                 
                 FROM bookings

                 INNER JOIN users ON users.mem_ID = bookings.mem_ID
                 INNER JOIN rooms ON rooms.room_ID = bookings.room_ID
                 
            

              
                 """)
        
        x = self.tree.get_children()
        for item in x:
             self.tree.delete(item)
        list = c.execute(sql_query3)
        for row in list:
                 self.tree.insert("",0,text=row[0], values=(row[1], row[4], row[7], row[2], row[3]))
        c.close()
        
                
    def delete_booking(self):

            conn = sqlite3.connect('roombookings.db')
            c = conn.cursor()
            Booking_Id = self.tree.item(self.tree.selection())['text']
            room_id = self.tree.item(self.tree.selection())['values'][2]
            query = ("DELETE FROM bookings WHERE booking_id='%s'" %Booking_Id)
            c.execute(query)
            conn.commit()
            c.close()
            self.msg["text"] = "Booking for %s Deleted" %room_id
            self.view_booking()


    def create_booking(self, Room, mem, time, date, paid):
            if Room == "Room":
                self.msg["text"] = "Please Enter room"
                return
            if Room == "Community Room":
                room = "1A"
            elif Room == "Sports Hall":
                room = "2A"
            elif Room == "Astro Turf (Full Pitch)":
                room = "3A"
            elif Room == "Astro Turf (Half Pitch)":
                room = "4A"
            elif Room == "Main Hall":
                room = "5A"
            elif Room == "Dining Room":
                room = "6A"
            elif Room == "Small Meeting Room":
                room = "7A"


            duration = self.numberfield.get()
                
        
            
            if mem == "":
                self.msg["text"] = "Please Enter member ID"
                return
            if time == "":
                self.msg["text"] = "Please Enter time"
                return
            if date == "":
                self.msg["text"] = "Please Enter date"
                return
            if duration == "":
                self.msg["text"] = "Please Enter duration of booking"
                return
            
            conn = sqlite3.connect('roombookings.db')
            c = conn.cursor()

            sql_query4 = ("""SELECT
                 booking_id,
                 bookings.time,
                 bookings.date,
                 bookings.room_ID
                 
                 FROM bookings

                 """)

            c.execute(sql_query4)
            list1 = c.fetchall()

            available = True

            for row in range(len(list1)):
                if (room in list1[row]) and (date in list1[row]) and (time in list1[row]):
                    self.msg["text"] = "Booking is not available for this time "
                    available = False

            setprice = ("SELECT roomprice FROM rooms WHERE room_ID='%s'"%room)
            c.execute(setprice)
            SetPrice = c.fetchone()
            setpriceint = int(SetPrice[0])
            durationint = int(duration)
            price = setpriceint * durationint
            
                       
            
            if available == True:
                c.execute("INSERT INTO bookings VALUES(NULL,?, ?, ?,?,?,?)", (room, mem, time, date, price, paid))
                conn.commit()
                            
                self.room.set("Room")
                self.mem_idfield.delete(0, END)
                self.timefield.delete(0, END)
                self.datefield.delete(0, END)
                self.numberfield.delete(0, END)
                self.msg["text"] = "Booking of %s Added" %Room
                self.view_booking()
                            

            

    def open_modify_window(self):
            try:
                
                
                Booking_ID = self.tree.item(self.tree.selection())['text']
                oldtime = self.tree.item(self.tree.selection())['values'][0]
                oldroom = self.tree.item(self.tree.selection())['values'][2]
                olddate = self.tree.item(self.tree.selection())['values'][3]
                payment = self.tree.item(self.tree.selection())['values'][4]
                Name = self.tree.item(self.tree.selection())['values'][1]

                
                self.tl = Tk()

                self.msg=Label(self.tl, text='', fg='red')
                self.msg.grid(row=10, column=1, sticky=W)
                
                Label(self.tl,text='Booking:').grid(row=0, column=1, sticky=W)
                room = Entry(self.tl)
                room.grid(row=0, column=2, sticky=W)
                room.insert(0,Booking_ID)
                room.config(state='readonly')

                Label(self.tl,text='Name:').grid(row=1, column=1, sticky=W)
                name = Entry(self.tl)
                name.grid(row=1, column=2, sticky=W)
                name.insert(0,Name)
                name.config(state='readonly')
            
            
                Label(self.tl, text='Old Room:').grid(row=2, column=1,sticky=W)
                ope = Entry(self.tl)
                ope.grid(row=2, column=2, sticky=W)
                ope.insert(0,(oldroom))
                ope.config(state='readonly')

                Label(self.tl, text='Old Time:').grid(row=3, column=1,sticky=W)
                time = Entry(self.tl)
                time.grid(row=3, column=2, sticky=W)
                time.insert(0,oldtime)
                time.config(state='readonly')

                Label(self.tl, text='Old Date:').grid(row=4, column=1,sticky=W)
                date = Entry(self.tl)
                date.grid(row=4, column=2, sticky=W)
                date.insert(0,olddate)
                date.config(state='readonly')
            
                Label(self.tl, text='New Room:').grid(row=5, column=1,sticky=W)
                Newrm = StringVar(self.tl)
                Newrm.set("Room")
                option2 = OptionMenu(self.tl, Newrm, "Community Room", "Sports Hall", "Astro Turf (Full Pitch)", "Astro Turf (Half Pitch)", "Main Hall", "Dining Room", "Small Meeting Room")
                option2.grid(row=5, column=2, sticky=W, padx=5, pady=2)
        
                Label(self.tl, text='New Time:').grid(row=6, column=1,sticky=W)
                newtm = StringVar()
                newtm = Entry(self.tl, textvariable=newtm)
                newtm.grid(row=6, column=2, sticky=W)

                Label(self.tl, text='New Date:').grid(row=7, column=1,sticky=W)
                newdt = StringVar()
                newdt = Entry(self.tl, textvariable=newdt)
                newdt.grid(row=7, column=2, sticky=W)

                Label(self.tl, text='Have they paid?:').grid(row=8, column=1,sticky=W)
                havepaid = StringVar()
                r6 = Radiobutton(self.tl, text='Yes', variable=havepaid, value='Yes')
                r6.grid(row=8, column=2, sticky=W)

                r7 = Radiobutton(self.tl, text='No', variable=havepaid, value='No')
                r7.grid(row=8, column=3, sticky=W)

                
                upbtn = ttk.Button(self.tl, text= 'Update Booking', command=lambda:self.update_booking(Newrm.get(), newtm.get(), newdt.get(), havepaid.get(), Booking_ID))
                upbtn.grid(row=9, column=2, sticky=E)
                
                self.tl.mainloop()
            
            except IndexError as e:
                self.msg["text"] = "Please Select Item to Modify"
            
    def update_booking(self, Newrm, newtm, newdt, havepaid, Booking_ID):
            
            if Newrm == "Community Room":
                newrm = "1A"
            elif Newrm == "Sports Hall":
                newrm = "2A"
            elif Newrm == "Astro Turf (Full Pitch)":
                newrm = "3A"
            elif Newrm == "Astro Turf (Half Pitch)":
                newrm = "4A"
            elif Newrm == "Main Hall":
                newrm = "5A"
            elif Newrm == "Dining Room":
                newrm = "6A"
            elif Newrm == "Small Meeting Room":
                newrm = "7A"
            else:
                self.msg["text"] = "Please Enter room"
                return
            
            conn = sqlite3.connect('roombookings.db')
            c = conn.cursor()
            c.execute("UPDATE bookings SET time=?, room_ID=?, date=?, paid=? WHERE booking_id=?" , (newtm, newrm, newdt, havepaid, Booking_ID) )
            conn.commit()
            c.close()
            self.tl.destroy()
            self.msg["text"] = "Booking of %s modified" %Booking_ID
            self.view_booking()

    def finduser(self):
        search = self.searchfield.get()
        conn = sqlite3.connect('roombookings.db')
        c = conn.cursor()

        win = Tk()
        win.title("Search result")
        fr9 = LabelFrame(win, text= 'User ', bg='white')
        fr9.grid(row=0, column=0, sticky=W)

        fr10 = LabelFrame(win, text= 'Paid bookings', bg='white')
        fr10.grid(row=1, column=0, sticky=W)

        fr11 = LabelFrame(win, text= 'Outstanding bookings', bg='white')
        fr11.grid(row=2, column=0, sticky=W)

        self.tree4 = ttk.Treeview(fr9, columns=('User Type','Firstname', 'Surname', 'Email', 'Telephone', 'Password'), selectmode="browse",height=2)
        self.tree4.grid(row=0, column=0, columnspan=1)
        self.tree4.heading('#0', text='Member_ID', anchor=W)
        self.tree4.heading('#1', text='User Type', anchor=W)
        self.tree4.heading('#2', text='Firstname', anchor=W)
        self.tree4.heading('#3', text='Surname', anchor=W)
        self.tree4.heading('#4', text='Email', anchor=W)
        self.tree4.heading('#5', text='Telephone', anchor=W)
        self.tree4.heading('#6', text='Password', anchor=W)

        
        sql_query6 = ("SELECT * FROM users WHERE users.mem_ID='%s'"%search)

        x = self.tree4.get_children()
        for item in x:
             self.tree4.delete(item)
        conn = sqlite3.connect('roombookings.db')
        c = conn.cursor()
        list = c.execute(sql_query6)
        for row in list:
                 self.tree4.insert("",6,text=row[0],values=(row[1], row[2], row[3], row[4], row[5], row[6]))
        

        self.tree5 = ttk.Treeview(fr10, columns=('Venue','Date', 'Time', 'Price'), selectmode="browse", height=5)
        self.tree5.grid(row=0, column=0, columnspan=1)
        self.tree5.heading('#0', text='Booking ID', anchor=CENTER)
        self.tree5.heading('#1', text='Venue', anchor=CENTER)
        self.tree5.heading('#2', text='Date', anchor=CENTER )
        self.tree5.heading('#3', text='Time', anchor=CENTER )
        self.tree5.heading('#4', text='Price', anchor=CENTER)

        sql_query7 = ("""SELECT
                 booking_id,
                 bookings.time,
                 bookings.date,
                 bookings.paid,
                 bookings.price,
                 users.firstname AS name,
                 users.mem_ID AS id,
                 rooms.room_ID,
                 rooms.roomname AS name
                 
                 FROM bookings

                 INNER JOIN users ON users.mem_ID = bookings.mem_ID
                 INNER JOIN rooms ON rooms.room_ID = bookings.room_ID
                 
                 WHERE bookings.paid='Yes' and users.mem_ID='%s'

              
                 """%search)
        
        x = self.tree5.get_children()
        for item in x:
             self.tree5.delete(item)
        conn = sqlite3.connect('roombookings.db')
        c = conn.cursor()
        list = c.execute(sql_query7)
        for row in list:
                 self.tree5.insert("",0,text=row[0],values=(row[8], row[2], row[1], row[4]))
        



        self.tree6 = ttk.Treeview(fr11, columns=('Venue','Date', 'Time', 'Price'), selectmode="browse", height=5)
        self.tree6.grid(row=0, column=0, columnspan=2)
        self.tree6.heading('#0', text='Booking ID', anchor=CENTER)
        self.tree6.heading('#1', text='Venue', anchor=CENTER)
        self.tree6.heading('#2', text='Date', anchor=CENTER )
        self.tree6.heading('#3', text='Time', anchor=CENTER )
        self.tree6.heading('#4', text='Price', anchor=CENTER)

        sql_query8 = ("""SELECT
                 booking_id,
                 bookings.time,
                 bookings.date,
                 bookings.paid,
                 bookings.price,
                 users.firstname AS name,
                 users.mem_ID AS id,
                 rooms.room_ID,
                 rooms.roomname AS name
                 
                 FROM bookings

                 INNER JOIN users ON users.mem_ID = bookings.mem_ID
                 INNER JOIN rooms ON rooms.room_ID = bookings.room_ID
                 
                 WHERE bookings.paid='No' and users.mem_ID='%s'

              
                 """%search)
        
        x = self.tree6.get_children()
        for item in x:
             self.tree6.delete(item)
        conn = sqlite3.connect('roombookings.db')
        c = conn.cursor()
        list = c.execute(sql_query8)
        for row in list:
                 self.tree6.insert("",6,text=row[0],values=(row[8], row[2], row[1], row[4]))
        
        

        Label(fr11, text='Outstanding balance = ',font="bold").grid(row=3, column=1,sticky=N)


        total = 0
        values = self.tree6.get_children()
        for value in values:
             total += float(self.tree6.item(value, 'values')[3])
             
        outstanding_balance = total
        
        balance = Entry(fr11,font="bold")
        balance.insert(0,outstanding_balance)
        balance.config(state='readonly')
        balance.grid(row=3, column=1, sticky=E)


        c.close()

        win.mainloop()

    def open_users_window(self):

        self.t2 = Tk()
        self.t2.title("View users")

      
        fr7 = LabelFrame(self.t2, text= 'Users', bg='white')
        fr7.grid(row=0, column=0, sticky=W)

        self.msg=Label(fr7, text='', fg='red')
        self.msg.grid(row=1, column=0, sticky=W)

        
        delbtn = ttk.Button(fr7, text="Delete user", command = self.delete_user).grid(row=0, column=0, sticky=W)


        
        fr8 = LabelFrame(self.t2, text= 'Users', bg='white')
        fr8.grid(row=1, column=0, sticky=W)

        self.tree2 = ttk.Treeview(fr8, columns=('Firstname', 'Surname', 'Email', 'Password', 'User Type'), selectmode="extended", height=100)
        self.tree2.grid(row=0, column=0, columnspan=3)
        self.tree2.heading('#0', text='Member_ID', anchor=CENTER)
        self.tree2.heading('#1', text='Firstname', anchor=CENTER )
        self.tree2.heading('#2', text='Surname', anchor=CENTER )
        self.tree2.heading('#3', text='Password', anchor=CENTER)
        self.tree2.heading('#4', text='Email', anchor=CENTER)
        self.tree2.heading('#5', text='User Type', anchor=CENTER)

        sql_query5 = ("""SELECT
                 mem_id,
                 firstname,
                 surname,
                 email,
                 telephone,
                 password,
                 usertype
                 
                 FROM users

                 """)
        
        x = self.tree2.get_children()
        for item in x:
             self.tree2.delete(item)
        conn = sqlite3.connect('roombookings.db')
        c = conn.cursor()
        list = c.execute(sql_query5)
        for row in list:
                 self.tree2.insert("",0,text=row[0],values=(row[1], row[2], row[3], row[5], row[6]))
        c.close()

        self.t2.mainloop()


    def delete_user(self):
        try:
            self.msg["text"] = ""
            conn = sqlite3.connect('roombookings.db')
            c = conn.cursor()
            member_Id = self.tree2.item(self.tree2.selection())['text']
            name = self.tree2.item(self.tree2.selection())['values'][0]
            query4 = ("DELETE FROM users WHERE mem_id='%s'" %member_Id)
            query5 = ("DELETE FROM bookings WHERE mem_ID='%s'" %member_Id)
            c.execute(query4)
            c.execute(query5)
            conn.commit()
            c.close()

            self.msg["text"] = " %s is deleted" %member_Id
            self.view_booking()
            
        except IndexError as e:
            self.msg["text"] = "Please Select Item to Modify"




def main():
    root = Tk()
    root.configure(background='white')
    application = login(root)
    root.mainloop()
if __name__ == '__main__':
    main()
