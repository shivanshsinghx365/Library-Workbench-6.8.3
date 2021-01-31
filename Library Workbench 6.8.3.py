#Library Workbench Created by Shivansh Singh


from tkinter import *

import mysql.connector

from tkinter import ttk


from PIL import ImageTk, Image

from tkinter import messagebox

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

root=Tk()

root.iconbitmap('D:/Study/CS Project/d.ico')
root.title('Library Workbench 6.8.3™')



my_img=ImageTk.PhotoImage(Image.open("D:\\Study\\CS Project\\Library2.jpg"))
my_label= Label(image=my_img)
my_label.pack(expand=YES)


root.geometry('800x620')      #fixing size of window
root.geometry('+200+50')      #fixing default location on screen
root.resizable(0, 0)          #denying resizing

frame=LabelFrame(root,text='Enter Password',padx=5,pady=3)
frame.pack(anchor=S+E)

e=Entry(frame,font=("monospaced", 10),fg='#292a37',bg='#cfd2e6',border=7,width=75)

e.grid(row=1,column=1,padx=10,pady=15)

def password():
    if e.get()=='XTreme683':
    	return()

    else:
        messagebox.showerror('Error 31719','Incorrect Password: Acesss Denied')



def net():

	global e

	if e.get()=='XTreme683':

		import tkinter as tk

		root = tk.Tk()

		root.geometry('800x620')      #fixing size of window
		root.geometry('+200+50')      #fixing default location on screen
		root.resizable(0, 0)          #denying resizing

		root.iconbitmap('D:/Study/CS Project/d.ico')
		root.title('Library Workbench 6.8.3™')

		frame=LabelFrame(root,text='Main Menu',padx=17,pady=7)
		frame.pack(anchor=S+E)

		ss=Button(frame,text='Add a Book',font=("Helvetica", 10),fg='#f8dede',bg='#000000',border=7,height=5,width=90,command=but)
		ss.grid(row=1,column=0,padx=5,pady=15)

		fs=Button(frame,text='Search a Book',font=("Helvetica", 10),fg='#f8dede',bg='#000000',border=7,height=5,width=90,command=search_customers)
		fs.grid(row=2,column=0,padx=5,pady=15)

		gs=Button(frame,text='Delete a book',font=("Helvetica", 10),fg='#f8dede',bg='#000000',border=7,height=5,width=90,command=delx)
		gs.grid(row=3,column=0,padx=5,pady=15)

		hs=Button(frame,text='Update a Book',font=("Helvetica", 10),fg='#f8dede',bg='#000000',border=7,height=5,width=90,command=upnow)
		hs.grid(row=4,column=0,padx=5,pady=15)

		
def but():

	import tkinter as tk

	root = tk.Tk()

	root.geometry('800x620')      #fixing size of window
	root.geometry('+200+50')      #fixing default location on screen
	root.resizable(0, 0)          #denying resizing

	root.iconbitmap('D:/Study/CS Project/d.ico')
	root.title('Library Workbench 6.8.3™')

	frame=LabelFrame(root,text='Add Details',padx=17,pady=7)
	frame.grid()

	Srnolabel= Label(root,text='Srno',font=('Helvetica',20))
	Srnolabel.grid(row=0,column=0)
	Namelabel= Label(root,text='Name',font=('Helvetica',16))
	Namelabel.grid(row=1,column=0)
	Authorlabel= Label(root,text='Author',font=('Helvetica',16))
	Authorlabel.grid(row=2,column=0)
	Pricelabel= Label(root,text='Price',font=('Helvetica',16))
	Pricelabel.grid(row=3,column=0)
	Genrelabel= Label(root,text='Genre',font=('Helvetica',16))
	Genrelabel.grid(row=4,column=0)
	Languagelabel= Label(root,text='Language',font=('Helvetica',16))
	Languagelabel.grid(row=5,column=0)
	Almirah_Nolabel= Label(root,text='Almirah_No',font=('Helvetica',16))
	Almirah_Nolabel.grid(row=6,column=0)
	Shelf_Nolabel= Label(root,text='Shelf_No',font=('Helvetica',16))
	Shelf_Nolabel.grid(row=7,column=0)


	Srno= Entry(root,width=52,font=('Helvetica',16),border=10)
	Srno.grid(row=0,column=1,padx=20,pady=10)
	Name= Entry(root,width=52,font=('Helvetica',16),border=10)
	Name.grid(row=1,column=1,padx=20,pady=10)
	Author= Entry(root,width=52,font=('Helvetica',16),border=10)
	Author.grid(row=2,column=1,padx=20,pady=10)
	Price= Entry(root,width=52,font=('Helvetica',16),border=10)
	Price.grid(row=3,column=1,padx=20,pady=10)
	Genre= Entry(root,width=52,font=('Helvetica',16),border=10)
	Genre.grid(row=4,column=1,padx=20,pady=10)	
	Language= Entry(root,width=52,font=('Helvetica',16),border=10)
	Language.grid(row=5,column=1,padx=20,pady=10)
	Almirah_No= Entry(root,width=52,font=('Helvetica',16),border=10)
	Almirah_No.grid(row=6,column=1,padx=20,pady=10)
	Shelf_No= Entry(root,width=52,font=('Helvetica',16),border=10)
	Shelf_No.grid(row=7,column=1,padx=20,pady=10)

	def submit():

		mydb=mysql.connector.connect(host='localhost',user='root',passwd='XTreme365',database='Library')
		my_cursor=mydb.cursor()

		h=int(Srno.get())
		a=str(Name.get())
		b=str(Author.get())
		c=int(Price.get())
		d=str(Genre.get())
		e=str(Language.get())
		f=int(Almirah_No.get())
		g=int(Shelf_No.get())

		my_cursor.execute('''insert into books values("%d","%s","%s","%d","%s","%s","%d","%d") '''%(h,a,b,c,d,e,f,g))
		mydb.commit()
		mydb.close()

		Srno.delete(0,END)
		Name.delete(0,END)
		Author.delete(0,END)
		Price.delete(0,END)
		Genre.delete(0,END)
		Language.delete(0,END)	
		Almirah_No.delete(0,END)
		Shelf_No.delete(0,END)

	submit_btn=Button(root,text='Add Record',command=submit,fg='#f8dede',bg='#000000',font=('Helvetica',20),height=1)
	submit_btn.grid(row=8,column=1,padx=10,pady=10,ipadx=100,sticky=S+E)

	back_btn=Button(root,text='Back',fg='#f8dede',bg='#000000',font=('Helvetica',20),height=1,command=root.destroy)
	back_btn.grid(row=8,column=0,padx=5,pady=5)

def but1():

	mydb=mysql.connector.connect(host='localhost',user='root',passwd='XTreme683',database='Library')
	my_cursor=mydb.cursor()

	import tkinter as tk

	root = tk.Tk()

	root.geometry('800x620')      #fixing size of window
	root.geometry('+200+50')      #fixing default location on screen
	root.resizable(0, 0)          #denying resizing

	root.iconbitmap('D:/Study/CS Project/d.ico')
	root.title('Library Workbench 6.8.3™')

	frame=LabelFrame(root,text='Add Details',padx=17,pady=7)
	frame.grid()

	Srnolabel= Label(root,text='Enter Srno to be altered',font=('Helvetica',20))
	Srnolabel.grid(row=0,column=0)
	Namelabel= Label(root,text='Enter New Name',font=('Helvetica',16))
	Namelabel.grid(row=1,column=0)
	Authorlabel= Label(root,text='Enter New Author',font=('Helvetica',16))
	Authorlabel.grid(row=2,column=0)
	Pricelabel= Label(root,text='Enter New Price',font=('Helvetica',16))
	Pricelabel.grid(row=3,column=0)
	Genrelabel= Label(root,text='Enter New Genre',font=('Helvetica',16))
	Genrelabel.grid(row=4,column=0)
	Languagelabel= Label(root,text='Enter New Language',font=('Helvetica',16))
	Languagelabel.grid(row=5,column=0)
	Almirah_Nolabel= Label(root,text='Enter New Almirah_No',font=('Helvetica',16))
	Almirah_Nolabel.grid(row=6,column=0)
	Shelf_Nolabel= Label(root,text='Enter New Shelf_No',font=('Helvetica',16))
	Shelf_Nolabel.grid(row=7,column=0)


	Srno= Entry(root,width=52,font=('Helvetica',10),border=10)
	Srno.grid(row=0,column=1,padx=20,pady=10)
	Name= Entry(root,width=52,font=('Helvetica',10),border=10)
	Name.grid(row=1,column=1,padx=20,pady=10)
	Author= Entry(root,width=52,font=('Helvetica',10),border=10)
	Author.grid(row=2,column=1,padx=20,pady=10)
	Price= Entry(root,width=52,font=('Helvetica',10),border=10)
	Price.grid(row=3,column=1,padx=20,pady=10)
	Genre= Entry(root,width=52,font=('Helvetica',10),border=10)
	Genre.grid(row=4,column=1,padx=20,pady=10)	
	Language= Entry(root,width=52,font=('Helvetica',10),border=10)
	Language.grid(row=5,column=1,padx=20,pady=10)
	Almirah_No= Entry(root,width=52,font=('Helvetica',10),border=10)
	Almirah_No.grid(row=6,column=1,padx=20,pady=10)
	Shelf_No= Entry(root,width=52,font=('Helvetica',10),border=10)
	Shelf_No.grid(row=7,column=1,padx=20,pady=10)

def search_customers():

	import tkinter as tk

	root = tk.Tk()

	root.geometry('800x620')      #fixing size of window
	root.geometry('+200+50')      #fixing default location on screen
	root.resizable(0, 0)          #denying resizing

	root.iconbitmap('D:/Study/CS Project/d.ico')
	root.title('Library Workbench 6.8.3™')

	frame=LabelFrame(root,text='Search Books',padx=50,pady=50)
	frame.grid()



	def search_now():

		from tkinter import messagebox

		mydb=mysql.connector.connect(host='localhost',user='root',passwd='XTreme365',database='Library')
		my_cursor=mydb.cursor()

		selected=drop.get()

		if selected=='Search by...':
			messagebox.showerror('Critical Error 20620 ','Choose a Search valid Option')

		if selected=='Name':
			searched=search_box.get()
			a=str(searched)

			my_cursor.execute('''SELECT * from books where Name="%s"'''%(a)) 

			result=my_cursor.fetchall()

			for index, x in enumerate(result):
				num=0
				index+=2
				Srno_reference=str(x[0])
			
				for y in x:
					lookup_label=Label(frame, text=y)
					lookup_label.grid(row=index+4,column=num+1)
					num+=1

			if not result:
				result=messagebox.showwarning('Warning 60803','This Name does not Exist')
			
		if selected=='Srno':
			searched=search_box.get()
			a=int(searched)
			my_cursor.execute('''SELECT * from books where Srno="%d"'''%(a)) 
			result=my_cursor.fetchall()

			for index, x in enumerate(result):
				num=0
				index+=2
				for y in x:
					lookup_label=Label(frame, text=y)
					lookup_label.grid(row=index+4,column=num)
					num+=1


			if not result:
				result=messagebox.showwarning('Warning 180503','This Serial Number does not Exist')
			
		if selected=='Genre':
			searched=search_box.get()
			a=str(searched)

			my_cursor.execute('''SELECT * from books where Genre="%s"'''%(a)) 

			result=my_cursor.fetchall()

			for index, x in enumerate(result):
				num=0
				for y in x:
					lookup_label=Label(frame, text=y)
					lookup_label.grid(row=index+4,column=num,padx=3)
					num+=1
				

			if not result:
				result=messagebox.showwarning('Warning 60819','This Genere does not Exist')

		if selected=='Language':
			searched=search_box.get()
			a=str(searched)
			my_cursor.execute('''SELECT * from books where Language="%s"'''%(a)) 
			result=my_cursor.fetchall()

			for index, x in enumerate(result):
				num=0
				for y in x:
					lookup_label=Label(frame, text=y)
					lookup_label.grid(row=index+4,column=num)
					num+=1

			if not result:
				result=messagebox.showwarning('Warning 23120','This Language does not Exist')

		if selected=='Author':
			searched=search_box.get()
			a=str(searched)
			my_cursor.execute('''SELECT * from books where Author="%s"'''%(a))
			result=my_cursor.fetchall()

			for index, x in enumerate(result):
				num=0
				for y in x:
					lookup_label=Label(frame, text=y)
					lookup_label.grid(row=index+4,column=num)
					num+=1

			if not result:
				result=messagebox.showwarning('Warning 10819','This Author does not Exist')
		

	search_box=Entry(frame,font=("Helvetica", 10))
	search_box.grid(row=0,column=1,padx=20,pady=20)

	search_box_label=Label(frame, text='Search Books',font=("Helvetica", 10))
	search_box_label.grid(row=0,column=0,padx=20,pady=20)

	search_button=Button(frame,text='Search Books',command=search_now,font=("Helvetica", 10),fg='#f8dede',bg='#000000')
	search_button.grid(row=1,column=1)

	drop=ttk.Combobox(frame, value=["Search by...","Srno","Name","Language","Genre","Author"])
	drop.current(0)
	drop.grid(row=0,column=2)

	back_btn=Button(root,text='Back',fg='#f8dede',bg='#000000',font=('Helvetica',20),height=1,command=root.destroy)
	back_btn.grid(row=8,column=0,padx=5,pady=5)

def delx():

	import mysql.connector

	mydb=mysql.connector.connect(host='localhost',user='root',passwd='XTreme365',database='Library')
	my_cursor=mydb.cursor()

	import tkinter as tk

	root = tk.Tk()

	root.geometry('800x620')      #fixing size of window
	root.geometry('+200+50')      #fixing default location on screen
	root.resizable(0, 0)          #denying resizing

	root.iconbitmap('D:/Study/CS Project/d.ico')
	root.title('Library Workbench 6.8.3™')
	frame=LabelFrame(root,text='Delete Books',padx=17,pady=7)
	frame.grid()

	Srnolabel= Label(root,text='Enter Srno to be Deleted',font=('Helvetica',20))
	Srnolabel.grid(row=0,column=0)

	Srno= Entry(root,width=52,font=('Helvetica',16),border=10)
	Srno.grid(row=1,column=0,padx=20,pady=10)

	def submitx():

		mydb=mysql.connector.connect(host='localhost',user='root',passwd='XTreme365',database='Library')
		my_cursor=mydb.cursor()

		h=int(Srno.get())
		my_cursor.execute('''delete from books where Srno="%d"'''%h)
		mydb.commit()
		mydb.close()
		Srno.delete(0,END)

	submit_btn=Button(root,text='Delete Record',command=submitx,fg='#f8dede',bg='#000000',font=('Helvetica',20),height=1)
	submit_btn.grid(row=2,column=0,padx=10,pady=10,ipadx=10,sticky=S+W)

	back_btn=Button(root,text='Back',fg='#f8dede',bg='#000000',font=('Helvetica',20),height=1,command=root.destroy)
	back_btn.grid(row=2,column=1,padx=20,pady=20,sticky=S)

def upnow():

	import tkinter as tk

	root = tk.Tk()

	root.geometry('800x620')      #fixing size of window
	root.geometry('+200+50')      #fixing default location on screen
	root.resizable(0, 0)          #denying resizing

	root.iconbitmap('D:/Study/CS Project/d.ico')
	root.title('Library Workbench 6.8.3™')

	frame=LabelFrame(root,text='Book record Update',padx=17,pady=7)
	frame.grid()

	Srnolabel= Label(root,text='Srno to be altered',font=('Helvetica',20))
	Srnolabel.grid(row=0,column=0)


	Srno= Entry(root,width=40,font=('Helvetica',16),border=10)
	Srno.grid(row=0,column=1,padx=20,pady=10)

	def b1():

		import tkinter as tk

		root = tk.Tk()

		root.geometry('800x620')      #fixing size of window
		root.geometry('+200+50')      #fixing default location on screen
		root.resizable(0, 0)          #denying resizing

		root.iconbitmap('D:/Study/CS Project/d.ico')
		root.title('Library Workbench 6.8.3™')

		frame=LabelFrame(root,text='Add New Details',padx=17,pady=7)
		frame.grid()

		Namelabel= Label(root,text='New Name',font=('Helvetica',16))
		Namelabel.grid(row=1,column=0)
		Authorlabel= Label(root,text='New Author',font=('Helvetica',16))
		Authorlabel.grid(row=2,column=0)
		Pricelabel= Label(root,text='New Price',font=('Helvetica',16))
		Pricelabel.grid(row=3,column=0)
		Genrelabel= Label(root,text='New Genre',font=('Helvetica',16))
		Genrelabel.grid(row=4,column=0)
		Languagelabel= Label(root,text='New Language',font=('Helvetica',16))
		Languagelabel.grid(row=5,column=0)
		Almirah_Nolabel= Label(root,text='New Almirah_No',font=('Helvetica',16))
		Almirah_Nolabel.grid(row=6,column=0)
		Shelf_Nolabel= Label(root,text='New Shelf_No',font=('Helvetica',16))
		Shelf_Nolabel.grid(row=7,column=0)

		Name= Entry(root,width=52,font=('Helvetica',16),border=10)
		Name.grid(row=1,column=1,padx=20,pady=10)
		Author= Entry(root,width=52,font=('Helvetica',16),border=10)
		Author.grid(row=2,column=1,padx=20,pady=10)
		Price= Entry(root,width=52,font=('Helvetica',16),border=10)
		Price.grid(row=3,column=1,padx=20,pady=10)
		Genre= Entry(root,width=52,font=('Helvetica',16),border=10)
		Genre.grid(row=4,column=1,padx=20,pady=10)	
		Language= Entry(root,width=52,font=('Helvetica',16),border=10)
		Language.grid(row=5,column=1,padx=20,pady=10)
		Almirah_No= Entry(root,width=52,font=('Helvetica',16),border=10)
		Almirah_No.grid(row=6,column=1,padx=20,pady=10)
		Shelf_No= Entry(root,width=52,font=('Helvetica',16),border=10)
		Shelf_No.grid(row=7,column=1,padx=20,pady=10)


		def submity():

			mydb=mysql.connector.connect(host='localhost',user='root',passwd='XTreme365',database='Library')
			my_cursor=mydb.cursor()

			h=int(Srno.get())
			a=str(Name.get())
			b=str(Author.get())
			c=int(Price.get())
			d=str(Genre.get())
			e=str(Language.get())
			f=int(Almirah_No.get())
			g=int(Shelf_No.get())

			my_cursor.execute('''update books set Name="%s" where Srno="%d"'''%(a,h))
			my_cursor.execute('''update books set Author="%s" where Srno="%d"'''%(b,h))
			my_cursor.execute('''update books set Price="%d" where Srno="%d"'''%(c,h))
			my_cursor.execute('''update books set Genre="%s" where Srno="%d"'''%(d,h))
			my_cursor.execute('''update books set Language="%s" where Srno="%d"'''%(e,h))
			my_cursor.execute('''update books set Almirah_No="%d" where Srno="%d"'''%(f,h))
			my_cursor.execute('''update books set Shelf_No="%d" where Srno="%d"'''%(g,h))

			mydb.commit()
			mydb.close()

			Srno.delete(0,END)
			Name.delete(0,END)
			Author.delete(0,END)
			Price.delete(0,END)
			Genre.delete(0,END)
			Language.delete(0,END)	
			Almirah_No.delete(0,END)
			Shelf_No.delete(0,END)

		submit_btn=Button(root,text='Change Record',command=submity,fg='#f8dede',bg='#000000',font=('Helvetica',20),height=1)
		submit_btn.grid(row=8,column=1,padx=10,pady=10,ipadx=100,sticky=S+E)

		back_btn=Button(root,text='Back',fg='#f8dede',bg='#000000',font=('Helvetica',20),height=1,command=root.destroy)
		back_btn.grid(row=8,column=0,padx=5,pady=5)

	upButton=Button(root,text='Update this record',command=b1,fg='#f8dede',bg='#000000',font=('Helvetica',20),height=1)
	upButton.grid(row=1,column=1,padx=20,pady=20,sticky=S+E)
	back_btn=Button(root,text='Back',fg='#f8dede',bg='#000000',font=('Helvetica',20),height=1,command=root.destroy)
	back_btn.grid(row=1,column=0,padx=5,pady=5)

def next():
	import tkinter as tk

	root = tk.Tk()

	root.geometry('800x620')      #fixing size of window
	root.geometry('+200+50')      #fixing default location on screen
	root.resizable(0, 0)          #denying resizing

	root.iconbitmap('D:/Study/CS Project/d.ico')
	root.title('Library Workbench 6.8.3™')

	framex=LabelFrame(root,text='About',padx=5,pady=3)
	label1= Label(root,text='This Library Management Software is created by Shivansh Singh',font=('Helvetica',16))
	label1.pack()
	label2= Label(root,text='& is completely free to use',font=('Helvetica',16))
	label2.pack()
	label3= Label(root,text='You can share,modify and redistribute it as per your wish',font=('Helvetica',16))
	label3.pack()
	label4= Label(root,text='It is completely Open Source Code',font=('Helvetica',16))
	label4.pack()
	label5= Label(root,text='and was Originally developed as a school project in India year 2020',font=('Helvetica',16))
	label5.pack()
	label6=Label(root,text='This program will no longer recieve any updates',font=('Helvetica',16))
	label6.pack()
	label7= Label(root,text='Developers are requested to update it according to there requirements',font=('Helvetica',16))
	label7.pack()
	label8= Label(root,text='the source code of the program is unfortunately not available here',font=('Helvetica',16))
	label8.pack()
	label9= Label(root,text='to view source code and dependencies kindly see the python pakage :)',font=('Helvetica',16))
	label9.pack()


ok =Button(frame,text='O K ',font=("monospaced", 12),bg='#0b67f2',fg='#f3f5f7',padx=3,command=combine_funcs(net,password, root.destroy),width=10)
ok.grid(row=1,column=2,pady=15,padx=7)

abbout=Button(frame,text='about',font=('Helvetica',12),fg='#292a37',bg='#cfd2e6',padx=3,command=next,width=10)
abbout.grid(row=1,column=0,pady=15,padx=7)

root.mainloop()

