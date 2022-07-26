 def solution(N):
    x=format(N, 'b')
    res = [int(u) for u in str(x)]  
    index=[]  
    c=[]
    index=[i for i, e in enumerate(res) if e == 1]
    for i in range(len(index)):
        if index[i]-index[i-1] >1:
            c.append(index[i]-index[i-1]-1)
        else:
            pass
    if len(c)==0:
        return 0
    else:
        return max(c)

print(solution(529))
