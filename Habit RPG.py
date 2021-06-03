# Habit RPG

from tkinter import *
import sqlite3

window = Tk()

# Create a database or connect to one
conn = sqlite3.connect('habit_database.db')
# Create cursor
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE habit (
			habit text,
			point integer
		)''')

# Create text labels
habit_label = Label(window, text='Habit', ).grid(row=0, column=0)
point_label = Label(window, text='Point').grid(row=1, column=0)

# Create entry boxes
habit_entry = Entry(window)
habit_entry.grid(row=0, column=1)
point_entry = Entry(window)
point_entry.grid(row=1, column=1)


# Commit changes
conn.commit()
# Close connection
conn.close()


window.mainloop()