import tkinter as tk
from tkinter import ttk
from datetime import datetime
from dateutil.zoneinfo import get_zonefile_instance
from dateutil.tz import gettz
from tzlocal import get_localzone

class TimezoneDropdown(tk.Frame):
    """
    This class contains the timezone dropdown box along with its label.
    The dropdown box will default to the local timezone of the device.

    Args:
        tk.Frame: Parent class
    """

    def __init__(self, root):
        """
        This function creates an instance of TimezoneDropdown.
        This will be called in each clock mode (DigitalClock, AnalogClock).

        Args:
            root: This will place TimezoneDropdown in a particular frame.
        """

        # Initialize object
        tk.Frame.__init__(self, root)

        # Create the timezone dropdown box and its label in a frame
        self.dropdown_frame = tk.Frame(root)
        self.dropdown_label = tk.Label(self.dropdown_frame, 
                text = "Select a timezone:", font = ("verdana", 12))
        timezone_list = list(get_zonefile_instance().zones)
        timezone_list.sort()
        self.timezone_dropdown = ttk.Combobox(self.dropdown_frame, 
                state = "readonly", values = timezone_list, 
                font = ("verdana", 12))
        
        # Set the default value to be the local time zone of the device
        # If something goes wrong (e.g. timezone isn't found), default to EST
        try:
            local_timezone = str(get_localzone())
            self.timezone_dropdown.set(local_timezone)
        except:
            self.timezone_dropdown.set("EST")
        
        # Place widgets into frame
        self.dropdown_label.pack(side = "left")
        self.timezone_dropdown.pack(side = "left")
        self.dropdown_frame.pack(side = "bottom")
    
    def get_datetime(self) -> datetime:
        """
        This function takes the selected timezone in the dropdown box and uses 
        it to convert the current local time to that timezone.
        This uses the value of the dropdown box, which would be otherwise 
        inaccessible outside of the class.

        Returns:
            datetime: Returns an object of type datetime containing 
                      info about the current time in the selected timezone.
        """

        current_timezone = self.timezone_dropdown.get()
        timezone_object = gettz(current_timezone)
        datetime_object = datetime.now(tz = timezone_object)
        return datetime_object