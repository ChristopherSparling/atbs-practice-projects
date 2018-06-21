level = [1] 
results = {} 
 
for c in range(20):
    newlevel = set() 
    for x in level: 
        odd = (x-1)/3 if not (x-4)%6 else 0
        if odd > 1: 
            newlevel.add(odd) 
            results[odd] = int(x) 

        newlevel.add(x*2) 
        results[x*2] = int(x) 

    level = newlevel
print(level)
print(results)

 
 
 
 
 









