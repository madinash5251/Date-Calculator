# Import necessary modules and functions
from datetime import datetime  # Importing datetime module to handle date and time
import tkinter as tk  # Importing Tkinter for GUI
from tkcalendar import Calendar  # Importing Calendar widget from tkcalendar module
from app.db import store_data_to_db  # Importing store_data_to_db function from app/db module


# Function to calculate date difference between two dates
def calculate_date_difference(date1_str, date2_str, result_label):
    try:
        # Convert date strings to datetime objects
        date1 = datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.strptime(date2_str, "%Y-%m-%d")

        # Calculate absolute difference in days between the dates
        date_diff = abs((date2 - date1).days)

        # Update the result label with the calculated date difference
        result_label.config(text=f"Date difference: {date_diff} days")
    except Exception:
        # Handle exceptions for invalid date format
        result_label.config(text="Invalid date format")


# Function to store data to a text file
def store_data_to_file(data):
    with open("dates.txt", "a") as file:
        file.write(data)


# Function to calculate date difference and store dates
def calculate_and_store_dates(date_picker1, date_picker2, result_label):
    # Get selected dates from the date pickers
    date1_str = date_picker1.get_date()
    date2_str = date_picker2.get_date()

    # Calculate date difference and update the result label
    calculate_date_difference(date1_str, date2_str, result_label)

    # Format data for storage in a text file
    data = f"Date 1: {date1_str}\nDate 2: {date2_str}\nDate Difference: {result_label.cget('text')}\n\n"

    # Store data to a text file
    store_data_to_file(data)


# Function to display date differences in the window
def display_differences(window):
    # Create two date picker calendars
    date_picker1 = Calendar(window, date_pattern="yyyy-mm-dd", selectmode="day")
    date_picker2 = Calendar(window, date_pattern="yyyy-mm-dd", selectmode="day")

    # Configure select background color for date pickers
    date_picker1.configure(selectbackground="hot pink")
    date_picker2.configure(selectbackground="hot pink")

    # Pack date pickers into the window
    date_picker1.pack()
    date_picker2.pack()

    # Create label to display the result
    result_label = tk.Label(window, text="")
    result_label.pack()

    # Create Calculate and Store Button
    calculate_button = tk.Button(window, text="Calculate and Store",
                                 command=lambda: calculate_and_store_dates(date_picker1, date_picker2, result_label))
    calculate_button.pack()
