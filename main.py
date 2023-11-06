from tkinter import Tk
from app.functions import display_differences

def main():
    window = Tk()
    window.title("Date Difference Calculator")
    window.geometry("400x400")

    # Call the display_differences function
    display_differences(window)

    # Create a text file to store the date differences
    file = open("dates.txt", "w")
    file.close()

    window.mainloop()

if __name__ == "__main__":
    main()
