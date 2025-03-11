import sympy as sp

class InterpolacionATrozos:
    def __init__(self, puntos):
        self.puntos = sorted(puntos)  # ordena los puntos 

    def interpolar_tramos_simbolico(self):
        x = sp.Symbol('x')      # define x como la variable independiente
        tramos = []             # lista vacía para almacenar las ecuaciones de los tramos
        for i in range(len(self.puntos) - 1):   # itera a través de todos los puntos consecutivos (por eso, el -1)
            x1, y1 = self.puntos[i]             # extrae el punto incial del segmento actual
            x2, y2 = self.puntos[i + 1]         # extrae el punto final del segmento actual
            tramo = y1 + (y2 - y1) * (x - x1) / (x2 - x1)  # calcula la ecuación del tramo (una recta) con la fórmula de pendiente 
            tramos.append((tramo, (x1, x2)))  # Guardar la ecuación y su intervalo.
        return tramos

    def interpolar(self, x_val):        
        for i in range(len(self.puntos) - 1):   # Recorrer cada segmento
            x1, y1 = self.puntos[i]
            x2, y2 = self.puntos[i + 1]
            if x1 <= x_val <= x2:               # Verificar si "x_val" está en el segmento actual.
                return y1 + (y2 - y1) * (x_val - x1) / (x2 - x1)    # Fórmula de la recta: y = y1 + (y2 - y1) * (x - x1) / (x2 - x1).
        return None # Si no está en ningún segmento, devolver None (fuera del rango).

    def graficar(self, rango_x):
        x_grafica = []              # listas para guardar los valores de los puntos X y Y
        y_grafica = []
        for x in rango_x:           # itera sobre los valores del rango indicado
            y = self.interpolar(x)  # calcula Y para cada valor de x
            if y is not None:       # verifica si el valor es válido
                x_grafica.append(x) # añade el valor de x a la lista
                y_grafica.append(y) # añade el valor de y a la lista
        puntos_x = [p[0] for p in self.puntos]  # guarda los puntos x originales
        puntos_y = [p[1] for p in self.puntos]  # guarda los puntos y originales
        x_funcion = [x / 10.0 for x in range(int(rango_x[0] * 10), int(rango_x[-1] * 10) + 1)]  # Genera valores de x en pasos uniformes para la función original
        y_funcion = [x**4 - 5*x**3 -2 for x in x_funcion]   # Calcula los valores Y de la función original (solo con fines de comparar)
        lista = (puntos_x,puntos_y,x_grafica,y_grafica,x_funcion,y_funcion) # crea una lista con los datos necesarios para graficar. Esta será retornada al archivo main posteriormente
        return lista
    
    def run(self):
        tramos = self.interpolar_tramos_simbolico() # obtiene las ecuaciones simbolicas de cada tramo
        print("\nEcuaciones de los tramos de la Interpolación a Trozos:")
        for tramo, intervalo in tramos:
            print(f"Tramo en intervalo {intervalo}: {tramo}")   # imprime cada ecuación por consola junto a su tramo
        rango = [x / 10.0 for x in range(-30, 51)]              # crea el rango donde se graficará la funcion (-3,5)
        lista = self.graficar(rango)
        return lista