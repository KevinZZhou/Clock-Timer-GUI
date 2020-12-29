import tkinter as tk
from tkinter import ttk

from DigitalClock import DigitalClock

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
        tabs = ttk.Notebook(root)

        # Digital clock
        tab_digital_clock = ttk.Frame(tabs)
        tabs.add(tab_digital_clock, text ='Digital Clock')
        digital_clock = DigitalClock(tab_digital_clock)
        digital_clock.pack()

        # Analog clock?
        tab_analog_clock = ttk.Frame(tabs)
        tabs.add(tab_analog_clock, text ='Analog Clock')
        # TODO: Create an instance of AnalogClock, position it

        # Stopwatch
        tab_stopwatch = ttk.Frame(tabs)
        tabs.add(tab_stopwatch, text = 'Stopwatch')
        # TODO: Create an instance of Stopwatch, position it

        # Timer
        tab_timer = ttk.Frame(tabs)
        tabs.add(tab_timer, text = "Timer")
        # TODO: Create an instance of Timer, position it

        # Pomodoro timer?
        tab_pomodoro_timer = ttk.Frame(tabs)
        tabs.add(tab_pomodoro_timer, text = "Pomodoro Timer")
        # TODO: Create an instance of PomodoroTimer, position it
        
        tabs.pack(expand = 1, fill ="both")


root = tk.Tk()
MainApp(root).pack(side = "top", fill = "both", expand = True)
root.resizable(width = False, height = False)
root.mainloop()