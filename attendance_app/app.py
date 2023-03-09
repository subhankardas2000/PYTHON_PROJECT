import tkinter as tk
from datetime import datetime

attendance_list = []

def submit_attendance():
    name = name_entry.get()
    # Add name and time to attendance list
    now = datetime.now()
    time_string = now.strftime("%m/%d/%Y %H:%M:%S")
    attendance_list.append((name, time_string))
    # Display confirmation message with name and time
    confirmation_label.config(text="Attendance submitted for "+name+" at "+time_string, fg="green")

def show_attendance():
    # Create a new window to display attendance details
    attendance_window = tk.Toplevel(root)
    attendance_window.title("Attendance Details")
    attendance_window.geometry("400x400")
    attendance_window.configure(bg="#f2f2f2")

    # Create a label to display attendance details
    attendance_label = tk.Label(attendance_window, text="Attendance Details", fg="#333333", font=("Arial", 12))
    attendance_label.pack(pady=10)

    # Create a text box to display attendance list
    attendance_text = tk.Text(attendance_window, bg="#f2f2f2", fg="#333333", font=("Arial", 12))
    attendance_text.pack()

    # Add attendance list to text box
    for name, time in attendance_list:
        attendance_text.insert(tk.END, name+" - "+time+"\n")

root = tk.Tk()
root.title("Attendance App")
root.geometry("400x400")

# Add label to show the current date and time
date_label = tk.Label(root, text=datetime.now().strftime("%m/%d/%Y %H:%M:%S"), font=("Arial", 12))
date_label.pack(pady=10)

# Add timer to update the date and time label every second
def update_clock():
    date_label.config(text=datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
    root.after(1000, update_clock)

update_clock()

label1 = tk.Label(root, text="Enter your name:", fg="#333333", font=("Arial", 12))
label1.pack(pady=10)

name_entry = tk.Entry(root, bg="#f2f2f2", fg="#333333", font=("Arial", 12))
name_entry.pack()

submit_button = tk.Button(root, text="Submit", bg="green", fg="#f2f2f2", font=("Arial", 12), command=submit_attendance)
submit_button.pack(pady=10)

confirmation_label = tk.Label(root, text="", fg="#333333", font=("Arial", 12))
confirmation_label.pack()

show_button = tk.Button(root, text="Show Attendance", bg="#333333", fg="#f2f2f2", font=("Arial", 12), command=show_attendance)
show_button.pack(pady=10)

root.mainloop()


#By subhankar das
