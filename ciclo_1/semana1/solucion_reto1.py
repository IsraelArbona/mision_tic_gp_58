def CDT(usuario, capital,tiempo):
    porcentaje_interes = 0.03
    porcentaje_aperder = 0.02

    if tiempo > 2:
        valor_inte = (capital * porcentaje_interes * tiempo) / 12
        valor_total = capital + valor_inte
    else:
        valor_aperder = capital * porcentaje_aperder
        valor_total = capital - valor_aperder
    
    rta  = "Para el usuario " + str(usuario)
    rta += " La cantidad de dinero a recibir, según el monto inicial " + str(capital)
    rta += " para un tiempo de " + str(tiempo) 
    rta += " meses es: " + str(valor_total)

    return rta 

print(CDT("AB1012",1000000,3))