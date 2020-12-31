import tkinter as tk

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
        

        Args:
            root ([type]): [description]
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
        self.stopwatch_label = tk.Label(root, text = self.stopwatch, 
                font = ("verdana", 32, "bold"), background = "white", 
                foreground = "black", borderwidth = 1, relief = "solid")
        self.start_button = tk.Button(root, text = "Start", 
                font = ("verdana", 14), command = self.start)
        self.stop_button = tk.Button(root, text = "Stop", 
                font = ("verdana", 14), command = self.stop)
        self.reset_button = tk.Button(root, text = "Reset", 
                font = ("verdana", 14), command = self.reset)
        
        # Place widgets into frame
        self.stopwatch_label.pack(expand = True, fill ="both")
        self.start_button.pack()
        self.stop_button.pack()
        self.reset_button.pack()

    def time_to_string(self):
        hours_string = "{:02d}".format(self.hours)
        minutes_string = "{:02d}".format(self.minutes)
        seconds_string = "{:02d}".format(self.seconds)
        milliseconds_string = "{:03d}".format(self.milliseconds)

        time_string = (hours_string + ":" + minutes_string + ":" + 
                seconds_string + ":" + milliseconds_string)
        return time_string

    def start(self):
        self.active = True
        self.tick()

    def stop(self):
        self.active = False

    def reset(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        self.stopwatch = self.time_to_string()
        self.stop()
    
    def tick(self):
        print("tick")