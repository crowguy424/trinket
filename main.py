from tkinter import*
root = Tk()

root.title("LE BAR")

Label(root, text="Title").grid(row=0,column=0)
Label(root, text="Author").grid(row=0,column=2)
Label(root, text="Year").grid(row=1,column=0)
Label(root, text="ISBN").grid(row=1,column=2)

title_text = StringVar()
Entry(root, textvariable=title_text).grid(row=0,column=1)
author_text = StringVar()
Entry(root, textvariable=author_text).grid(row=0,column=3)
year_text = StringVar()
Entry(root, textvariable=year_text).grid(row=1,column=1)
isbn_text = StringVar()
Entry(root, textvariable=isbn_text).grid(row=1,column=3)

list1 = Listbox(root, width=35, height=6)
list1.grid(row=2,rowspan=6,column=0,columnspan=2)

sb1 = Scrollbar(root)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

Button(root, text="Search Entry", width=12).grid(row=2,column=3)
Button(root, text="Add Entry", width=12).grid(row=3,column=3)
Button(root, text="Update Selected", width=12).grid(row=4,column=3)
Button(root, text="Delete Selected", width=12).grid(row=5,column=3)
Button(root, text="Close", width=12).grid(row=6,column=3)

mainloop()