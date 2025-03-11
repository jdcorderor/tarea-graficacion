# Interpolaciones
## Pasos para iniciar el proyecto.
#### Paso 1:
Primeramente, debe crear un entorno virtual de Python en su equipo. Ejecute el siguiente comando en su consola, en la ubicación que desee.

`virtualenv -p python env`

> [!WARNING]
> En caso de no tener descargada la libreria virtualenv (Se puede comprobar buscando su nombre si se escribe `pip list`), debe descargarlo escribiendo el siguiente comando en su consola: `pip install virtualenv`

#### Paso 2:
Luego, entrará a su entorno virtual (`cd env`) y clonará el repositorio dentro del mismo, escribiendo el siguiente comando en la consola:
`git clone https://github.com/jdcorderor/tarea-graficacion.git`

#### Paso 3:
Ahora, procederá a activarlo, escribiendo en la consola, con la ubicación de su entorno el siguiente comando:
`Scripts\activate`

#### Paso 4:
Seguidamente, entrará a la nueva carpeta recién creada e instalará las dependencias necesarias, escribiendo en la consola el siguiente comando: 
`pip install -r requirements.txt`

#### Paso 5:
Con esto, ya podrá ejecutar el archivo <b>main.py</b>, el principal del proyecto. Este abrirá una nueva ventana donde se podrán apreciar las 4 gráficas de las interpolaciones, y por consola podrá ver los polinomios de cada tipo de interpolación. Si desea ejecutar el archivo Python desde su consola, escriba en ella lo siguiente:
`python main.py`


## Enunciado:
En la ciudad de Estocolmo se realizaron investigaciones meteorológicas, con el objetivo de estudiar la variación de la temperatura, procesar datos y analizar el cambio climático de la región. En las investigaciones se evaluaron las temperaturas en un lapso de 24 horas, con 4.8 horas entre análisis, los datos obtenidos fueron: 
<b>
- ( -2, 54)

- ( -1, 4)

- ( 0, -2)

- (1, -6)

- ( 2, -26)
</b>
Se determinó que la temperatura presenta un comportamiento similar a la expresión matemática:  <b>y = x^4 - 5x^3 - 2</b>. De esta manera, se asume que los valores de las funciones derivadas para las abscisas <b>-2, 0 y 2 son -92, 0 y -28</b>, respectivamente.  Conociendo estos datos, el equipo de investigadores desea realizar una interpolación, con la finalidad de comparar los resultados. En este sentido, utilizarán cuatro métodos: Taylor, Lagrange, Hermite, y Polinómica a Trozos (Interpolador por splines). Además, para la interpolación de Taylor, se desea aproximar al punto x = 1, con un máximo de 3 derivadas.


> [!NOTE]
> En la graficación, el eje X representa el tiempo del estudio. El cero representa el punto medio del mismo, es decir, la hora 12 del análisis meteorológico.
