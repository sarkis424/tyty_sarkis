import tkinter as tk

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "x":
            result = num1 * num2
        elif operation == "÷":
            if num2 == 0:
                label_result.config(text="Ошибка: деление на 0!")
                return
            result = num1 / num2
            
        label_result.config(text=f"Результат: {result}")
        
    except ValueError:
        label_result.config(text="Ошибка: введи числа!")

def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    label_result.config(text="Результат: ")

window = tk.Tk()
window.title("Калькулятор")
window.geometry("300x280")

entry1 = tk.Entry(window, font=("Arial", 12), justify="center")
entry1.pack(pady=5)

entry2 = tk.Entry(window, font=("Arial", 12), justify="center")
entry2.pack(pady=5)

frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=10)

btn_plus = tk.Button(frame_buttons, text="+", font=("Arial", 12), width=3, command=lambda: calculate("+"))
btn_plus.pack(side="left", padx=2)

btn_minus = tk.Button(frame_buttons, text="-", font=("Arial", 12), width=3, command=lambda: calculate("-"))
btn_minus.pack(side="left", padx=2)

btn_mult = tk.Button(frame_buttons, text="x", font=("Arial", 12), width=3, command=lambda: calculate("x"))
btn_mult.pack(side="left", padx=2)

btn_div = tk.Button(frame_buttons, text="÷", font=("Arial", 12), width=3, command=lambda: calculate("÷"))
btn_div.pack(side="left", padx=2)

# Кнопка очистить и Наклейка с результатом
btn_clear = tk.Button(window, text="Очистить", font=("Arial", 10), command=clear_fields)
btn_clear.pack(pady=5)

label_result = tk.Label(window, text="Результат: ", font=("Arial", 14, "bold"))
label_result.pack(pady=10)

window.mainloop()
