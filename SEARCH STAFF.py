# Python Program to search string in text using Tkinter

from tkinter import *

# to create a window
root = Tk()

# root window is the parent window
fram = Frame(root)

# adding label to search box
Label(fram, text='STAFF:').pack(side=LEFT)

# adding of single line text box
edit = Entry(fram)

# positioning of text box
edit.pack(side=LEFT, fill=BOTH, expand=1)

# setting focus
edit.focus_set()

# adding of search button
butt = Button(fram, text='Find by Name')
butt.pack(side=RIGHT)
fram.pack(side=TOP)

# text box in root window
text = Text(root)

# text input area at index 1 in text window
text.insert('1.0', '''
RAMYA                               678675646545
RUCHI                               344657689090
NAINIKA                             567698797787
NEHA                                243657687990
ANUPRIYA                            123547689989
SUKRITI                             344657689090
SHIVANI                             567698797787
MEESHO                              243657687990
PRIYA                               123547689989
ANJALI                              344657689090
HANSIKA                             567698797787
AMIESHA                             243657687990
MEGHA                               123547689989
RIYA                                344657689090
SIYA                                567698797787
TANU                                243657687990
NISHI                               123547689989
AVNI                                344657689090
AANAYA                              567698797787
SHREE                               243657687990
SANU                                123547689989
NAVPRIT                             344657689090
JAYA                                567698797787
AMEYA                               243657687990
SHRISTY                             123547689989
ISHA                                344657689090
SHREYA                              567698797787
SHRUTI                              243657687990
TANAYA                              123547689989''')
text.pack(side=BOTTOM)


# function to search string in text
def find():
    # remove tag 'found' from index 1 to END
    text.tag_remove('found', '1.0', END)

    # returns to widget currently in focus
    s = edit.get()
    if s:
        idx = '1.0'
        while 1:
            # searches for desired string from index 1
            idx = text.search(s, idx, nocase=1,
                              stopindex=END)
            if not idx: break

            # last index sum of current index and
            # length of text
            lastidx = '%s+%dc' % (idx, len(s))

            # overwrite 'Found' at idx
            text.tag_add('found', idx, lastidx)
            idx = lastidx

        # mark located string as red
        text.tag_config('found', foreground='red')
    edit.focus_set()


butt.config(command=find)

# mainloop function calls the endless loop of the window,
# so the window will wait for any
# user interaction till we close it
root.mainloop()
