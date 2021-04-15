import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.font as tkFont

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

class App:
    def __init__(self, root):
        # setting title
        root.title("Energy Usage 2010")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.__Load_CSV = tk.Button(root)
        self.__Load_CSV["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=8)
        self.__Load_CSV["font"] = ft
        self.__Load_CSV["fg"] = "#000000"
        self.__Load_CSV["justify"] = "center"
        self.__Load_CSV["text"] = "Load CSV File"
        self.__Load_CSV.place(x=70, y=50, width=70, height=35)
        self.__Load_CSV["command"] = self.__Load_CSV_command

        self.__Cities_List= ttk.Combobox(root)
        self.__Cities_List.place(x=350, y=50, width=80, height=25)
        self.__Cities_List.bind("<<ComboboxSelected>>", self.__comboBoxCb)

        self.__FileName_Label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.__FileName_Label["font"] = ft
        self.__FileName_Label["fg"] = "#333333"
        self.__FileName_Label["justify"] = "center"
        self.__FileName_Label["text"] = "Energy Usage 2010"
        self.__FileName_Label.place(x=150, y=50, width=110, height=25)

        self.__FileName_Label.pack(side=tk.LEFT, pady=15)


        self.__CitySelect_Label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.__CitySelect_Label["font"] = ft
        self.__CitySelect_Label["fg"] = "#333333"
        self.__CitySelect_Label["justify"] = "center"
        self.__CitySelect_Label["text"] = "Select City"
        self.__CitySelect_Label.place(x=150, y=50, width=110, height=25)

        self.__FileName_Label.pack(side=tk.LEFT, pady=15)


        for i in range(1):
            for j in range(2):
                frame = tk.Frame(
                    master=window,
                        relief=tk.RAISED,
                             borderwidth=1)
        frame.grid(row=i, column=j, padx=15, pady=15)
        CitySelect_Label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        FileName_Label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()


        # these canvases are broken, fix them
        self.__GLineEdit_517 = tk.Canvas(root)
        self.__GLineEdit_517.place(x=50, y=130, width=234, height=140)

        self.__GLineEdit_985 = tk.Canvas(root)
        self.__GLineEdit_985.place(x=310, y=130, width=239, height=139)

        self.__GLineEdit_392 = tk.Canvas(root)
        self.__GLineEdit_392.place(x=50, y=290, width=233, height=157)

        self.__GLineEdit_700 = tk.Canvas(root)
        self.__GLineEdit_700.place(x=310, y=290, width=234, height=158)

    def __Load_CSV_command(self):
        filePath = fd.askopenfilename(initialdir='.')
        try:
            self.__df = pd.read_csv(filePath)
            self.__df = self.__df.dropna()
            self.__Cities_List['values'] = list(self.__df['COMMUNITY AREA NAME'].unique())
        except:
            # quick and dirty, desired behavior would be to show a notification pop up that says
            # "nope!"
            print('nope')

    # desired behavior: select one area, show 4 plots drawn on 4 canvases of that area: 
    # top left: bar chart, average KWH by month
    # top right: bar chart, average THERM by month
    # bottom left and bottom right up to you
    def __comboBoxCb(self, event=None):
        self.__subdf = self.__df.loc[self.__df['COMMUNITY AREA NAME'] == self.__GListBox_563.get()]
        print(self.__subdf.head())
        fig1 = Figure(figsize=(self.__GLineEdit_392.winfo_width, self.__GLineEdit_392.winfo_height), dpi=100)
        ax1 = fig1.add_subplot(111)
        self.__subdf.iloc[:, range(self.__subdf.columns.get_loc['KWH JANUARY 2010'], 12)].mean().plot.bar(ax=ax1)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
