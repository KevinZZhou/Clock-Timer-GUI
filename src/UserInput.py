import tkinter as tk

class UserInput(tk.Frame):

    def __init__(self, root, message, minimum, maximum): 
        """
        This function creates an instance of UserInput.

        Args:
            root: This will place UserInput in a particular frame.
            message (str): This is the message that will be displayed next to 
                           to the user entry box.
            minimum (int): This is the lower bound on the integer value of 
                           the user input.
            maximum (int): This is the upper bound on the integer value of 
                           the user input.
        """

        # Initialize object
        tk.Frame.__init__(self, root)
        self.root = root
        self.message = message
        self.minimum = minimum
        self.maximum = maximum

        # Create the entry box, its label, and the Submit button in a frame
        self.input_frame = tk.Frame(self.root)
        self.input_label = tk.Label(self.input_frame, 
                text = self.message, font = ("verdana", 12))
        self.input = tk.StringVar()
        self.input_entry = tk.Entry(self.input_frame, 
                textvariable = self.input, font = ("verdana", 12))

        # Place widgets into frame
        self.input_label.pack(side = "left")
        self.input_entry.pack(side = "left")
        self.input_frame.pack()
    
    def get_value(self):
        """
        This function returns an integer value based on the user's input.

        Returns:
            int: Returns the value of the input field.  If it is not an 
                 integer or if the value is out of bounds, returns 0.
        """

        # Get the integer value of the input field
        # If something goes wrong, return 0
        try:
            input_int = int(self.input_entry.get())
            if input_int < self.minimum or input_int > self.maximum:
                input_int = 0
            return input_int
        except:
            return 0