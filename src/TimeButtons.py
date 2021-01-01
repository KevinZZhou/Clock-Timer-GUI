import tkinter as tk

class TimeButtons(tk.Frame):
    """
    This class contains the Start, Stop, and Reset buttons that are used in 
    several modes, including Stopwatch, Timer, and PomodoroTimer.

    Args:
        tk.Frame: Parent class
    """

    def __init__(self, root, start_func, stop_func, reset_func):
        """
        This function creates an instance of TimeButtons.

        Args:
            root: This will place TimeButtons in a particular frame.
            start_func: This will become the command for the Start button.
            stop_func: This will become the command for the Stop button.
            reset_func: This will become the command for the Reset button.
        """

        # Initialize object
        tk.Frame.__init__(self, root)
        self.root = root

        # Create frames
        self.button_frame = tk.Frame(self.root)
        self.start_stop_frame = tk.Frame(self.button_frame)
        self.reset_frame = tk.Frame(self.button_frame)

        # Create the start, stop, and reset buttons
        self.start_button = tk.Button(self.start_stop_frame, text = "Start", 
                font = ("verdana", 14), command = start_func)
        self.stop_button = tk.Button(self.start_stop_frame, text = "Stop", 
                font = ("verdana", 14), command = stop_func)
        self.reset_button = tk.Button(self.reset_frame, text = "Reset", 
                font = ("verdana", 14), command = reset_func)
        
        # Place widgets into frame
        self.start_button.pack(side = "left")
        self.stop_button.pack(side = "left")
        self.reset_button.pack(side = "bottom")
        self.start_stop_frame.pack()
        self.reset_frame.pack()
        self.button_frame.pack(side = "bottom")