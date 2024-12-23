def oddeve(lr, ur) :
    mtlist=[]
    for i in range (lr, ur + 1) :
        mtlist.append(i**2)
    leven=[]
    lodd=[]
    for i in mtlist :
        if i%2==0 :
            leven.append(i)
        else :
            lodd.append(i)
    print("list of even squares : ", leven)
    print("list of odd squares : ", lodd)
lr=int(input("enter a lower range : "))
ur=int(input("enter an upper range : "))
oddeve(lr, ur)
