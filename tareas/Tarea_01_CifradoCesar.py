arreglo = [chr(i) for i in range(65, 91)]  
cifrado=[]
descifrado=[]
mensaje_cifrado=""
mensaje_descifrado=""

def cifrarMensaje(arreglo):
    n = int(input("Ingresa la clave: "))
    cadena = input("Ingresa la cadena: ")
    cifrado = []
    
    for letra in cadena:
        for j in range(len(arreglo)):
            if letra.upper() == arreglo[j]: 
                operacion_cifrado = (j + n) % len(arreglo)
                cifrado.append(arreglo[operacion_cifrado])
    
    mensaje_cifrado = "".join(cifrado)  
    return mensaje_cifrado

def descifrarMensaje(arreglo):
    n = int(input("Ingresa la clave: "))
    mensaje_cifrado = input("Ingresa el mensaje cifrado: ")
    descifrado = []
    
    for letra in mensaje_cifrado:
        for j in range(len(arreglo)):
            if letra.upper() == arreglo[j]:  
                operacion_descifrado = (j - n) % len(arreglo)
                descifrado.append(arreglo[operacion_descifrado])
    
    mensaje_descifrado = "".join(descifrado) 
    return mensaje_descifrado

def menu():
    while True:
        print("\nSelecciona una opción:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Salir")
        
        opcion = input("Opción: ")
        
        if opcion == "1":
            print("\nMensaje cifrado:", cifrarMensaje(arreglo))
        elif opcion == "2":
            print("\nMensaje descifrado:", descifrarMensaje(arreglo))
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")


menu()
