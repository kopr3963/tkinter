#library.py
import commands;
from sys import platform;
from itertools import izip;
try :
	from Tkinter import *
except ImportError :
	from tkinter import *
else :
	print("ImportError");

def __init__():
	# print('init');
	pass;
def test() : 
	# print('test');
	pass;
def hello():
	# print ("hi");
	pass;
st = command = commands.getstatusoutput('v4l2-ctl -d /dev/video0 --list-ctrls');
# print ( st);
st = st[1];
st = st.strip();
st = st.replace(" ","");
out = st.split("\n");

def t (list):
	s = [];
	for i in range(len(list)):
		s = s + list[i].split(":");
	i = iter(s);
	result = dict(izip(i,i));
	return result;

	pass;
result = t(out);
# print ( result )


def settings_Menu(self):
	# print('library.py  settings_menu()' );
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



	
	
