import math

# Las abreviaturas usadas son: v =volumen, r = radio, a = área, 
# esf = esfera, cn= cono sum = suma y slds = sólidos.

def v_slds( r_esf = float, r_cn = float, h_cn = float ) ->  float:
    v_esf = (4/3) * math.pi * r_esf**3
    v_cn = (1/3) * math.pi * r_cn**2 * h_cn
    return v_esf + v_cn

def a_slds( r_esf = float, r_cn = float, h_cn = float ) ->  float:
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

# Las abreviaturas usadas son: per = perímetro, r = radio, ar = área, 
# circu = círculo, rtg = rectángulo fgs = figuras, sum = suma
# a = altura rectángulo y b = base rectángulo.

def ar_per_fgs( r_circu = float, a_rtg = float, b_rtg = float ) ->  float:
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


# Las abreviaturas usadas son: ct = cantidad, crn = carne, gna = gallina y
# pto = pollito

def ct_crn_aves(ct_gna = float, ct_gallo = float, ct_pto = float) ->  float:
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


#Las abreviaturas usadas son: v = valor, p = panes, l = leche, h = huevos

def mandado(p = float, l = float, h = float, billete = float) ->  float:
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


#Las abreviaturas usadas son: ti = tasa de interés y m = meses

def prestamo( capital = float, ti = float, m = float) ->  float:
    val_prestamo = capital * (1 + ti)**m
    return val_prestamo

if __name__ == "__main__":
    capital = float(input("Ingrese el capital inicial"))
    ti = float(input("Ingrese la tasa de interés"))
    m = float(input("Ingrese cantidad de meses a la que se realizó el préstamo"))
    val_prestamo = prestamo(capital, ti, m)
    print("El valor del préstamo es " + str(val_prestamo))


#Las abreviaturas usadas son: d = días, c = casos y enf= enfermos

def contagios( enf = int, d = int) ->  int:
    total_contagios = enf * (2)**d
    return total_contagios

if __name__ == "__main__":
    enf = int(input("Ingrese la cantidad de enfermos actuales"))
    d = int(input("Ingrese cantidad de días a estimar número de enfermos"))
    c_enf_totales= contagios(enf, d)
    print("Los días a estimar la cantidad de enfermos son " + str(d))
    print("El número de personas contagiados será " + str(c_enf_totales))


from functools import reduce

# Se definen funciones

def promedio(a : float, b : float, c : float, d : float, e : float) -> float:
    return (a + b + c + d + e) / 5

def mediana(a : float, b : float, c : float, d : float, e : float):
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



