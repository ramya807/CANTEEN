# import tkinter module
from tkinter import *

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
			total += int(val[0].get())*val[1]

	label16 = Label(window,
					text="Your Total Bill is - "+str(total),
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
