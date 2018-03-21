#library.py
try :
	from Tkinter import *
except ImportError :
	from tkinter import *
else :
	print("ImportError");

print('a');


def __init__():
	print('init');

def test() : 
	print('test');

def hello():
	print ("hi");



def settings_Menu(self):
	print('library.py  settings_menu()' );
	self.menubar = Menu(self);
	self.menubar.add_command(label="Hello!", command=hello)
	self.menubar.add_command(label="Quit!", command=self.quit)

	filemenu = Menu(self.menubar, tearoff=0)
	filemenu.add_command(label="Open", command=hello)
	filemenu.add_command(label="Save", command=hello)
	filemenu.add_separator()
	filemenu.add_command(label="Exit", command=self.quit)
	self.menubar.add_cascade(label="File", menu=filemenu)



	editmenu = Menu(self.menubar, tearoff=0)
	editmenu.add_command(label="Cut", command=hello)
	editmenu.add_command(label="Copy", command=hello)
	editmenu.add_command(label="Paste", command=hello)
	self.menubar.add_cascade(label="Edit", menu=editmenu)

	helpmenu = Menu(self.menubar, tearoff=0)
	helpmenu.add_command(label="About", command=hello)
	self.menubar.add_cascade(label="Help", menu=helpmenu)

	self.config(menu=self.menubar)


	pass;



	
	
