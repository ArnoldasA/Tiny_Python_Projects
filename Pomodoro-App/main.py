from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 8
MY_TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    REPS = 8
    window.after_cancel(MY_TIMER)
    canvas.itemconfig(timer_count_down, text="00:00")
    timer_text.config(text="Timer")
    marks = ""
    work_sesh = math.floor(REPS / 2)
    for _ in range(work_sesh):  # Finish code from here
        marks += "✔"
    tick_text.config(text=marks)



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS # Controls when we switch between breaks and working
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    marks = ""
    work_sesh = math.floor(REPS / 2)
    for _ in range(work_sesh):  # Finish code from here
        marks += "✔"
    tick_text.config(text=marks)

    if REPS % 2 == 0 and REPS != 0:
        timer_text.config(text="Work",fg=GREEN)
        count_down(4)
        REPS -= 1
    elif REPS == 1:
        timer_text.config(text="Long Break",fg=YELLOW)
        timer_text.place(x=35,y=-50)
        marks += "Finished!"
        tick_text.config(text=marks)
        count_down(6)
        REPS -= 1
    elif REPS != 1 and REPS >0:
        timer_text.config(text="Break",fg=YELLOW)
        count_down(2)
        REPS -= 1
    print(REPS)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global REPS
    global MY_TIMER
    count_min = math.floor(count / 60)  # getting the minutes
    count_sec = count % 60  # getting the seconds
    if count_sec < 10:  # we can use dynamic typing to change the seconds to a str then revert it back to an int
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_count_down, text=f"{count_min}:{count_sec}")  # we can change our canvas variable with
    # this function
    if count > 0:
        MY_TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=RED)

# Pomodoro Images and Counter
timer_text = Label(window, text="Timer", font=("Arial", 20), bg=RED, fg="green")
timer_text.place(x=68, y=-50)
canvas = Canvas(width=200, height=224, bg=RED, highlightthickness=0)  # Highlight thickness removes borders
tomato_image = PhotoImage(file="tomato.png")  # Retrieve the tomato image
canvas.create_image(100, 112, image=tomato_image)  # Create the image on the canvas
timer_count_down = canvas.create_text(100, 130, text="00:00", fill="white", font=("Arial", 35, "bold"))
canvas.pack()

# Pomodoro Buttons and  Text
start_bt = Button(window, text="Start", font=("Arial", 8), bg="white", bd=0, command=start_timer)
start_bt.place(x=-15, y=200)
tick_text = Label(window, font=(4), bg=RED, fg="green")
tick_text.place(x=60, y=240)
reset_bt = Button(window, text="Reset", font=("Arial", 8), bg="white", bd=0, command=reset_timer)
reset_bt.place(x=180, y=200)

window.mainloop()
