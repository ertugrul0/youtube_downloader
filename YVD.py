from Tkinter import *
import wx
import pafy

def download(x):
	for c in x: # to remove the first unnecesasary blanks from the url.
		if c!=' ':
			break
		else:
			x = x[1:]
	
	beginning = "https://www.youtube.com/watch?v="
	if beginning not in x:
		print "Error"
		return 1
	first = len(beginning)
	xxx = x[first:first+11]
		 
	v = pafy.new(xxx)
	s = v.getbest()
	print("Size is %s" % s.get_filesize())
	filename = s.download()  # starts download
	print 

	

def show_entry_fields():
   x = e1.get()
   download(x)
   e1.delete(0,END)
  		
master = Tk()
master.title("Youtube Video Downloader")
master.geometry('275x60')
master.resizable(width=FALSE, height=FALSE) # disable full screen mode
Label(master, text="Enter video url").grid(row=0)
e1 = Entry(master)
e2 = Entry(master)
e1.insert(10,"")
e1.grid(row=0, column=1)
Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Download', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop()
