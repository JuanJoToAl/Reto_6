import funciones
if __name__ == "__main__":
    r_esf = float(input("Ingrese el valor del radio de la esfera"))
    r_cn = float(input("Ingrese el valor del radio del cono"))
    h_cn = float(input("Ingrese el valor de la altura del cono"))
    volums = funciones.v_slds(r_esf, r_cn, h_cn)
    areas = funciones.a_slds(r_esf, r_cn, h_cn)
    print("La suma de los volúmenes es " + str(round(volums, 3)))
    print("La suma de las áreas es " + str(round(areas, 3)))