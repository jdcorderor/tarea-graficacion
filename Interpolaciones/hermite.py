import sympy as sp

class InterpolacionHermite:
    def __init__(self, valores_x, valores_y, derivadas):
        self.valores_x = valores_x      # guarda los nodos de interpolación
        self.valores_y = valores_y      # valores Y asociados a los nodos
        self.derivadas = derivadas      # derivadas de cada función en cada nodo x
        self.polinomio = self.calcular_polinomio_hermite() # calcula y guarda el polinomio de hermite

    def calcular_polinomio_hermite(self):
        x = sp.symbols('x')         # define x como la variable independiente 
        n = len(self.valores_x)     # calcula la cantidad total de puntos de interpolación
        H = 0                       # inicia el polinomio en un valor neutro (0)
        for i in range(n):          # itera por cada punto de interpolación
            h_i = 0                 # inicializa un termino base de lagrange
            for j in range(n):      # Bucle para construir el producto
                if i != j:          # evita la división por cero
                    h_i *= (x - self.valores_x[j]) / (self.valores_x[i] - self.valores_x[j])    # construye el término de lagrange
            derivada_h_i = sp.diff(h_i, x)          # calcula la derivada del termino recien calculado respecto a x
            H += (1 - 2 * derivada_h_i.subs(x, self.valores_x[i]) * (x - self.valores_x[i])) * h_i**2 * self.valores_y[i]   # primer término del polinomio de Hermite con los valores de y
            H += (x - self.valores_x[i]) * h_i**2 * self.derivadas[i]       # segundo término con las derivadas de la función en el nodo i
        return sp.simplify(H)   # retorna la función simplificada

    def graficar(self, puntos=100):
        x = sp.symbols('x')         # define x como la variable independiente 
        funcion_hermite = sp.lambdify(x, self.polinomio, modules='sympy')   # convierte el polinomio de Hermite a una función numérica para poder introducir valores, y retornar su imagen
        x_min, x_max = min(self.valores_x) - 1, max(self.valores_x) + 3     # Rango de la funcion: Xmenor - 1, Xmayor + 3 (-2-1 = -3; 2+3 = 5).
        paso = (x_max - x_min) / (puntos - 1)       # calcula el intervalor entre puntos en base a cuantos son necesarios
        valores_x_grafica = [x_min + i * paso for i in range(puntos)]               # genera una lista con los puntos en x dentro del rango
        valores_y_grafica = [funcion_hermite(x_val) for x_val in valores_x_grafica] # genera una lista con los puntos en y para el polinomio de Hermite
        lista = (valores_x_grafica,valores_y_grafica,self.valores_x,self.valores_y) # crea una lista con los datos necesarios para graficar. Esta será retornada al archivo main posteriormente
        return lista
    
    def run(self):
        print("\nPolinomio de Hermite: ",self.polinomio)    # muestra por consola el polinomio de Hermite
        lista = self.graficar()                             # llama al metodo graficar para obtener la lista con los datos necesarios 
        return lista