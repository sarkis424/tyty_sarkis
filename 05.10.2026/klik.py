import tkinter as tk

clicks = 0
def count_click():
    global clicks
    clicks += 0.5
    label_count.config(text=f"Число кликов: {clicks}")

def reset_click():
    global clicks
    clicks = 0
    label_count.config(text=f"Число кликов: {clicks}")


window = tk.Tk()
window.title("Счётчик кликов")
window.geometry("300x250")

label_count = tk.Label(window, text="Число кликов: 0", font=("Arial", 16))
label_count.pack(pady=20)

button_click = tk.Button(window, text="Клик!", font=("Arial", 12), command=count_click)
button_click.pack(pady=10)

button_reset = tk.Button(window, text="Сброс", font=("Arial", 12), command=reset_click)
button_reset.pack(pady=10)

window.mainloop()