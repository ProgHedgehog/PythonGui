from tkinter import *

top = Tk()


def onPress(rows, cols):
    for rows in range(rows):
        for columns in range(cols):
            Label(top, text='| element |',
                  borderwidth=2).grid(row=rows + 3, column=columns)


labelColumns = Label(top, text='Колонки').grid(row=0, column=0)
textBoxColumns = Text(top, height=1, width=20, background="grey", foreground="black").grid(row=0, column=1)
labelRows = Label(top, text='Строки').grid(row=0, column=2)
textBoxRows = Text(top, height=1, width=20, background="grey", foreground="black").grid(row=0, column=3)
B = Button(top, text="Create", command=lambda: onPress(textBoxRows.get(1), textBoxColumns.get(1))).grid(row=1, column=1, columnspan=2)

top.mainloop()
