# BIBLE QUOTES PROGRAM

from tkinter import *
import sqlite3

root = Tk()
root.title("Bible Quotes")
root.geometry('550x450')

### Database
# Create a database or connect to one
conn = sqlite3.connect('bible_quotes_database.db')

# Create cursor
c = conn.cursor()

# Create table
# c.execute('''CREATE TABLE bible( 
#             quotes text,
#             book_of text,
#             chapter integer,
#             verse integer
#         	)''')


### Function
# Add Function ---> Add records from user input to bible table 
def add():
	# Create a database or connect to one
	conn = sqlite3.connect('bible_quotes_database.db')
	# Create cursor
	c = conn.cursor()

	# Insert into table
	c.execute("INSERT INTO bible VALUES (:quotes, :book_of, :chapter, :verse)",
				{
				'quotes': quotes_entry.get(),
				'book_of': book_of_entry.get(),
				'chapter': chapter_entry.get(),
				'verse': verse_entry.get()
				}
			)

	# Commit changes
	conn.commit()
	# Close connection
	conn.close()

	# Clear the input text boxes
	quotes_entry.delete(0,END)
	book_of_entry.delete(0,END)
	chapter_entry.delete(0,END)
	verse_entry.delete(0,END)

# Show Function ---> Show records from bible table
def show():
	# Create new window
	show = Tk()
	show.title('Show Records')
	show.geometry('700x700')

	# Create a database or connect to one
	conn = sqlite3.connect('bible_quotes_database.db')
	# Create cursor
	c = conn.cursor()

	# Show all record
	c.execute("SELECT rowid, * FROM bible")
	records = c.fetchall()
	
	show_records = ''
	for record in records:
		show_records += 'ID : ' + str(record[0]) + '\n'
		show_records += str(record[1]) + '\n'
		show_records += str(record[2]) + ' ' + str(record[3]) + ' : ' + str(record[4]) + '\n'
		show_records += '-'*100 + '\n' + '\n'  

	show_label = Label(show, text=show_records, justify=LEFT).grid(row=1, column=0)

	# Commit changes
	conn.commit()
	# Close connection
	conn.close()

# Delete Function ---> Delete records from bible table
def delete():
	# Create a database or connect to one
	conn = sqlite3.connect('bible_quotes_database.db')
	# Create cursor
	c = conn.cursor()

	#Delete from table
	c.execute("DELETE FROM bible WHERE rowid = " + select_id_entry.get())
	
	# Clear the select id box
	select_id_entry.delete(0,END)

	# Commit changes
	conn.commit()
	# Close connection
	conn.close()

# Update Function ---> Update records from bible table
def update():
	# Create a database or connect to one
	conn = sqlite3.connect('bible_quotes_database.db')
	# Create cursor
	c = conn.cursor()

	# Update a record
	c.execute("""UPDATE bible SET
    	quotes = :q,
        book_of = :bo,
        chapter = :c,
        verse = :v

        WHERE rowid = :rowid""",
        {
        'q': quotes_entry_editor.get(),
        'bo': book_of_entry_editor.get(),
        'c': chapter_entry_editor.get(),
        'v': verse_entry_editor.get(),
        'rowid': record_id
        })

	# Commit changes
	conn.commit()
	# Close connection
	conn.close()

	# Close the window
	editor.destroy()

# Edit Function ---> Edit records from bible table
def edit():
	# Create global variable for update function
	global editor
	global record_id

	global quotes_entry_editor
	global book_of_entry_editor
	global chapter_entry_editor
	global verse_entry_editor

	# Create new window
	editor = Tk()
	editor.title('Edit a Record')
	editor.geometry('550x150')
	
	# Create a database or connect to one
	conn = sqlite3.connect('bible_quotes_database.db')
	# Create cursor
	c = conn.cursor()

	# Create label text boxes (label)
	quotes_label = Label(editor, text='Quotes').grid(row=0, column=0, pady=(20,5), padx=20)
	book_of_label = Label(editor, text='Book of').grid(row=1, column=0)
	chapter_label = Label(editor, text='Chapter').grid(row=1, column=2)
	verse_label = Label(editor, text ='Verse').grid(row=1, column=4)

	# Create input text boxes (entry)
	quotes_entry_editor = Entry(editor, width=75)
	quotes_entry_editor.grid(row=0, column=1, columnspan=6, pady=(10,0))
	book_of_entry_editor = Entry(editor, width=25)
	book_of_entry_editor.grid(row=1, column=1, sticky='w')
	chapter_entry_editor = Entry(editor, width=5)
	chapter_entry_editor.grid(row=1, column=3, sticky='w')
	verse_entry_editor = Entry(editor, width=5)
	verse_entry_editor.grid(row=1, column=5, sticky='w')

	# Create loop to fill the entry boxes
	record_id = select_id_entry.get()
	c.execute("SELECT rowid, * FROM bible WHERE rowid = " + record_id)
	records = c.fetchall()
	for record in records:
		quotes_entry_editor.insert(0, record[1])
		book_of_entry_editor.insert(0, record[2])
		chapter_entry_editor.insert(0, record[3])
		verse_entry_editor.insert(0, record[4])

	# Create update record button
	update_button = Button(editor, text='Update Record', command=update).grid(row=3, column=0, columnspan=6, pady=10, padx=10, ipadx=115)

	# Clear the select id box
	select_id_entry.delete(0,END)

	# Commit changes
	conn.commit()
	# Close connection
	conn.close()

# Pick Random Function ---> Get one random quote from bible table
def pick_random():
	# Create a database or connect to one
	conn = sqlite3.connect('bible_quotes_database.db')
	# Create cursor
	c = conn.cursor()

	# Create new window
	qscreen = Tk()
	qscreen.title('QUOTES OF THE DAY')
	qscreen.geometry('550x150')

	# Show one random quote
	c.execute("SELECT rowid, * FROM bible ORDER BY random() LIMIT 1")
	records = c.fetchall()
	quote = ''
	for record in records:
		quote += record[1] + '\n'
		quote += record[2] + ' ' + str(record[3]) + ' : ' + str(record[4])
	show_quote = Label(qscreen, text=quote).grid(row=8, column=0)
	#TODO Formatting text on label

	# Commit changes
	conn.commit()
	# Close connection
	conn.close()

# Create label text boxes (label)
quotes_label = Label(root, text='Quotes').grid(row=0, column=0, pady=(20,5), padx=20)
book_of_label = Label(root, text='Book of').grid(row=1, column=0)
chapter_label = Label(root, text='Chapter').grid(row=1, column=2)
verse_label = Label(root, text ='Verse').grid(row=1, column=4)

# Create input text boxes (entry)
quotes_entry = Entry(root, width=75)
quotes_entry.grid(row=0, column=1, columnspan=6, pady=(20,5))
book_of_entry = Entry(root, width=25)
book_of_entry.grid(row=1, column=1, sticky='w')
chapter_entry = Entry(root, width=5)
chapter_entry.grid(row=1, column=3, sticky='w')
verse_entry = Entry(root, width=5)
verse_entry.grid(row=1, column=5, sticky='w')


# Create add button
add_button = Button(root, text='Add Record', command=add).grid(row=2, column=0, columnspan=6, pady=10, padx=10, ipadx=113)

# Create show button
show_button = Button(root, text='Show Records', command=show).grid(row=3, column=0, columnspan=6, pady=(10,50), padx=10, ipadx=107)

# Create delete button
delete_button = Button(root, text='Delete Record', command=delete).grid(row=5, column=0, columnspan=6, pady=10, padx=10, ipadx=108)

# Create select label and input box
select_id_label = Label(root, text='Select ID').grid(row=4, column=0, columnspan=2)
select_id_entry = Entry(root, width=5)
select_id_entry.grid(row=4, column=1)

# Create last id label
c.execute("SELECT max(rowid) FROM bible")
last_id = c.fetchone()
last_id_label = Label(root, text='Select ID from 1 - ' + str(last_id[0])).grid(row=4, column=2, columnspan=2, sticky='w')

# Create edit button
edit_button = Button(root, text='Edit Record', command=edit).grid(row=6, column=0, columnspan=6, pady=10, padx=10, ipadx=115)

# Create pick random button
pick_random_button = Button(root, text='Quotes of the Day', command=pick_random).grid(row=7, column=0, columnspan=6, pady=(10,30), padx=10, ipadx=100)

# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()





##### NOTES #####

# Window = root, editor, show

#TODO 
# - Formatting text on label
# - Make slider in show window so we can see all the records

