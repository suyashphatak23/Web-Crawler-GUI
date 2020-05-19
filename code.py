from tkinter import *
import tkinter as tk
from tkinter import messagebox as ms
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import urllib

def Scrape(arg=None):
    
    # Checking for blank url
    if url_entry.get() == '':
        ms.showerror('Oops', 'Enter A Valid URL !!!')
        
    else:
        try:
            ''' Scraping Method Start'''
            # Giving url
            url = url_entry.get()
            
            # Reading all content
            content = urllib.request.urlopen(url).read()
            
            # Passing the content to function
            soup = BeautifulSoup(content, features="lxml")

            # Storing html in one variable
            info = soup.prettify()
            '''Scrape Method End'''

            '''Window Settings Start'''
            # Creating New Window
            root = tk.Toplevel()

            # Creating Title
            root.title('Thank You For Using Our Service !!!!')

            # Creating title icon
            root.iconbitmap('img/logo.ico')

            # Locking the window size
            root.resizable(width=False, height=False)
            
            ''' Window Setting End'''
            
            # Adding scrollbar to the window
            scrollbar = Scrollbar(root)
            scrollbar.pack(side=RIGHT, fill=Y)

            # Using text widget to show scraped content
            text = Text(root, yscrollcommand=scrollbar.set, wrap = WORD)
            text.insert(INSERT, info)
            text.pack()

            # Scroll bar settings
            scrollbar.config(command=text.yview)

        except ValueError:
            ms.showerror('Error', 'Enter A Valid URL !!!')
    
''' Window Setting Start '''
# Creating Widget
crawler = tk.Tk()

# Creating size of window
crawler.geometry('500x500')

# Locking the window size
crawler.resizable(width=False, height=False)

# Creating Title
crawler.title('Web Scraper for HTML & XML')

# Creating title icon
crawler.iconbitmap('img/logo.ico')
''' Window Setting End '''

# Top Frame
top_frame = Label(crawler, text='WEB CRAWLER',font = ('Cosmic', 25, 'bold'), bg='#C70039', fg='white', relief='groove',padx=500, pady=30, bd='5')
top_frame.pack(side='top')

''' Background Image Start'''
# Sizing Image
canvas = Canvas(crawler, width=500, height=500)

# Opening Image
image = ImageTk.PhotoImage(Image.open('img/bg6.jpg'))

#Positioning Image
canvas.create_image(0,0, anchor=NW, image=image)
canvas.pack()
'''Background Image End'''

# Creating Frame
frame = LabelFrame(crawler, padx=30, pady=40, bg='white', bd='5', relief='groove')
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)

# Label 
url_add = tk.Label(frame, text = 'Enter a URL or Web Address',font=('Arial',10, 'bold'),bg='white', fg='green').pack()

# Entry or Input
url_entry = tk.Entry(frame, font=('calibre',10,'normal'), justify = 'center', bg='#FBB13C', width='30')

# Returning value to the function
url_entry.bind('<Return>', Scrape)

# Setting focus for input
url_entry.focus_set()

# Placing the button
url_entry.pack()

# Label for seperating Buttons
label = Label(frame, bg='white').pack()

# Creating Submit button and positioning it
crawl = tk.Button(frame, text = "Scrape", width="10", bd = '3', command = Scrape, font = ('Times', 12, 'bold'), bg='#7268A6',relief='groove', justify = 'center', pady='5').pack()

# Creating window only once
crawler.mainloop()

 
