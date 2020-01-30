def toh(n, r1, r2, r3, array):
    if n == 1:
        print(n,":",r1,"->",r2)
        array[r1].remove(n)
        array[r2].append(n)
        return array
    toh(n-1, r1, r3, r2, array) 
    print(n,":",r1,"->",r2)
    array[r1].remove(n)
    array[r2].append(n)
    toh(n-1, r3, r2, r1, array)
    return array

def toh_factory(n):
    towers = dict(
        A=[],
        B=[],
        C=[]
    )
    for i in range(n):
        towers['A'].append(n-i)
    return toh(n,'A','C','B',towers)

    
ret = toh_factory(5)
print('\nResults\n=========================================')
for k in ret.keys():
    print(k,':',', '.join([str(i) for i in ret[k]]))
