from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess, sys

"""
root=tk.Tk()
image_frame=tk.Frame(root)
image_frame.pack(padx=5, pady=5)
buttons=False
label=False
last_img=None

buttons_frame=tk.Frame(root)
buttons_frame.pack()

def open_img(image):
    global label, lab_img
    if not(label):
        lab_img=tk.Label(image_frame)
        lab_img.pack()
        label=True
    
    show_image=Image.open(image)
    show_image_tk=ImageTk.PhotoImage(show_image)
    lab_img.config(image=show_image_tk, height=show_image_tk.height(), width=show_image_tk.width())
    lab_img.image=show_image_tk
    if not(buttons):
        create_menu()    

def control_img(state):
    try:
        if state:
            get_image(path, True)
        if not(state): 
            get_image(path, False)
    except:
        messagebox.showwarning("Warning", "There's no last/next image.")        
    
def exit():
    root.destroy()
    return subprocess.Popen([sys.executable] +sys.argv)

def create_menu():
    global buttons
    buttons=True
    
    last_img_button=tk.Button(buttons_frame, text="<<<Last image", font=("Times New Roman", 10), width=16, command =lambda :control_img(False)).pack(side=tk.LEFT, fill=tk.BOTH, pady=5, padx=5)
    next_img_button=tk.Button(buttons_frame, text="Next image>>>", font=("Times New Roman", 10), width=16,  command=lambda :control_img(True)).pack(side=tk.RIGHT, fill=tk.BOTH, pady=5, padx=5)
    exit_button=tk.Button(buttons_frame, text="Exit", font=("Times New Roman", 10),width=16,  command=exit).pack(fill=tk.BOTH, pady=5)

def get_image(path, get_state):
    global last_img, first_i
    possible_formats=[".jpg", ".png", ".gif", ".webp"]
    files=sorted(os.listdir(path))
    if last_img!=None:
        i=files.index(os.path.basename(last_img)) # get index of current
        if get_state:
            next_files=files[i+1:]
        else:
            if i>first_i:
                next_files=files[i-1::-1]    
    else:
        i=0  
        next_files=files[i:]  
    for image_path in next_files:
        split_path=os.path.splitext(image_path)
        if split_path[-1] in possible_formats:
            whole_image_path=os.path.join(path, image_path)
            img=Image.open(whole_image_path)
            img=img.resize((250, int(250 * img.size[1]/img.size[0])))
            if last_img == None:
                first_i=files.index(os.path.basename(whole_image_path))
            last_img=whole_image_path
            img.save(whole_image_path)
            open_img(whole_image_path)
            break     

def choose_path():
    try:
        global path
        path=filedialog.askdirectory()
    except:
        messagebox.showerror("Error", "An error occcured choosing your directory!")    
        return choose_path()
    button_path.destroy()
    get_image(path, None)

button_path=tk.Button(root, text="Choose a path to view images", font=("Times New Roman", 15),  command=choose_path)
button_path.pack(padx=10, pady=10)

root.mainloop()"""

"""
requirements:
1. Choose path button 
-> messagebox
2. giant label with image
3. frame:
3.1. <<< last image
3.2. exit -> 1. ???
3.3. next image >>>
"""

class ImageViewer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.buttons=False
        self.label=False
        self.last_img=None   
        self.image_frame=tk.Frame(self)
        self.image_frame.pack(padx=5, pady=5)
        self.buttons_frame=tk.Frame(self)
        self.buttons_frame.pack()
        self.button_path=tk.Button(self, text="Choose a path to view images", font=("Times New Roman", 15),  command=self.choose_path)
        self.button_path.pack(padx=10, pady=10)
        self.mainloop()
    def open_img(self, image):
        if not(self.label):
            self.lab_img=tk.Label(self.image_frame)
            self.lab_img.pack()
            self.label=True
        show_image=Image.open(image)
        show_image=show_image.resize((250, int(250 * show_image.size[1]/show_image.size[0])))
        show_image_tk=ImageTk.PhotoImage(show_image)
        self.lab_img.config(image=show_image_tk, height=show_image_tk.height(), width=show_image_tk.width())
        self.lab_img.image=show_image_tk
        if not(self.buttons):
            self.create_menu()    

    def control_img(self, state):
        try:
            if state:
                self.get_image(self.path, True)
            if not(state): 
                self.get_image(self.path, False)
        except:
            messagebox.showwarning("End", "There's no next image.")        
        
    def exit_app(self):
        self.destroy()
        return subprocess.Popen([sys.executable] +sys.argv)

    def create_menu(self):
        self.buttons=True 
        last_img_button=tk.Button(self.buttons_frame, text="<<<Last image", font=("Times New Roman", 10), width=16,  command=lambda :self.control_img(False))
        last_img_button.pack(side=tk.LEFT, fill=tk.BOTH, pady=5, padx=5)
        next_img_button=tk.Button(self.buttons_frame, text="Next image>>>", font=("Times New Roman", 10), width=16,  command=lambda :self.control_img(True))
        next_img_button.pack(side=tk.RIGHT, fill=tk.BOTH, pady=5, padx=5)
        exit_button=tk.Button(self.buttons_frame, text="Exit", font=("Times New Roman", 10),width=16,  command=self.exit_app)
        exit_button.pack(fill=tk.BOTH, pady=5)

    def get_image(self, path, get_state):
        possible_formats=[".jpg", ".png", ".gif", ".webp"]
        files=sorted(os.listdir(path))
        if self.last_img!=None:
            i=files.index(os.path.basename(self.last_img)) # get index of current
            if get_state:
                next_files=files[i+1:]
            else:
                if i>self.first_i:
                    next_files=files[i-1::-1]    
        else:
            i=0  
            next_files=files[i:]  
        for image_path in next_files:
            split_path=os.path.splitext(image_path)
            if split_path[-1] in possible_formats:
                whole_image_path=os.path.join(path, image_path)
                if self.last_img == None:
                    self.first_i=files.index(os.path.basename(whole_image_path))
                self.last_img=whole_image_path
                self.open_img(whole_image_path)
                break 
        else:
            messagebox.showinfo("End", "No more images.")        

    def choose_path(self):
        try:
            self.path=filedialog.askdirectory()
        except:
            messagebox.showerror("Error", "An error occcured choosing your directory!")    
            return self.choose_path()
        self.button_path.destroy()
        self.get_image(self.path, None)    

start=ImageViewer() 