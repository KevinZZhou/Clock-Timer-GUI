import tkinter as tk

from TimeButtons import TimeButtons

class Stopwatch(tk.Frame): 
    """
    This class is the stopwatch that will appear in MainApp.
    The stopwatch counts hours, minutes, seconds, and milliseconds.
    It will start when the Start button is pressed, will stop when the Stop 
    button is pressed, and will reset when the Reset button is pressed.

    Args:
        tk.Frame: Parent class
    """

    def __init__(self, root): 
        """
        This function creates an instance of Stopwatch.

        Args:
            root: An instance of Tk will be placed here.  
                  This will place Stopwatch in a window.
        """

        # Initialize object
        tk.Frame.__init__(self, root)
        self.root = root
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        self.stopwatch = self.time_to_string()
        self.active = False

        # Create the stopwatch label and the start, stop, and reset buttons
        self.stopwatch_label = tk.Label(self.root, text = self.stopwatch, 
                font = ("verdana", 32, "bold"), background = "white", 
                foreground = "black", borderwidth = 1, relief = "solid")
        self.buttons = TimeButtons(self.root, 
                self.start, self.stop, self.reset)
        
        # Place widgets into frame
        self.stopwatch_label.pack(expand = True, fill ="both")
        self.buttons.pack()

    def time_to_string(self):
        """
        This function takes the integer values of the stopwatch and converts 
        them into a single string that looks like a stopwatch's output.

        Returns:
            str: A string displaying the current stopwatch output
        """

        # Convert self.hours, self.minutes, self.seconds, and 
        # self.milliseconds into strings
        hours_string = "{:02d}".format(self.hours)
        minutes_string = "{:02d}".format(self.minutes)
        seconds_string = "{:02d}".format(self.seconds)
        milliseconds_string = "{:03d}".format(self.milliseconds)

        # Return a string combining the four values
        time_string = (hours_string + ":" + minutes_string + ":" + 
                seconds_string + ":" + milliseconds_string)
        return time_string

    def start(self):
        """
        This function starts the stopwatch.
        """
        self.active = True
        self.tick()

    def stop(self):
        """
        This function stops the stopwatch.
        """
        self.active = False

    def reset(self):
        """
        This function resets the stopwatch.
        """

        # Set values to 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0

        # Display the correct string output and stop the stopwatch
        self.stopwatch = self.time_to_string()
        self.stopwatch_label.config(text = self.stopwatch)
        self.stop()
    
    def tick(self):
        """
        This function increments the number of milliseconds by 1 when the 
        stopwatch is active.
        It then adjusts the of number seconds, minutes, and hours if necessary 
        and sets the new stopwatch output.
        """

        # Adjusts the stopwatch values if it is active
        if self.active == True:
            self.milliseconds = (self.milliseconds + 1) % 1000
            if self.milliseconds == 0:
                self.seconds = (self.seconds + 1) % 60
                if self.seconds == 0: 
                    self.minutes = (self.minutes + 1) % 60
                    if self.minutes == 0:
                        self.hours = (self.hours + 1) % 100
            
            # Display the correct string output
            self.stopwatch = self.time_to_string()
            self.stopwatch_label.config(text = self.stopwatch)
            self.after(1, self.tick)