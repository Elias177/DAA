import math
import random
from itertools import chain
from collections import defaultdict

def papadimitriou(cPares):
    varSet = set(map(abs, chain(*cPares)))
    reps = int(math.log(len(varSet), 2))
    for i in range(reps):
        aux = {}
        for var in varSet:
            aux[var] = random.choice([True, False])
            aux[-var] = not aux[var]
        for j in range(2 * pow(len(varSet), 2)):
            cParesFalse = cFalseElegir(cPares, aux)
            if cParesFalse == []:
                return 1
            else:
                cElegida = random.choice(cParesFalse)
                varElegida = abs(random.choice(cElegida))
                aux[varElegida] = not aux[varElegida]
                aux[-varElegida] = not aux[varElegida]
    return 0


def cFalseElegir(cPares, aux):
    return [x for x in cPares if not (aux[x[0]] | aux[x[1]])]

def cReducir(cParesTodos):
    sVar = set()
    cVarDict = {} 
    varClaDict = defaultdict(set)
    for x, y in cParesTodos:
        varClaDict[x].add((x, y))
        varClaDict[y].add((x, y))
        cVarDict[(x,y)] = [x, y]
    while True:
        for var in sVar:
            for clausula in varClaDict[var].copy():
                del cVarDict[clausula]
                varClaDict[clausula[0]] -= set([clausula])
                varClaDict[clausula[1]] -= set([clausula])
        varReducida = set(chain(*cVarDict.values()))
        sVar = set([i for i in varReducida if -i not in varReducida])
        if sVar == set():
            break
    return set(cVarDict.keys())
 

def main():
    out = []
    for i in range(1, 7):
        cParesTodos = set()
        with open('2sat%s.txt' % i) as file_in:
            next(file_in)
            for line in file_in:
                x, y = map(int, line.strip().split(' '))
                cParesTodos.add((x, y))
        cParesReducidos = cReducir(cParesTodos)
        out.append(papadimitriou(cParesReducidos))
    return out


if __name__ == "__main__":
    print main()
