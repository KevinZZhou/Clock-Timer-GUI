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
        15 minute long break after every 5th study period

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

        # Create timer, status, and pomodoro labels and time buttons
        self.timer_label = tk.Label(self.root, text = self.timer, 
                font = ("verdana", 32, "bold"), background = "white", 
                foreground = "black", borderwidth = 1, relief = "solid")
        self.status_label = tk.Label(self.root, text = self.status, 
                font = ("verdana", 16), background = "white", 
                foreground = "black", borderwidth = 1, relief = "solid")
        self.pomodoro_label = tk.Label(self.root, text = "Number of " + 
                "pomodoros: " + str(self.pomodoro_number) + "/4", font = 
                ("verdana", 16), background = "white", foreground = "black", 
                borderwidth = 1, relief = "solid")
        self.time_buttons = TimeButtons(self.root, 
                self.start, self.stop, self.reset)
        
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

    def set_timer(self, minutes, seconds):
        """
        This function sets the pomodoro timer for its various modes.

        Args:
            minutes (int): Sets the number of minutes
            seconds (int): Sets the number of seconds
        """
        self.minutes = minutes
        self.seconds = seconds
        self.timer = self.time_to_string()
        self.timer_label.config(text = self.timer)
    
    def start(self):
        """
        This function starts the pomodoro timer.
        """
        self.active = True
        self.after(1000, self.tick)

    def stop(self):
        """
        This function stops the pomodoro timer.
        """
        self.active = False

    def reset(self):
        """
        This function resets the timer.
        """
        self.set_timer(25, 0)
        self.stop()
    
    def tick(self):
        """
        This function decrements the number of seconds by 1 when the timer is 
        active, adjusting the number of minutes if needed.  It uses 
        self.pomodoro_number to determine the length of the next timer.
        """

        # Adjusts the timer values if it is active
        if self.active == True:
            # Switches the pomodoro timer mode if necessary
            if self.timer == "00:00":
                playsound("files/sounds/beep.mp3")
                if self.status == "Studying!":
                    self.pomodoro_number += 1
                    if self.pomodoro_number == 5:
                        self.pomodoro_number = 0
                        self.status = "Taking a longer break!"
                        self.set_timer(15, 0)
                    elif self.pomodoro_number < 5:
                        self.status = "Taking a short break!"
                        self.set_timer(5, 0)
                    self.pomodoro_label.config(text = "Number of " + 
                            "pomodoros: " + str(self.pomodoro_number) + "/4")
                else:
                    self.status = "Studying!"
                    self.set_timer(25, 0)
                self.status_label.config(text = self.status)
                        
            # Otherwise, adjusts the values of the active timer
            else:
                # Adjusts the timer values
                total_seconds = (self.seconds + (self.minutes * 60))
                total_seconds -= 1
                self.set_timer(total_seconds // 60, total_seconds % 60)
            self.after(1000, self.tick)