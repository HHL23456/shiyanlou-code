for i in range(1,101):
    if i%7==0 or (i-7)%10==0:
        continue
    elif int(i/10)==7:
        continue
    print(i)
