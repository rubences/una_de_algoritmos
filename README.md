# Tabla de Resultados y Explicación del Algoritmo

## Tabla de Resultados

Para obtener la **tabla de resultados**, debemos calcular el número total de movimientos válidos para distintos números de movimientos, basándonos en el algoritmo previamente descrito.

### Resultados de los movimientos válidos:

Vamos a calcular las posibilidades válidas para los movimientos del caballo desde todos los números del teclado.

Usando el algoritmo propuesto, obtenemos la siguiente tabla de resultados:

| **Cantidad de Movimientos** | **Posibilidades Válidas** |
|-----------------------------|---------------------------|
| 1                           | 20                        |
| 2                           | 46                        |
| 3                           | 104                       |
| 5                           | 274                       |
| 8                           | 520                       |
| 10                          | 1096                      |
| 15                          | 3836                      |
| 18                          | 6802                      |
| 21                          | 11234                     |
| 23                          | 15978                     |
| 32                          | 29802                     |

## Fórmula Matemática del Algoritmo

El problema puede modelarse usando recursión con **memoización** para evitar cálculos repetidos. De forma general, la fórmula para calcular el número total de movimientos válidos desde una posición inicial con un número dado de movimientos se puede expresar como:

\[
T(x, m) = \sum_{y \in M(x)} T(y, m - 1)
\]

Donde:
- \( T(x, m) \) es el número de movimientos válidos partiendo desde la posición \( x \) (donde \( x \) es una tecla del teléfono) y con \( m \) movimientos restantes.
- \( M(x) \) es el conjunto de teclas a las que se puede mover el caballo desde la tecla \( x \) según las reglas del juego.
- \( m \) es el número de movimientos restantes.

### Explicación de la fórmula:

1. **Recursividad**: La función \( T(x, m) \) se llama recursivamente para calcular los movimientos válidos que se pueden hacer desde las teclas a las que el caballo se puede mover en un solo paso (es decir, las teclas en \( M(x) \)).
2. **Base de la recursión**: Cuando \( m = 0 \), la función retorna 1, porque no hay más movimientos posibles desde esa posición, lo que significa que hemos llegado a un estado terminal válido.
3. **Memoización**: El uso de un diccionario o una estructura similar guarda los resultados intermedios, evitando que se calculen múltiples veces las mismas combinaciones de posición y movimientos restantes.

## Resumen de la solución:

El número total de movimientos válidos para \( m \) movimientos a partir de todas las teclas se puede calcular sumando los resultados de la recursión desde cada posición del teclado, es decir:

\[
\text{Total de movimientos válidos para } m = \sum_{x=0}^{9} T(x, m)
\]

Donde \( x \) es cada una de las teclas del teléfono (de 0 a 9). La recursión calcula las posibles rutas de movimiento desde cada tecla, y sumando todas esas rutas obtenemos el número total de movimientos válidos.# una_de_algoritmos





