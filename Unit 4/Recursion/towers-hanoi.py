DCHART = {}

def dchart(n,r1,r2,depth):
    global DCHART
    print(n,":",r1,"->",r2,depth)
    if depth in DCHART.keys():
        DCHART[depth].append(str(n)+r1+r2)
    else:
        DCHART[depth] = []
        DCHART[depth].append(str(n)+r1+r2)


def toh(n, r1, r2, r3, array, depth):
    if n == 1:
        array[r1].remove(n)
        array[r2].append(n)
        dchart(n,r1,r2,depth)
        return array
    toh(n-1, r1, r3, r2, array, depth+1) 
    dchart(n,r1,r2,depth)
    array[r1].remove(n)
    array[r2].append(n)
    toh(n-1, r3, r2, r1, array, depth+1)
    return array

def toh_factory(n):
    global DCHART
    towers = dict(
        A=[],
        B=[],
        C=[]
    )
    for i in range(n):
        towers['A'].append(n-i)
    return toh(n,'A','C','B',towers,0)


COUNT = 7

ret = toh_factory(COUNT)
print('\nResults\n=========================================')
print('Recursions: ',sum([2 ** i for i in range(COUNT)]))
for k in ret.keys():
    print(k,':',', '.join([str(i) for i in ret[k]]))
print('')
for k in range(len(DCHART.keys())):
    print(k,':',', '.join([str(i) for i in DCHART[k]]))