# Import necessary modules and functions
from tkinter import Tk  # Importing Tkinter for GUI
from app.functions import display_differences  # Importing the display_differences function from app/functions module

# Define the main function
def main():
    window = Tk()  # Create the main window
    window.title("Date Difference Calculator")  # Set the window title
    window.geometry("400x400")  # Set the window size

    # Call the display_differences function to calculate and display date differences in the window
    display_differences(window)

    # Create a text file named "dates.txt" to store the date differences (if it doesn't exist and overwrites if exists)
    file = open("dates.txt", "w")
    file.close()  # Close the file

    window.mainloop()  # Run the main GUI event loop

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
