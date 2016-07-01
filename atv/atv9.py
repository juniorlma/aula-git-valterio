#9
i=0
while True:
    p=int(input("Digite um numero:"))
    for v in range (i,p,p):
        somatoria=i+p
        media=somatoria/p
        total=p
        print(somatoria,media,total)
        if p < 0:
            print("Execursão negada")
        

