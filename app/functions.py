from datetime import datetime
import tkinter as tk
from tkcalendar import Calendar
from app.db import store_data_to_db

def calculate_date_difference(date1_str, date2_str, result_label):
    try:
        date1 = datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.strptime(date2_str, "%Y-%m-%d")
        date_diff = abs((date2 - date1).days)
        result_label.config(text=f"Date difference: {date_diff} days")
    except Exception:
        result_label.config(text="Invalid date format")

def store_data_to_file(data):
    with open("dates.txt", "a") as file:
        file.write(data)

def calculate_and_store_dates(date_picker1, date_picker2, result_label):
    date1_str = date_picker1.get_date()
    date2_str = date_picker2.get_date()
    calculate_date_difference(date1_str, date2_str, result_label)
    data = f"Date 1: {date1_str}\nDate 2: {date2_str}\nDate Difference: {result_label.cget('text')}\n\n"
    store_data_to_file(data)

def display_differences(window):
    date_picker1 = Calendar(window, date_pattern="yyyy-mm-dd", selectmode="day")
    date_picker2 = Calendar(window, date_pattern="yyyy-mm-dd", selectmode="day")

    date_picker1.configure(selectbackground="hot pink")
    date_picker2.configure(selectbackground="hot pink")

    date_picker1.pack()
    date_picker2.pack()

    # Create label to display the result
    result_label = tk.Label(window, text="")
    result_label.pack()

    # Calculate and Store Button
    calculate_button = tk.Button(window, text="Calculate and Store", command=lambda: calculate_and_store_dates(date_picker1, date_picker2, result_label))
    calculate_button.pack()
