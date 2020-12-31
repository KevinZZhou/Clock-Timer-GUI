import tkinter as tk
from pathlib import Path
from PIL import Image
from time import strftime
import math

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
        
        # Initialize clock hands
        self.hand_hours = self.canvas.create_line(0, 0, 0, 0)
        self.hand_minutes = self.canvas.create_line(0, 0, 0, 0)
        self.hand_seconds = self.canvas.create_line(0, 0, 0, 0)
        
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
        self.update_hands()
        self.after(100, self.tick)
    
    def update_hands(self):
        """
        This function updates all three clock hands (hour, minute, second).
        """

        # Get the current time based on the timezone as a datetime object
        datetime_object = self.dropdown.get_datetime()

        # Update clock hands
        self.update_hours(datetime_object)
        self.update_minutes(datetime_object)
        self.update_seconds(datetime_object)
        
    def update_hours(self, datetime_object): 
        """
        This function updates the hour hand of the clock.

        Args:
            datetime_object (datetime): Current time based on the timezone
        """

        # Values
        hours: int = datetime_object.hour
        minutes: int = datetime_object.minute
        hours_length: int = self.center_X

        # Calculate the angle of the hour hand
        angle_hours_deg = ((hours * 30) + (minutes * 30 / 60) - 90) % 360
        angle_hours_rad = angle_hours_deg * math.pi / 180

        # Position the new clock hand
        self.canvas.delete(self.hand_hours)
        self.hand_hours = self.canvas.create_line(
                self.center_X, self.center_Y, 
                self.center_X + hours_length * math.cos(angle_hours_rad), 
                self.center_X + hours_length * math.sin(angle_hours_rad), 
                width = 6, fill = "black")

    def update_minutes(self, datetime_object):
        """
        This function updates the minute hand of the clock.

        Args:
            datetime_object (datetime): Current time based on the timezone
        """

        # Values
        minutes: int = datetime_object.minute
        seconds: int = datetime_object.second
        minutes_length: int = self.center_X // 2

        # Calculate the angle of the minute hand
        angle_minutes_deg = ((minutes * 6) + (seconds * 6 / 60) - 90) % 360
        angle_minutes_rad = angle_minutes_deg * math.pi / 180

        # Position the new clock hand
        self.canvas.delete(self.hand_minutes)
        self.hand_minutes = self.canvas.create_line(
                self.center_X, self.center_Y, 
                self.center_X + minutes_length * math.cos(angle_minutes_rad), 
                self.center_X + minutes_length * math.sin(angle_minutes_rad), 
                width = 4, fill = "dark gray")

    def update_seconds(self, datetime_object):
        """
        This function updates the second hand of the clock.

        Args:
            datetime_object (datetime): Current time based on the timezone
        """

        # Values
        seconds: int = datetime_object.second
        seconds_length: int = self.center_X
        
        # Calculate the angle of the second hand
        angle_seconds_deg = ((seconds * 6) - 90) % 360
        angle_seconds_rad = angle_seconds_deg * math.pi / 180

        # Position the new clock hand
        self.canvas.delete(self.hand_seconds)
        self.hand_seconds = self.canvas.create_line(
                self.center_X, self.center_Y, 
                self.center_X + seconds_length * math.cos(angle_seconds_rad), 
                self.center_X + seconds_length * math.sin(angle_seconds_rad), 
                width = 2, fill = "gray")