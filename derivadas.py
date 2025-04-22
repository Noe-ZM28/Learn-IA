#1
# f(x) =  7x^2 + 3x + 2
# f'(x) = 14x + 3
# f''(x) = 14

# from sympy import symbols, diff

# # Define la variable
# x = symbols('x')

# # Función para calcular la derivada
# def calcular_derivada(funcion):
#     return diff(funcion, x)

# # Ejemplo de uso
# f = 7 * x**2 + 3 * x - 2
# derivada = calcular_derivada(f)

# print("La derivada de la función es:", derivada)
# segunda_derivada = diff(f, x, 2)

# print("La segunda derivada de la función es:", segunda_derivada)



# #2
# import numpy as np
# import matplotlib.pyplot as plt
# from sympy import symbols, diff, lambdify

# # Define la variable simbólica
# x = symbols('x')

# # Función para calcular la derivada
# def calcular_derivada(funcion, orden=1):
#     return diff(funcion, x, orden)

# # Ejemplo de uso
# f = 7 * x**2 + 3 * x - 2

# # Calcula la primera y segunda derivada
# primera_derivada = calcular_derivada(f)
# segunda_derivada = calcular_derivada(f, orden=2)

# # Convierte las funciones simbólicas a funciones numéricas
# f_num = lambdify(x, f, 'numpy')
# primera_derivada_num = lambdify(x, primera_derivada, 'numpy')
# segunda_derivada_num = lambdify(x, segunda_derivada, 'numpy')

# # Rango de valores para graficar
# x_vals = np.linspace(-10, 10, 500)

# # Evalúa las funciones en el rango de valores
# f_vals = f_num(x_vals)
# primera_derivada_vals = primera_derivada_num(x_vals)

# # Si la segunda derivada es una constante, ajusta su forma
# if np.isscalar(segunda_derivada_num(0)):  # Verifica si es constante
#     segunda_derivada_vals = np.full_like(x_vals, segunda_derivada_num(0))
# else:
#     segunda_derivada_vals = segunda_derivada_num(x_vals)

# # Graficar las funciones
# plt.figure(figsize=(10, 6))
# plt.plot(x_vals, f_vals, label="Función original: $f(x)$", color="blue")
# plt.plot(x_vals, primera_derivada_vals, label="Primera derivada: $f'(x)$", color="green")
# plt.plot(x_vals, segunda_derivada_vals, label="Segunda derivada: $f''(x)$", color="red")
# plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
# plt.title("Gráfica de la función y sus derivadas")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()
# plt.grid()
# plt.show()

#3


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from sympy import symbols, diff, lambdify

# Define la variable simbólica
x = symbols('x')

# Función para calcular la derivada
def calcular_derivada(funcion, orden=1):
    return diff(funcion, x, orden)

# Ejemplo de uso
f = 7 * x**2 + 3 * x - 2

# Calcula la primera y segunda derivada
primera_derivada = calcular_derivada(f)
segunda_derivada = calcular_derivada(f, orden=2)

# Convierte las funciones simbólicas a funciones numéricas
f_num = lambdify(x, f, 'numpy')
primera_derivada_num = lambdify(x, primera_derivada, 'numpy')
segunda_derivada_num = lambdify(x, segunda_derivada, 'numpy')

# Rango de valores para graficar
x_vals = np.linspace(-10, 10, 500)

# Evalúa las funciones en el rango de valores
f_vals = f_num(x_vals)
primera_derivada_vals = primera_derivada_num(x_vals)
segunda_derivada_vals = np.full_like(x_vals, segunda_derivada_num(0))  # Segunda derivada constante

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.25)  # Ajustar espacio para la barra deslizante

# Graficar las funciones iniciales
line_f, = ax.plot(x_vals, f_vals, label="Función original: $f(x)$", color="blue")
line_f1, = ax.plot(x_vals, primera_derivada_vals, label="Primera derivada: $f'(x)$", color="green")
line_f2, = ax.plot(x_vals, segunda_derivada_vals, label="Segunda derivada: $f''(x)$", color="red")
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax.set_title("Gráfica de la función y sus derivadas")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid()

# Crear el slider
ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03])  # [left, bottom, width, height]
slider = Slider(ax_slider, 'x', -10.0, 10.0, valinit=0)

# Función para actualizar la gráfica
def update(val):
    x_val = slider.val
    # Recalcular los valores de las funciones en función del slider
    f_vals = f_num(x_vals + x_val)  # Desplaza la función original
    primera_derivada_vals = primera_derivada_num(x_vals + x_val)
    segunda_derivada_vals = np.full_like(x_vals, segunda_derivada_num(0))  # Segunda derivada constante

    # Actualizar las líneas
    line_f.set_ydata(f_vals)
    line_f1.set_ydata(primera_derivada_vals)
    line_f2.set_ydata(segunda_derivada_vals)
    fig.canvas.draw_idle()

# Conectar el slider con la función de actualización
slider.on_changed(update)

plt.show()