import tkinter as tk
from tkinter import ttk
from time import strftime
from dateutil.zoneinfo import get_zonefile_instance
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

        tk.Frame.__init__(self, root)
        self.root = root
        self.time = ""

        # Create the time label
        self.label = tk.Label(root, text = self.time, font = ("arial", 
                32, "bold"), background = "navy", foreground = "white")
        
        # Create the timezone dropdown box
        timezone_list = list(get_zonefile_instance().zones)
        timezone_list.sort()
        self.timezone_dropdown = ttk.Combobox(root, state = "readonly", 
                values = timezone_list)
        # Set the default value to be the local time zone of the device
        # If something goes wrong (e.g. timezone isn't found), default to EST
        try:
            local_timezone = str(get_localzone())
            self.timezone_dropdown.set(local_timezone)
        except:
            self.timezone_dropdown.set("EST")
        
        # Place widgets into frame
        self.label.pack(anchor = "center", expand = True, fill ="both")
        self.timezone_dropdown.pack()

        # Start the clock
        self.tick()

    def tick(self):
        """
        This function updates the displayed time.
        """

        time: str = strftime("%H:%M:%S %p")
        self.time = time
        self.label.config(text = self.time)
        self.label.after(1000, self.tick)
