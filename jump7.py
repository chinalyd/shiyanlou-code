for n in range(100):
    if n%7==0 or n%10==7 or n==0 or int(n/10)==7:
        continue
    print(n)
