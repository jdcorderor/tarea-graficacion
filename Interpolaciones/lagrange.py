import sympy as sp

class InterpolacionLagrange:
    def __init__(self, puntos):
        self.puntos = puntos                # puntos para realizar la interpolación
        self.x_simbolo = sp.Symbol('x')     # variable independiente

    def calcular_polinomio_sympy(self):
        polinomio = 0                       # inicia el polinomio en un valor neutro (0)
        for i in range(len(self.puntos)):   # itera por cada punto que se haya introducido
            termino = self.puntos[i][1]     # toma el valor de y del punto en el que nos encontremos (valor y i-ésimo punto)
            for j in range(len(self.puntos)):   # segundo bucle para formar el producto
                if i != j:                  # se asegura de que los terminos del divisor sean distintos, pues si no sería una división entre 0 
                    termino *= (self.x_simbolo - self.puntos[j][0]) / (self.puntos[i][0] - self.puntos[j][0])   #Construye un termino de lagrange   
            polinomio += termino    # suma el termino recien calculado al polinomio
        return str(sp.simplify(polinomio))  # retorna el polinomio simplificado

    def calcular_polinomio(self, x_val):
        resultado = 0                       # inicia el resultado en 0
        for i in range(len(self.puntos)):   # itera sobre cada punto
            termino = self.puntos[i][1]     # toma el valor de y del punto en el que nos encontremos (valor y i-ésimo punto)
            for j in range(len(self.puntos)):   # anida otro bucle para construir el producto
                if i != j:                  # se asegura que el denominador sea distinto de 0
                    termino *= (x_val - self.puntos[j][0]) / (self.puntos[i][0] - self.puntos[j][0])    # calcula el termino numérico correspondiente
            resultado += termino    # se suma el valor calculado al resultado
        return resultado

    def graficar(self, rango_x):
        x_grafica = []  # listas para guardar los valores de los puntos X y Y
        y_grafica = []
        for x in rango_x:   # itera por cada punto en el rango definido
            x_grafica.append(x) # añade el termino x a la lista
            y_grafica.append(self.calcular_polinomio(x))    # calcula y añade el término Y correspondiente
        # Graficar los puntos originales
        puntos_x = [p[0] for p in self.puntos]      # guarda los puntos x originales
        puntos_y = [p[1] for p in self.puntos]      # guarda los puntos y originales
        lista = (puntos_x,puntos_y,x_grafica,y_grafica) # crea una lista con los datos necesarios para graficar. Esta será retornada al archivo main posteriormente
        return lista

    def run(self):
        print("\nPolinomio de Lagrange:", self.calcular_polinomio_sympy())  # muestra por consola el polinomio de LaGrange
        rango = [x / 10.0 for x in range(-30, 51)]      # rango entre -3 y 5
        lista = self.graficar(rango)                    # llama al metodo graficar para obtener la lista con los datos necesarios 
        return lista