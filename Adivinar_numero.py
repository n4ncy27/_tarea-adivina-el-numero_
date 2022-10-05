# Este es el juego de adivinar el número.

# Variables
número=33 # número que se desea adivinar 
control=0 # variable de control del ciclo
intentos=1 #Controlar los intentos

print("------------------------------------")
print("------------¡¡¡HOLA!!!--------------")
print("-Este es el juego adivina un número-")

while(control==0):
    print("Intento número: ",intentos)
    print(" Digite un número: ")
    num = int(input()) # solicitamos un numero para comparar
    if(num==número):
        print("------------------------------------")
        print("-------¡ADIVINASTE EL NUMERO!-------")
        print("------------------------------------")
        print("Utilizaste",intentos,"intentos")
        print("----------¡FIN DEL JUEGO!----------")
        print("------------------------------------")
        control=1
    elif(num > número ):
        print("El número ingresado es MAYOR, intenta nuevamente")
        intentos+=1
    elif(num < número ):
        print("El número ingresado es MENOR, intenta nuevamente")
        intentos+=1