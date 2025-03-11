# Análisis de riesgo en un portafolio de inversiones.

import math
import matplotlib.pyplot as plt

class Determinante:
    def __init__(self):
        pass
    
    def determinante(self, matriz):
        if len(matriz) == 2:
            return ((matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0]))  # calcula la determinante de una matriz cuadrada (condición de parada para función recursiva)
        determinante = 0
        for c in range(len(matriz)):
            # Crear una submatriz. Expansión por cofactores a partir de la fila 1.
            submatriz = [fila[:c] + fila[c+1:] for fila in matriz[1:]]
            # Calcular el determinante.
            determinante += ((-1) ** c) * matriz[0][c] * self.determinante(submatriz)
        return determinante

class Inversa:
    def __init__(self):
        pass

    def inversa(self, matriz):
        n = len(matriz)
        A = self.copiar_matriz(matriz)  # copia la matriz para que no haya problemas luego
        identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]  # crea una matriz identidad del tamaño de la matriz original
        for i in range(n):
            A[i] += identidad[i]    # adjunta la matriz identidad a la matriz original para calcular su inversa
        for i in range(n):
            if abs(A[i][i]) < 1e-12:    # verificación para evitar valores muy pequeños en el pivote
                for j in range(i + 1, n):
                    if abs(A[j][i]) > abs(A[i][i]):
                        A[i], A[j] = A[j], A[i]
                        break
            pivote = A[i][i]        # eliminación gaussiana
            A[i] = [x / pivote for x in A[i]]
            for j in range(n):
                if j != i:
                    factor = A[j][i]
                    A[j] = [a - factor * b for a, b in zip(A[j], A[i])]
        return [fila[n:] for fila in A] # retorna la matriz inversa (como duplico el tamaño de la matriz original, el tamaño inicial (n) es ahora la mitad de la matriz resultante)
    
class NumeroCondicion(Determinante, Inversa):
    def __init__(self, A):
        self.A = A
        Determinante.__init__(self)
        self.detA = self.determinante(A)
        Inversa.__init__(self)
        self.condA = self.calcular_condA()

    def calcular_condA(self):
        if self.detA == 0:
            print("La matriz A no es invertible.")
            return None
        else:
            invA = self.inversa(self.A)
            return self.norma_matriz(self.A) * self.norma_matriz(invA)
    
    def copiar_matriz(self, matriz):
        return [fila[:] for fila in matriz] # hace una copia por trozos de la matriz
    
    def norma_matriz(self, matriz):
        return math.sqrt(sum(x**2 for fila in matriz for x in fila))
    
class MetodoPotencia:
    def __init__(self, A, x0, tolerancia):
        self.A = A
        self.x0 = x0
        self.tolerancia = tolerancia
        self.autovaloresmax, self.autovectoresmax = self.metodo_potencia()

    def metodo_potencia(self, error = 1):
        if (len(self.A) == len(self.x0)):   # verifica que la matriz cuadrada tenga la misma cantidad de columnas, que filas el vector
            autovalores = []    # lista para guardas los autovalores
            autovectores = []   # lista para guardas los autovectores
            vector = self.x0
            while error > self.tolerancia:  # mientras el error sea mayor a la tolerancia máxima, se repetirá el ciclo
                Ax = self.producto(self.A, vector)   # calcula el producto entre la matriz y el vector
                norma = self.norma_vectormp(Ax)      # calcula la norma del autovector recien calculado
                autovalores.append(norma)   # añade la norma a la lista de autovalores
                vector = [x / norma for x in Ax]    # Normaliza el autovector, para seguidamente guardarlo
                autovectores.append(vector)
                if (len(autovalores) > 1):
                    error = abs(autovalores[-1] - autovalores[-2])  # calcula el nuevo error (último elemento de la lista, menos el penúltimo)
            return autovalores, autovectores
        else:
            print("Error de dimensiones")
        
    def producto(self, matriz, vector):
        return [sum(a * b for a, b in zip(fila, vector)) for fila in matriz]
    
    def norma_vectormp(self, vector):
        return math.sqrt(sum(x**2 for x in vector))
    
class MetodoPotenciaInversa(Determinante, Inversa):
    def __init__(self, A, x0, tolerancia):
        self.A = A              # matriz cuadrada
        self.x0 = x0            # vector inicial
        self.tolerancia = tolerancia    # tolerancia máxima
        Determinante.__init__(self)
        self.detA = self.determinante(A)    # determinante de la matriz cuadrada
        if self.detA != 0:          # si la determinante es != 0, es una matriz invertible
            Inversa.__init__(self)
            self.invA = self.inversa(A)
            self.autovaloresmin, self.autovectoresmin = self.metodo_potenciainv()
        else:
            print("La matriz no es invertible")
    
    def copiar_matriz(self, matriz):
        return [fila[:] for fila in matriz] # hace una copia por trozos de la matriz

    def metodo_potenciainv(self, error = 1):    # Calcula el autovalor mínimo y su autovector correspondiente usando el método de potencia inversa
        if (len(self.A) == len(self.x0)):       # Verifica que las dimensiones de la matriz y el vector sean compatibles
            autovalores = []
            autovectores = []
            vector = self.x0
            while error > self.tolerancia:
                invAx = self.producto(self.invA, vector)   # calcula el autovector menor
                norma = self.norma_vectormpi(invAx)   # calcula el autovalor menor
                autovalores.append(1/norma)     # añade el autovalor mínimo a la lista
                vector = [x / norma for x in invAx]     # Normaliza el autovector y lo añade a la lista
                autovectores.append(vector)
                if (len(autovalores) > 1):
                    error = abs(autovalores[-1] - autovalores[-2])  # calcula el nuevo error
            return autovalores, autovectores
        else:
            print("Error de dimensiones")
        
    def producto(self, matriz, vector):
        return [sum(a * b for a, b in zip(fila, vector)) for fila in matriz]
    
    def norma_vectormpi(self, vector):
        return math.sqrt(sum(x**2 for x in vector))
    
class MatrizCovarianza(NumeroCondicion, MetodoPotencia, MetodoPotenciaInversa):
    def __init__(self, A):
        NumeroCondicion.__init__(self, A)
        MetodoPotencia.__init__(self, A, [1, 0, 0], 1e-8)
        MetodoPotenciaInversa.__init__(self, A, [1, 0, 0], 1e-8)

# Código Principal:

# Matriz de covarianza entre los retornos de los activos.
matrizcovarianza = [[4, 5, 7], 
                    [5, 8, 1], 
                    [7, 1, 1]]

mc = MatrizCovarianza(matrizcovarianza)

# Número de condición de la matriz de covarianza.
print("--- Nivel de condicionamiento y estabilidad del sistema de activos ---")
print(f"Número de condición: {mc.condA}")

# Autovalor dominante de la matriz de covarianza.
print("\n--- Autovalor dominante: Riesgo principal del portafolio ---")
print(f"\nAutovalor máximo: {mc.autovaloresmax[-1]}")
print(f"Autovector normalizado (combinación de activos de mayor riesgo): {mc.autovectoresmax[-1]}")

# Comprobación:
print(f"\nComprobación\nAX = {mc.producto(mc.A, mc.autovectoresmax[-1])}")
print(f"LambdaX = {[mc.autovaloresmax[-1] * x for x in mc.autovectoresmax[-1]]}")

plt.plot(mc.autovaloresmax, marker='o')
plt.title('Convergencia del Autovalor Dominante: Riesgo principal del portafolio')
plt.xlabel('Iteraciones')
plt.ylabel('Autovalor')
plt.grid()
plt.axhline(y=mc.autovaloresmax[-1], color='r', linestyle='--', label='Valor final')
plt.legend()
plt.show()

# Autovalor mínimo de la matriz de covarianza.
if (mc.detA != 0):
    print("\n--- Autovalor mínimo: Identifica oportunidades de diversificación con menor riesgo ---")
    print(f"\nAutovalor mínimo: {mc.autovaloresmin[-1]}")
    print(f"Autovector normalizado (combinación de activos con el menor riesgo): {mc.autovectoresmin[-1]}")

    # Comprobación:
    print(f"\nComprobación\ninvAX = {mc.producto(mc.invA, mc.autovectoresmin[-1])}")
    print(f"LambdaX = {[(1/mc.autovaloresmin[-1]) * x for x in mc.autovectoresmin[-1]]}")

    plt.plot(mc.autovaloresmin, marker='o')
    plt.title('Convergencia del Autovalor Mínimo: Oportunidades de diversificación con menor riesgo')
    plt.xlabel('Iteraciones')
    plt.ylabel('Autovalor')
    plt.grid()
    plt.axhline(y=mc.autovaloresmin[-1], color='r', linestyle='--', label='Valor final')
    plt.legend()
    plt.show()