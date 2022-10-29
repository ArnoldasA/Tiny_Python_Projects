from tkinter import *
from random import *
import pyperclip
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    #for char in password_list:
    #    password += char

    pass_info = password_input.get()
    if len(pass_info) == 0:
        password_input.insert(0,password)
    else:
        messagebox.showinfo(title="Field must be empty",message="Please remove previous password information.")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
# Save website, email and password parameters
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty!")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email} \nPassword:{password} \nIs it okay to save?")

        if is_okay:
            with open("Password_Information.txt","a") as data_file:
                data_file.write(f"\n{website}/{email}/{password}")
            website_input.delete(0,END)
            password_input.delete(0,END)





# ---------------------------- UI SETUP ------------------------

# setting up the Window,Canvas and Image
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

canvas = Canvas(width=200, height=200)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(column=1, columnspan=2, row=0)

# Text
website_text = Label(window, text="Website:", font=("Arial", 10))
website_text.grid(column=0, row=1)
email_text = Label(window, text="Email:", font=("Arial", 10))
email_text.grid(column=0, row=2)
password_text = Label(window, text="Password:", font=("Arial", 10))
password_text.grid(column=0, row=3)
# Input Fields
website_input = Entry(width=35)
website_input.focus()  # Puts our cursor into the field
website_input.grid(column=1, row=1, columnspan=2)
email_input = Entry(width=35)
email_input.insert(0, "arnoldasalencikas@gmail.com")  # Populate our password manager with our email each time
email_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=35)
password_input.grid(column=1, row=3, columnspan=2)
# Buttons
generate_password_btn = Button(text="Generate Password", width=14,command=password_generator)
generate_password_btn.grid(column=2, columnspan=2, row=3)
add_btn = Button(text="Add", width=29, command=save_password)
add_btn.grid(column=1, columnspan=2, row=4)
window.mainloop()
