import tkinter as tk
from tkinter import ttk

from DigitalClock import DigitalClock
from AnalogClock import AnalogClock
from Stopwatch import Stopwatch
from Timer import Timer

class MainApp(tk.Frame): 
    """
    This class is the main clock and timer application that will be run.
    It will combine all of the different modes (clock, stopwatch, etc.) into 
    window.
    Each mode can be accessed by clicking its tab.

    tk.Frame: Parent class
    """

    def __init__(self, root): 
        """
        This function creates an instance of MainApp.

        Args:
            root: An instance of Tk will be placed here.  
                  This will place MainApp in a root window.
        """

        tk.Frame.__init__(self, root)
        self.root = root

        # Create the tabs that will hold each mode
        style = ttk.Style()
        style.configure('TNotebook.Tab', font = ("verdana", 11))
        self.tabs = ttk.Notebook(self.root)

        # Digital clock
        tab_digital_clock = ttk.Frame(self.tabs)
        self.tabs.add(tab_digital_clock, text ='Digital Clock')
        digital_clock = DigitalClock(tab_digital_clock)
        digital_clock.pack()

        # Analog clock
        tab_analog_clock = ttk.Frame(self.tabs)
        self.tabs.add(tab_analog_clock, text ='Analog Clock')
        analog_clock = AnalogClock(tab_analog_clock)
        analog_clock.pack()

        # Stopwatch
        tab_stopwatch = ttk.Frame(self.tabs)
        self.tabs.add(tab_stopwatch, text = 'Stopwatch')
        stopwatch = Stopwatch(tab_stopwatch)
        stopwatch.pack()

        # Timer
        tab_timer = ttk.Frame(self.tabs)
        self.tabs.add(tab_timer, text = "Timer")
        timer = Timer(tab_timer)
        timer.pack()

        # Pomodoro timer?
        tab_pomodoro_timer = ttk.Frame(self.tabs)
        self.tabs.add(tab_pomodoro_timer, text = "Pomodoro Timer")
        # TODO: Create an instance of PomodoroTimer
        
        self.tabs.pack(expand = True, fill = "both", side = "top")


root = tk.Tk()
root.title("Python Clock and Timer App")
root.resizable(width = False, height = False)
MainApp(root)
root.mainloop()