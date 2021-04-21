# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 07:35:43 2021

@author: Francis
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.font as tkFont
from pandas import DataFrame

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
class App:
    def __init__(self, root):
        dpi = root.winfo_fpixels(100)
         # Creating the frame for Buttons & Root controls
        self.controls = tk.Frame(root)
        self.controls.pack(ipadx=10, ipady=10)
         # frame for  Bar charts
        self.graphs = tk.Frame(root)
        self.graphs.pack(side=tk.BOTTOM,
                             padx=5, pady=5,
                             fill=tk.BOTH, expand=True)
        root.title("Energy Usage 2010")
        # Expanded Window Size to fit a full data display
        width = 1200
        height = 700
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        #File Loading Button
        self.loadbutton = tk.Button(root)
        self.loadbutton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.loadbutton["font"] = ft
        self.loadbutton["fg"] = "#000000"
        self.loadbutton["justify"] = "center"
        self.loadbutton["text"] = "Load File"
        self.loadbutton.place(x=70, y=15, width=70, height=25,)
        self.loadbutton["command"] = self.loadfile_command

        self.selectorcombo = ttk.Combobox(root)
        self.selectorcombo.place(x=550, y=15, width=80, height=25)
        self.selectorcombo.bind("<<ComboboxSelected>>", self.hCombo_city_selected)
        #Displaying the loaded File Name/Path through a Label
        self.filename = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.filename["font"] = ft
        self.filename["fg"] = "#333333"
        self.filename["justify"] = "center"
        self.filename["text"] = "File Name"
        self.filename.place(x=150, y=15, width=200, height=25)
        #Select City Label
        self.townselectorlabel = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.townselectorlabel["font"] = ft
        self.townselectorlabel["fg"] = "#333333"
        self.townselectorlabel["justify"] = "center"
        self.townselectorlabel["text"] = "Select City"
        self.townselectorlabel.place(x=450, y=15, width=70, height=25)
       #Canvases
        self.Canvas_upleft = tk.Frame(self.graphs)
        self.Canvas_upleft.place(relx=0, rely=0,
                                   relwidth=0.5, relheight=0.5)
        self.fig1 = plt.figure(dpi=100)
        self.ax1 = self.fig1.add_subplot(111)
        self.ax1.text(0.1,0.5,"Plot 1", fontsize=10)
        self.chart1 = FigureCanvasTkAgg(self.fig1, self.Canvas_upleft)
        self.chart1.get_tk_widget().pack(padx=5, pady=5,
                                         side=tk.BOTTOM,
                                         fill=tk.BOTH, expand=True)
        self.Canvas_upright = tk.Frame(self.graphs)
        self.Canvas_upright.place(relx=0.5, rely=0,
                                    relwidth=0.5, relheight=0.5)
        self.fig2 = plt.figure(dpi=100)
        self.ax2 = self.fig2.add_subplot(111)
        self.ax2.text(0.1,0.5,"Plot 2 ", fontsize=10)
        self.chart2 = FigureCanvasTkAgg(self.fig2, self.Canvas_upright)
        self.chart2.get_tk_widget().pack(padx=5, pady=5,
                                         side=tk.BOTTOM,
                                         fill=tk.BOTH, expand=True)
        self.Canvas_botleft = tk.Frame(self.graphs)
        self.Canvas_botleft.place(relx=0, rely=0.5,
                                    relwidth=0.5, relheight=0.5)
        self.fig3 = plt.figure(dpi=100)
        self.ax3 = self.fig3.add_subplot(111)
        self.ax3.text(0.1,0.5,"Plot 3 ", fontsize=10)
        self.chart3 = FigureCanvasTkAgg(self.fig3, self.Canvas_botleft)
        self.chart3.get_tk_widget().pack(padx=5, pady=5,
                                         side=tk.BOTTOM,
                                         fill=tk.BOTH, expand=True)
        self.Canvas_botright = tk.Frame(self.graphs)
        self.Canvas_botright.place(relx=0.5, rely=0.5,
                                     relwidth=0.5, relheight=0.5)
        self.fig4 = plt.figure(dpi=100)
        self.ax4 = self.fig4.add_subplot(111)
        self.ax4.text(0.1,0.5,"Plot 4", fontsize=10)
        self.chart4 = FigureCanvasTkAgg(self.fig4, self.Canvas_botright)
        self.chart4.get_tk_widget().pack(padx=5, pady=5,
                                         side=tk.BOTTOM,
                                         fill=tk.BOTH, expand=True)
    def loadfile_command(self):
        filePath = fd.askopenfilename(initialdir='.')
        try:
            self.csv_contents = pd.read_csv(filePath)
            self.csv_cleaned = self.csv_contents.dropna()
            self.selectorcombo['values'] = list(self.csv_cleaned['COMMUNITY AREA NAME'].unique())
            self.filename["text"] = filePath
        except:
            tk.messagebox.showinfo("Nope","NOPE ")

    
    def hCombo_city_selected(self, event=None):
        selected_city = self.selectorcombo.get()
        print(f"Selected city: {selected_city}")
        self.subfields = self.csv_cleaned.loc[self.csv_cleaned['COMMUNITY AREA NAME'] == self.selectorcombo.get()]
        print(self.subfields.head())
        x_axis = 'Months'
        y_axis='Energy Consumption'
        def upleft(self):
            # Figure = KWH Average by month
            self.ax1.clear()
            janind = self.subfields.columns.get_loc("KWH JANUARY 2010")
            self.ax1.bar(range(1, 13),
                         (self.subfields.iloc[:,  range(janind, (janind + 12))]).mean())
            self.ax1.set_title('KWH Monthly Average')
            self.ax1.set_xlabel(x_axis); self.ax1.set_ylabel(y_axis)
            self.chart1.draw()
        def upright(self):
            # Figure = THERM value by month
            self.ax2.clear()
            janind = self.subfields.columns.get_loc("THERM JANUARY 2010")
            self.ax2.bar(range(1, 13),
                         (self.subfields.iloc[:, range(janind, (janind + 12))]).mean())
            self.ax2.set_title('THERM Monthly Average')
            self.ax2.set_xlabel(x_axis); self.ax2.set_ylabel(y_axis)
            self.chart2.draw()
        def botleft(self):
            # Figure = Max KWH value by month 
            self.ax3.clear()
            janind = self.subfields.columns.get_loc("KWH JANUARY 2010")
            self.ax3.bar(range(1, 13),
                         (self.subfields.iloc[:,  range(janind, (janind + 12))]).max())
            self.ax3.set_title('KWH Monthly Maximum')
            self.ax3.set_xlabel(x_axis); self.ax1.set_ylabel(y_axis)
            self.chart3.draw()
        def botfig(self):
            # Figure = Min THERM value by month
            self.ax4.clear()
            janind = self.subfields.columns.get_loc("THERM JANUARY 2010")
            self.ax4.bar(range(1, 13),
                         (self.subfields.iloc[:,  range(janind, (janind + 12))]).min())
            self.ax4.set_title('THERM Monthly Minimum')
            self.ax4.set_xlabel(x_axis);self.ax1.set_ylabel(y_axis)
            self.chart4.draw()
        upleft(self)
        upright(self)
        botleft(self)
        botfig(self)

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()

