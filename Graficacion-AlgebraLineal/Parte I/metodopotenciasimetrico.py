import math
import matplotlib.pyplot as plt

class MetodoPotencia:
    def __init__(self, A, x0, tolerancia):
        self.A = A  # matriz
        self.determinante = self.determinante(self.A)
        self.x0 = x0    # vector
        self.tolerancia = tolerancia
        self.autovalores, self.autovectores = self.metodo_potencia()
    
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

    def metodo_potencia(self, error = 1):
        if (len(self.A) == len(self.x0)):   # verifica que la matriz cuadrada tenga la misma cantidad de columnas, que filas el vector
            autovalores = []    # lista para guardas los autovalores
            autovectores = []   # lista para guardas los autovectores
            vector = self.x0    
            while error > self.tolerancia:  # mientras el error sea mayor a la tolerancia máxima, se repetirá el ciclo
                Ax = self.producto(self.A, vector)  # calcula el producto entre la matriz y el vector
                norma = self.norma(Ax)      # calcula la norma del autovector recien calculado
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
    
    def norma(self, vector):
        return math.sqrt(sum(x**2 for x in vector))

class MetodoPotenciaInversa:
    def __init__(self, A, x0, tolerancia):
        self.A = A              # matriz cuadrada
        self.x0 = x0            # vector inicial
        self.tolerancia = tolerancia    # tolerancia máxima
        self.detA = self.determinante(A)    # determinante de la matriz cuadrada
        if self.detA != 0:          # si la determinante es != 0, es una matriz invertible
            self.invA = self.inversa(A)
            self.autovalores, self.autovectores = self.metodo_potenciainv()
        else:
            print("La matriz no es invertible")

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
    
    def copiar_matriz(self, matriz):
        return [fila[:] for fila in matriz] # hace una copia por trozos de la matriz

    def metodo_potenciainv(self, error = 1):    # Calcula el autovalor mínimo y su autovector correspondiente usando el método de potencia inversa
        if (len(self.A) == len(self.x0)):       # Verifica que las dimensiones de la matriz y el vector sean compatibles
            autovalores = []
            autovectores = []
            vector = self.x0
            while error > self.tolerancia:
                invAx = self.producto(self.invA, vector)  # calcula el autovector menor
                norma = self.norma(invAx)   # calcula el autovalor menor
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
    
    def norma(self, vector):
        return math.sqrt(sum(x**2 for x in vector))

matrizsimetrica =  [[6, 2, 1],
                    [2, 3, 1],
                    [1, 1, 4]]

vector = [1, 0, 0]

tolerancia = 1e-8

mp = MetodoPotencia(matrizsimetrica, vector, tolerancia)
mpi = MetodoPotenciaInversa(matrizsimetrica, vector, tolerancia)

if mp.determinante!=0:
    # Datos autovalor dominante
    print(f"Autovalor máximo: {mp.autovalores[-1]}")
    print(f"Autovector normalizado: {mp.autovectores[-1]}")
    print(f"\nAX = {mp.producto(mp.A, mp.autovectores[-1])}")
    print(f"LambdaX = {[mp.autovalores[-1] * x for x in mp.autovectores[-1]]}")
    # Datos autovalor menor
    print(f"\n\nAutovalor mínimo: {mpi.autovalores[-1]}")
    print(f"Autovector normalizado: {mpi.autovectores[-1]}")
    print(f"\ninvAX = {mpi.producto(mpi.invA, mpi.autovectores[-1])}")
    print(f"LambdaX = {[(1/mpi.autovalores[-1]) * x for x in mpi.autovectores[-1]]}")

    plt.plot(mp.autovalores, marker='o',color="blue",label="Autovalor Dominante")
    plt.plot(mpi.autovalores, marker='o',color="orange",label="Autovalor Mínimo")
    plt.axhline(y=mp.autovalores[-1], color='r', linestyle='--', label='Valor final (autovalor dominante)')
    plt.axhline(y=mpi.autovalores[-1], color='r', linestyle='--', label='Valor final (autovalor mínimo)')
    plt.title('Convergencia de Autovalores\n(Autovalor Dominante y Autovalor Mínimo)')
    plt.xlabel('Iteraciones')
    plt.ylabel('Autovalor')
    plt.grid()
    plt.legend()
    plt.show()