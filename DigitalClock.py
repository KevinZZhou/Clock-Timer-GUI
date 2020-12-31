import tkinter as tk
from time import strftime

from TimezoneDropdown import TimezoneDropdown

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

        # Initialize object
        tk.Frame.__init__(self, root)
        self.root = root
        self.time = ""
        self.date = ""

        # Create the time and date label, and timezone dropdown box
        self.time_label = tk.Label(self.root, text = self.time, 
                font = ("verdana", 32, "bold"), background = "white", 
                foreground = "black", borderwidth = 1, relief = "solid")
        self.date_label = tk.Label(self.root, text = self.date, 
                font = ("verdana", 20, "bold"), background = "white", 
                foreground = "black", borderwidth = 1, relief = "solid")
        self.dropdown = TimezoneDropdown(self.root)

        # Place widgets into frame
        self.time_label.pack(expand = True, fill ="both")
        self.date_label.pack(expand = True, fill ="both")
        self.dropdown.pack()
        
        # Start the clock
        self.tick()

    def tick(self):
        """
        This function updates the displayed time based on the timezone.
        """

        # Use the timezone dropdown box to adjust the displayed time
        # If something goes wrong, default to displaying local time
        try:
            datetime_object = self.dropdown.get_datetime()
            time = datetime_object.strftime("%I:%M:%S %p")
            date = datetime_object.strftime("%A, %B %d, %Y")
        except:
            time = strftime("%I:%M:%S %p")
            date = strftime("%A, %B %d, %Y")
        
        # Update time and/or date if necessary
        if self.time != time:
            self.time = time
            self.time_label.config(text = self.time)
        if self.date != date:
            self.date = date
            self.date_label.config(text = self.date)
        
        self.after(100, self.tick)