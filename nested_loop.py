building=['floor1','floor2']
room=[1,2,3]
for floor in building:
    for j in room:
        print(j)
        
building=['floor1','floor2']
room=[1,2,3]
for floor in building:
    for j in room:
        if j==1 or j==3:
            continue
    