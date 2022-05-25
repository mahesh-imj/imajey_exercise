import os
import platform
import shutil
import turtle
from tkinter import EXCEPTION, DoubleVar, StringVar, TclError, simpledialog
from tkinter.constants import NSEW, NW, W
from tkinter.filedialog import askdirectory,asksaveasfilename,askopenfilename,SaveFileDialog

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
    
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    from ttkthemes import themed_tk as tkk
    
    #from validator import validate
    py3 = True
    
import math
from tkinter import messagebox
#from context_menu import menus

def vp_start_gui():
    #Starting point when module is the main routine.
    global w, root
    root = tkk.ThemedTk()
    root.get_themes()
    root.set_theme("smog") #arc, elegance(faint, borders), smog(perfect for combox), breeze(highlight:not proper aligned),
    top = Toplevel1(root)
    # cm = menus.ContextMenu('Field')
    # cmd = menus.ContextCommand('Show', python=top.show_field())
    # cm.add_items([cmd])
    # cm.compile()
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, root
    root = rt
    w = tk.Toplevel(root, bd=5, relief="raised")
    top = Toplevel1(w)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None
    
class Toplevel1():
    def __init__(self, top=None, *args, **kwargs):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        
        #_bgmenu = 'pink'
        
        self.common = ("black", "#111111", "#222222", "#333333", "#444444", "#555555", "#666666", "#777777", "#888888", "#999999", "#aaaaaa", "#bbbbbb", "#cccccc", "#dddddd", "#eeeeee", "white")
        _bgmenu = self.common[10]
        _fgmenu = self.common[1]
        
        top.geometry("1329x600")
        top.minsize(120, 1)
        top.maxsize(1329, 750)
        top.resizable(1,  1)
        top.title("MAGNETIC FIELD SIMULATION")
        #top.configure(background="#e7d3e1", relief="raised", bd=5)
        top.configure(background="#899889", relief="raised", bd=5)
        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.017, rely=0.04, relheight=0.941, relwidth=0.973)
        self.Canvas1.configure(background=self.common[13])
        self.Canvas1.configure(borderwidth="5")
        self.Canvas1.configure(relief="ridge")
        
        self.LabelIn = tk.Label(self.Canvas1)
        self.LabelIn.place(relx=0.06, rely=0.024, height=48, width=386)
        self.LabelIn.configure(bg=self.common[4], fg=self.common[12], justify="center")
        self.LabelIn.configure(borderwidth="3")
        self.LabelIn.configure(font="-family {Verdana} -size 13 -weight bold", justify="center")
        self.LabelIn.configure(relief="raised")
        self.LabelIn.configure(text='''Select Coil Properties and Options''')
            
#Display Field Canvas
        self.Canv = tk.Canvas(self.Canvas1)
        self.Canv.place(relx=0.437, rely=0.024, relheight=0.957, relwidth=0.545)
        self.Canv.configure(background="white")
        self.Canv.configure(borderwidth="4")
        self.Canv.configure(relief="sunken")
        
        self.canv1 = tk.Canvas(self.Canvas1)
        self.canv1.place(relx=0.009, rely=0.13, relheight=0.7, relwidth=0.205)
        self.canv1.configure(background="grey")
        self.canv1.configure(borderwidth="2")
        self.canv1.configure(insertbackground="black")
        self.canv1.configure(relief="ridge")
       
        self.MagnetA = tk.Label(self.canv1)
        #self.MagnetA.grid(row = 0, column = 0, sticky = NSEW,pady = 5)
        self.MagnetA.place(relx=0.293, rely=0.032, height=34, width=97)
        self.MagnetA.configure(background=self.common[5])
        self.MagnetA.configure(borderwidth="3", relief="raised")
        #self.MagnetA.configure(command=lambda:self.create_incoil())
        self.MagnetA.configure(font="-family {Segoe UI Black} -size 15 -weight bold")
        self.MagnetA.configure(foreground=self.common[14], justify="center")
        self.MagnetA.configure(text='''Coil A''')
        
        self.current = StringVar()
        self.radius = StringVar()
        self.minilabel = "-family {Verdana} -size 10 -weight bold"
        self.minimenu = "-family {Verdana} -size 8 -weight bold"
        self.infont = "-family {Segoe UI Black} -size 10 -weight bold"
        self.Label2 = ttk.Label(self.canv1, borderwidth=3, relief="raised", text="Enter current (I)", font=self.minimenu)
        self.Label2.place(relx=0.042, rely=0.234)
        self.Label3 = ttk.Label(self.canv1, borderwidth=3, relief="raised",  text="Enter Radius (r)", font=self.minimenu)
        self.Label3.place(relx=0.042, rely=0.305)
        self.Ientry = ttk.Entry(self.canv1,  textvariable=self.current, font=self.infont)
        self.Ientry.place(relx=0.5, rely=0.234, relwidth=0.47)
        self.Rentry = ttk.Entry(self.canv1,  textvariable=self.radius, font=self.infont)
        self.Rentry.place(relx=0.5, rely=0.300, relwidth=0.47)
        
        self.canv2 = tk.Canvas(self.Canvas1)
        self.canv2.place(relx = 0.223, rely = 0.13, relheight = 0.7, relwidth = 0.205)
        self.canv2.configure(background = "grey")
        self.canv2.configure(borderwidth = "2")
        self.canv2.configure(relief = "ridge")
        
        self.MagnetB = tk.Label(self.canv2)
        self.MagnetB.place(relx = 0.292, rely = 0.032, height = 34, width = 97)
        self.MagnetB.configure(background=self.common[5])
        self.MagnetB.configure(borderwidth="3",relief="raised")
        #self.MagnetB.configure(command = lambda:self.create_outcoil())
        self.MagnetB.configure(font = "-family {Segoe UI Black} -size 15 -weight bold")
        self.MagnetB.configure(foreground=self.common[14], justify="center")
        self.MagnetB.configure(text = '''Coil B''')
        
        self.current1 = StringVar()
        self.radius1 = StringVar()
        
        self.Label4 = ttk.Label(self.canv2, borderwidth = 3, relief = "raised", text = "Enter current (I)", font=self.minimenu)
        self.Label4.place(relx = 0.042, rely = 0.234)
        self.Label5 = ttk.Label(self.canv2, borderwidth = 3, relief = "raised",  text = "Enter Radius (r)", font=self.minimenu)
        self.Label5.place(relx = 0.042, rely = 0.305)
        self.Ientry1 = ttk.Entry(self.canv2, textvariable=self.current1, font = self.infont)
        self.Ientry1.place(relx = 0.5, rely = 0.234, relwidth=0.47)
        self.Rentry1 = ttk.Entry(self.canv2, textvariable=self.radius1, font = self.infont)
        self.Rentry1.place(relx = 0.5, rely = 0.300, relwidth=0.47)
        self.label_set = [self.Label2, self.Label3, self.Label4, self.Label5]
        self.entry_set = [self.Ientry, self.Rentry, self.Ientry1, self.Rentry1]
        for i in range(0,len(self.label_set)):
            if type(self.label_set[i]) == tk.Label():
                self.label_set[i].config(background= self.common[15], fg=self.common[4])
            if type(self.entry_set[i]) == tk.Entry():
                self.entry_set[i].config(background=self.common[11], foreground = self.common[1], borderwidth=2, relief="sunken")
                
        self.LabelOut = tk.Label(self.Canv)
        self.LabelOut.place(relx = 0.25, rely = 0.025, height = 51, width = 354)
        self.LabelOut.configure(background = self.common[4], foreground =self.common[12], justify="center")
        self.LabelOut.configure(borderwidth = "3")
        self.LabelOut.configure(font = "-family {Verdana} -size 14 -weight bold")
        self.LabelOut.configure(relief = "raised")
        self.LabelOut.configure(text = '''COILS WITH RESULTANT FIELD''')
  
        self.value_list  =  ['X (Into coil)','. (Out of coil)']
        self.left   =  tk.StringVar()
        self.drfont="-family {Segoe UI} -size 12 -weight bold"
        
        self.Left  =  tk.OptionMenu(self.canv1, self.left, *self.value_list)
        self.Left.place(relx = 0.084, rely = 0.128, relheight = 0.074, relwidth = 0.849)
        self.Left.configure(background = "#ffffff")#, relief="ridge", bd=3)
        self.Left.configure(font = self.drfont)
        self.Left.configure(foreground = "black", activeforeground="blue")
        
        self.right  =  ttk.Combobox(self.canv2, values = self.value_list)
        self.right.place(relx = 0.084, rely = 0.128, relheight = 0.074, relwidth = 0.849)
        self.right.configure(font = self.drfont, state="readonly")
        self.right.configure(background = "#ffffff", foreground="black", justify="center")
        
        self.Button1  =  tk.Button(self.Canvas1)
        self.Button1.place(relx = 0.137, rely = 0.85, height = 40, width = 207)
        self.Button1.configure(bg=self.common[4], fg=self.common[12], activebackground="#eeeeee", activeforeground = "#222222")
        self.Button1.configure(borderwidth = "5")
        self.Button1.configure(font = "-family {Verdana} -size 14 -weight bold")
        self.Button1.configure(text = '''SIMULATE''')
        self.Button1.bind("<Button-1>", lambda e: self.show_field(), add = True)

        self.popup =  ttk.Label(self.Canvas1, borderwidth = 3,  font = "-family {Segoe UI} -size 12 -weight bold", justify="center")
        self.popup.place(relx = 0.1, rely = 0.94)
        #self.popup.config(bg = _bgmenu, fg="#222222")
        self.limit=ttk.Label(self.Canv, borderwidth=3, relief= "raised",  text = "Field varies with varying radius", font = "-family {Segoe UI} -size 12 -weight bold")
        self.limit.place(relx=0.3, rely=0.9)
        #self.limit.config(fg="brown")
        
        self.f = tk.Menubutton(top, text="File", font=self.minilabel, bg = _bgmenu, bd=3)
        self.f.place(relx=0.01, rely=0.001, relwidth=0.07, relheight=0.04)
        self.file = tk.Menu(self.f, font= self.minimenu, bg = _bgmenu, bd=3,  tearoff=0)
        self.f.configure(menu=self.file)
        self.e = tk.Menubutton(top, text="Edit", font=self.minilabel, bg = _bgmenu, bd=3)
        self.e.place(relx=0.09, rely=0.001, relwidth=0.07, relheight=0.04)
        self.edit = tk.Menu(self.e, font= self.minimenu, bg = _bgmenu, bd=3,  tearoff=0)
        self.e.configure(menu=self.edit)
        self.v = tk.Menubutton(top, text="View", font=self.minilabel, bg = _bgmenu, bd=3)
        self.v.place(relx=0.17, rely=0.001, relwidth=0.07, relheight=0.04)
        self.view = tk.Menu(self.v, font= self.minimenu,  bg = _bgmenu, bd=3,  tearoff=0)
        self.v.configure(menu=self.view)
        self.w = tk.Menubutton(top, text="Window", font=self.minilabel, bg = _bgmenu, bd=3)
        self.w.place(relx=0.25, rely=0.001, relwidth=0.07, relheight=0.04)
        self.window = tk.Menu( self.w, font= self.minimenu, bg = _bgmenu, bd=3,  tearoff=0)
        self.w.configure(menu=self.window)
        self.h = tk.Menubutton(top, text="Help", font= self.minilabel, bg = _bgmenu, bd=3)
        self.h.place(relx=0.33, rely=0.001, relwidth=0.07, relheight=0.04)
        self.help = tk.Menu(self.h, font= self.minimenu, bg = _bgmenu, bd=3,  tearoff=0)
        self.h.configure(menu=self.help)
        self.a = tk.Menubutton(top,text="About", font= self.minilabel, bg = _bgmenu, bd=3)
        self.a.place(relx=0.41, rely=0.001, relwidth=0.07, relheight=0.04)
        self.about = tk.Menu(self.a, font= self.minimenu, bg = _bgmenu, bd=3,  tearoff=0)
        self.a.configure(menu=self.about)
        self.file_opts = ['New problem', 'Open problem', 'Save As', 'Save']
        self.file_items = [self.create_file, self.open_file, self.save_file_as, self.save_file]
        for i in range(0,len(self.file_opts)):
            self.file.add_command(label=self.file_opts[i], command=self.file_items[i])
        self.file.add_separator()
        self.file.add_command(label="Exit", command=top.destroy)
       
        self.edit_opts = ['Properties', 'Edit Model']
        self.edit_items = []
        
        for i in range(0,len(self.edit_opts)):
            self.edit.add_command(label=self.edit_opts[i])
        self.edit.add_separator()
        # self.menu=tk.Menu(self.window,font= self.minimenu, bg = _bgmenu, bd=5, tearoff=0)
        # self.window.add_cascade(label='Menu Style', menu=self.menu)
        # self.menu.add_command(label='Simple', command=self.simplify_menu)
        self.theme=tk.Menu(self.window, font= self.minimenu, bg = _bgmenu, bd=5, tearoff=0)
        self.window.add_cascade(label="Change Theme", menu=self.theme)
        self.theme_labels = ['Pink',  'Green', 'Default']
        self.theme_vals = [self.to_pink, self.to_green, self.to_default]
        for i in range(0,len(self.theme_labels)):
            self.theme.add_command(label=self.theme_labels[i], command=self.theme_vals[i])
        self.menu_set = [self.f, self.e, self.v, self.w, self.h, self.a]
        self.menu_labels = ['File', 'View', 'Window', 'Help', 'About']
        self.menu_items = [self.file, self.view, self.window, self.help, self.about]

        self.current.set("1")
        self.radius.set("70")
        self.current1.set("1")
        self.radius1.set("70")
        
    def to_green(self):
        #top.configure(bg='#d9d9d9')
        self.green = ["#003030", "#005000", '#112211', "#1e273e","#aee494", "#00ffff","#aafafa","#f8eeba"]
        _bgmenu = "#aafafa" 
        _fgmenu = "#005000"
        self.Canvas1.configure(bg="#aee494")
        self.Canv.configure(bg="#f8eeba")
        self.canv1.configure(bg="#003030")
        self.canv2.configure(bg="#003030")
        self.LabelIn.configure(bg="#00ffff", fg= "#1e273e")
        self.LabelOut.configure(bg="#00ffff", fg='blue')
        self.Button1.configure(bg="#1e273e", fg='yellow', activebackground='#112211', activeforeground='pink')
        self.MagnetA.configure(background = "#005000")
        self.MagnetB.configure(background = "#005000")
        for i in range(0,len(self.menu_set)):
            self.menu_set[i].config(bg=_bgmenu, fg=_fgmenu)
        for i in range(0,len(self.label_set)):
            type(self.label_set[i]) == tk.Label()
            self.label_set[i].config(background = self.green[2],foreground = self.green[7])
            type(self.entry_set[i]) == tk.Entry()
            self.entry_set[i].config(background = self.green[6],foreground = self.green[1])        
        
    def to_pink(self):
        _bgmenu = "pink"
        _fgmenu = "brown"
        self.pink = ["#000030","#1100aa","#1e273e", "#730e8c","#800000", "#9299e4", "#aea4e4", "#f4b300","#e8d7ba"]
        self.Canvas1.configure(bg="#aea4e4")
        self.Canv.configure(bg="#e8d7ba")
        self.canv1.configure(bg="#1e273e")
        self.canv2.configure(bg="#1e273e")
        self.LabelIn.configure(bg="#1100aa", fg="pink")
        self.LabelOut.configure(bg="#1e273e", fg='yellow')
        self.MagnetA.configure(background = "#800000")
        self.MagnetB.configure(background = "#800000")
        self.Button1.configure(background = "#730e8c", foreground = "#f4b300", activebackground="#1100aa", activeforeground = "pink")
        for i in range(0,len(self.menu_set)):
            self.menu_set[i].config(bg=_bgmenu, fg=_fgmenu)
        for i in range(0,len(self.label_set)):
            type(self.label_set[i]) == tk.Label()
            self.label_set[i].config(background = self.pink[0],foreground = "yellow")
            type(self.entry_set[i]) == tk.Entry()
            self.entry_set[i].config(background = self.pink[5],foreground = self.pink[1])
        
    def to_default(self):
        _bgmenu = self.common[10]
        _fgmenu = self.common[1]
        self.Canvas1.configure(background=self.common[13])
        self.Canv.configure(bg="white")
        self.canv1.configure(bg="grey")
        self.canv2.configure(bg="grey")
        self.LabelIn.configure(bg=self.common[4], fg=self.common[12])
        self.LabelOut.configure(bg=self.common[4], fg=self.common[12])
        self.Button1.configure(bg=self.common[4], fg=self.common[12], activebackground="#cccccc", activeforeground = "#222222")
        for i in range(0,len(self.menu_set)):
            self.menu_set[i].config(bg=_bgmenu, fg=_fgmenu)
        for i in range(0,len(self.label_set)):
            #if type(self.label_set[i]) == tk.Label():
                self.label_set[i].config(background = self.common[15],foreground = self.common[4])
            #if type(self.entry_set[i]) == tk.Entry():
                self.entry_set[i].config(background = self.common[11],foreground = self.common[1])
        self.MagnetA.configure(background = self.common[5], fg=self.common[14])
        self.MagnetB.configure(background = self.common[5], fg=self.common[14])
        
    def simplify_menu(self):
        _bgmenu='#aaddaa'
        self.menubar  =  tk.Menu(self.Canvas1,font = self.infont, bg = _bgmenu, bd=10, fg = "brown", relief="raised")
        # for items in self.menu_items:
        #     items = tk.Menu(self.menubar, font= self.minilabel, bg = _bgmenu, bd=5, tearoff=0)

        for i in range(0,len(self.menu_set)):
            self.menubar.add_cascade(label=self.menu_labels[i], menu=self.menu_items[i], underline=True)
        
        for i in range(0,len(self.file_opts)):
            self.file.add_command(label=self.file_opts[i], command=self.file_items[i])
        self.file.add_separator()
        #self.file.add_command(label="Exit", command=top.destroy)
       
        for i in range(0,len(self.edit_opts)):
            self.edit.add_command(label=self.edit_opts[i])
        self.edit.add_separator()
        

    def create_file(self):
        fname=simpledialog.askstring("New File wizard", "Enter the Filename : ", parent=self.Canvas1)
        #one more outside try block for different OS(currently for Windows)
        if os.name=='nt':
            try:
                self.directory = "C:\\ProgramData\\Models\\"
            except:
                messagebox.showwarning("Folder does not exist", "The folder or directory to create file doesnt exist")
            else:
                os.mkdir("Models")
                shutil.move("Models", "C:\\ProgramData")
                self.directory = "C:\\ProgramData\\Models\\"
        elif os.name=='posix':
            try:
                self.directory = "/Applications/Models/"
            except:
                messagebox.showwarning("Folder does not exist", "The folder or directory to create file doesnt exist")
            else:
                os.mkdir("Models")
                shutil.move("Models", "/Applications")
                self.directory = "/Applications/Models/"
        else:
            messagebox.showwarning("Wrong OS Name suggested", "Contact developer/company to update the OS compatibility")
        self.filepath=os.path.join(self.directory, str(fname)+'.pbm')
        self.n=0
        try:
            open(self.filepath,'w+')
        except FileExistsError:
            self.n+=1
            self.filepath=self.filepath+str(self.n)
            open(self.filepath,'w+')

    def open_file(self): #read/write mode is used
        self.save_path = askdirectory()#simpledialog.askstring("Open File wizard", "Enter the path to open file : ", parent=self.Canvas1)
        self.fname = askopenfilename()#simpledialog.askstring("Open File wizard", "Enter the file name : ", parent=self.Canvas1)
        self.full_name=str(os.path.join(self.save_path, str(self.fname)))
        try:  
            open(self.full_name,"r+")
        except FileNotFoundError:
            messagebox.showerror("File Not Found 😕", "Please enter valid Name")

    def save_file_as(self): #write mode is perfect
        self.save_path=askdirectory()#simpledialog.askstring("Save File wizard", "Enter the path to save file : ", parent=self.Canvas1)
        self.fname=asksaveasfilename()
        self.full_name=str(os.path.join(self.save_path, str(self.fname)+'.pbm'))
        self.n=0
        try:
            if self.fname=="":
                self.fname="new"
            if self.save_path=="":
                self.save_path=os.getcwd()
            self.full_name=str(os.path.join(self.save_path, str(self.fname)+'.pbm'))
            open(self.full_name, 'w')
        except FileExistsError:
            self.n+=1
            self.full_name=str(os.path.join(self.save_path, str(self.fname)+str(self.n)+'.pbm'))
            with open(self.full_name,'w+') as fp:
                pass

    def save_file(self): #append mode is used
        self.full_name=str(os.path.join(os.getcwd(), str(self.save_file_as())+'.pbm'))
        open(self.full_name, 'a')

    def define_limit(self):
        self.LabelOut.configure(foreground ="yellow")
        
        if float(self.radius.get())<=30 or float(self.radius1.get()) <=30 or float(self.radius.get())>=180 or float(self.radius1.get())>=180:
            self.r = simpledialog.askfloat("Radius values(30-180)", "Enter Coil A radius Again", initialvalue=70, minvalue=30, maxvalue=180, parent=self.canv1)
            self.r1 = simpledialog.askfloat("Radius values(30-180)", "Enter Coil B radius Again", initialvalue=70, minvalue=30, maxvalue=180, parent=self.canv2)
            self.radius.set(str(self.r))
            self.radius1.set(str(self.r1))
           
            self.limit.configure(text="Enter radius values between 30-180")
            #self.limit.config( fg="red")
                        
    def create_incoil(self):
            self.coil  =  turtle.RawTurtle(self.Canv, "circle")
            self.coil.color("#000030","brown")
            self.coil.shapesize(stretch_wid = 3, stretch_len = 3, outline=7)
            self.coil.speed(10)
                        
            self.cr1 = turtle.RawTurtle(self.Canv)
            self.cr1.color("#aaee00")
            self.cr1.turtlesize(stretch_wid = 0.5, stretch_len = 0.5)
            self.cr1.speed(10)
            self.cr1.pensize(7)
            
            self.cr2 = turtle.RawTurtle(self.Canv)
            self.cr2.color("#aaee00")
            self.cr2.turtlesize(stretch_wid = 0.5, stretch_len = 0.5)
            self.cr2.speed(10)
            self.cr2.pensize(7)
            
    def create_infield(self):
            self.dir = turtle.RawTurtle(self.Canv, "arrow")
            self.dir.color("#1e273e")
            self.dir.begin_fill()
            self.dir.fillcolor("blue")
            self.dir.turtlesize(stretch_wid = 1, stretch_len = 1)
            self.dir.pensize(7)
            self.dir.rt(180)
            self.dir.end_fill()
            #self.define_limit()
            if float(self.radius.get())==0:
                self.dir.ht()
    
    def create_outcoil(self):
            self.coil1  =  turtle.RawTurtle(self.Canv, "circle")
            self.coil1.color("#000030","brown")
            self.coil1.speed(10)
            self.coil1.shapesize(stretch_wid = 3, stretch_len = 3, outline=7)          
            self.thumb = turtle.RawTurtle(self.Canv, "circle")
            self.thumb.color("#aaee00")
            self.thumb.turtlesize(stretch_wid = 1, stretch_len = 1)
            self.thumb.pensize(2)
            self.thumb.speed(10)
    
    def create_outfield(self):                    
            self.dir1 =  turtle.RawTurtle(self.Canv, "arrow")
            self.dir1.color("#1e273e")
            self.dir1.begin_fill()
            self.dir1.fillcolor("blue")
            self.dir1.turtlesize(stretch_wid = 1, stretch_len = 1)
            self.dir1.pensize(7)
            self.dir1.end_fill()
            #self.define_limit()
            if float(self.radius1.get())==0:
                self.dir1.ht()
                                        
    def calc_field(self, i11, r11):
        if self.radius.get().isdigit()==False or self.radius1.get().isdigit()==False or self.current.get().isdigit()==False or self.current1.get().isdigit()==False:
            self.c = simpledialog.askfloat("Current values", "Enter Coil A current in numbers", initialvalue=7, minvalue=1, maxvalue=100, parent=self.canv1)
            self.c1 = simpledialog.askfloat("Current values", "Enter Coil B current in numbers", initialvalue=7, minvalue=1, maxvalue=100, parent=self.canv2)
            self.r = simpledialog.askfloat("Radius values", "Enter Coil A radius in numbers", initialvalue=70, minvalue=30, maxvalue=180, parent=self.canv1)
            self.r1 = simpledialog.askfloat("Radius values", "Enter Coil B radius in numbers", initialvalue=70, minvalue=30, maxvalue=180, parent=self.canv2)
            self.current.set(str(self.c))
            self.current1.set(str(self.c1))
            self.radius.set(str(self.r))
            self.radius1.set(str(self.r1))
        try:
            self.field = (float(i11)/float(r11))*(10**-7)
            messagebox.showinfo("RESULTANT FIELD","The resultant Field is shown aside and calculated as : {g:1.10f}".format(g=self.field))
        except (ValueError, TclError, ZeroDivisionError):
            i11=(self.c+self.c1)/2
            r11=(self.r+self.r1)/2
            self.field = (float(i11)/float(r11))*(10**-7)
            messagebox.showwarning("Enter Numbers only", "Please enter numerical values(except zero)")
        self.popup.configure(text ="Resultant Field is  : {g:1.10f}".format(g=self.field))
        return self.field
        
    def show_xx(self):
        self.Canv.delete("all")
        self.Button1.unbind('<Button-1>')
        #self.calc = self.calc_field(self.current.get(), self.r)-self.calc_field(self.current1.get(), float(self.radius.get()))
        self.create_incoil()
        self.cr1.write("Field generated for Inward current", align="left")
        #first coil
        self.coil.penup()
        self.coil.goto(10,-140)
        self.coil.pendown()
        self.define_limit()
        try:    
            self.coil.turtlesize(stretch_wid = float(self.radius.get())/20, stretch_len = float(self.radius.get())/20)
        except:
            self.radius.set(str(self.r))
            self.radius1.set(str(self.r1))
        self.cr1.penup()
        self.cr1.goto(0,-185)
        self.cr1.pendown()
        self.cr1.penup()
        self.cr1.lt(90)
        self.cr1.fd(60)
        self.cr1.pendown()
        self.cr1.goto(25,-150)
        self.cr2.penup()
        self.cr2.goto(25,-185)
        self.cr2.pendown()
        self.cr2.penup()
        self.cr2.lt(90)
        self.cr2.fd(60)
        self.cr2.pendown()
        self.cr2.goto(0,-150)
        
        #second coil
        self.create_incoil()
        self.coil.penup()
        self.coil.goto(300,-200)
        self.coil.pendown()
        self.coil.penup()
        self.coil.lt(90)
        self.coil.fd(60)
        self.coil.pendown()
        try:
            self.coil.turtlesize(stretch_wid = float(self.radius1.get())/20, stretch_len = float(self.radius1.get())/20)
        except:
            self.radius.set(str(self.r))
            self.radius1.set(str(self.r1))
        self.cr1.penup()
        self.cr1.goto(290,-185)
        self.cr1.pendown()
        self.cr1.penup()
        self.cr1.lt(90)
        self.cr1.fd(60)
        self.cr1.pendown()
        self.cr1.goto(315,-150)
        self.cr2.penup()
        self.cr2.goto(315,-185)
        self.cr2.pendown()
        self.cr2.penup()
        self.cr2.lt(90)
        self.cr2.fd(60)
        self.cr2.pendown()
        self.cr2.goto(290,-150)
        self.create_infield()
        self.dir.penup()
        self.dir.goto(320, -(float(self.radius.get())+float(self.radius1.get()))/2-140)
        self.dir.pendown()

        for i in range(10,30,10):
           self.dir.forward(320)
           self.dir.circle(-((float(self.radius1.get())+float(self.radius.get()))/2),180)
           
        self.Button1.bind("<Button-1>", lambda e: self.show_field(), add = True)
        
    def show_xo(self):
        self.Canv.delete("all")
        self.Button1.unbind('<Button-1>')
        self.create_incoil()
        self.create_outcoil()

        self.coil.penup()
        self.coil.goto(10,-140)
        self.coil.pendown()
        self.define_limit()
        try:
            self.coil.turtlesize(stretch_wid = float(self.radius.get())/20, stretch_len = float(self.radius.get())/20)
        except:
            self.radius.set(str(self.r))
            self.radius1.set(str(self.r1))
        self.cr1.penup()
        self.cr1.goto(0,-185)
        self.cr1.pendown()
        self.cr1.penup()
        self.cr1.lt(90)
        self.cr1.fd(60)
        self.cr1.pendown()
        self.cr1.goto(25,-150)
        self.cr2.penup()
        self.cr2.goto(25,-185)
        self.cr2.pendown()
        self.cr2.penup()
        self.cr2.lt(90)
        self.cr2.fd(60)
        self.cr2.pendown()
        self.cr2.goto(0,-150)
        
        self.coil1.penup()
        self.coil1.goto(300,-200)
        self.coil1.pendown()
        self.coil1.penup()
        self.coil1.lt(90)
        self.coil1.fd(60)
        self.coil1.pendown()
        try:
            self.coil1.turtlesize(stretch_wid = float(self.radius1.get())/20, stretch_len = float(self.radius1.get())/20)
        except:
            self.radius.set(str(self.r))
            self.radius1.set(str(self.r1))
        self.thumb.penup()
        self.thumb.goto(300,-200)
        self.thumb.pendown()
        self.thumb.penup()
        self.thumb.lt(90)
        self.thumb.fd(60)
        self.thumb.pendown()
        self.create_infield()
        self.dir.penup()
        self.dir.goto(10,-float(self.radius.get())-140)
        self.dir.pendown()
        self.create_outfield()
        self.dir1.penup()
        self.dir1.goto(300,-float(self.radius1.get())-140)
        self.dir1.pendown()
        
        for i in range(10,20,10):
            self.dir.circle(-float(self.radius.get()))
            self.dir1.circle(float(self.radius1.get()))
            
        self.Button1.bind("<Button-1>", lambda e: self.show_field(), add = True)
        
    def show_ox(self):
        self.Canv.delete("all")
        self.Button1.unbind('<Button-1>')
        self.create_outcoil()
        self.create_incoil()
        self.coil1.penup()
        self.coil1.goto(10,-140)
        self.coil1.pendown()
        self.define_limit()
        try:
            self.coil1.turtlesize(stretch_wid = float(self.radius.get())/20, stretch_len = float(self.radius.get())/20)
        except:
            self.radius.set(str(self.r))
            self.radius1.set(str(self.r1))
        self.thumb.penup()
        self.thumb.goto(12,-200)
        self.thumb.pendown()
        self.thumb.penup()
        self.thumb.lt(90)
        self.thumb.fd(60)
        self.thumb.pendown()

        self.coil.penup()
        self.coil.goto(300,-200)
        self.coil.pendown()
        self.coil.penup()
        self.coil.lt(90)
        self.coil.fd(60)
        self.coil.pendown()
        try:
            self.coil.turtlesize(stretch_wid = float(self.radius1.get())/20, stretch_len = float(self.radius1.get())/20)
        except:
            self.radius.set(str(self.r))
            self.radius1.set(str(self.r1))    
        self.cr1.penup()
        self.cr1.goto(290,-185)
        self.cr1.pendown()
        self.cr1.penup()
        self.cr1.lt(90)
        self.cr1.fd(60)
        self.cr1.pendown()
        self.cr1.goto(315,-150)
        self.cr2.penup()
        self.cr2.goto(315,-185)
        self.cr2.pendown()
        self.cr2.penup()
        self.cr2.lt(90)
        self.cr2.fd(60)
        self.cr2.pendown()
        self.cr2.goto(290,-150)

        self.create_outfield()
        self.dir1.penup()
        self.dir1.goto(10, -float(self.radius.get())-140)
        self.dir1.pendown()
        self.create_infield()
        self.dir.penup()
        self.dir.goto(300,-float(self.radius1.get())-140)
        self.dir.pendown()
        
        for i in range(10,20,10):
            self.dir1.circle(float(self.radius.get()))
            self.dir.circle(-float(self.radius1.get()))
        self.Button1.bind("<Button-1>", lambda e: self.show_field(), add = True)
        
    def show_oo(self):
        self.Canv.delete("all")
        self.Button1.unbind('<Button-1>')
        #self.calc = self.calc_field(self.current.get(), float(self.radius.get()))+self.calc_field(self.current1.get(), self.r1)-self.calc_field(self.current1.get(), float(self.radius1.get()))
        self.create_outcoil()
        self.thumb.write("Field generated for Outward current", align="left")        
        #first coil Out
        self.coil1.penup()
        self.coil1.goto(10,-140)
        self.coil1.pendown()
        self.define_limit()
        try:
            self.coil1.turtlesize(stretch_wid = float(self.radius.get())/20, stretch_len = float(self.radius.get())/20)
        except:
            self.radius.set(str(self.r))
            self.radius1.set(str(self.r1))
        self.thumb.penup()
        self.thumb.goto(12,-200)
        self.thumb.pendown()
        self.thumb.penup()
        self.thumb.lt(90)
        self.thumb.fd(60)
        self.thumb.pendown()
        
        #second coil Out
        self.create_outcoil()
        self.coil1.penup()
        self.coil1.goto(300,-200)
        self.coil1.pendown()
        self.coil1.penup()
        self.coil1.lt(90)
        self.coil1.fd(60)
        self.coil1.pendown()
        
        try:
            self.coil1.turtlesize(stretch_wid = float(self.radius1.get())/20, stretch_len = float(self.radius1.get())/20)
        except:
            self.radius.set(str(self.r))
            self.radius1.set(str(self.r1))
        self.thumb.penup()
        self.thumb.goto(300,-200)
        self.thumb.pendown()
        self.thumb.penup()
        self.thumb.lt(90)
        self.thumb.fd(60)
        self.thumb.pendown()
        
        self.create_outfield()
        self.dir1.penup()
        self.dir1.goto(320, -140-(float(self.radius.get())+float(self.radius1.get()))/2)
        self.dir1.pendown()
        #self.dir.ht()
        for i in range(10,30,10):
          self.dir1.circle((float(self.radius1.get())+float(self.radius.get()))/2,180)
          self.dir1.forward(320)
        self.Button1.bind("<Button-1>", lambda e: self.show_field(), add = True)
        
    def show_field(self):
        self.field=self.calc_field(self.current.get()+self.current1.get(), self.radius.get()+self.radius1.get())
        #self.popup.configure(text ="Resultant Field is  :  {g:1.10f}".format(g=self.field))   
        
        if self.left.get()[0].lower() == 'x':
            if self.right.get()[0].lower() == 'x':
                self.Button1.unbind("<Button-1>")
                #Canv method
                self.Button1.bind("<Button-1>", lambda e: self.show_xx(), add = True)
            elif self.right.get().__contains__('.'):
                self.Button1.unbind("<Button-1>")
                #Canv method
                self.Button1.bind("<Button-1>", lambda e: self.show_xo(), add = True)
        elif self.left.get().__contains__('.'):
            if self.right.get()[0].lower() == 'x':
                self.Button1.unbind("<Button-1>")
                #Canv method
                self.Button1.bind("<Button-1>", lambda e: self.show_ox(), add = True)
            elif self.right.get().__contains__('.'):
                self.Button1.unbind('<Button-1>')
                self.Button1.bind("<Button-1>", lambda e: self.show_oo(), add = True)
        else:
            self.Canv.delete("all")
            self.popup.configure(text = "Select both coil directions")
            self.Button1.bind("<Button-1>", lambda e: 
            self.calc_field(self.current.get()+self.current1.get(), self.radius.get()+self.radius1.get()), add = True)
                
if __name__  ==  '__main__':
    vp_start_gui()
