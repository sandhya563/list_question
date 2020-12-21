num=int(input(""))
index=1
z=1
while index<=num:
    if index%2==0:    
        counter=1
        k=index+z-1
        while counter<=index:
            print(k,end=" ")
            counter=counter+1
            k=k-1
            z=z+1
        print()
    else:
        y=1
        k=z
        while y<=index:
            print(k,end=" ")
            y=y+1
            z=z+1
            k=k+1
        print()
    index=index+1