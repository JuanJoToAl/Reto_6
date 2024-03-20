# Reto_6
_El siguiente repositorio muestra la solución al reto 6_

## 1. Dado la figura de la imagen, desarrolle:
[![68747470733a2f2f692e706f7374696d672e63632f465276436d7078782f696d6167652e706e67.png](https://i.postimg.cc/s2RCrKcZ/68747470733a2f2f692e706f7374696d672e63632f465276436d7078782f696d6167652e706e67.png)](https://postimg.cc/4YwSv6jJ)
+ Una función matemática para calcular el volumen y el área superficial.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r1`, `r2` y `h`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*
import math

```python
import math

# Las abreviaturas usadas son: v =volumen, r = radio, a = área, 
# esf = esfera, cn= cono sum = suma y slds = sólidos.

def v_slds( r_esf : float, r_cn : float, h_cn : float ) ->  float:
    v_esf = (4/3) * math.pi * r_esf**3
    v_cn = (1/3) * math.pi * r_cn**2 * h_cn
    return v_esf + v_cn

def a_slds( r_esf : float, r_cn : float, h_cn : float ) ->  float:
    a_sup_esf = 4 * math.pi * r_esf**2
    a_sup_cn = math.pi * r_cn**2 + math.pi * ((r_cn**2 + h_cn**2)**0.5) * r_cn
    return a_sup_esf + a_sup_cn

if __name__ == "__main__":
  r_esf = float(input("Ingrese el valor del radio de la esfera"))
  r_cn = float(input("Ingrese el valor del radio del cono"))
  h_cn = float(input("Ingrese el valor de la altura del cono"))
  sum_v_slds, sum_a_slds = v_slds(r_esf, r_cn, h_cn), a_slds(r_esf, r_cn, h_cn)
  print("La suma de volúmenes de esfera y cono es " + str(round(sum_v_slds, 3)))
  print("La suma de áreas de esfera y cono es " + str(round(sum_a_slds, 3)))

```

## 2. Dado la figura de la imagen, desarrolle:

[![68747470733a2f2f692e706f7374696d672e63632f3174344d727a734c2f696d6167652e706e67.png](https://i.postimg.cc/NfSt9c13/68747470733a2f2f692e706f7374696d672e63632f3174344d727a734c2f696d6167652e706e67.png)](https://postimg.cc/xcvhhBp5)

+ Una función matemática para calcular el área y el perimetro.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r`, `a` y `b`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*

```python
import math

# Las abreviaturas usadas son: per = perímetro, r = radio, ar = área, 
# circu = círculo, rtg = rectángulo fgs = figuras, sum = suma
# a = altura rectángulo y b = base rectángulo.

def ar_per_fgs( r_circu : float, a_rtg : float, b_rtg : float ) ->  float:
    ar_circu = math.pi * r_circu**2
    ar_rtg = a_rtg * b_rtg
    per_circu = 2 * math.pi * r_circu
    per_rtg = 2 * a_rtg + 2 * b_rtg
    return ar_circu + ar_rtg, per_circu + per_rtg

if __name__ == "__main__":
    r_circu = float(input("Ingrese el valor del radio del círculo"))
    a_rtg = float(input("Ingrese el valor de la altura del rectángulo"))
    b_rtg = float(input("Ingrese el valor de la base del rectángulo"))
    sum_ar_fgs, sum_per_fgs = ar_per_fgs(r_circu, a_rtg, b_rtg)
    print("La suma de las áreas de la esfera y el cono es " + str(round(sum_ar_fgs, 3)))
    print("La suma de los perímetros de la esfera y el cono es " + str(round(sum_per_fgs, 3)))

```

## 3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```python
# Las abreviaturas usadas son: ct = cantidad, crn = carne, gna = gallina y
# pto = pollito

def ct_crn_aves(ct_gna : float, ct_gallo : float, ct_pto : float) ->  float:
    crn_gna =  6 * ct_gna
    crn_gallo = 7 * ct_gallo 
    return crn_gna, crn_gallo, ct_pto

if __name__ == "__main__":
    ct_gna = float(input("Ingrese la canidad de carne de gallina en kg"))
    ct_gallo = float(input("Ingrese la canidad de carne de gallo en kg"))
    ct_pto = float(input("Ingrese la canidad de carne de pollito en kg"))
    kg_crn_gna, kg_crn_gallo, kg_crn_pto = ct_crn_aves(ct_gna, ct_gallo, ct_pto)
    print("La cantidad de carne de gallina es " + str(kg_crn_gna) + "kg")  
    print("La cantidad de carne de gallo es " + str(kg_crn_gallo) + "kg") 
    print("La cantidad de carne de pollito es " + str(kg_crn_pto) + "kg")
```

## 4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a  3300 cada una y H huevos a  350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```python
#Las abreviaturas usadas son: v = valor, p = panes, l = leche, h = huevos

def mandado(p : float, l : float, h : float, billete : float) ->  float:
    v_vueltas = billete - (300 * p + 3300 * l + 350 * h) 
    return v_vueltas

if __name__ == "__main__":
    p = float(input("¿Cuántos panes dijo mamá?"))
    l = float(input("¿Cuánta leche dijo mamá?"))
    h = float(input("¿Cuántos huevos dijo mamá?"))
    billete = float(input("¿Cuánta plata me dio mamá?"))
    vueltas = mandado(p, l, h, billete)
    if vueltas >= 0:
        print("Las vueltas son " + str(vueltas))
    else: 
        print("Pailas doña Mariluz, le quedo debiendo " + str(vueltas))
```

## 5. Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.

```python
#Las abreviaturas usadas son: ti = tasa de interés y m = meses

def prestamo( capital : float, ti : float, m : float) ->  float:
    return capital * (1 + ti)**m

if __name__ == "__main__":
    capital = float(input("Ingrese el capital inicial"))
    ti = float(input("Ingrese la tasa de interés en formato decimal"))
    m = float(input("Ingrese cantidad de meses a la que se realizó el préstamo"))
    val_prestamo = prestamo(capital, ti, m)
    print("El valor del préstamo es " + str(val_prestamo))
```

## 6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

```python
#Las abreviaturas usadas son: d = días, c = casos y enf= enfermos

def contagios( enf : int, d : int) ->  int:
    total_contagios = enf * (2)**d
    return total_contagios

if __name__ == "__main__":
    enf = int(input("Ingrese la cantidad de enfermos actuales"))
    d = int(input("Ingrese cantidad de días a estimar número de enfermos"))
    c_enf_totales= contagios(enf, d)
    print("Los días a estimar la cantidad de enfermos son " + str(d))
    print("El número de personas contagiados será " + str(c_enf_totales))
```

## 7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número

```python
from functools import reduce

# Se definen funciones

def promedio(a : float, b : float, c : float, d : float, e : float) -> float:
    return (a + b + c + d + e) / 5

def mediana(a : float, b : float, c : float, d : float, e : float) -> float:
    return (a + b + c + d + e) // 5

def promedio_multiplicativo(a : float, b : float, c : float, d : float, e : float) -> float:
    return (reduce(lambda x, y: x * y, (a, b, c, d, e))) ** (1/5)

def ord_asce(a : float, b : float, c : float, d : float, e : float) -> float:
    return sorted((a, b, c, d, e))

def ord_desce(a : float, b : float, c : float, d : float, e : float) -> float:
    return sorted((a, b, c, d, e), reverse = True)

def poten(a : float, b : float, c : float, d : float, e : float) -> float:
    return max(a, b, c, d, e) ** min(a, b, c, d, e)

def raiz(a : float, b : float, c : float, d : float, e : float) -> float:
    return min(a, b, c, d, e) ** (1/3)

# Pedimos los números al usuario
if __name__ == "__main__":
  a = float(input("Ingrese el primer número: "))
  b = float(input("Ingrese el segundo número: "))
  c = float(input("Ingrese el tercer número: "))
  d = float(input("Ingrese el cuarto número: "))
  e = float(input("Ingrese el quinto número: "))

# Calculamos los valores
  num_promedio = promedio(a, b, c, d, e)
  num_mediana = mediana(a, b, c, d, e)
  num_pro_multi = promedio_multiplicativo(a, b, c, d, e)
  num_asce = ord_asce(a, b, c, d, e)
  num_desce = ord_desce(a, b, c, d, e)
  num_pot = poten(a, b, c, d, e)
  num_raz = raiz(a, b, c, d, e)
# Imprimimos los resultados
  print("El promedio es:", num_promedio)
  print("La mediana es:", num_mediana)
  print("El promedio multiplicativo es:", num_pro_multi)
  print("Los números en orden ascendente son:", num_asce)
  print("Los números en orden descendente son:", num_desce)
  print("La potencia del número mayor elevado al número menor es:", num_pot)
  print("La raíz cúbica del número menor:", num_raz)
```

## 8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.
Los archivos están arriba :)

## 9. Consultar qué es y cómo funciona *pip* en python.

Pip es un administrador de paquetes para Python que te permite instalar, actualizar y eliminar bibliotecas y frameworks de terceros de forma sencilla.
Para usar pip, abre una terminal o ventana de comandos y navega hasta el directorio donde deseas instalar la biblioteca o framework. Luego, ejecuta el siguiente comando:

```python
pip install nombre_del_paquete
```

## 10. Hacer un listado de módulos populares para python que se puedan instalar com *pip* y consultar cómo instalarlos.

Lista de algunos de los módulos de Python más populares que se pueden instalar con pip:

### Ciencia de datos:

+ NumPy: biblioteca fundamental para computación científica con Python.
+ Pandas: biblioteca para análisis y manipulación de datos.
+ Scikit-learn: biblioteca para aprendizaje automático.
+ Matplotlib: biblioteca para visualización de datos.
+ TensorFlow: biblioteca para aprendizaje profundo.

### Desarrollo web:

Django: framework para desarrollo web rápido y seguro.
Flask: microframework para desarrollo web ligero.
Pyramid: framework para desarrollo web flexible y escalable.
TurboGears: framework para desarrollo web rápido y fácil de usar.
Web2py: framework para desarrollo web completo y sin necesidad de configuración.

### Utilidades:

+ Requests: biblioteca para realizar peticiones HTTP.
+ Beautiful Soup: biblioteca para extraer datos de páginas web.
+ Selenium: biblioteca para automatizar la interacción con navegadores web.
+ PyQt: biblioteca para crear interfaces gráficas de usuario.
+ Twisted: biblioteca para desarrollo de aplicaciones de red.
