import funciones

if __name__ == "__main__":
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    d = float(input("Ingrese el cuarto número: "))
    e = float(input("Ingrese el quinto número: "))
    prom = funciones.promedio(a, b, c, d, e)
    print("El promedio es:", prom)

    
if __name__ == "__main__":
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    d = float(input("Ingrese el cuarto número: "))
    e = float(input("Ingrese el quinto número: "))
    med = funciones.mediana(a, b, c, d, e)
    print("La mediana es:", med)


if __name__ == "__main__":
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    d = float(input("Ingrese el cuarto número: "))
    e = float(input("Ingrese el quinto número: "))
    pro_med = funciones.promedio_multiplicativo(a, b, c, d, e)
    print("El promedio multiplicativo es:", round(pro_med, 3))


if __name__ == "__main__":
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    d = float(input("Ingrese el cuarto número: "))
    e = float(input("Ingrese el quinto número: "))
    orden_asc = funciones.ord_asce(a, b, c, d, e)
    print("Los números en orden ascendente son:", orden_asc)


if __name__ == "__main__":
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    d = float(input("Ingrese el cuarto número: "))
    e = float(input("Ingrese el quinto número: "))
    orden_desc = funciones.ord_desce(a, b, c, d, e)
    print("Los números en orden descendente son:", orden_desc)


if __name__ == "__main__":
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    d = float(input("Ingrese el cuarto número: "))
    e = float(input("Ingrese el quinto número: "))
    poten_m = funciones.poten(a, b, c, d, e)
    print("La potencia del número mayor elevado al número menor es:", poten_m)
    

if __name__ == "__main__":
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    d = float(input("Ingrese el cuarto número: "))
    e = float(input("Ingrese el quinto número: "))
    raiz_m = funciones.raiz(a, b, c, d, e)
    print("La raíz cúbica del número menor:", raiz_m)