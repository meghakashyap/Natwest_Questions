def nonDivisibleSubset(S,k):
    count = [0] * k

    for i in S:
        remainder = i % k
        count[remainder] +=1
    
    ans = min( count[0] , 1)         

    if k % 2 == 0:                    
        ans += min(count[k//2] ,1 )

    for i in range( 1 , k//2 + 1):    
        if i != k - i:           
            ans += max(count[i] , count[k-i])
    return ans

n,k = map(int,input("1.Enter the lenght of list 2.Enter the divisor: ").split())
S = list(map(int,input("Enter the elements of list : ").split(" ",n)))
print(nonDivisibleSubset(S,k))