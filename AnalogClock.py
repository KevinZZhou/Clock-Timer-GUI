import tkinter as tk
from pathlib import Path

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
        self.canvas = tk.Canvas(self.root, width = 600, height = 600, 
                bg = "white")

        # Place the analog clock image on the canvas
        path = Path("files/images/")
        analog_clock = path / "analog-clock.png"
        self.image = tk.PhotoImage(file = analog_clock)
        self.canvas.create_image(300, 300, image = self.image)

        # Place widgets into frame
        self.canvas.pack()

    def tick(self):
        """
        This function updates the displayed time based on the timezone.
        """
