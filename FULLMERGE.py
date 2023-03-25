from tkinter import *


def func_for_file1():


    roota = Tk()
    roota.title("COMPUTERISATION OF BIT CANTEEN MANAGEMENT")  # Title of the application
    roota.geometry('500x500+400+100')  # Size of the screen
    Label(text='CANTEEN MANAGEMENT', fg='red', font=44).pack()  # text size and color of the topic

    Chooser = Menu()  # chooser is used for menubar
    itemone = Menu()  # itemone is display for the topics which comes under the my-profile
    itemone.add_command(label='Login', command=func_for_file2)
    itemone.add_command(label='Customer Details')  # topic one under my-profile
    itemone.add_command(label='Update Details')  # topic two under my-profile

    itemtwo = Menu()  # itemtwo is display for the topics which comes under the users
    itemtwo.add_command(label='Customer Info')
    itemtwo.add_command(label='Upload Photo')
    itemtwo.add_command(label='Add Customer')

    itemthree = Menu()  # itemthree is display for the topics which comes under the hostels
    itemthree.add_command(label='Staff Records')
    itemthree.add_command(label='Customer Records')

    itemfour = Menu()  # itemfour is display for the topics which comes under the warden
    itemfour.add_command(label='Transaction List')
    itemfour.add_command(label='Food item List')

    itemfive = Menu()  # itemfive is display for the topics which comes under the payment list
    itemfive.add_command(label='Pending Bill',command=func_for_file3 )
    itemfive.add_command(label='Paid Bill', command=func_for_file3)

    itemsix = Menu()  # itemsix is display for the topics which comes under the room list
    itemsix.add_command(label='Floor List')
    itemsix.add_command(label='Table List')
    itemsix.add_command(label='Table Availability')
    itemsix.add_command(label='Update Info')

    itemseven = Menu()  # itemseven is display for the topics which comes under the visitor
    itemseven.add_command(label='Customer')
    itemseven.add_command(label='Staff')

    itemeight = Menu()  # itemseven is display for the topics which comes under the visitor
    itemeight.add_command(label='Veg', command=func_for_file4)
    itemeight.add_command(label='Non-Veg', command=func_for_file5)
    itemeight.add_command(label='Straters', command=func_for_file6)

    # Used to view in screen all the labels in menubar
    Chooser.add_cascade(label='My Profile', menu=itemone)
    Chooser.add_cascade(label='Users', menu=itemtwo)
    Chooser.add_cascade(label='Canteen Details', menu=itemthree)
    Chooser.add_cascade(label='Admin', menu=itemfour)
    Chooser.add_cascade(label='Payment List', menu=itemfive)
    Chooser.add_cascade(label='Record List', menu=itemsix)
    Chooser.add_cascade(label='Search', menu=itemseven)
    Chooser.add_cascade(label='Menu', menu=itemeight)

    roota.config(menu=Chooser)
    roota.mainloop()


def func_for_file2():

    import tkinter.messagebox as tkMessageBox
    import sqlite3

    root = Tk()
    root.title("Login")

    width = 640
    height = 480
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    # =======================================VARIABLES=====================================
    USERNAME = StringVar()
    PASSWORD = StringVar()
    FIRSTNAME = StringVar()
    LASTNAME = StringVar()

    # =======================================METHODS=======================================
    def Database():
        global conn, cursor
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, firstname TEXT, lastname TEXT)")

    def LOGOUT():
        result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            root.destroy()
            exit()

    def LoginForm():
        global LoginFrame, lbl_result1
        LoginFrame = Frame(root)
        LoginFrame.pack(side=TOP, pady=80)
        lbl_username = Label(LoginFrame, text="Username:", font=('arial', 25), bd=18)
        lbl_username.grid(row=1)
        lbl_password = Label(LoginFrame, text="Password:", font=('arial', 25), bd=18)
        lbl_password.grid(row=2)
        lbl_result1 = Label(LoginFrame, text="", font=('arial', 18))
        lbl_result1.grid(row=3, columnspan=2)
        username = Entry(LoginFrame, font=('arial', 20), textvariable=USERNAME, width=15)
        username.grid(row=1, column=1)
        password = Entry(LoginFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
        password.grid(row=2, column=1)
        btn_login = Button(LoginFrame, text="LOGIN", font=('arial', 18), width=35, command=Login)
        btn_login.grid(row=4, columnspan=2, pady=20)
        lbl_register = Label(LoginFrame, text="Register", fg="Blue", font=('arial', 12))
        lbl_register.grid(row=0, sticky=W)
        lbl_register.bind('<Button-1>', ToggleToRegister)

    def RegisterForm():
        global RegisterFrame, lbl_result2
        RegisterFrame = Frame(root)
        RegisterFrame.pack(side=TOP, pady=40)
        lbl_username = Label(RegisterFrame, text="Username:", font=('arial', 18), bd=18)
        lbl_username.grid(row=1)
        lbl_password = Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
        lbl_password.grid(row=2)
        lbl_firstname = Label(RegisterFrame, text="Firstname:", font=('arial', 18), bd=18)
        lbl_firstname.grid(row=3)
        lbl_lastname = Label(RegisterFrame, text="Lastname:", font=('arial', 18), bd=18)
        lbl_lastname.grid(row=4)
        lbl_result2 = Label(RegisterFrame, text="", font=('arial', 18))
        lbl_result2.grid(row=5, columnspan=2)
        username = Entry(RegisterFrame, font=('arial', 20), textvariable=USERNAME, width=15)
        username.grid(row=1, column=1)
        password = Entry(RegisterFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
        password.grid(row=2, column=1)
        firstname = Entry(RegisterFrame, font=('arial', 20), textvariable=FIRSTNAME, width=15)
        firstname.grid(row=3, column=1)
        lastname = Entry(RegisterFrame, font=('arial', 20), textvariable=LASTNAME, width=15)
        lastname.grid(row=4, column=1)
        btn_login = Button(RegisterFrame, text="Register", font=('arial', 18), width=35, command=Register)
        btn_login.grid(row=6, columnspan=2, pady=20)
        lbl_login = Label(RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
        lbl_login.grid(row=0, sticky=W)
        lbl_login.bind('<Button-1>', ToggleToLogin)

    def ToggleToLogin(event=None):
        RegisterFrame.destroy()
        LoginForm()

    def ToggleToRegister(event=None):
        LoginFrame.destroy()
        RegisterForm()

    def Register():
        Database()
        if USERNAME.get == "" or PASSWORD.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get == "":
            lbl_result2.config(text="Please complete the required field!", fg="orange")
        else:
            cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (USERNAME.get(),))
            if cursor.fetchone() is not None:
                lbl_result2.config(text="Username is already taken", fg="red")
            else:
                cursor.execute("INSERT INTO `member` (username, password, firstname, lastname) VALUES(?, ?, ?, ?)",
                               (str(USERNAME.get()), str(PASSWORD.get()), str(FIRSTNAME.get()), str(LASTNAME.get())))
                conn.commit()
                USERNAME.set("")
                PASSWORD.set("")
                FIRSTNAME.set("")
                LASTNAME.set("")
                lbl_result2.config(text="Successfully Created!", fg="black")
            cursor.close()
            conn.close()

    def Login():
        Database()
        if USERNAME.get == "" or PASSWORD.get() == "":
            lbl_result1.config(text="Please complete the required field!", fg="orange")
        else:
            cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                lbl_result1.config(text="You Successfully Login", fg="blue")
            else:
                lbl_result1.config(text="Invalid Username or password", fg="red")

    LoginForm()

    # ========================================MENUBAR WIDGETS==================================
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="LOGOUT", command=LOGOUT)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)

    # ========================================INITIALIZATION===================================
    if __name__ == '__main__':
        root.mainloop()


def func_for_file3():
    ### Importing required libraries ###
    ###BILLING OF STARTERS, VEG, NON-VEG, DRINKS###

    import random
    import time
    from tkinter import ttk
    from tkinter import messagebox
    import sqlite3


    # It is definition of System
    def system():
        root = Tk()
        root.geometry("1700x800")
        root.title("Canteen Management System")

        def Database():
            global connectn, cursor
            connectn = sqlite3.connect("Restaurant.db")
            cursor = connectn.cursor()
            # creating bill table
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS Restaurantrecords(ordno text,piz text,bur text,ice text, dr text, ct text,sb text,tax text,sr text,tot text)")

        # variable datatype assignment
        orderno = StringVar()
        pizza = StringVar()
        burger = StringVar()
        icecream = StringVar()
        drinks = StringVar()
        cost = StringVar()
        subtotal = StringVar()
        tax = StringVar()
        service = StringVar()
        total = StringVar()

        # defining total function
        def tottal():
            # fetching the values from entry box
            order = (orderno.get())
            pi = float(pizza.get())
            bu = float(burger.get())
            ice = float(icecream.get())
            dr = float(drinks.get())

            # computing the cost of items

            costpi = pi * 240
            costbu = bu * 125
            costice = ice * 80
            costdr = dr * 60

            # computing the charges
            costofmeal = (costpi + costbu + costice + costdr)
            ptax = ((costpi + costbu + costice + costdr) * 0.18)
            sub = (costpi + costbu + costice + costdr)
            ser = ((costpi + costbu + costice + costdr) / 99)
            str(ptax)
            str(ser)
            overall = str(ptax + ser + sub)

            # Displaying the values
            cost.set(costofmeal)
            tax.set(ptax)
            subtotal.set(sub)
            service.set(ser)
            total.set(overall)

        # defining reset function
        def reset():
            orderno.set("")
            pizza.set("")
            burger.set("")
            icecream.set("")
            drinks.set("")
            cost.set("")
            subtotal.set("")
            tax.set("")
            service.set("")
            total.set("")

        # defining exit function
        def exit():
            root.destroy()

        # Topframe
        topframe = Frame(root, bg="white", width=1600, height=50)
        topframe.pack(side=TOP)

        # Leftframe
        leftframe = Frame(root, width=900, height=700)
        leftframe.pack(side=LEFT)

        # rightframe
        rightframe = Frame(root, width=400, height=700)
        rightframe.pack(side=RIGHT)

        ################## display data ####################
        def DisplayData():
            Database()
            my_tree.delete(*my_tree.get_children())
            cursor = connectn.execute("SELECT * FROM Restaurantrecords")
            fetch = cursor.fetchall()
            for data in fetch:
                my_tree.insert('', 'end', values=(data))
            cursor.close()
            connectn.close()

        style = ttk.Style()
        style.configure("Treeview",
                        foreground="black",
                        rowheight=40,
                        fieldbackground="white"
                        )
        style.map('Treeview',
                  background=[('selected', 'lightblue')])

        ###########  Creating table #############
        my_tree = ttk.Treeview(rightframe)
        my_tree['columns'] = ("ordno", "piz", "bur", "ice", "dr", "ct", "sb", "tax", "sr", "tot")

        ############ creating  for table ################
        horizontal_bar = ttk.Scrollbar(rightframe, orient="horizontal")
        horizontal_bar.configure(command=my_tree.xview)
        my_tree.configure(xscrollcommand=horizontal_bar.set)
        horizontal_bar.pack(fill=X, side=BOTTOM)

        vertical_bar = ttk.Scrollbar(rightframe, orient="vertical")
        vertical_bar.configure(command=my_tree.yview)
        my_tree.configure(yscrollcommand=vertical_bar.set)
        vertical_bar.pack(fill=Y, side=RIGHT)

        # defining column for table
        my_tree.column("#0", width=0, minwidth=0)
        my_tree.column("ordno", anchor=CENTER, width=80, minwidth=25)
        my_tree.column("piz", anchor=CENTER, width=60, minwidth=25)
        my_tree.column("bur", anchor=CENTER, width=50, minwidth=25)
        my_tree.column("ice", anchor=CENTER, width=80, minwidth=25)
        my_tree.column("dr", anchor=CENTER, width=50, minwidth=25)
        my_tree.column("ct", anchor=CENTER, width=50, minwidth=25)
        my_tree.column("sb", anchor=CENTER, width=100, minwidth=25)
        my_tree.column("tax", anchor=CENTER, width=50, minwidth=25)
        my_tree.column("sr", anchor=CENTER, width=100, minwidth=25)
        my_tree.column("tot", anchor=CENTER, width=50, minwidth=25)

        # defining  headings for table
        my_tree.heading("ordno", text="Order No", anchor=CENTER)
        my_tree.heading("piz", text="Starters", anchor=CENTER)
        my_tree.heading("bur", text="Veg", anchor=CENTER)
        my_tree.heading("ice", text="Non-Veg", anchor=CENTER)
        my_tree.heading("dr", text="Drinks", anchor=CENTER)
        my_tree.heading("ct", text="Cost", anchor=CENTER)
        my_tree.heading("sb", text="Subtotal", anchor=CENTER)
        my_tree.heading("tax", text="Tax", anchor=CENTER)
        my_tree.heading("sr", text="Service", anchor=CENTER)
        my_tree.heading("tot", text="Total", anchor=CENTER)

        my_tree.pack()
        DisplayData()

        # defining add function to add record
        def add():
            Database()
            # getting  data
            orders = orderno.get()
            pizzas = pizza.get()
            burgers = burger.get()
            ices = icecream.get()
            drinkss = drinks.get()
            costs = cost.get()
            subtotals = subtotal.get()
            taxs = tax.get()
            services = service.get()
            totals = total.get()
            if orders == "" or pizzas == "" or burgers == "" or ices == "" or drinkss == "" or costs == "" or subtotals == "" or taxs == "" or services == "" or totals == "":
                messagebox.showinfo("Warning", "Please fill the empty field!!!")
            else:
                connectn.execute(
                    'INSERT INTO Restaurantrecords (ordno, piz, bur , ice ,dr ,ct ,sb ,tax, sr, tot) VALUES (?,?,?,?,?,?,?,?,?,?)',
                    (orders, pizzas, burgers, ices, drinkss, costs, subtotals, taxs, services, totals));
                connectn.commit()
                messagebox.showinfo("Message", "Stored successfully")
            # refresh table data
            DisplayData()
            connectn.close()

        # defining function to access data from sqlite datrabase
        def DisplayData():
            Database()
            my_tree.delete(*my_tree.get_children())
            cursor = connectn.execute("SELECT * FROM Restaurantrecords")
            fetch = cursor.fetchall()
            for data in fetch:
                my_tree.insert('', 'end', values=(data))
            cursor.close()
            connectn.close()

        # defining function to delete record
        def Delete():
            # open database
            Database()
            if not my_tree.selection():
                messagebox.showwarning("Warning", "Select data to delete")
            else:
                result = messagebox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                                icon="warning")
            if result == 'yes':
                curItem = my_tree.focus()
                contents = (my_tree.item(curItem))
                selecteditem = contents['values']
                my_tree.delete(curItem)
                cursor = connectn.execute("DELETE FROM Restaurantrecords WHERE ordno= %d" % selecteditem[0])
                connectn.commit()
                cursor.close()
                connectn.close()

        # Time
        localtime = time.asctime(time.localtime(time.time()))
        # Top part
        main_lbl = Label(topframe, font=('Calibri', 25, 'bold'), text="Canteen Management System", fg="Blue",
                         anchor=W)
        main_lbl.grid(row=0, column=0)
        main_lbl = Label(topframe, font=('Calibri', 15,), text=localtime, fg="lightgreen", anchor=W)
        main_lbl.grid(row=1, column=0)

        ### Labels
        # items
        ordlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Order No.", fg="black", bd=5, anchor=W).grid(
            row=1,
            column=0)
        ordtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                       textvariable=orderno).grid(row=1, column=1)
        # Pizza
        pizlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Starters", fg="black", bd=5, anchor=W).grid(row=2,
                                                                                                                  column=0)
        piztxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                       textvariable=pizza).grid(row=2, column=1)
        # burger
        burlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Veg", fg="black", bd=5, anchor=W).grid(row=3,
                                                                                                             column=0)
        burtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                       textvariable=burger).grid(row=3, column=1)

        # icecream
        icelbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Non-Veg", fg="black", bd=5, anchor=W).grid(row=4,
                                                                                                                 column=0)
        icetxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                       textvariable=icecream).grid(row=4, column=1)
        # drinks
        drinklbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Drinks", fg="black", bd=5, anchor=W).grid(row=5,
                                                                                                                  column=0)
        drinktxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                         textvariable=drinks).grid(row=5, column=1)
        # cost
        costlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Cost", bd=5, anchor=W).grid(row=6, column=0)
        costtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                        textvariable=cost).grid(row=6, column=1)
        # subtotal
        sublbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Subtotal", bd=5, anchor=W).grid(row=7, column=0)
        subtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                       textvariable=subtotal).grid(row=7, column=1)
        # tax
        taxlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Tax", bd=5, anchor=W).grid(row=8, column=0)
        taxtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                       textvariable=tax).grid(row=8, column=1)
        # service
        servicelbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Service", bd=5, anchor=W).grid(row=9,
                                                                                                         column=0)
        servicetxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                           textvariable=service).grid(row=9, column=1)
        # total
        totallbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Total", bd=5, anchor=W).grid(row=10,
                                                                                                     column=0)
        totaltxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                         textvariable=total).grid(row=10, column=1)
        # ---button--

        totbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Total", bg="Lightgrey", fg="black", bd=3, padx=5,
                        pady=5,
                        width=6, command=tottal).grid(row=6, column=3)

        resetbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Reset", bg="lightgrey", fg="black", bd=3,
                          padx=5,
                          pady=5, width=6, command=reset).grid(row=4, column=3)

        exitbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Exit The System", bg="lightgrey", fg="black",
                         bd=3, padx=5,
                         pady=5, width=12, command=exit).grid(row=6, column=2)

        addbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Add", bg="lightgrey", fg="black", bd=3, padx=5,
                        pady=5,
                        width=6, command=add).grid(row=2, column=3)

        deletebtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Delete Record", bg="lightgrey", fg="black",
                           bd=3,
                           padx=5, pady=5, width=12, command=Delete).grid(row=4, column=2)

        ########################### feedback form ################################

        def feedbackk():
            feed = Tk()
            feed.geometry("600x500")
            feed.title("Submit Feedback form")
            # database #
            connectn = sqlite3.connect("Restaurant.db")
            cursor = connectn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS FEEDBACK(n text,eid text,feedback5 text,com text)")
            # variable datatype asssignment #
            name = StringVar()
            email = StringVar()
            comments = StringVar()

            # defiing submit function
            def submit():
                n = name.get()
                eid = email.get()
                com = txt.get('1.0', END)
                feedback1 = ""
                feedback2 = ""
                feedback3 = ""
                feedback4 = ""
                if (checkvar1.get() == "1"):
                    feedback1 = "Excellent"
                if (checkvar2.get() == "1"):
                    feedback2 = "Good"
                if (checkvar3.get() == "1"):
                    feedback2 = "Average"
                if (checkvar4.get() == "1"):
                    feedback2 = "Poor"
                feedback5 = feedback1 + " " + feedback2 + " " + feedback3 + " " + feedback4
                conn = sqlite3.connect("Restaurant.db")
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO FEEDBACK VALUES ('" + n + "','" + eid + "','" + com + "','" + feedback5 + "')")
                messagebox.showinfo("message", "data inserted !")
                feed.destroy()

            # defining cancel button
            def cancel():
                feed.destroy()

            # label#
            lb1 = Label(feed, font=("Calisto MT", 15, "bold"), text="Thanks for Visiting!", fg="black").pack(side=TOP)
            lbl2 = Label(feed, font=("calisto MT", 15), text="We're glad you chose us ! Please tell us how it was!",
                         fg="black").pack(side=TOP)
            # name
            namelbl = Label(feed, font=('vardana', 15), text="Name:-", fg="black", bd=10, anchor=W).place(x=10, y=150)
            nametxt = Entry(feed, font=('vardana', 15), bd=6, insertwidth=2, bg="white", justify='right',
                            textvariable=name).place(x=15, y=185)
            # email
            emaillbl = Label(feed, font=('vardana', 15), text="Email:-", fg="black", bd=10, anchor=W).place(x=280,
                                                                                                            y=150)
            emailtxt = Entry(feed, font=('vardana', 15), bd=6, insertwidth=2, bg="white", justify='right',
                             textvariable=email).place(x=285, y=185)
            ###checkbutton
            ratelbl = Label(feed, font=('vardana', 15), text="How would you rate us?", fg="black", bd=10,
                            anchor=W).place(
                x=10, y=215)
            checkvar1 = StringVar()
            checkvar2 = StringVar()
            checkvar3 = StringVar()
            checkvar4 = StringVar()
            c1 = Checkbutton(feed, font=('Calibri', 10, "bold"), text="Excellent", bg="white", variable=checkvar1)
            c1.deselect()
            c1.place(x=15, y=265)
            c2 = Checkbutton(feed, font=('Calibri', 10, "bold"), text="Good", bg="white", variable=checkvar2, )
            c2.deselect()
            c2.place(x=120, y=265)
            c3 = Checkbutton(feed, font=('Calibri', 10, "bold"), text=" Average", bg="white", variable=checkvar3, )
            c3.deselect()
            c3.place(x=220, y=265)
            c4 = Checkbutton(feed, font=('Calibri', 10, "bold"), text="   Poor  ", bg="white", variable=checkvar4, )
            c4.deselect()
            c4.place(x=320, y=265)
            # comments"
            commentslbl = Label(feed, font=('Calibri', 15), text="Comments", fg="black", bd=10, anchor=W).place(x=10,
                                                                                                                y=300)
            txt = Text(feed, width=50, height=5)
            txt.place(x=15, y=335)
            # button
            submit = Button(feed, font=("Calibri", 15), text="Submit", fg="black", bg="green", bd=2,
                            command=submit).place(
                x=145, y=430)
            cancel = Button(feed, font=("Calibri", 15), text="Cancel", fg="black", bg="red", bd=2,
                            command=cancel).place(
                x=245, y=430)
            feed.mainloop()

        # Feedbackbutton
        feedbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Feedback Form", fg="black", bg="lightgrey",
                         bd=3, padx=10,
                         pady=10, width=10, command=feedbackk).grid(row=8, column=2, columnspan=1)

        ##################### Menu card ################################
        def menu():
            roott = Tk()
            roott.title("Price Menu")
            roott.geometry("300x300")
            lblinfo = Label(roott, font=("Calibri", 20, "bold"), text="ITEM LIST", fg="black", bd=10)
            lblinfo.grid(row=0, column=0)
            lblprice = Label(roott, font=("Calibri", 20, "bold"), text="Prices", fg="black", bd=10)
            lblprice.grid(row=0, column=3)
            lblpizza = Label(roott, font=("Calibri", 20, "bold"), text="Pizza", fg="Blue", bd=10)
            lblpizza.grid(row=1, column=0)
            lblpricep = Label(roott, font=("Calibri", 20, "bold"), text="240/-", fg="blue", bd=10)
            lblpricep.grid(row=1, column=3)
            lblburger = Label(roott, font=("Calibri", 20, "bold"), text="Burger", fg="Blue", bd=10)
            lblburger.grid(row=3, column=0)
            lblpriceb = Label(roott, font=("Calibri", 20, "bold"), text="125/-", fg="blue", bd=10)
            lblpriceb.grid(row=3, column=3)
            lblicecream = Label(roott, font=("Calibri", 20, "bold"), text="Ice-Cream", fg="Blue", bd=10)
            lblicecream.grid(row=4, column=0)
            lblpricei = Label(roott, font=("Calibri", 20, "bold"), text="80/-", fg="blue", bd=10)
            lblpricei.grid(row=4, column=3)
            lbldrinks = Label(roott, font=("Calibri", 20, "bold"), text="Drinks", fg="Blue", bd=10)
            lbldrinks.grid(row=5, column=0)
            lblpriced = Label(roott, font=("Calibri", 20, "bold"), text="60/-", fg="blue", bd=10)
            lblpriced.grid(row=5, column=3)
            roott.mainloop()

        # menubutton
        menubtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Menu Card", bg="lightgrey", fg="black", bd=3,
                         padx=6,
                         pady=6, width=12, command=menu).grid(row=2, column=2)

        root.mainloop()

    system()


def func_for_file4():
    # import tkinter module
    ###VEG PAGE


    # make a window
    root = Tk()
    root.title("BITD CANTEEN")
    # specify it's size
    root.geometry("700x600")

    # main title
    label9 = Label(root, text="BITD CANTEEN",
                   font="times 28 bold")
    label9.place(x=580, y=50, anchor="center")

    # Menu Card
    label1 = Label(root, text="VEG",
                   font="times 28 bold")
    label1.place(x=520, y=70)

    label2 = Label(root, text="Aloo Paratha-----Rs 30",
                   font="times 18")
    label2.place(x=450, y=120)

    label3 = Label(root, text="Samosa-----Rs 5",
                   font="times 18")
    label3.place(x=450, y=150)

    label4 = Label(root, text="Pizza-----Rs 150",
                   font="times 18")
    label4.place(x=450, y=180)

    label5 = Label(root, text="Chilli Potato-----Rs 50",
                   font="times 18")
    label5.place(x=450, y=210)

    label6 = Label(root, text="Chowmein-----Rs 70",
                   font="times 18")
    label6.place(x=450, y=240)

    label7 = Label(root, text="Paneer Chilli-----Rs 135",
                   font="times 18")
    label7.place(x=450, y=270)

    label8 = Label(root, text="Mushroom Butter Masala-----Rs 155",
                   font="times 18")
    label8.place(x=450, y=300)

    # closing the main loop
    root.mainloop()


def func_for_file5():
    # import tkinter module


    # make a window
    window = Tk()
    window.title("BITD CANTEEN")
    # specify it's size
    window.geometry("700x600")

    # function to calculate the
    # price of all the orders
    def calculate():

        # dic for storing the
        # food quantity and price
        dic = {'chicken_chilli': [e1, 180],
               'egg_roll': [e2, 75],
               'kabab': [e3, 150],
               'fish_curry': [e4, 200],
               'prawns': [e5, 170],
               'chicken_masala': [e6, 135]
               }
        total = 0
        for key, val in dic.items():
            if val[0].get() != "":
                total += int(val[0].get()) * val[1]

        label16 = Label(window,
                        text="Your Total Bill is - " + str(total),
                        font="times 18")

        # position it
        label16.place(x=20, y=490)
        label16.after(1000, label16.destroy)
        window.after(1000, calculate)

    label8 = Label(window,
                   text="BITD CANTEEN",
                   font="times 28 bold")
    label8.place(x=350, y=20, anchor="center")

    label1 = Label(window,
                   text="Menu",
                   font="times 28 bold")

    label1.place(x=520, y=70)

    label2 = Label(window, text="Chicken Chilli \
    Rs 180", font="times 18")

    label2.place(x=450, y=120)

    label3 = Label(window, text="Egg Roll \
    Rs 75", font="times 18")

    label3.place(x=450, y=150)

    label4 = Label(window, text="Kabab	 \
    Rs 150", font="times 18")
    label4.place(x=450, y=180)

    label5 = Label(window, text="Fish Curry \
    Rs 200", font="times 18")

    label5.place(x=450, y=210)

    label6 = Label(window, text="Prawns \
    Rs 170", font="times 18")

    label6.place(x=450, y=240)

    label7 = Label(window, text="Chicken Masala \
    Rs 135", font="times 18")

    label7.place(x=450, y=270)

    # billing section
    label9 = Label(window, text="Select the items",
                   font="times 18")
    label9.place(x=115, y=70)

    label10 = Label(window,
                    text="Chicken Chilli",
                    font="times 18")
    label10.place(x=20, y=120)

    e1 = Entry(window)
    e1.place(x=20, y=150)

    label11 = Label(window, text="Egg Roll",
                    font="times 18")
    label11.place(x=20, y=200)

    e2 = Entry(window)
    e2.place(x=20, y=230)

    label12 = Label(window, text="Kabab",
                    font="times 18")
    label12.place(x=20, y=280)

    e3 = Entry(window)
    e3.place(x=20, y=310)

    label13 = Label(window,
                    text="Fish Curry",
                    font="times 18")
    label13.place(x=20, y=360)

    e4 = Entry(window)
    e4.place(x=20, y=390)

    label14 = Label(window,
                    text="Prawns",
                    font="times 18")
    label14.place(x=250, y=120)

    e5 = Entry(window)
    e5.place(x=250, y=150)

    label15 = Label(window,
                    text="Chicken Masala",
                    font="times 18")

    label15.place(x=250, y=200)

    e6 = Entry(window)
    e6.place(x=250, y=230)

    # execute calculate function after 1 second
    window.after(1000, calculate)

    # closing the main loop
    window.mainloop()


def func_for_file6():
    ##QUANTITY##

    import tkinter as tk
    from tkinter import ttk
    from tkinter import BOTH, END, LEFT

    menu = {0: ['NOODLES', 45], 1: ['PIZZA', 135], 2: ['BURGER', 160],
            3: ['BISCUIT', 20], 4: ['COFFEE', 50], 5: ['SOFT-DRINK', 35],
            6: ['TEA', 15], 7: ['WATER', 20]}
    sb = []

    my_w = tk.Tk()
    my_w.geometry("1000x800")

    my_w.title("STRATERS AND DRINKS")
    my_w.columnconfigure(0, weight=8)
    my_w.columnconfigure(1, weight=2)
    my_w.rowconfigure(0, weight=1)
    my_w.rowconfigure(1, weight=12)  # change weight to 4
    my_w.rowconfigure(2, weight=1)

    frame_top = tk.Frame(my_w, bg='white')
    frame_bottom = tk.Frame(my_w, bg='white')

    frame_m_right = tk.Frame(my_w, bg='#f8fab4')
    frame_m_left = tk.Frame(my_w, bg='#bfedf2')

    # placing in grid
    frame_top.grid(row=0, column=0, sticky='WENS', columnspan=2)
    frame_m_left.grid(row=1, column=0, sticky='WENS')
    frame_m_right.grid(row=1, column=1, sticky='WENS')
    frame_bottom.grid(row=2, column=0, sticky='WENS', columnspan=2)
    trv = ttk.Treeview(frame_m_right, selectmode='browse')
    trv.grid(row=0, column=0, columnspan=2, padx=3, pady=2)

    # column identifiers
    trv["columns"] = ("1", "2", "3")
    trv.column("#0", width=80, anchor='w')
    trv.column("1", width=60, anchor='w')
    trv.column("2", width=50, anchor='c')
    trv.column("3", width=50, anchor='c')

    # Headings
    # respective columns
    trv.heading("#0", text="Item", anchor='w')
    trv.heading("1", text="Price", anchor='w')
    trv.heading("2", text="qty", anchor='c')
    trv.heading("3", text="Total", anchor='c')

    def my_reset():
        for item in trv.get_children():
            trv.delete(item)
        # for i in range(len(sb)):
        #    sb[i].config(textvariable=0)    # reset spinbox
        l1 = []
        for i in range(8):
            l1.append(tk.IntVar(value=0))
        for i in range(len(sb)):
            print(sb[i].config(textvariable=l1[i]))

        for w in frame_m_right.grid_slaves(1):
            w.grid_remove()
        for w in frame_m_right.grid_slaves(2):
            w.grid_remove()
        for w in frame_m_right.grid_slaves(3):
            w.grid_remove()

    def my_bill():
        total = 0
        for item in trv.get_children():
            trv.delete(item)
        for i in range(len(sb)):
            if (int(sb[i].get()) > 0):
                price = int(sb[i].get()) * menu[i][1]
                total = total + price
                my_str1 = (str(menu[i][1]), str(sb[i].get()), str(price))
                trv.insert("", 'end', iid=i, text=menu[i][0], values=my_str1)
        lr1 = tk.Label(frame_m_right, text='Total', font=font1)
        lr1.grid(row=1, column=0, sticky='nw')
        lr2 = tk.Label(frame_m_right, text=str(total), font=font1)
        lr2.grid(row=1, column=1, sticky='nw')
        lr21 = tk.Label(frame_m_right, text='Tax 10%', font=font1)
        lr21.grid(row=2, column=0, sticky='nw')
        tax = 0.1 * total
        lr22 = tk.Label(frame_m_right, text=str(tax), font=font1)
        lr22.grid(row=2, column=1, sticky='nw')
        lr31 = tk.Label(frame_m_right, text='Total', font=font2)
        lr31.grid(row=3, column=0, sticky='nw')
        final = total + tax
        lr32 = tk.Label(frame_m_right, text=str(final), font=font2)
        lr32.grid(row=3, column=1, sticky='nw')

    # Layout is over , sart placing buttons
    # path_image="G:\\My Drive\\testing\\plus2_restaurant_v1\\images\\"
    font1 = ('Times', 20, 'normal')
    font2 = ('Times', 32, 'bold')
    pdx, pdy = 40, 5
    # img_top = tk.PhotoImage(file = path_image+"restaurant-3.png")
    # bg=tk.PhotoImage(file=path_image+'bg.png')

    # c1 = tk.Canvas(frame_m_left,width=1000,height=500)
    # c1.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='nw',padx=0)
    # c1.create_image(0,0,image=bg,anchor='nw')

    # img_l1 = tk.Label(frame_top,  image=img_top)
    # img_l1.grid(row=0,column=0,sticky='nw',pady=1)

    # img_menu1=tk.PhotoImage(file=path_image+"food-item-1.png")
    # img_menu2=tk.PhotoImage(file=path_image+"food-item-2.png")
    # img_menu3=tk.PhotoImage(file=path_image+"food-item-3.png")
    # img_menu4=tk.PhotoImage(file=path_image+"food-item-4.png")
    # img_menu5=tk.PhotoImage(file=path_image+"food-item-5.png")
    # img_menu6=tk.PhotoImage(file=path_image+"food-item-6.png")
    # img_menu7=tk.PhotoImage(file=path_image+"food-item-7.png")
    # img_menu8=tk.PhotoImage(file=path_image+"food-item-8.png")

    menu1 = tk.Button(frame_m_left, text='NOODLES')
    menu1.grid(row=0, column=0, sticky='nw', padx=pdx, pady=pdy)
    menu2 = tk.Button(frame_m_left, text='PIZZA')
    menu2.grid(row=0, column=1, sticky='nw', padx=pdx, pady=pdy)
    menu3 = tk.Button(frame_m_left, text='BURGER')
    menu3.grid(row=0, column=2, sticky='nw', padx=pdx, pady=pdy)
    menu4 = tk.Button(frame_m_left, text='BISCUIT')
    menu4.grid(row=0, column=3, sticky='nw', padx=pdx, pady=0)
    sv1 = tk.IntVar()
    sb1 = tk.Spinbox(frame_m_left, from_=0, to_=5, font=font1, width=1, textvariable=sv1)
    sb1.grid(row=1, column=0, sticky='nw', padx=pdx, pady=0)
    sb.append(sb1)
    sv2 = tk.IntVar()
    sb2 = tk.Spinbox(frame_m_left, from_=0, to_=5, font=font1, width=1, textvariable=sv2)
    sb2.grid(row=1, column=1, sticky='nw', padx=pdx, pady=0)
    sb.append(sb2)
    sv3 = tk.IntVar()
    sb3 = tk.Spinbox(frame_m_left, from_=0, to_=5, font=font1, width=1, textvariable=sv3)
    sb3.grid(row=1, column=2, sticky='nw', padx=pdx, pady=0)
    sb.append(sb3)
    sv4 = tk.IntVar()
    sb4 = tk.Spinbox(frame_m_left, from_=0, to_=5, font=font1, width=1, textvariable=sv4)
    sb4.grid(row=1, column=3, sticky='nw', padx=pdx, pady=0)
    sb.append(sb4)
    menu5 = tk.Button(frame_m_left, text='COFFEE')
    menu5.grid(row=2, column=0, sticky='nw', padx=pdx, pady=pdy)
    menu6 = tk.Button(frame_m_left, text='SOFT-DRINK')
    menu6.grid(row=2, column=1, sticky='nw', padx=pdx, pady=pdy)
    menu7 = tk.Button(frame_m_left, text='TEA')
    menu7.grid(row=2, column=2, sticky='nw', padx=pdx, pady=pdy)
    menu8 = tk.Button(frame_m_left, text='WATER')
    menu8.grid(row=2, column=3, sticky='nw', padx=pdx, pady=pdy)
    sv5 = tk.IntVar()
    sb5 = tk.Spinbox(frame_m_left, from_=0, to_=5, font=font1, width=1, textvariable=sv5)
    sb5.grid(row=3, column=0, sticky='nw', padx=pdx, pady=pdy)
    sb.append(sb5)
    sv6 = tk.IntVar()
    sb6 = tk.Spinbox(frame_m_left, from_=0, to_=5, font=font1, width=1, textvariable=sv6)
    sb6.grid(row=3, column=1, sticky='nw', padx=pdx, pady=pdy)
    sb.append(sb6)
    sv7 = tk.IntVar()
    sb7 = tk.Spinbox(frame_m_left, from_=0, to_=5, font=font1, width=1, textvariable=sv7)
    sb7.grid(row=3, column=2, sticky='nw', padx=pdx, pady=pdy)
    sb.append(sb7)
    sv8 = tk.IntVar()
    sb8 = tk.Spinbox(frame_m_left, from_=0, to_=5, font=font1, width=1, textvariable=sv8)
    sb8.grid(row=3, column=3, sticky='nw', padx=pdx, pady=pdy)
    sb.append(sb8)
    b1 = tk.Button(frame_m_left, text='Get Bill', command=my_bill)
    b1.grid(row=4, column=1)
    b2 = tk.Button(frame_m_left, text='Confirm ( Reset)', command=my_reset)
    b2.grid(row=4, column=2)
    my_w.mainloop()


def main():
        # Decide what order you want to call these methods.
        func_for_file1()

if __name__ == '__main__':
        main()