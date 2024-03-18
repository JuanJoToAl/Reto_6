import funciones

#Las abreviaturas usadas son: d = días, tot = total y enf= enfermos

if __name__ == "__main__":
    enf= int(input("Ingrese la cantidad de enfermos actuales"))
    d = int(input("Ingrese cantidad de días a estimar número de enfermos"))
    tot_enfermos = funciones.contagios(enf, d)
    print("Los días a estimar la cantidad de enfermos son " + str(d))
    print("El número de personas contagiados será " + str(tot_enfermos))