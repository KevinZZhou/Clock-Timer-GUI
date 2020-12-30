import tkinter as tk
from datetime import datetime
from tkinter import ttk
from time import strftime
from dateutil.zoneinfo import get_zonefile_instance
from dateutil.tz import gettz
from tzlocal import get_localzone

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

        # Create the time, date, and dropdown box label
        self.time_label = tk.Label(root, text = self.time, 
                font = ("verdana", 32, "bold"), background = "white", 
                foreground = "black", borderwidth = 1, relief = "solid")
        self.date_label = tk.Label(root, text = self.date, 
                font = ("berdana", 20, "bold"), background = "white", 
                foreground = "black", borderwidth = 1, relief = "solid")
        self.dropdown_label = tk.Label(root, text = "Select a timezone:", 
                font = ("verdana", 14))
        
        # Create the timezone dropdown box
        timezone_list = list(get_zonefile_instance().zones)
        timezone_list.sort()
        self.timezone_dropdown = ttk.Combobox(root, state = "readonly", 
                values = timezone_list, font = ("verdana", 14))
        # Set the default value to be the local time zone of the device
        # If something goes wrong (e.g. timezone isn't found), default to EST
        try:
            local_timezone = str(get_localzone())
            self.timezone_dropdown.set(local_timezone)
        except:
            self.timezone_dropdown.set("EST")
        
        # Place widgets into frame
        self.time_label.pack(anchor = "center", expand = True, fill ="both")
        self.date_label.pack(anchor = "center", expand = True, fill ="both")
        self.dropdown_label.pack()
        self.timezone_dropdown.pack()

        # Start the clock
        self.tick()

    def tick(self):
        """
        This function updates the displayed time based on the timezone.
        """

        # Use the timezone dropdown box to adjust the displayed time
        # If something goes wrong, default to displaying local time
        try:
            current_timezone: str = self.timezone_dropdown.get()
            timezone_object = gettz(current_timezone)
            datetime_object = datetime.now(tz = timezone_object)
            time: str = datetime_object.strftime("%I:%M:%S %p")
            date: str = datetime_object.strftime("%A, %B %d, %Y")
        except:
            time: str = strftime("%I:%M:%S %p")
            date: str = strftime("%A, %B %d, %Y")
        
        # Update time and/or date if necessary
        if self.time != time:
            self.time = time
            self.time_label.config(text = self.time)
        if self.date != date:
            self.date = date
            self.date_label.config(text = self.date)
        
        self.after(100, self.tick)