import tkinter as tk

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
        This creates an instance of the main application.

        Args:
            root: An instance of Tk will be placed here.  
                  This will place MainApp in a root window.
        """

        tk.Frame.__init__(self, root)
        self.root = root

root = tk.Tk()
MainApp(root).pack(side = "top", fill = "both", expand = True)
root.mainloop()