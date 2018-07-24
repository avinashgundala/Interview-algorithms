#dynamic programming based on python 
#returns maximum profit that can be get on knapsack with capacity W
#W = capacity of knapsack,w=list of weight of item,p = list of profit of weights
#n = length of the list of weights or profit
#time complexity is O(nW)

def krushkal(w,p,W)
n = len(w)
v = [[0 for i in range(0,W+1)] for j in range(0,n+1)]
for i in range(0,n+1):
    for j in range(0,W+1):
        if i == 0 or j == 0:
            v[i][j]= 0
        elif j < w[i]:
            v[i][j] = v[i-1][j]
        else:
            v[i][j] = max(v[i-1][j],v[i-1][j-w[i]]+p[i])
return v[n][W]            
            
