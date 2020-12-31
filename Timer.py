import tkinter as tk
from playsound import playsound

from UserInput import UserInput
from TimeButtons import TimeButtons

class Timer(tk.Frame):
    """
    This class is the timer that will appear in MainApp.
    It will allow the user to input the number of hours, minutes, and seconds 
    that the timer will count down from when the Start button is pressed.

    Args:
        tk.Frame: Parent class
    """

    def __init__(self, root):
        """
        This function creates an instance of Timer.

        Args:
            root: An instance of Tk will be placed here.  
                  This will place Timer in a root window.
        """

        # Initialize object
        tk.Frame.__init__(self, root)
        self.root = root
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.timer = self.time_to_string()
        self.active = False
        self.file_path = ""

        # Create timer label
        self.timer_label = tk.Label(self.root, text = self.timer, 
                font = ("verdana", 32, "bold"), background = "white", 
                foreground = "black", borderwidth = 1, relief = "solid")
        
        # Create user input boxes for self.hours, self.minutes, self.seconds
        self.input_frame = tk.Frame(self.root)
        self.hours_input = UserInput(self.input_frame, 
                "How many hours?", 0, 99)
        self.minutes_input = UserInput(self.input_frame, 
                "How many minutes?", 0, 59)
        self.seconds_input = UserInput(self.input_frame, 
                "How many seconds?", 0, 59)
        
        # Create submit button and time buttons
        self.submit_frame = tk.Frame(self.root)
        self.submit_button = tk.Button(self.submit_frame, text = "Submit", 
                font = ("verdana", 12), command = self.submit)
        self.time_buttons = TimeButtons(self.root, 
                self.start, self.stop, self.reset)

        # Place widgets into frame
        self.timer_label.pack(expand = True, fill ="both")
        self.hours_input.pack()
        self.minutes_input.pack()
        self.seconds_input.pack()
        self.input_frame.pack(side = "left")
        self.submit_button.pack(fill = "both")
        self.submit_frame.pack(fill = "both", pady = 20)
        self.time_buttons.pack(side = "bottom")

    def submit(self):
        """
        This function updates the displayed output of the timer.
        """
        self.hours = self.hours_input.get_value()
        self.minutes = self.minutes_input.get_value()
        self.seconds = self.seconds_input.get_value()
        self.timer = self.time_to_string()
        self.timer_label.config(text = self.timer)

    def time_to_string(self):
        """
        This function takes the integer values of the timer and converts 
        them into a single string that looks like a timer's output.

        Returns:
            str: A string displaying the current timer output
        """

        # Convert self.hours, self.minutes, and self.seconds into strings
        hours_string = "{:02d}".format(self.hours)
        minutes_string = "{:02d}".format(self.minutes)
        seconds_string = "{:02d}".format(self.seconds)

        # Return a string combining the three values
        time_string = (hours_string + ":" + minutes_string + ":" + 
                seconds_string)
        return time_string
    
    def start(self):
        """
        This function starts the timer.
        """
        if self.timer != "00:00:00":
            self.active = True
            self.after(1000, self.tick)

    def stop(self):
        """
        This function stops the timer.
        """
        self.active = False

    def reset(self):
        """
        This function resets the timer.
        """

        # Set values to 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        # Display the correct string output and stop the timer
        self.timer = self.time_to_string()
        self.timer_label.config(text = self.timer)
        self.stop()

    def tick(self):
        """
        This function decrements the number of seconds by 1 when the timer is 
        active.  It then adjusts the number of minutes and hours if necessary 
        and sets the new stopwatch output.
        """

        # Adjusts the timer values if it is active
        if self.active == True:
            # Stops the timer if necessary and plays a short audio clip
            if self.timer == "00:00:00":
                playsound("files/sounds/beep.mp3")
                self.stop()
            else:
                # Adjusts the timer values if it is active
                total_seconds = (self.seconds + 
                        (self.minutes * 60) + (self.hours * 24 * 60))
                total_seconds -= 1
                self.hours = total_seconds // (24 * 60)
                remaining_time = total_seconds % (24 * 60)
                self.minutes = remaining_time // 60
                self.seconds = remaining_time % 60

                # Display the correct string output                
                self.timer = self.time_to_string()
                self.timer_label.config(text = self.timer)
                self.after(1000, self.tick)