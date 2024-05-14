def toh(n, from_rod, to_rod, aux):
    
    if n == 0:
        return
    
    toh(n-1, from_rod,aux,to_rod)
    print("Moved disk",n,"From Rod",from_rod,"To Rod",to_rod)

    toh(n-1,aux,to_rod,from_rod)

toh(4, "A","C","B")