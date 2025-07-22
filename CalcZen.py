import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.title("CalcZen")
root.geometry("500x650")
root.resizable(False, False)
root.configure(bg="#4CB4E4")
entry = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# --- Calculator Functions ---
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expr = entry.get().replace('^', '**')
        expr = expr.replace('√', 'math.sqrt')
        expr = expr.replace('sin', 'math.sin')
        expr = expr.replace('cos', 'math.cos')
        expr = expr.replace('tan', 'math.tan')
        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# --- Conversion Functions ---
def convert_cm_to_m():
    value = simpledialog.askfloat("Convert cm to m", "Enter value in cm:")
    if value is not None:
        result = value / 100
        messagebox.showinfo("Result", f"{value} cm = {result} m")

def convert_m_to_cm():
    value = simpledialog.askfloat("Convert m to cm", "Enter value in meters:")
    if value is not None:
        result = value * 100
        messagebox.showinfo("Result", f"{value} m = {result} cm")

def convert_kg_to_g():
    value = simpledialog.askfloat("Convert kg to g", "Enter value in kg:")
    if value is not None:
        result = value * 1000
        messagebox.showinfo("Result", f"{value} kg = {result} g")

def convert_g_to_kg():
    value = simpledialog.askfloat("Convert g to kg", "Enter value in grams:")
    if value is not None:
        result = value / 1000
        messagebox.showinfo("Result", f"{value} g = {result} kg")
def convert_km_to_m():
    value = simpledialog.askfloat("Convert km to m", "Enter value in kilometers:")
    if value is not None:
        result = value * 1000
        messagebox.showinfo("Result", f"{value} km = {result} m")
def convert_hour_to_minute():
    value = simpledialog.askfloat("Convert hour to minute", "Enter value in hour:")
    if value is not None:
        result = value * 60
        messagebox.showinfo("Result", f"{value} hour = {result} minutes/minute")

# --- calculate area,perimeter---#
def calculate_area():
    shape = simpledialog.askstring("Calculate Area", "Enter type of shape:")
    if shape == "square":
        value=simpledialog.askfloat("Calculate Area", "Enter side length:")
        result= value * value
        messagebox.showinfo("Result", f"Area of square = {result}")
    elif shape == "rectangle":
        length = simpledialog.askfloat("Calculate Area", "Enter length:")
        width = simpledialog.askfloat("Calculate Area", "Enter width:")
        result = length * width
        messagebox.showinfo("Result", f"Area of rectangle = {result}")
    elif shape =="circle":
        radius = simpledialog.askfloat("Calculate Area", "Enter radius:")
        result = 3.14 * radius * radius
        messagebox.showinfo("Result", f"Area of circle = {result}")
    else:
        messagebox.showinfo("Result", "We just support square,rectangle,circle")

def calculate_perimeter():
    shape = simpledialog.askstring("Calculate Perimeter", "Enter type of shape:")
    if shape == "square":
        value=simpledialog.askfloat("Calculate Perimeter", "Enter side length:")
        result= value*4
        messagebox.showinfo("Result", f"Perimeter of square = {result}")
    elif shape == "rectangle":
        length = simpledialog.askfloat("Calculate Perimeter", "Enter length:")
        width = simpledialog.askfloat("Calculate Perimeter", "Enter width:")
        result = (length + width)*2
        messagebox.showinfo("Result", f"Perimeter of rectangle = {result}")
    elif shape =="circle":
        radius = simpledialog.askfloat("Calculate Perimeter", "Enter radius:")
        result = 3.14 * radius * 2
        messagebox.showinfo("Result", f"Perimeter of circle = {result}")
    else:
        messagebox.showinfo("Result", "We just support square,rectangle,circle")
def calculate_volume():
    shape = simpledialog.askstring("Calculate Volume", "Enter type of shape:")
    if shape =="cube":
        value=simpledialog.askfloat("Calculate Volume", "Enter side length:")
        result= value * value * value
        messagebox.showinfo("Result", f"Volume of cube = {result}")
    elif shape =="rectangular prism":
        length = simpledialog.askfloat("Calculate Volume", "Enter length:")
        width = simpledialog.askfloat("Calculate Volume", "Enter width:")
        height = simpledialog.askfloat("Calculate Volume", "Enter height:")
        result = length * width * height
        messagebox.showinfo("Result", f"Volume of rectangular prism = {result}")
    else:
        messagebox.showinfo("Result", "We just support cube,rectangular prism")
#---Help Menu---
def help_how_to_use():
    messagebox.showinfo("How to use","Press the number or enter the number and enter the operation to calculate")
def help_web_CalcZen():
    messagebox.showinfo("Web CalcZen","Find the html file via github:https://github.com/HGGMCODING/CalcZen")
def help_About_us():
    messagebox.showinfo("About us","Find us on youtube:https://www.youtube.com/@hgmmyt")
# --- Menu Bar ---
menu_bar = tk.Menu(root)
convert_menu = tk.Menu(menu_bar, tearoff=0)
shape_menu=tk.Menu(menu_bar,tearoff=0)
help_menu=tk.Menu(menu_bar,tearoff=0)
convert_menu.add_command(label="cm → m", command=convert_cm_to_m)
convert_menu.add_command(label="m → cm", command=convert_m_to_cm)
convert_menu.add_command(label="kg → g", command=convert_kg_to_g)
convert_menu.add_command(label="g → kg", command=convert_g_to_kg)
convert_menu.add_command(label="km → m", command=convert_km_to_m)
convert_menu.add_command(label="hour → minute", command=convert_hour_to_minute)
menu_bar.add_cascade(label="Convert", menu=convert_menu)
menu_bar.add_cascade(label="Shape", menu=shape_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)
shape_menu.add_command(label="Calculate Area", command=calculate_area)
shape_menu.add_command(label="Calculate Perimeter", command=calculate_perimeter)
shape_menu.add_command(label="Calculate Volume", command=calculate_volume)
help_menu.add_command(label="How to use",command=help_how_to_use)
help_menu.add_command(label="Web CalcZen",command=help_web_CalcZen)
help_menu.add_command(label="About us ",command=help_About_us)
root.config(menu=menu_bar)

# --- Calculator Buttons ---
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
    ('√(', '^', '(', ')'),
    ('sin(', 'cos(', 'tan(', 'C')
]

for i, row in enumerate(buttons):
    for j, char in enumerate(row):
        if char == '=':
            btn = tk.Button(root, text=char, width=5, height=2, font=("Arial", 18),
                            command=calculate)
        elif char == 'C':
            btn = tk.Button(root, text=char, width=5, height=2, font=("Arial", 18),
                            command=clear)
        else:
            btn = tk.Button(root, text=char, width=5, height=2, font=("Arial", 18),
                            command=lambda ch=char: click(ch))
        btn.grid(row=i+1, column=j, padx=5, pady=5)

root.mainloop()
