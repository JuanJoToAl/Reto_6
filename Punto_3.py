import funciones

# Las abreviaturas usadas son: ct = cantidad, car = carne, gna = gallina y
# pto = pollito

if __name__ == "__main__":
    ct_gna = float(input("Ingrese la canidad de carne de gallina en kg"))
    ct_gallo = float(input("Ingrese la canidad de carne de gallo en kg"))
    ct_pto = float(input("Ingrese la canidad de carne de pollito en kg"))
    car_gna, car_gallo, car_pto = funciones.ct_crn_aves(ct_gna, ct_gallo, ct_pto)
    print("La cantidad de carne de gallina es " + str(car_gna) + "kg")  
    print("La cantidad de carne de gallo es " + str(car_gallo) + "kg") 
    print("La cantidad de carne de pollito es " + str(car_pto) + "kg")