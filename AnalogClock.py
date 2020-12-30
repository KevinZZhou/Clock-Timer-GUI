import tkinter as tk

class AnalogClock(tk.Frame):
    """
    This class is the analog clock that will appear in MainApp.
    The clock will default to displaying the local time on the device.
    It will contain a dropdown menu of time zones, which will allow the 
    user to change the timezone of the displayed analog time.

    tk.Frame: Parent class
    """

    def __init__(self, root): 
        """
        This function creates an instance of AnalogClock.

        Args:
            root: An instance of Tk will be placed here.  
                  This will place AnalogClock in a window.
        """

    def tick(self):
        """
        This function updates the displayed time based on the timezone.
        """
