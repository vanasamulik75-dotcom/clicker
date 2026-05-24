from customtkinter import *

window = CTk()
window.title("Clicker")
window.geometry("400x300")

count = 0

label = CTkLabel(window, text="clicks: 0", font=("Arial", 28))
label.pack(pady=10)


def click():
    global count
    count += 1
    label.configure(text=f"clicks: {count}",)

btn = CTkButton(window, text="click", command=click)
btn.pack(pady=10)


def click2():
    global count
    count -= 1
    label.configure(text=f"clicks: {-count}",)


btn = CTkButton(window, text="click2", command=click)
btn.pack(pady=10)



window.mainloop()