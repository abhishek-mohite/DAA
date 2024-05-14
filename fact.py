# def fact(n):

#     ans = 1
#     for i in range(1,n+1):
#         ans = ans*i

#     return ans

# print(fact(5))

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

print(fact(5))
