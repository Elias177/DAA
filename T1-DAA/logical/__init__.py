lisPais = []
dicVecinos = {}
dicVisitados = {}
lisColores = ['Rojo','Azul', 'Amarillo', 'Verde']

europa = open('paises.txt', 'r')

for l in europa:
    lineas = []
    for x in l.split():
        lineas.append(x)
    dicVecinos.update({lineas[0]: lineas[1:]})
    
for p in dicVecinos.keys():
    lisPais.append(p)
    
def vecino(p, c):
    for v in dicVecinos.get(p):
        colActual = dicVisitados.get(v)
        if colActual == c:
            return False
    return True

for p in lisPais:
    for c in lisColores:
        if vecino(p, c):
            dicVisitados[p] = c
            
for k in dicVisitados:
    print(k, dicVisitados[k])