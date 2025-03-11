import sympy as sp

class InterpolacionTaylor:
    def __init__(self, funcion, valor_x, num_derivadas, simbolo):
        self.funcion = funcion              # función simbolica      
        self.valor_x = valor_x              # punto a aproximar
        self.num_derivadas = num_derivadas  # número de derivadas para realizar la aproximación
        self.simbolo = simbolo              # variable independiente de la función
        self.polinomio = self.calcular_polinomio_taylor()  # crea y guarda el polinomio de taylor con los datos antes guardados

    def calcular_polinomio_taylor(self):
        taylor = 0                              # inicia el polinomio en un valor neutro (0)
        for i in range(self.num_derivadas + 1): # iteración entre 0 y el número de derivadas de la función, incluyendo a la misma
            derivada_i = sp.diff(self.funcion, self.simbolo, i)  # calcula la derivada correspondiente al ciclo (i-ésima derivada)
            termino = (derivada_i.subs(self.simbolo, self.valor_x) / sp.factorial(i)) * (self.simbolo - self.valor_x)**i    # crea el término de la serie de taylor correspondiente ((f´n(a) * (x-a)**n)/(n!))
            taylor += termino                   # se suma el termino recien calculado 
        return sp.simplify(taylor)              # se retorna el termino simplificado

    def graficar(self, rango=(-3, 5), puntos=100):
        funcion_original = sp.lambdify(self.simbolo, self.funcion, modules='sympy')     # convierte la función original (4 grado) a una función numérica para poder introducir valores, y retornar su imagen
        funcion_taylor = sp.lambdify(self.simbolo, self.polinomio, modules='sympy')     # Convierte el polinomio de taylor calculado a una función numérica, mismo caso que la anterior
        x_min, x_max = rango                                                    # indica el rango donde se calcularán los puntos para realizar la graficación
        paso = (x_max - x_min) / (puntos - 1)                                   # calcula el intervalor entre puntos en base a cuantos son necesarios
        valores_x_grafica = [x_min + i * paso for i in range(puntos)]           # genera una lista con los puntos en x dentro del rango
        valores_y_original = [funcion_original(x) for x in valores_x_grafica]   # genera una lista con los puntos en y para la función original (4 grado)
        valores_y_taylor = [funcion_taylor(x) for x in valores_x_grafica]       # genera una lista con los puntos en y para la función de taylor
        lista = (valores_x_grafica,valores_y_original,valores_y_taylor)         # crea una lista con los datos necesarios para graficar. Esta será retornada al archivo main posteriormente
        return lista

    def run(self):
        print("Polinomio de Taylor:",self.polinomio)        # muestra por consola el polinomio de taylor
        lista = self.graficar(rango=(-3, 5), puntos=200)    # llama al metodo graficar para obtener la lista con los datos necesarios 
        return lista