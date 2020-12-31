import tkinter as tk
from playsound import playsound

from TimeButtons import TimeButtons

class PomodoroTimer(tk.Frame):
    """
    This class is the pomodoro timer that will appear in MainApp.
    When the Start button is pressed, the timer will automatically begin 
    counting down at preset intervals: 
        25 minute study period
        5 minute short break after each study period
        Additional 15 minute long break after every 5th study period

    Args:
        tk.Frame: Parent class
    """

    def __init__(self, root):
        """
        This function creates an instance of PomodoroTimer.

        Args:
            root: An instance of Tk will be placed here.  
                  This will place PomodoroTimer in a root window.
        """

        # Initialize object
        tk.Frame.__init__(self, root)
        self.root = root
        self.minutes = 25
        self.seconds = 0
        self.timer = self.time_to_string()
        self.active = False
        self.pomodoro_number = 0
        self.status = "Studying!"

        # Create timer, status, and pomodoro label
        self.timer_label = tk.Label(self.root, text = self.timer, 
                font = ("verdana", 32, "bold"), background = "white", 
                foreground = "black", borderwidth = 1, relief = "solid")
        self.status_label = tk.Label(self.root, text = self.status, 
                font = ("verdana", 20), background = "white", 
                foreground = "black", borderwidth = 1, relief = "solid")
        self.pomodoro_label = tk.Label(self.root, text = "Number of " + 
                "pomodoros: " + str(self.pomodoro_number) + "/4", font = 
                ("verdana", 20), background = "white", foreground = "black", 
                borderwidth = 1, relief = "solid")
        
        # Place widgets into frame
        self.timer_label.pack(expand = True, fill = "both")
        self.status_label.pack(fill = "both")
        self.pomodoro_label.pack(fill = "both")

    def time_to_string(self):
        """
        This function takes the integer values of the pomodoro timer and 
        converts them into a single string as a pomodoro timer's output.

        Returns:
            str: A string displaying the current pomodoro timer output
        """

        # Convert self.hours, self.minutes, and self.seconds into strings
        minutes_string = "{:02d}".format(self.minutes)
        seconds_string = "{:02d}".format(self.seconds)

        # Return a string combining the three values
        time_string = minutes_string + ":" + seconds_string
        return time_string

