from tkinter import *


roota = Tk()
roota.title("COMPUTERISATION OF CANTEEN MANAGEMENT")  # Title of the application
roota.geometry('500x500+400+100')  # Size of the screen
Label(text='CANTEEN MANAGEMENT', fg='red', font=44).pack()  # text size and color of the topic


Chooser = Menu()  # chooser is used for menubar
itemone = Menu()  # itemone is display for the topics which comes under the my-profile
itemone.add_command(label='Login')
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
itemfive.add_command(label='Pending Bill')
itemfive.add_command(label='Paid Bill')

itemsix = Menu()  # itemsix is display for the topics which comes under the room list
itemsix.add_command(label='Floor List')
itemsix.add_command(label='Table List')
itemsix.add_command(label='Table Availability')
itemsix.add_command(label='Update Info')

itemseven = Menu()  # itemseven is display for the topics which comes under the visitor
itemseven.add_command(label='Customer')
itemseven.add_command(label='Staff')

# Used to view in screen all the labels in menubar
Chooser.add_cascade(label='My Profile', menu=itemone)
Chooser.add_cascade(label='Users', menu=itemtwo)
Chooser.add_cascade(label='Canteen Details', menu=itemthree)
Chooser.add_cascade(label='Admin', menu=itemfour)
Chooser.add_cascade(label='Payment List', menu=itemfive)
Chooser.add_cascade(label='Record List', menu=itemsix)
Chooser.add_cascade(label='Search', menu=itemseven)

roota.config(menu=Chooser)
roota.mainloop()
