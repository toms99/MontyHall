import random

def init():
    '''puertasTotales = int(input("Inserta el total de puertas: "))
    puertasPorAbrir = int(input("Inserta el número de puertas por abrir: "))
    cambiar = bool(input("¿Desea que el usuario cambie la puerta? "))
    casos = int(input("¿Cuántos casos para Monte Carlo?: "))'''
    
    puertasTotales = 3
    puertasPorAbrir = 1
    cambiar = 1
    casos = 10
    MonteCarlo(casos, puertasTotales, puertasPorAbrir, cambiar)


def MonteCarlo(casos, puertasTotales, puertasPorAbrir, cambiar):
    datos = []
    while casos > 0:
        puertaUsuario = random.randrange(puertasTotales)
        puertas = definirPuertas(puertasTotales, puertaUsuario)
        result = abrirPuertas(puertasTotales, puertasPorAbrir, puertas, cambiar)
        datos.append(result)
        casos -= 1
    print("El censo: ", datos)
    print(Average(datos))

def Average(lst): 
    return sum(lst) / len(lst) 

def definirPuertas(numeroTotal, puertaUsuario):
    # Definimos la lista de puertas y la posicion en
    # la que colocaremos el premio.
    puertas = []
    premio = random.randrange(numeroTotal)
    
    # Insertamos el total de puertas con valor neutro.
    while (numeroTotal > 0):
        puertas.append(0)
        numeroTotal-=1
    puertas[premio] = 1
    
    # Si el premio se ubica en la misma puerta que desea abrir el 
    # usuario entonces lo identificamos con -3.
    if (premio == puertaUsuario -1):
        puertas[premio] = -3
    else:
    # Si no se ubican en la misma puerta entonces identificamos el
    # premio con 1 y la puerta del usuario con 3.
        puertas[premio] = 1
        puertas[puertaUsuario -1] = 3
        
    # Retornamos el estado de todas las puertas.
    return puertas
    

def abrirPuertas(puertasTotales, puertasPorAbrir, puertas, cambiar):
    # Definimos una lista de puertas abiertas.
    abiertas = []
    
    # Comenzamos a abrir las puertas utilizando posiciones random.
    while puertasPorAbrir > 0:
        # Escogemos una posicion random para abrir la puerta.
        ranInt = random.randrange(puertasTotales)
        
        # Verificamos que la posicion que escogimos no corresponda a
        # la puerta del usuario ni del premio.
        if puertas[ranInt] != 1 and puertas[ranInt] != 3 and puertas[ranInt] != -3:
            
            # Abrimos la puerta.
            abiertas.append(ranInt)
            puertas[ranInt] = 2
            puertasPorAbrir -= 1
    
    result = cambioDePuerta(puertas, abiertas, cambiar)
    return result

def cambioDePuerta(puertas, abiertas, cambiar):
    print("puertas sin cambio: ", puertas)
    result = -1
    
    # Si no queremos cambiar
    if (cambiar == 0):
        # Si la puerta del usuario no corresponde al premio
        if (3 in puertas):
            # Retornamos fracaso
            result = 0
        # Si la puerta del usuario corresponde al premio
        elif (-3 in puertas):
            # Retornamos exito
            result = 1
        else: result = -1
            
    # Si el usuario desea cambiar       
    else:
        # Escogemos aleatoriamente una puerta cerrada 
        print("puertas: ", puertas)
        print("abiertas: ", abiertas)
        ranPuerta = cicloRan(abiertas, len(puertas))
        print("ranPuerta: ", ranPuerta)
        
        # Si la puerta corresponde al premio
        if (puertas[ranPuerta] == 1):
            # Retornamos exito
            result = 1
        # Si la puerta no corresponde al premio
        else:
            # Retornamos fracaso
            result = 0
    
    return result


def cicloRan(lista, rango):
    ranInt = random.randrange(rango)
    if (ranInt in lista):
        return cicloRan(lista, rango)
    else:
        return ranInt
        
        
init()