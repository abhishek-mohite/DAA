def ks(w, wt, val, n):
    
    if (w == 0 or  n==0):
        return 0
    
    if (wt[n-1] > w):
        return ks(w, ks, val, n-1)
    
    else:
        return max(val[n-1] + ks(w-wt[n-1], wt, val, n-1), ks(w , wt, val, n-1))



val = [60,100,120]
wt = [10,20,30]
n = len(val)

print(ks(50, wt, val, n))