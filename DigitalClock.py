import tkinter as tk
from tkinter import ttk
from time import strftime

class DigitalClock(tk.Frame):
    """
    This class is the digital clock that will appear in MainApp.
    The clock will default to displaying the local time on the device.
    It will contain a dropdown menu of time zones, which will allow the 
    user to change the timezone of the displayed digital time.

    tk.Frame: Parent class
    """

    def __init__(self, root): 
        """
        This function creates an instance of DigitalClock.

        Args:
            root: An instance of Tk will be placed here.  
                  This will place DigitalClock in a window.
        """

        tk.Frame.__init__(self, root)
        self.root = root
        self.time = ""
        self.label = tk.Label(root, text = self.time, font = ("arial", 
                32, "bold"), background = "navy", foreground = "white")
        self.label.pack(anchor = "center", fill ="both")
        self.tick()

    def tick(self):
        """
        This function updates the displayed time.
        """

        time: str = strftime("%H:%M:%S %p")
        self.time = time
        self.label.config(text = self.time)
        self.label.after(1000, self.tick)









