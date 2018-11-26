aris = [map(int, x.split(' ')) for x in open('clustering1.txt', 'r').read().split('\n')[1:-1]]

aris.sort(key=lambda x: x[2])

verts = {}
for ari in aris:
    verts[ari[0]] = ari[0]
    verts[ari[1]] = ari[1]

costos = {}
for v in verts:
    costos[v] = 0

cClusters = len(verts)

for ari in aris:
    h1 = verts[ari[0]]
    while verts[h1] != h1:
        h1 = verts[h1] 

    head2 = verts[ari[1]]
    while verts[head2] != head2:
        head2 = verts[head2] 

    if h1 != head2:
        if cClusters <= 4:
            distancia = ari[2]
            break
        verts[head2] = h1
        costos[h1] += (ari[2] + costos[head2])
        cClusters -= 1

print 'La distancia es: %d' % (distancia)