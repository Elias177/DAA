import time, itertools, math, exceptions

def distancia(c1, c2):
    return     math.sqrt((int(c2[1]) - int(c1[1]))**2 + (int(c2[2])-int(c1[2]))**2)

def valor(s):
    try:
        return int(s)
    except exceptions.ValueError:
        return float(s)

def ciudad(file_in):
    for line in file_in:
        try:
            p = line.split()
            if p[0].isdigit():
                c = [valor(p[0]), valor(p[1]), valor(p[2].strip('\n')), False]
                ciudades.append(c)
        except Exception as e:
            pass

def calcVecinoCercano(i):
    cercano = [-1, float("inf")]

    for index in range(len(ciudades)):
        if i == index or ciudades[index][3] == True:
            pass
        else:
            dis = distancia(ciudades[i], ciudades[index])
            if dis < cercano[1]:
                cercano = [index, dis]

    ciudades[cercano[0]][3] = True
    return cercano

def vecinoCercano(ciudades):
    d = []
    viaje = [[],0]
    primero = calcVecinoCercano(0)
    d.append(primero)
    siguiente = primero
    for index in range(1,len(ciudades)):
        actual = calcVecinoCercano(siguiente[0])
        d.append(actual)
        siguiente = actual

    for ele in d:
        viaje[1] += ele[1]
        viaje[0].append(ele[0])
    viaje[1] += distancia(ciudades[viaje[0][-1]],ciudades[viaje[0][0]])
    return viaje

ciudades = []
file_in = open('ca4663.tsp','r')
ciudad(file_in)
inicio = time.time()
viajeOptimo = vecinoCercano(ciudades)
fin = time.time()

print 'Problema del vendedor viajero hecho con un algoritmo del vecino mas cercano.'

print '\nHay %d ciudades en este viaje.\n' % (len(viajeOptimo[0]))   

print 'El recorrido optimo es: %s \nCosto: (%f)' % (viajeOptimo[0], viajeOptimo[1])
print '\nSe tomo %0.3f segundos para calcular el recorrido.' % (fin-inicio)