# Import the tkinkter module shortened to tk for easier use
import tkinter as tk

# Import the messagebox module from tkinter to be used for when alarm or timer ends
from tkinter import messagebox

# Import the ttk module from tkinter to be used for the tabs
from tkinter import ttk

# Imports the time module
import time

# Creates the window
window = tk.Tk()

# Sets the windows name to Clock App
window.title("Clock App")

# Global veriables for stopwatch
stopwatch_running = False
stopwatch_seconds = 0

# Input validation for setting alarm and timer. Tries to format the input as hours and minutes, if there is a value error return False, if not return True.
def input_check(input):
    try:
        time.strptime(input, "%H:%M")
    except ValueError:
        return False
    return True

# Function to update the main clock
def update_time():

    # Sets the variable current_time to the systems clock using non-military format
    current_time = time.strftime("%I:%M:%S")
    
    # Changes the text on the clock label to the current time
    clock_label.config(text=current_time)
    
    # Runs the function again after 1000 milliseconds, which is 1 second
    clock_label.after(1000, update_time)

# Function to start the alarm
def start_alarm():
    
    # Sets the variable to the users input
    set_alarm = alarm_time.get()
    
    # Runs the input validation, and if True is returned then runs the next function
    if input_check(set_alarm):
        alarm_run(set_alarm)

# Function to actually run the alarm   
def alarm_run(set_alarm):
    
    # Sets the variable to the current time in military format
    current_time = time.strftime("%H:%M")
    
    # If the users input is not the same as the current time
    if set_alarm != current_time:
        
        # Runs the function again after 1 second
        window.after(1000, alarm_run, set_alarm)
    
    # Once the users input is the same as the current time, show a messagebox called Alarm that says the alarm is done
    elif set_alarm == current_time:
        messagebox.showinfo("Alarm", "Alarm is done")

# Function to start the timer
def start_timer():
    
    # Sets the variable to the user input
    set_timer = timer_time.get()
    
    # Runs the input validation on the user input
    if input_check(set_timer):
        
        # Sets the minutes and seconds variable to what the user inputted by splitting the input into a list and getting the two integers
        minutes, seconds = map(int, set_timer.split(":"))
        
        # Sets the total_seconds variable to the total seconds on the timer
        total_seconds = minutes * 60 + seconds
        
        # Runs the countdown function with the parameter of the total_seconds
        countdown(total_seconds)

# Function to countdown the timer with the parameter of seconds remaining
def countdown(seconds):
    
    # If seconds is greater than 0
    if seconds > 0:
        
        # Change the text on the timer remaining label to the current seconds remaining
        timer_remaining.config(text=str(seconds) + " seconds remaining")
        
        # Run the function again with the seconds parameter subtracted by 1 after 1 second
        timer_remaining.after(1000, countdown, seconds - 1)
    
    # Once seconds is no longer 0 display a messagebox called Timer saying that the timer is done
    else:
        messagebox.showinfo("Timer", "Timer is done")

# Function to update the stopwatch
def update_stopwatch_label():

    # Calls the global variables for stopwatch seconds and if its running
    global stopwatch_seconds
    global stopwatch_running

    # If the stopwatch_running variable is True
    if stopwatch_running:

        # Add one to the stopwatch seconds
        stopwatch_seconds += 1
    
    # Set hours to the stopwatch seconds divided by 3600 rounded down to the nearest integer
    hours = stopwatch_seconds // 3600
    
    # Divides stopwatch seconds by 60, rounds down to the nearest integer, and sets the remainder of that by 60 to minutes
    minutes = (stopwatch_seconds // 60) % 60
    
    # Set seconds the remainder of stopwatch seconds and 60
    seconds = stopwatch_seconds % 60
    
    # Sets the stopwatch time using formatting to have each number be two digits
    stopwatch_time = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    
    # Changes the text on the stopwatch label to show the formatted time
    stopwatch_label.config(text=stopwatch_time)

    # Runs the function again after 1 second
    stopwatch_label.after(1000, update_stopwatch_label)

# Function to start the stopwatch
def start_stopwatch():

    # Calls the global variable for if the stopwatch is running
    global stopwatch_running
    
    # Sets the variable to True
    stopwatch_running = True
    
    # Runs the function to update the stopwatch
    update_stopwatch_label()

# Function to stop the stopwatch
def stop_stopwatch():
    
    # Calls the global variable for if the stopwatch is running
    global stopwatch_running

    # Sets the variable to False
    stopwatch_running = False

# Function to reset the stopwatch
def reset_stopwatch():
    # Calls the global variables for stopwatch seconds and if its running
    global stopwatch_seconds
    global stopwatch_running
    
    # Sets the stopwatch seconds to 0 and if its running to False
    stopwatch_seconds = 0
    stopwatch_running = False
    
    # Reset the label back to original
    stopwatch_label.config(text="00:00:00")

# Creates the tab control for the window and all the tabs as a part of the tab control
tab_control = ttk.Notebook(window)
clock_tab = ttk.Frame(tab_control)
alarm_tab = ttk.Frame(tab_control)
timer_tab = ttk.Frame(tab_control)
stopwatch_tab = ttk.Frame(tab_control)

# Adds each tab with their respective names
tab_control.add(clock_tab, text= "Clock")
tab_control.add(alarm_tab, text= "Alarm")
tab_control.add(timer_tab, text= "Timer")
tab_control.add(stopwatch_tab, text= "Stopwatch")

# Packs the tab control to make them visible in the window
tab_control.pack(expand=1, fill="both")

# Creates labels for the alarm and timer in their respective tabs and adds them to the grid
tk.Label(alarm_tab, text="Set the alarm time in the format HH:MM in military format").grid()
tk.Label(timer_tab, text="Set the timer time in the format MM:SS").grid()

# Creates the blank label for the time remaining on a timer in the timer tab and adds it to the grid
timer_remaining = tk.Label(timer_tab, text="")
timer_remaining.grid()

# Creates the base label for the stopwatch time in the stopwatch tab and adds it to the grid
stopwatch_label = tk.Label(stopwatch_tab, text="00:00:00")
stopwatch_label.grid()

# Creates the label for the clock in the clock tab with a font size of 25 to make it bigger
clock_label = tk.Label(clock_tab, text="", font=25)

# Adds the label to the grid seperately since it will be modified
clock_label.grid()
# Runs the update_time function to keep the clock updated
update_time()

# Creates the entry field for the alarm time in the alarm tab and adds it to the grid
alarm_time = tk.Entry(alarm_tab)
alarm_time.grid()

# Creates the entry field for the timer time in the timer tab and adds it to the grid
timer_time = tk.Entry(timer_tab)
timer_time.grid()


# Creates the start alarm button in the alarm tab that runs the start_alarm function when pressed
alarm_start = tk.Button(alarm_tab, text="Start", command = start_alarm).grid()

# Creates the start timer button in the timer tab that runs the start_timer function when pressed
timer_start = tk.Button(timer_tab, text="Start", command = start_timer).grid()

# Creates the start stopwatch button in the stopwatch tab that runs the start_stopwatch function when pressed
stopwatch_start = tk.Button(stopwatch_tab, text="Start", command= start_stopwatch).grid()

# Creates the stop stopwatch button in the stopwatch tab that runs the stop_stopwatch function when pressed
stopwatch_stop = tk.Button(stopwatch_tab, text="Stop", command= stop_stopwatch).grid()

# Creates the reset stopwatch button in the stopwatch tab that runs the reset_stopwatch function when pressed
stopwatch_reset = tk.Button(stopwatch_tab, text="Reset", command= reset_stopwatch).grid()

# Calls the mainloop to actually create the window and run the code
window.mainloop()