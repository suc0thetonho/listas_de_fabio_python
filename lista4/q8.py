cont  = 0

while(True):
    altura = float(input("DIGITE AQUI SUA ALTURA EM METROS: "))

    if(altura >= 1.20):
        cont+=1
    
    if(altura == 0):
        break

if(cont == 0):
    print("ninguém foi ao brinquedo, assim não havendo lucro")
elif(cont>1):
    total = cont*4.50
    lucro = total - 1000
    if(lucro < 1000):
        print(f"R$ {lucro} lucro\n"
              f"{cont} utilizaram o brinquedo\n"
              "não é viavel")
    elif(lucro > 1000):
        print(f"R$ {lucro} lucro\n"
              f"{cont} utilizaram o brinquedo\n"
              "é viavel")
    


