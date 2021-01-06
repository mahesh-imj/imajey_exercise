import tkinter as tk
from tkinter import ttk
import awesometkinter as atk

# our root
root = tk.Tk()
root.config(background=atk.DEFAULT_COLOR)

# select tkinter theme required for things to be right on windows,
# only 'alt', 'default', or 'classic' can work fine on windows 10
s = ttk.Style()
s.theme_use('default')

# 3d frame
f1 = atk.Frame3d(root)
f1.pack(side='left', expand=True, fill='both', padx=3, pady=3)

# 3d progressbar
bar = atk.RadialProgressbar3d(f1, fg='cyan', size=120)
bar.pack(padx=20, pady=20)
bar.start()

# 3d button
atk.Button3d(f1, text='3D Button').pack(pady=10)

'''if b1.Pressed(f1):
  bar1.start()
else: 
  bar1.stop()'''

f2 = atk.Frame3d(root)
f2.pack(side='left', expand=True, fill='both', padx=3, pady=3)

# flat radial progressbar
bar = atk.RadialProgressbar(f2, fg='green')
bar.pack(padx=30, pady=30)
bar.start()

'''if b1.Pressed(f2):
  bar.start()
else:
  bar.stop()'''

atk.Button3d(f2, text='Pressed Button').pack(pady=10)

root.mainloop()
