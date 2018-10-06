N = int(input())

if (N > 0 and N < 101): # The range of N must be within 1-100
    if N % 2 != 0: # if N is ODD
        print("Weird") # Prints weird
    else: # N is even 
        if N > 1 and N < 6: # Inclusive range of 2-5
            print("Not Weird") # Prints not weird
        elif N > 5 and N < 21: # Inclusive rnage of 6-20
            print("Weird")
        else: # all the rest
            print("Not Weird")
