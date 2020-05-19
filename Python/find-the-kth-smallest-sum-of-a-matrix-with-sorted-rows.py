def kthSmallest(self, mat,k): 
  def twoArray(num1,num2,n1,n2,k):
    k=min(k,n1*n2)
    seen=set()
    h=[(num1[0]+num2[0],0,0)]
    heapq.heapify(h)
    res=[]
    while k:
        s,i,j=heapq.heappop(h)
        k-=1
        res.append(s)
        if i+1<n1 and (i+1,j) not in seen:
            seen.add(i+1,j)
            heapq.heappush(h,(num1[i+1]+num2[j],i+1,j))
        if j+1<n2 and (i,j+1) not in seen:
            seen.add(i,j+1)
            heapq.heappush(h,(num1[i]+num2[j+1],i,j+1))
    return res

    m=len(mat)
    arr1=mat[0]
    n1=len(arr1)   

    for i in range(1,m):
        res=twoArray(arr1,mat[i],n1,len(mat[i]),k)
    return res   
        
      
                                                          
