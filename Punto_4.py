import funciones

# Las abreviaturas usadas son: p = panes, l = leche, h = huevos

if __name__ == "__main__":
    p = float(input("¿Cuántos panes dijo mamá?"))
    l = float(input("¿Cuánta leche dijo mamá?"))
    h = float(input("¿Cuántos huevos dijo mamá?"))
    billete = float(input("¿Cuánta plata me dio mamá?"))
    cambio = funciones.mandado(p, l, h, billete)
    if cambio >= 0:
        print("Las vueltas son " + str(cambio))
    else: 
        print("Pailas doña Mariluz, le quedo debiendo " + str(cambio))