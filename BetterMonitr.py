from tkinter import *
import os
import time

root = Tk()
root.title("inverseCPU")
root.geometry("300x150")
canvas = Canvas(root, bg="white", height=300, width=300)

def do_nothing():
    for _ in range(10000000):
        pass

def measure_cpu_usage(do_nothing):
    start_time = os.times()
    do_nothing()
    end_time = os.times()
    cpu_time_used = end_time.user-start_time.user+end_time.system-start_time.system
    real_time_elapsed = end_time.elapsed - start_time.elapsed
    cpu_usage_percent = (cpu_time_used / real_time_elapsed) * 100
    return cpu_usage_percent

def cpu_load():
	cpu_usage = measure_cpu_usage(do_nothing)
	return cpu_usage

def drawLine():
    global linestartx, linestarty, time, lineendx, previous_linestarty, line
    linestartx += 10
    lineendx += 10
    current_linestarty = cpu_load() * 2  # Calculate current linestarty
    
    if linestartx > 300:  # If the line reaches the right end of the canvas
        # Delete the previous line
        canvas.delete("all")
        # Reset linestartx and lineendx to start a new line
        linestartx = 0
        lineendx = 10

    # Create a new line and store its ID
    line = canvas.create_line(linestartx, previous_linestarty, lineendx, current_linestarty, fill="black")
    previous_linestarty = current_linestarty  # Update previous_linestarty
    linedrawrepeat = root.after(time, drawLine)

time = 1000
linestartx = 0
previous_linestarty = cpu_load() * 2  # Initialize previous_linestarty
lineendx = 10
line = None  # Store the ID of the current line
drawLine()
canvas.pack()
root.mainloop()
