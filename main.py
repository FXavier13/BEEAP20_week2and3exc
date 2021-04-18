import pandas as pd
import pandas
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.font as tkFont

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

class App:
    def __init__(self, root):
        # setting title
        root.title("Energy Usage 2010")
        # setting window size
        width = 650
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
        self.__Cities_List["justify"] = "center" #Getting the List Box to display all characters of the City name
        self.__Cities_List.place(x=400, y=50, width=120, height=25)
        self.__Cities_List.bind("<<ComboboxSelected>>", self.__comboBoxCb)

       
        self.__FileName_Label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.__FileName_Label["font"] = ft
        self.__FileName_Label["fg"] = "#333333"
        self.__FileName_Label["justify"] = "center"
        self.__FileName_Label["text"] = "Energy Usage 2010"
        self.__FileName_Label.place(x=150, y=50, width=110, height=25)

        self.__CitySelect_Label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.__CitySelect_Label["font"] = ft
        self.__CitySelect_Label["fg"] = "#333333"
        self.__CitySelect_Label["justify"] = "center"
        self.__CitySelect_Label["text"] = "Select City"
        self.__CitySelect_Label.place(x=300, y=50, width=110, height=25)
        
        #TRIAL CODE FOR CANVAS 1

        #The Energy Usage 2010 Dataset that will be used to obtain the plots 
        OriginalDataSet=pd.read_csv('Energy_Usage_2010.csv')
        OriginalDataSet=OriginalDataSet.dropna()
        OriginalDataSet.head()
        print(OriginalDataSet)

        #Mothly KWH Average
        OriginalDataSet[:,OriginalDataSet.columns.get_loc('KWH JANUARY 2010','KWH FEBRUARY 2010','KWH MARCH 2010','KWH APRIL 2010','KWH MAY 2010','KWH JUNE 2010','KWH JULY 2010','KWH AUGUST 2010','KWH SEPTEMBER 2010','KWH OCTOBER 2010','KWH NOVEMBER 2010','KWH DECEMBER 2010')].mean()
        
        #Monthly THERM Average
        OriginalDataSet[:,OriginalDataSet.columns.get_loc('THERM JANUARY 2010','THERM FEBRUARY 2010','THERM MARCH 2010','TERM APRIL 2010','THERM MAY 2010','THERM JUNE 2010','THERM JULY 2010','THERM AUGUST 2010','THERM SEPTEMBER 2010','THERM OCTOBER 2010','THERM NOVEMBER 2010','THERM DECEMBER 2010')].mean()

        #KWH Standard Deviation

        #THERM Standard Deviation


        #Creating the Plot Function Class
class Plot:
        def __init__(self, root): 
            fig=Figure(figsize=(3,3),dpi=100)
            fig, axs = plt.subplots(2, 2,sharex=True)
            fig.suptitle('Energy Usage Summary')
            x=np.linspace(100,1000,num=200)
            y=np.linspace(100,2000,num=200)

        #Monthly KWH Canvas
        plt.hist(OriginalDataSet.Monthly_KWH_Average,bins=100,density=True,histtype='bar')
        axs[0, 0].plot(x, y,color='#4257f5')
        axs[0, 0].set_title('Monthly KWH Average')
        Monthly_KWH_Average = fig.add_subplot(111)


        #Establishing labels for x and y axes
        for ax in axs.flat:
            ax.set(xlabel='Months', ylabel='Consumption')


        #Making x axis invisible
        for ax in axs.flat:
            ax.label_outer()

        Monthly_KWH_Average.plot(x,y)
        plt.show() 

        self.__Monthly_KWH_Average = FigureCanvasTkAgg(fig,self = root)
        self.__Monthly_KWH_Average = tk.Canvas(root)
        self.__Monthly_KWH_Average.place(x=50, y=130, width=234, height=140)
        Monthly_KWH_Average.draw() #Or Canvas.draw()?

        #Placing the Canvas onto the TKinter Window
        
        Monthly_KWH_Average.get_tk_widget().pack()
        
        #Creating the MatplotLib Tool Bar
        
        toolbar=NavigationToolbar2Tk(Monthly_KWH_Average,root)

        #Placing the Tool Bar onto the Tkinter Window
        Monthly_KWH_Average.get_tk_widget().pack()

        #Button for displaying the plot
        Energy_Usage_Summary_button=Button(self=root, command = plot, height =2, width = 10,text ="Plot Summary")

        #Placing the button onto the main window
        Energy_Usage_Summary_button.pack()
        
        root.mainloop() #Running the GUI

        #END OF TRIAL CODE



        # these canvases are broken, fix them
        self.__Monthly_KWH_Average = tk.Canvas(root)
        self.__Monthly_KWH_Average.place(x=50, y=130, width=234, height=140)
        Monthly_KWH_Average.draw()

        self.__GLineEdit_985 = tk.Canvas(root)
        self.__GLineEdit_985.place(x=310, y=130, width=239, height=139)

        self.__GLineEdit_392 = tk.Canvas(root)
        self.__GLineEdit_392.place(x=50, y=290, width=233, height=157)

        self.__GLineEdit_700 = tk.Canvas(root)
        self.__GLineEdit_700.place(x=310, y=290, width=234, height=158)

        def __Load_CSV_command(self,root):
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
        self.__subdf = self.__df.loc[self.__df['COMMUNITY AREA NAME'] == self.__Cities_List.get()]
        print(self.__subdf.head())
        fig1 = Figure(figsize=(self.__GLineEdit_392.winfo_width, self.__GLineEdit_392.winfo_height), dpi=100)
        ax1 = fig1.add_subplot(111)
        self.__subdf.iloc[:, range(self.__subdf.columns.get_loc['KWH JANUARY 2010'], 12)].mean().plot.bar(ax=ax1)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
