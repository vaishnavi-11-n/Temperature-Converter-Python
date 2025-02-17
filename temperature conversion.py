import tkinter as tk
from tkinter import ttk, messagebox

# Conversion functions
def convert_temperature():
    try:
        value = float(entry_temp.get())
        unit = unit_var.get()

        if unit == "Celsius":
            fahrenheit = (value * 9/5) + 32
            kelvin = value + 273.15
            result_text.set(f"{value}°C = {fahrenheit:.2f}°F\n{value}°C = {kelvin:.2f}K")

        elif unit == "Fahrenheit":
            celsius = (value - 32) * 5/9
            kelvin = (value - 32) * 5/9 + 273.15
            result_text.set(f"{value}°F = {celsius:.2f}°C\n{value}°F = {kelvin:.2f}K")

        elif unit == "Kelvin":
            celsius = value - 273.15
            fahrenheit = (value - 273.15) * 9/5 + 32
            result_text.set(f"{value}K = {celsius:.2f}°C\n{value}K = {fahrenheit:.2f}°F")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric temperature.")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")
root.resizable(False, False)

# UI Elements
tk.Label(root, text="Enter Temperature:", font=("Arial", 12)).pack(pady=5)
entry_temp = tk.Entry(root, font=("Arial", 12))
entry_temp.pack(pady=5)

tk.Label(root, text="Select Unit:", font=("Arial", 12)).pack(pady=5)
unit_var = tk.StringVar(value="Celsius")
unit_menu = ttk.Combobox(root, textvariable=unit_var, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", font=("Arial", 12))
unit_menu.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_temperature, font=("Arial", 12), bg="lightblue")
convert_button.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Run the GUI
root.mainloop()



