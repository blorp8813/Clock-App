import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

window = tk.Tk()

window.title("Clock App")

tab_control = ttk.Notebook(window)

clock_tab = ttk.Frame(tab_control)

alarm_tab = ttk.Frame(tab_control)

timer_tab = ttk.Frame(tab_control)

stopwatch_tab = ttk.Frame(tab_control)

tab_control.add(clock_tab, text= "Clock")

tab_control.add(alarm_tab, text= "Alarm")

tab_control.add(timer_tab, text= "Timer")

tab_control.add(stopwatch_tab, text= "Stopwatch")

tab_control.pack(expand=1, fill="both")

tk.Label(alarm_tab, text="Set the alarm time in the format HH:MM").grid()

tk.Label(timer_tab, text="Set the timer time in the format MM:SS").grid()

tk.Label(stopwatch_tab, text="00:00:00").grid()

alarm_time = tk.Entry(alarm_tab).grid()

timer_time = tk.Entry(timer_tab).grid()

alarm_start = tk.Button(alarm_tab, text="Start").grid()

timer_start = tk.Button(timer_tab, text="Start").grid()

stopwatch_start = tk.Button(stopwatch_tab, text="Start").grid()

stopwatch_stop = tk.Button(stopwatch_tab, text="Stop").grid()

stopwatch_rest = tk.Button(stopwatch_tab, text="Reset").grid()

window.mainloop()