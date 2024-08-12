from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .1
SHORT_BREAK_MIN = .1
LONG_BREAK_MIN = .1
reps = 0
amt_of_checks = ''
timer2 = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global amt_of_checks
    global timer2
    global reps
    reps = 0
    window.after_cancel(timer2)
    amt_of_checks = ''
    check.config(text=amt_of_checks)
    canvas.itemconfig(timer, text='00:00')
    timer_label.config(text='Timer', fg=GREEN, background=YELLOW, highlightthickness=0, font=(FONT_NAME, 40, 'bold'))


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break)
        timer_label.config(text='Break', fg=RED)
    elif reps % 2 == 1:
        timer_label.config(text='Work', fg=GREEN)
        countdown(work)
    else:
        timer_label.config(text='Break', fg=PINK)
        countdown(short_break)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps
    global amt_of_checks
    count_min = math.floor(count / 60)
    count_sec = int(count % 60)
    if count_sec == 0 or count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer2
        timer2 = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            amt_of_checks += '✓'
            check.config(text=amt_of_checks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, background=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer_label = Label(text='Timer', fg=GREEN, background=YELLOW, highlightthickness=0, font=(FONT_NAME, 40, 'bold'))
timer_label.grid(column=1, row=0)

start_button = Button(text='Start', font=(FONT_NAME, 10, 'bold'), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', font=(FONT_NAME, 10, 'bold'), command=reset)
reset_button.grid(column=2, row=2)

check = Label(fg=GREEN, bg=YELLOW, font=(False, 30, 'normal'))
check.grid(column=1, row=3)

window.mainloop()
