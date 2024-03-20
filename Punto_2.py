import funciones

# Las abreviaturas usadas son: per = perímetro, r = radio, ar = área, 
# circu = círculo, rtg = rectángulo fgs = figuras, sum = suma
# a = altura rectángulo y b = base rectángulo.

if __name__ == "__main__":
    r_circu = float(input("Ingrese el valor del radio del círculo"))
    a_rtg = float(input("Ingrese el valor de la altura del rectángulo"))
    b_rtg = float(input("Ingrese el valor de la base del rectángulo"))
    sum_ar, sum_per = funciones.ar_per_fgs(r_circu, a_rtg, b_rtg)
    print("La suma de los volúmenes es "  + str(round(sum_ar, 3)))
    print("La suma de las áreas es " + str(round(sum_per, 3)))