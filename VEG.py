# import tkinter module
###VEG PAGE
from tkinter import *

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