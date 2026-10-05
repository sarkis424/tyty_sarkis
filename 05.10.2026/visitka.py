import tkinter as tk


window = tk.Tk()
window.title("Моя визитка")
window.geometry("350x250")

label_name = tk.Label(window, text="Сафонов", font=("Arial", 20))
label_name.pack(pady=15)

label_status = tk.Label(window, text="Охранник Пятерочки", font=("Arial", 14))
label_status.pack(pady=10)

label_city = tk.Label(window, text="Пушкино, дом Калатушкино", font=("Arial", 14))
label_city.pack(pady=10)

window.mainloop()