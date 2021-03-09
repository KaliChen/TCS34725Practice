import time
from PIL import Image, ImageTk, ImageDraw, ExifTags, ImageColor,ImageFont
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox as msg
from tkinter.ttk import Notebook
#from tkinter import filedialog
#from tkinter import ttk
#from tkinter.colorchooser import *
#import recipe_266466_1
#import i2c_symbus
from demo import show_picture, Testing, main
from maze import Maze
from sys_info import SysInfo

class SSD1306GUI():
    def __init__(self, master):
        self.parent = master

        self.init_SSD1306GUI_tab()
    def init_SSD1306GUI_tab(self):
        self.SSD1306GUI_tab = tk.Frame(self.parent)
        self.SSD1306GUI_tab.pack(side = tk.LEFT, expand=tk.YES, fill=tk.BOTH)

        self.MarkSettingPanel = tk.LabelFrame(self.SSD1306GUI_tab, text="SSD1306 GUI Panel",font=('Courier', 8))
        self.MarkSettingPanel.pack(side=tk.TOP, expand=tk.NO)

        SSD1306GUIPanel = tk.Frame(self.MarkSettingPanel)
        SSD1306GUIPanel.grid(row = 0, column = 0 ,sticky = tk.E+tk.W)        
        
        self.SysInfoButton = tk.Button(SSD1306GUIPanel, text = "System Info",font=('Courier', 7), command = SysInfo)
        self.SysInfoButton.grid(row = 0, column = 0, sticky = tk.E+tk.W)

        self.showPIctureButton = tk.Button(SSD1306GUIPanel, text = "Show Picture",font=('Courier', 7), command = show_picture)
        self.showPIctureButton.grid(row = 1, column = 0, sticky = tk.E+tk.W)
        
        self.TestingButton = tk.Button(SSD1306GUIPanel, text = "Testing",font=('Courier', 7), command = Testing)
        self.TestingButton.grid(row = 2, column = 0, sticky = tk.E+tk.W) 
        
        self.mainButton = tk.Button(SSD1306GUIPanel, text = "main",font=('Courier', 7), command = main)
        self.mainButton.grid(row = 3, column = 0, sticky = tk.E+tk.W)

        #self.MazeDemoButton = tk.Button(SSD1306GUIPanel, text = "main",font=('Courier', 7), command = self.MazeDemo(20))
        #self.MazeDemoButton.grid(row = 4, column = 0, sticky = tk.E+tk.W)



                        
if __name__ == '__main__':
    root = tk.Tk()
    SSD1306GUI(root)

    root.mainloop()
