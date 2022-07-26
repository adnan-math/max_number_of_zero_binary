 def solution(N):
    x=format(N, 'b')
   #format function takes a number and convert it into binary, you can also use bin() dunction
    res = [int(u) for u in str(x)]  
    # convert a integer into list
    index=[]  
    c=[]
    index=[i for i, e in enumerate(res) if e == 1]
    #ind the index/address for each 1's in the list
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
