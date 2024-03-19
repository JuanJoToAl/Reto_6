import funciones

#Las abreviaturas usadas son: ti = tasa de interés y m = meses

if __name__ == "__main__":
    capital = float(input("Ingrese el capital inicial"))
    ti = float(input("Ingrese la tasa de interés en formato decimal"))
    m = float(input("Ingrese cantidad de meses a la que se realizó el préstamo"))
    prestamo = funciones.prestamo(capital, ti, m)
    print("El valor del préstamo es " + str(round(prestamo, 3)))