import tkinter 
from tkinter import messagebox

from sheety import Sheety

BACKGROUNG = "lightblue"
TEXT_BG = "#333A73"
TEXT_COLOR = "#387ADF"

TEXT_FONT = "Courier"

sheety = Sheety()

def register_button_click():
    email_list = sheety.get_sheet_data()
    email = email_input.get()
    if '@gmail.com' in email and " " not in email:
        if email not in email_list:
            sheety.post_sheet_data(email)
            messagebox.showinfo(title="popup", message=f"✅ Email {email} registered successfully.")
        else:
            messagebox.showinfo(title="popup", message=f"⚠️  Email {email} already registered.")
    else:
        messagebox.showinfo(title="error", message="❌ Please enter valid email.")


def delete_button_click():
    email_list = sheety.get_sheet_data()
    email = email_input.get()
    if '@gmail.com' in email and " " not in email:
        if email not in email_list:
            messagebox.showinfo(title="pop", message=f"⚠️  Email {email} is not registered.")
        else:
            email_index = email_list.index(email) + 2
            sheety.delete_sheet_data(email_index)
            messagebox.showinfo(title="pop", message=f"✅ Email {email} is successfully deleted.")
    else:
        messagebox.showinfo(title="error", message="❌ Please enter valid email.")


window = tkinter.Tk()
window.title("GUI")
window.minsize(height=200, width=200)
window.config(bg=BACKGROUNG, padx=30, pady=30)

heading = tkinter.Label(text="Weather App 🌤️", font=(TEXT_FONT, 40, "normal"), fg=TEXT_COLOR, bg=BACKGROUNG)
heading.grid(column=0, row=0, columnspan=3)
heading.config(padx=10, pady=40)

input_label = tkinter.Label(text="Email:",font=(TEXT_FONT, 18, "normal"), fg="black", bg=BACKGROUNG)
input_label.grid(column=0, row=1)

email_input = tkinter.Entry(width=35, bg="lightgray", fg="black")
email_input.grid(column=1, row=1, columnspan=3)
email_input.focus()

space = tkinter.Label(text="", bg=BACKGROUNG)
space.grid(row=2, column=0, columnspan=3)
space.config(padx=10, pady=10)

email_button = tkinter.Button(text="Register ✅", width=10, background=BACKGROUNG, font=(TEXT_FONT, 16, "bold"), fg=TEXT_COLOR, bg=BACKGROUNG, command=register_button_click)
email_button.grid(column=1, row=3)
email_button.config(padx=10)

delete_email_button = tkinter.Button(text="Delete ❌", width=10, background=BACKGROUNG, font=(TEXT_FONT, 16, "bold"), fg=TEXT_COLOR, bg=BACKGROUNG, command=delete_button_click)
delete_email_button.grid(column=2, row=3)
delete_email_button.config(padx=10)

window.mainloop()
