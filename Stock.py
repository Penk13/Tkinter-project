# Stock Analysis

from tkinter import *
import sqlite3



window = Tk()
window.title('Stock Analysis')

# Create a database or connect to one
conn = sqlite3.connect('stock_database.db')
# Create cursor
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE IF NOT EXISTS stock(
			code text,	
			total integer,
			var1 integer,
			var2 integer,
			var3 integer,
			var4 integer,
			var5 integer,
			var6 integer,
			var7 integer,
			var8 integer,
			var9 integer,
			var10 integer,
			var11 integer
		)""")


### FUNCTION ###
# Create save function ---> Insert stock and criteria to database
def save():
	# Create a database or connect to one
	conn = sqlite3.connect('stock_database.db')
	# Create cursor
	c = conn.cursor()

	# # Insert to database
	c.execute("INSERT INTO stock VALUES (:code, :total, :var1, :var2, :var3, :var4, :var5, :var6, :var7, :var8, :var9, :var10, :var11)",
				{
				'code': code_entry.get(),
				'total': var1.get() + var2.get() + var3.get() + var4.get() + var5.get() + var6.get() + var7.get() + var8.get() + var9.get() + var10.get() + var11.get(),
				'var1': var1.get(),
				'var2': var2.get(),
				'var3': var3.get(),
				'var4': var4.get(),
				'var5': var5.get(),
				'var6': var6.get(),
				'var7': var7.get(),
				'var8': var8.get(),
				'var9': var9.get(),
				'var10': var10.get(),
				'var11': var11.get()
				}
			)

	# Clear all checkbox
	reset()

	# Commit changes
	conn.commit()
	# Close connection
	conn.close()

# Create reset function ---> Reset stock and criteria checkbox
def reset():
	# Clear all checkbox
	code_entry.delete(0,END)
	var1.set(0)
	var2.set(0)
	var3.set(0)
	var4.set(0)
	var5.set(0)
	var6.set(0)
	var7.set(0)
	var8.set(0)
	var9.set(0)
	var10.set(0)
	var11.set(0)
	select_id_entry.delete(0,END)

# Create show function ---> Show stock and criteria
def show():
	# Create a new window
	show_w = Tk()
	show_w.title('Show Records')

	# Create a database or connect to one
	conn = sqlite3.connect('stock_database.db')
	# Create a cursor
	c = conn.cursor()

	# Show all records
	c.execute("SELECT rowid, * FROM stock")
	records = c.fetchall()
	text = ''
	for record in records:
		text += 'ID : ' + str(record[0]) + '\t|\t'
		text += 'Code : ' + record[1] + '\t|\t'
		text += 'Total : ' + str(record[2])
		text += '\n'
	show_label = Label(show_w, text=text).grid(row=0, column=0)

	# Commit changes
	conn.commit()
	# Close connection
	conn.close()

# Create edit function ---> Edit stock and criteria
def edit():
	# Create global variable for update and delete function
	global selected_code
	global edit_w

	global var1_edit
	global var2_edit
	global var3_edit
	global var4_edit
	global var5_edit
	global var6_edit
	global var7_edit
	global var8_edit
	global var9_edit
	global var10_edit
	global var11_edit

	# Create a new window
	edit_w = Tk()
	edit_w.title('Edit record')

	# Create a database or connect to one
	conn = sqlite3.connect('stock_database.db')
	# Create a cursor
	c = conn.cursor()

	# Create text labels
	selected_code = select_id_entry.get()
	txt = '\t\tCode : ' + selected_code
	code_label = Label(edit_w, text=txt).grid(row=0, column=0, columnspan=2, sticky=W, pady=(20,5))
	criteria_label = Label(edit_w, text='\nCriteria : \n').grid(row=1, column=0, columnspan=2, sticky=W)

	# Create checkboxes (Criteria)
	var1_edit = IntVar()
	var2_edit = IntVar()
	var3_edit = IntVar()
	var4_edit = IntVar()
	var5_edit = IntVar()
	var6_edit = IntVar()
	var7_edit = IntVar()
	var8_edit = IntVar()
	var9_edit = IntVar()
	var10_edit = IntVar()
	var11_edit = IntVar()
	crt1 = Checkbutton(edit_w, text='1. Grafik harga cenderung naik selama 5 tahun', variable=var1_edit)
	crt1.grid(row=2, column=0, columnspan=2, sticky=W)
	crt2 = Checkbutton(edit_w, text='2. Laporan keuangan perusahaan mengalami kenaikan keuntungan setiap tahun', variable=var2_edit)
	crt2.grid(row=3, column=0, columnspan=2, sticky=W)
	crt3 = Checkbutton(edit_w, text='3. Hutang jangka panjang lebih rendah dari ekuitas', variable=var3_edit)
	crt3.grid(row=4, column=0, columnspan=2, sticky=W)
	crt4 = Checkbutton(edit_w, text='4. ROE > 10%', variable=var4_edit)
	crt4.grid(row=5, column=0, columnspan=2, sticky=W)
	crt5 = Checkbutton(edit_w, text='5. Ada dividend', variable=var5_edit)
	crt5.grid(row=6, column=0, columnspan=2, sticky=W)
	crt6 = Checkbutton(edit_w, text='6. PER < 10', variable=var6_edit)
	crt6.grid(row=7, column=0, columnspan=2, sticky=W)
	crt7 = Checkbutton(edit_w, text='7. Book Value Per Share(BVPS) < 1', variable=var7_edit)
	crt7.grid(row=8, column=0, columnspan=2, sticky=W)
	crt8 = Checkbutton(edit_w, text='8. Ekuitas > Market Cap', variable=var8_edit)
	crt8.grid(row=9, column=0, columnspan=2, sticky=W)
	crt9 = Checkbutton(edit_w, text='9. EPS bertumbuh tiap tahun', variable=var9_edit)
	crt9.grid(row=10, column=0, columnspan=2, sticky=W)
	crt10 = Checkbutton(edit_w, text='10. BV > Harga saham sekarang', variable=var10_edit)
	crt10.grid(row=11, column=0, columnspan=2, sticky=W)
	crt11 = Checkbutton(edit_w, text='11. Margin of Safety(MOS) yang besar', variable=var11_edit)
	crt11.grid(row=12, column=0, columnspan=2, sticky=W)

	# Create loop to fill the checkbox
	c.execute("SELECT * FROM stock WHERE code = ?",(selected_code,))
	records = c.fetchall()
	if records[0][2]:
		crt1.select()
	if records[0][3]:
		crt2.select()
	if records[0][4]:
		crt3.select()
	if records[0][5]:
		crt4.select()
	if records[0][6]:
		crt5.select()
	if records[0][7]:
		crt6.select()
	if records[0][8]:
		crt7.select()
	if records[0][9]:
		crt8.select()
	if records[0][10]:
		crt9.select()
	if records[0][11]:
		crt10.select()
	if records[0][12]:
		crt11.select()

	# Create update button
	update_btn = Button(edit_w, text='Update', command=update).grid(row=13, column=0, columnspan=2, pady=(30,10), ipadx=120)

	# Create delete button
	delete_btn = Button(edit_w, text='Delete', command=delete).grid(row=14, column=0, columnspan=2, pady=(10,30), ipadx=125)

	# Clear all checkbox in window 
	reset()

	# Commit changes
	conn.commit()
	# Close connection
	conn.close()

# Create update function ---> Update stock and criteria to database
def update():
	# Create a database or connect to one
	conn = sqlite3.connect('stock_database.db')
	# Create a cursor
	c = conn.cursor()

	#TODO2
	# Update a record
	c.execute("""UPDATE stock SET
		code = :c,
		total = :t,
		var1 = :v1,
		var2 = :v2,
		var3 = :v3,
		var4 = :v4,
		var5 = :v5,
		var6 = :v6,
		var7 = :v7,
		var8 = :v8,
		var9 = :v9,
		var10 = :v10,
		var11 = :v11

		WHERE code = :c""",
		{
				'c': selected_code,
				't': var1_edit.get() + var2_edit.get() + var3_edit.get() + var4_edit.get() + var5_edit.get() + var6_edit.get() + var7_edit.get() + var8_edit.get() + var9_edit.get() + var10_edit.get() + var11_edit.get(),
				'v1': var1_edit.get(),
				'v2': var2_edit.get(),
				'v3': var3_edit.get(),
				'v4': var4_edit.get(),
				'v5': var5_edit.get(),
				'v6': var6_edit.get(),
				'v7': var7_edit.get(),
				'v8': var8_edit.get(),
				'v9': var9_edit.get(),
				'v10': var10_edit.get(),
				'v11': var11_edit.get()
		})

	# Commit changes
	conn.commit()
	# Close connection
	conn.close()

	# Close window
	edit_w.destroy()

# Create delete function ---> Delete stock and criteria from database
def delete():
	# Create a database or connect to one
	conn = sqlite3.connect('stock_database.db')
	# Create a cursor
	c = conn.cursor()

	# Delete a record
	c.execute("DELETE FROM stock WHERE code = ?", (selected_code,))

	# Commit changes
	conn.commit()
	# Close connection
	conn.close()

	# Close window
	edit_w.destroy()


# Create text labels
code_label = Label(window, text='Code').grid(row=0, column=0, sticky=E)
criteria_label = Label(window, text='\nCriteria : \n').grid(row=1, column=0, columnspan=3, sticky=W)

# Create entry boxes
code_entry = Entry(window)
code_entry.grid(row=0, column=1, sticky=W)	

# Create checkboxes (Criteria)
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
crt1 = Checkbutton(window, text='1. Grafik harga cenderung naik selama 5 tahun', variable=var1).grid(row=2, column=0, columnspan=3, sticky=W)
crt2 = Checkbutton(window, text='2. Laporan keuangan perusahaan mengalami kenaikan keuntungan setiap tahun', variable=var2).grid(row=3, column=0, columnspan=3, sticky=W)
crt3 = Checkbutton(window, text='3. Hutang jangka panjang lebih rendah dari ekuitas', variable=var3).grid(row=4, column=0, columnspan=3, sticky=W)
crt4 = Checkbutton(window, text='4. ROE > 10%', variable=var4).grid(row=5, column=0, columnspan=3, sticky=W)
crt5 = Checkbutton(window, text='5. Ada dividend', variable=var5).grid(row=6, column=0, columnspan=3, sticky=W)
crt6 = Checkbutton(window, text='6. PER < 10', variable=var6).grid(row=7, column=0, columnspan=3, sticky=W)
crt7 = Checkbutton(window, text='7. Book Value Per Share(BVPS) < 1', variable=var7).grid(row=8, column=0, columnspan=3, sticky=W)
crt8 = Checkbutton(window, text='8. Ekuitas > Market Cap', variable=var8).grid(row=9, column=0, columnspan=3, sticky=W)
crt9 = Checkbutton(window, text='9. EPS bertumbuh tiap tahun', variable=var9).grid(row=10, column=0, columnspan=3, sticky=W)
crt10 = Checkbutton(window, text='10. BV > Harga saham sekarang', variable=var10).grid(row=11, column=0, columnspan=3, sticky=W)
crt11 = Checkbutton(window, text='11. Margin of Safety(MOS) yang besar', variable=var11).grid(row=12, column=0, columnspan=3, sticky=W)

# Create save button
save_btn = Button(window, text='Save', command=save).grid(row=13, column=0, columnspan=3, pady=(30,10), ipadx=100)

# Create reset button
reset_btn = Button(window, text='Reset', command=reset).grid(row=14, column=0, columnspan=3, pady=10, ipadx=100)

# Create show button
show_btn = Button(window, text='Show', command=show).grid(row=15, column=0, columnspan=3, pady=10, ipadx=100)

# Create select id label and entry
select_id_label = Label(window, text='Select ID : ').grid(row=16, column=0)
select_id_entry = Entry(window)
select_id_entry.grid(row=16, column=1)

# Create edit button
edit_btn = Button(window, text='Edit', command=edit).grid(row=16, column=2, pady=10, ipadx=30)





# Commit changes
conn.commit()
# Close connection
conn.close()



window.mainloop()





### NOTES ###

#Window : window, show (Create and show total point of checkbox)

#TODO2 (Create update function)

#TODO3 (Check entry box, you cannot add same code and the code must be 4 uppercase letters)
