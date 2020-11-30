import random

''' Crea una lista con puertas cerradas segun el total
param: numeroTotal -> total de puertas requerido
retorna la lista de puertas cerradas''' 
def definirPuertas(numeroTotal):
    # Definimos la lista de puertas y la posicion en
    # la que colocaremos el premio.
    puertas = []
    
    # Insertamos el total de puertas con valor neutro.
    while (numeroTotal > 0):
        puertas.append(0)
        numeroTotal-=1
        
    # Retornamos el estado de todas las puertas.
    return puertas

''' Abre las puertas conviertiendolas en 1.
param: puertasPorAbrir -> numero de puertas que se desean abrir.
param: puertas -> lista de puertas cerradas.
param: usuario -> puerta que escogio el usuario
param: premio -> numero de puerta en el que se encuentra el premio
Retorna una lista con dos listas: la lista de puertas abiertas y cerradas y la 
lista de puertas abiertas. '''
def abrirPuertas(puertasPorAbrir, puertas, usuario, premio):
    return abrirPuertasAux(puertasPorAbrir, puertas,usuario, premio,  [])

''' Funcion auxiliar para abrirPuertas() ya que es recursiva.'''
def abrirPuertasAux(puertasPorAbrir, puertas, usuario, premio, abiertas):
    puertasTotales = len(puertas)
    
    # Escogemos una posicion random para abrir la puerta.
    ranInt = random.randrange(puertasTotales)
    
    if (puertasPorAbrir == 0):
        result = [puertas, abiertas]
        return result
    
    # Si el la puerta escogida no esta abierta ni es la que escogio el usuario ni
    # la que esconde el premio.
    elif not(ranInt in abiertas) and (ranInt != usuario) and (ranInt != premio):
        # Abrimos la puerta.
        abiertas.append(ranInt)
        puertas[ranInt] = 1
        puertasPorAbrir -= 1
        return abrirPuertasAux(puertasPorAbrir, puertas,usuario, premio, abiertas) 
    
    # De lo contrario escoja otro valor.
    else:
        return abrirPuertasAux(puertasPorAbrir, puertas,usuario, premio, abiertas) 
        
      
'''Se analiza si el usuario desea cambiar de puerta y se retorna el resultado del juego.
param: puertas -> lista de puertas
param: abiertas -> lista de puertas abiertas
param: cambiar -> booleano que indica si se debe realizar un cambio
param: premio -> numero de puerta donde se ubica el premio
param: usuario -> puerta del usuario
Retorna 1 o 0 indicando si gana o pierde.''' 
def cambioDePuerta(puertas, abiertas, cambiar, premio, usuario):
    # Si no queremos cambiar
    if (cambiar == 0):
        # Si la puerta del usuario no corresponde al premio
        if (usuario != premio):
            # Retornamos fracaso
            result = 0
        # Si la puerta del usuario corresponde al premio
        else:
            # Retornamos exito
            result = 1
            
    # Si el usuario desea cambiar       
    else:
        # Escogemos aleatoriamente una puerta cerrada 
        ranPuerta = cicloRan(abiertas, len(puertas), usuario)
        
        # Si la puerta corresponde al premio
        if (ranPuerta != premio):
            # Retornamos exito
            result = 0
        # Si la puerta no corresponde al premio
        else:
            # Retornamos fracaso
            result = 1
    
    return result

''' Funcion auxiliar para cambioPuerta. Busca una puerta cerrada para 
realizar el cambio de puerta.
param: lista -> lista de puertas abiertas
param: rango -> total de puertas
param: usuario -> puerta del usuario
Retorna la puerta a la que se realiza el cambio. '''
def cicloRan(lista, rango, usuario):
    # Escogemos un valor random para la puerta que queremos cambiar.
    ranInt = random.randrange(rango)
    
    # Si la puerta no esta entre las abiertas ni corresponde a la del usuario.
    if not(ranInt in lista) and (ranInt != usuario):
        # Retorno la puerta que escogimos
        return ranInt
    else:
        # De lo contrario sigale dandonle.
        return cicloRan(lista, rango, usuario)

''' Verifica que la puerta escogida para esconder el premio no este abierta
ni corresponda a la puerta del usuario.
param: abiertas -> lista de puertas abiertas.
param: puertasTotales -> el numero total de puertas.
Retorna la puerta en la que se ubica el premio'''
def verificarPremio(abiertas, puertasTotales):
    premio = random.randrange(puertasTotales)
    if not(premio in abiertas):
        return premio
    else:
        return verificarPremio(abiertas, puertasTotales)

'''Corre el ciclo de Monte Carlo para el caso de Monty Hall con n puertas.
param: casos -> total de casos que se desean evaluar.
param: puertasTotales-> el numero n de puertas totales que se desean.
param: puertasPorAbrir -> el numero de puertas que se desean abrir.
param: cambiar -> si se desea cambiar o no.'''
def MonteCarlo(casos, puertasTotales, puertasPorAbrir, cambiar):
    datos = []    
    
    while casos > 0:
        # Construimos las puertas
        puertas = definirPuertas(puertasTotales)
        
        # Escondemos un premio
        premio = random.randrange(puertasTotales)
        
        # El jugador escoge una puerta
        usuario = random.randrange(puertasTotales)
        
        # Abrimos una puerta
        conjuntoPuertas = abrirPuertas(puertasPorAbrir, puertas, usuario, premio)
        
        #Calculamos el resultado
        result = cambioDePuerta(conjuntoPuertas[0], conjuntoPuertas[1], cambiar, premio, usuario)
                
        #print(premio, usuario, conjuntoPuertas[0], cambiar, result)
        datos.append(result)
        casos -= 1
                
    print("cambiar", cambiar, Average(datos))
   
    
''' Funcion que calcula el promedio de los numeros en una lista'''
def Average(lst): 
    return sum(lst) / len(lst) 


numeroTotal = 3
porAbrir = 1
casos = 50000
cambiar = 1
MonteCarlo(casos, numeroTotal, porAbrir, cambiar)

