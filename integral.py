import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import tkinter as tk
from tkinter import messagebox

total_area = 0.0

# Diccionario de funciones seguras
safe_dict = {
    'sin': np.sin,
    'cos': np.cos,
    'tan': np.tan,
    'exp': np.exp,
    'log': np.log,
    'sqrt': np.sqrt,
    'pi': np.pi,
    'e': np.e
}

def integrand(x, user_function):
    # Crear un entorno local con x y las funciones seguras
    local_dict = {'x': x}
    return eval(user_function, {"__builtins__": None}, {**safe_dict, **local_dict})

def plot_integral(user_function, lower_limit, upper_limit):
    global total_area  
    # Generar puntos x uniformemente entre los límites de integración
    x = np.linspace(lower_limit, upper_limit, 1000)
    # Evaluar esos puntos
    y = np.array([integrand(val, user_function) for val in x])

    # Calcular la integral
    integral, _ = integrate.quad(lambda x: integrand(x, user_function), lower_limit, upper_limit)
    total_area += integral
    # Graficar la función
    plt.plot(x, y, 'r', label='Función')
    plt.fill_between(x, 0, y, where=(x >= lower_limit) & (x <= upper_limit), alpha=0.3)
    plt.title('Suma de áreas = {:.2f}'.format(total_area))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()

    # Añadir texto con el valor de la integral
    plt.text(0.5 * (lower_limit + upper_limit), 0.5 * max(y), 'Integral = {:.2f}'.format(integral), horizontalalignment='center')

    plt.show()

def calculate_integral():
    global total_area

    user_function = entry_function.get()
    lower_limit = entry_lower_limit.get()
    upper_limit = entry_upper_limit.get()
   
    try:
        lower_limit = float(lower_limit)
        upper_limit = float(upper_limit)
        plot_integral(user_function, lower_limit, upper_limit)
    except ValueError:
        messagebox.showerror("Error", "Los límites de integración deben ser números.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

    

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Integrales Definidas")

# Crear etiquetas y campos de entrada
label_function = tk.Label(root, text="Función (utilice 'x' como variable):")
label_function.pack()
entry_function = tk.Entry(root)
entry_function.pack()

label_lower_limit = tk.Label(root, text="Límite inferior de integración (a):")
label_lower_limit.pack()
entry_lower_limit = tk.Entry(root)
entry_lower_limit.pack()

label_upper_limit = tk.Label(root, text="Límite superior de integración (b):")
label_upper_limit.pack()
entry_upper_limit = tk.Entry(root)
entry_upper_limit.pack()

# Botón para calcular la integral
button_calculate = tk.Button(root, text="Calcular Integral", command=calculate_integral)
button_calculate.pack()

# Ejecutar la interfaz de usuario
root.mainloop()
