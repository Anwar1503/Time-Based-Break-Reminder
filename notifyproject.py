import tkinter as tk

def greet():  
    global time_value
    global name_    
    name_=name.get()
    time_value = time.get()  
    if(name_):
        label1.config(text="Email set ", fg="green")
    else:
        label1.config(text="Email not set ", fg="red")
    if(time_value):
        label2.config(text="Time set ", fg="green")
    else:
        label2.config(text="Time not set ", fg="red")
    if(time_value and name_):
        title_bar.config(text="ready to go!!!", fg="Maroon")

def close_window():
    app.destroy()

# Create the main application window
app = tk.Tk()
app.title("Parental Control")
app.geometry('300x300')
app.config(bg="#FA8072")  # Setting background color
title_bar = tk.Label(app, text="Required(*)", font=('Times', 15, "bold italic"), bg='coral', fg='black')
title_bar.pack(side='top',padx=6, pady=6, fill='x')


# Create a label widget
label1 = tk.Label(app, text="*Enter Parent Email:", font=('Times', 15, "bold italic"), bg='#FFEFDB', fg='black')
label1.pack(side='top', padx=6, pady=6, fill='x')

# Create a text entry widget
name = tk.Entry(app, bg="#e0e0e0", fg="black", font=('Arial', 15))
name.pack(side='top', padx=6, pady=6, fill='x')
name.pack_configure(padx=10)

label2 = tk.Label(app, text="*Enter Time in Seconds:", font=('Times', 15, "bold italic"), bg='#FFEFDB', fg='black')
label2.pack(side='top', padx=6, pady=6, fill='x')

time = tk.Entry(app, bg="#e0e0e0", fg="black", font=('Arial', 15))
time.pack(side='top', padx=6, pady=6, fill='x')

# Create a close button
close_button = tk.Button(app, text="Close", command=close_window, font=('Times', 15, "bold italic"), bg='black', fg='white', relief="raised")
close_button.pack(side='bottom', padx=2, pady=2, fill='x')


# Create a button widget
button = tk.Button(app, text="Submit", command=greet, font=('Times', 15, "bold italic"), bg='black', fg='white', relief="raised")
button.pack(side='bottom', padx=2,pady=2, fill='x') 

# Run the application
app.mainloop()
