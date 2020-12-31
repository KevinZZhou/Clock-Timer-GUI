import tkinter as tk
from pathlib import Path
from PIL import Image
from time import strftime

from TimezoneDropdown import TimezoneDropdown

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

        # Initialize object
        tk.Frame.__init__(self, root)
        self.root = root
        self.time = ""
        self.date = ""
        self.canvas = tk.Canvas(self.root, width = 600, height = 600, 
                bg = "white")
        
        # Get clock image that will be placed on the canvas
        self.image_path = Path("files/images/") / "analog-clock.png"
        self.image = tk.PhotoImage(file = self.image_path)

        # Get image dimensions
        img = Image.open(self.image_path)
        self.width, self.height = img.size
        self.center_X, self.center_Y = self.width // 2, self.height //2

        # Create the date label and timezone dropdown box
        self.date_label = tk.Label(root, text = self.date, 
                font = ("verdana", 16, "bold"), background = "white", 
                foreground = "black", borderwidth = 1, relief = "solid")
        self.dropdown = TimezoneDropdown(root)

        # Place widgets into frame
        self.canvas.create_image(self.center_X, self.center_Y, 
                image = self.image)
        self.canvas.pack()
        self.date_label.pack(expand = True, fill ="both")
        self.dropdown.pack()

        # Start the clock
        self.tick()

    def tick(self):
        """
        This function updates the displayed time based on the timezone.
        """

        # Use the timezone dropdown box to adjust the displayed date
        try:
            datetime_object = self.dropdown.get_datetime()
            date: str = datetime_object.strftime("%A, %B %d, %Y")
        except:
            date: str = strftime("%A, %B %d, %Y")
        
        # Update date if necessary
        if self.date != date:
            self.date = date
            self.date_label.config(text = self.date)
        
        self.after(100, self.tick)
