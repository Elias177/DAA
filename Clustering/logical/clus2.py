verts = ["".join(x.split(' ')) for x in open('clustering2.txt', 'r').read().split('\n')[1:-1]]

def invBit(bit):
    if bit != '0' and bit != '1':
        raise ValueError
    return '1' if bit == '0' else '0'

def sim(v):
    o = []
    for i in range(len(v)):
        o.append(v[:i]+invBit(v[i]) + v[i+1:])
        for j in range(i+1, len(v)):
            o.append(v[:i]+invBit(v[i])+v[i+1:j]+invBit(v[j])+v[j+1:])
    return o
 
hs = {}
for v in verts:
    hs[v] = v
clus = len(hs) 
for v in verts:
    v_head = hs[v]
    while hs[v_head] != v_head:
        v_head = hs[v_head]

    for f in sim(v):
        if hs.get(f):
            h = hs[f]
            while hs[h] != h:
                h = hs[h]
            if v_head != h:
                hs[h] = v_head
                clus -= 1
print 'El valor mas grande es: %d' % (clus)