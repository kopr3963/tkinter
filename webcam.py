#webcam.py
# __author__ = 'kim';
import os;
import subprocess
from sys import platform
os_ = "";
if platform == "linux" or platform == "linux2":
    # linux
	os_ = "linux";
	pass;

elif platform == "darwin":
    # OS X
	os_ = "osx";
	pass;
elif platform == "win32":
    # Windows...
	os_ = "window";
	pass;

print(os_);
# output = commands.getoutput('v4l2-ctl -d /dev/video9 --list-c    trls');
V4L2 = False;

def cam():
	# output = commands.getoutput('v4l2-ctl -d /dev/video9 --list-c    trls');
	# output = subprocess.check_output('v4l2-ctl -d /dev/video9 --l    ist-ctrls', shell=True);
	# return output;
	pass;
c = cam();
# print (c);
try :
	from Tkinter import *
except ImportError:
	from tkinter import *
else : 
	print ('ImportError');
from library import *
import cv2
from PIL import Image
from PIL import ImageTk

print ( result);
root = Tk()
print ( Image.__file__);
w = root.winfo_screenwidth();
h = root.winfo_screenheight();

root.title('webcam');
root.geometry('{}x{}'.format(w, h));
root.resizable(width=False, height=False)
settings_Menu(root);
#w = w/2;

#Settings_Menu();
print(w,h)
root.configure(bg='#817B7A');

left_frame = Frame(root , width=800, height=400);
right_frame= Frame(root, bg='#988C89', width=w/2, height=600);

left_frame.grid_propagate(0);
right_frame.grid_propagate(0);

root.grid_rowconfigure(1, weight=1);
root.grid_columnconfigure(0, weight=1);

left_frame.grid(row=0, column=0, sticky="new");
right_frame.grid(row=0, column= 1, sticky="new");

left_frame = Label(left_frame);
left_frame.configure(bg='White');

test_label = Label(left_frame, text='test');
test2_label= Label(right_frame, text='right');
test3_label = Label(left_frame, text='aaaa');

cap = cv2.VideoCapture(0);
cap.set(cv2.CAP_PROP_FPS,60);

#cap2 = cv2.VideoCapture(1);
#cap2.set(cv2.CAP_PROP_FPS,60);
def hello():
    print ("hello!")

def show_frame():
	_, frame = cap.read()
	frame = cv2.flip(frame,1)
	cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA);
	img=Image.fromarray(cv2image)
	imgtk = ImageTk.PhotoImage(image=img)
	left_frame.imgtk = imgtk
	left_frame.configure(image=imgtk);
	left_frame.grid(row=0,column=0, sticky="new");
	left_frame.after(10, show_frame);
	pass;
def over (event):
	print("over");
left_frame.bind("<Enter>",over);
show_frame();
root.mainloop();

