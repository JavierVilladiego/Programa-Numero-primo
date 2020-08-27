def Primo():
    numero=  int(input("Por favor digite un numero: "))
    contador=0
    for i in range (1, numero+1):
        if numero%i==0:
            contador += 1
    if contador == 2:
        print ( "El numero digitado ES PRIMO")
    else: 
        print ("El numero digitado NO ES PRIMO")

    return()

def main():
    Primo()

if __name__ == "__main__":
    main()