list=[2,4,6],[9,4,3],[2,4,3]
sum1=0
sum2=0
i=0
while i<len(list):
    sum1=sum1+list[i][i]
    sum2=sum2+list[i][2-i]
    i=i+1
if sum1==sum2:
    print("megic squaru hai")
else:
    print("not megic squaru")