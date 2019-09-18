def damage(n_x, g_dmg, i_h):
    tf = []
    for i in g_dmg:
        if(i<=0):
            tf.append(False)
        else:
            tf.append(True)
    if(any(tf)):
        return -1
    else:
        h = i_h
        count = 0
        while(h>0):
            i = g_dmg.index(max(g_dmg))
            h = h-n_x[i][0]+n_x[i][1]
            count += 1
        return count
 
 
queries = input()
 
for i in range(int(queries)):
    itrs = list(map(int, input().split()))
    it = itrs[0]
    i_h = itrs[1]
    n_x = [list(map(int, input().split())) for i in range(it)]
    
    dmg = [(i[0]-i[1]) for i in n_x]
    
    print(damage(n_x, dmg, i_h))
