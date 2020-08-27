numero=  int(input("Por favor digite un numero: "))
def Primo(numero):
    
    contador=0
    for i in range (1, numero+1):
        if numero%i==0:
            contador += 1
    if contador == 2:
        return True
    else: 
        return False

    

if Primo(numero)==True:
    print("El numero que digito ES PRIMO" )
else:
    print("El numero que digito NO ES PRIMO")
