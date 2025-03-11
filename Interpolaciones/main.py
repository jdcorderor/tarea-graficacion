import matplotlib.pyplot as plt
import sympy as sp
from taylor import InterpolacionTaylor      # Importación de las clases para las interpolaciones
from lagrange import InterpolacionLagrange
from hermite import InterpolacionHermite
from atrozos import InterpolacionATrozos

puntos = [(-2,54),(-1,4),(0,-2),(1,-6),(2,-26)]             # (x,y).
puntos_con_derivadas = [(-2,54,-92),(0,-2,0),(2,-26,-28)]   # (x,y,y').

# Datos para la Interpolación de Taylor.
x = sp.symbols('x')  
funcion = x**4 - 5*x**3 -2  
valor_x = 1  
num_derivadas = 3  
taylor = InterpolacionTaylor(funcion, valor_x, num_derivadas, x)
valores_x_grafica_taylor,valores_y_original_taylor,valores_y_taylor = taylor.run()

# Datos para la Interpolación de Lagrange.
puntos_dados = puntos # Se requieren "n" puntos para conseguir una función de grado n-1.
lagrange = InterpolacionLagrange(puntos_dados)
puntos_x_lagrange,puntos_y_lagrange,x_grafica_lagrange,y_grafica_lagrange = lagrange.run()

# Datos para la Interpolación de Hermite.
valores_x = [puntos_con_derivadas[0][0],puntos_con_derivadas[1][0],puntos_con_derivadas[2][0]]
valores_y = [puntos_con_derivadas[0][1],puntos_con_derivadas[1][1],puntos_con_derivadas[2][1]]
derivadas = [puntos_con_derivadas[0][2],puntos_con_derivadas[1][2],puntos_con_derivadas[2][2]]
hermite = InterpolacionHermite(valores_x, valores_y, derivadas)
valores_x_grafica_hermite,valores_y_grafica_hermite,valores_x_hermite,valores_y_hermite = hermite.run()

# Datos para la Interpolación a Trozos.
puntos_dados = puntos
trozos = InterpolacionATrozos(puntos_dados)
puntos_x_trozos,puntos_y_trozos,x_grafica_trozos,y_grafica_trozos,x_funcion_trozos,y_funcion_trozos = trozos.run()

plt.figure(figsize=(14, 7))

# Gráfica de la Interpolación de Taylor.
plt.subplot(2, 2, 1)
plt.plot(valores_x_grafica_taylor, valores_y_taylor, label='Interpolación de Taylor', color='blue')
plt.plot(valores_x_grafica_taylor, valores_y_original_taylor, label='Función x^4 - 5x^3 -2', color='green', linestyle='--')
plt.scatter(puntos[3][0],puntos[3][1],label="Punto de aproximación", color="red", marker="o")
plt.title('Interpolación de Taylor')
plt.xlabel("Tiempo del estudio")
plt.ylabel("Temperatura")
plt.legend()
plt.grid(True)

# Gráfica de la Interpolación de Lagrange.
plt.subplot(2, 2, 2)
plt.plot(x_grafica_lagrange, y_grafica_lagrange, label='Interpolación de Lagrange', color='blue')
plt.scatter(puntos_x_lagrange, puntos_y_lagrange, color='red', label='Puntos originales')
plt.title("Interpolación de Lagrange")
plt.xlabel("Tiempo del estudio")
plt.ylabel("Temperatura")
plt.legend()
plt.grid(True)

# Gráfica de la Interpolación de Hermite.
plt.subplot(2, 2, 3)  
plt.plot(valores_x_grafica_hermite, valores_y_grafica_hermite, label='Interpolación de Hermite', color='blue')
plt.scatter(valores_x_hermite, valores_y_hermite, color='red', label='Puntos originales')
plt.title('Interpolación de Hermite')
plt.xlabel("Tiempo del estudio")
plt.ylabel("Temperatura")
plt.legend()
plt.grid(True)

# Gráfica de la Interpolación a Trozos.
plt.subplot(2, 2, 4)
plt.plot(x_grafica_trozos, y_grafica_trozos, color='blue', label='Interpolación a trozos')
plt.plot(x_funcion_trozos, y_funcion_trozos, color='green', linestyle='--', label='Función x^4 - 5x^3 -2')
plt.scatter(puntos_x_trozos, puntos_y_trozos, color='red', label='Puntos originales')
plt.title("Interpolación a Trozos")
plt.xlabel("Tiempo del estudio")
plt.ylabel("Temperatura")
plt.legend()
plt.grid(True)

plt.tight_layout() # NOTA: NO QUITAR, AJUSTA LOS ESPACIOS PARA EVITAR COLISIONES EN LA GRÁFICA
plt.show()
