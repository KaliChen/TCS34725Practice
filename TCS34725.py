import time
from PIL import Image, ImageTk, ImageDraw, ExifTags, ImageColor,ImageFont
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox as msg
from tkinter.ttk import Notebook
from tkinter import filedialog
from tkinter import ttk
from tkinter.colorchooser import *
import recipe_266466_1
import simpletest

class TCS34725():
    def __init__(self, master):
        self.parent = master

        self.init_TCS34725_tab()
    def init_TCS34725_tab(self):
        self.TCS34725_tab = tk.Frame(self.parent)
        self.TCS34725_tab.pack(side = tk.LEFT, expand=tk.YES, fill=tk.BOTH)
        #self.settingnotebook.add(self.ColorDraw_tab, text = "Color&Draw")

        self.MarkSettingPanel = tk.LabelFrame(self.TCS34725_tab, text="Color Panel",font=('Courier', 8))
        self.MarkSettingPanel.pack(side=tk.TOP, expand=tk.NO)

        '''Color Panel'''
        ColorPanel = tk.Frame(self.MarkSettingPanel)
        ColorPanel.grid(row = 0, column = 0 ,sticky = tk.E+tk.W)        
        self.ColorButton = tk.Button(ColorPanel, text = "Return Color",font=('Courier', 7), command = self.askcolor)
        self.ColorButton.grid(row = 0, column = 0, sticky = tk.E+tk.W)
        self.checkClearButton = tk.Button(ColorPanel, text = "Check Clear",font=('Courier', 7), command = self.checkClear)
        self.checkClearButton.grid(row = 1, column = 0, sticky = tk.E+tk.W) 
        
    def askcolor(self, event = None):
        #self.color = askcolor()
        self.color = recipe_266466_1.RGBToHTMLColor(simpletest.luminance())
        print(self.color)
        self.ColorButton.configure(bg=self.color)
        #print(self.HTMLColorToRGB(self.color1[1]))
        
    def checkClear(self, event = None):
        print("checkClear")
        
if __name__ == '__main__':
    root = tk.Tk()
    TCS34725(root)
    #root.resizable(width=True, height=True)
    #root.geometry(MAIN_DISPLAY_SIZE)
    root.mainloop()
