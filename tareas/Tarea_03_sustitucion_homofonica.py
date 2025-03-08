import random
CLAVES = {
    "A": ["0000000", "0000001"],
    "B": ["0000101", "0000110"],
    "C": ["0001010", "0001011"],
    "D": ["0001111", "0010000"],
    "E": ["0010100", "0010101"],
    "F": ["0011001", "0011010"],
    "G": ["0011110", "0011111"],
    "H": ["0100011", "0100100"],
    "I": ["0101000", "0101001"],
    "J": ["0101101", "0101110"],
    "K": ["0110010", "0110011"],
    "L": ["0110111", "0111000"],
    "M": ["0111100", "0111101"],
    "N": ["1000001", "1000010"],
    "Ñ": ["1000110", "1000111"],
    "O": ["1001011", "1001100"],
    "P": ["1010000", "1010001"],
    "Q": ["1010101", "1010110"],
    "R": ["1011010", "1011011"],
    "S": ["1011111", "1100000"],
    "T": ["1100100", "1100101"],
    "U": ["1101001", "1101010"],
    "V": ["1101110", "1101111"],
    "W": ["1110011", "1110100"],
    "X": ["1111000", "1111001"],
    "Y": ["1111101", "1111110"],
    "Z": ["0000010", "0000011"]
}

def verificar_unicidad():
    claves_usadas = set()
    for letra, binarios in CLAVES.items():
        if len(binarios) != 2:
            raise ValueError(f"La letra {letra} no tiene exactamente 2 claves.")
        for binario in binarios:
            if binario in claves_usadas:
                raise ValueError(f"Clave duplicada detectada: {binario} en la letra {letra}")
            claves_usadas.add(binario)

CLAVES_INVERSAS = {binario: letra for letra, binarios in CLAVES.items() for binario in binarios}

def cifrar(texto):
    texto = texto.upper()
    cifrado = []
    for letra in texto:
        if letra in CLAVES:
            cifrado.append(random.choice(CLAVES[letra]))
        else:
            cifrado.append(letra)  # Mantener espacios u otros caracteres sin cifrar
    return "".join(cifrado)  

def descifrar(cifrado):
    if len(cifrado) % 7 != 0:
        raise ValueError("El mensaje cifrado no tiene una longitud múltiplo de 7 bits.")
    binarios = [cifrado[i:i+7] for i in range(0, len(cifrado), 7)]
    texto = "".join(CLAVES_INVERSAS.get(b, "?") for b in binarios)
    
    return texto


def menu():
    while True:
        print("\nMenú:")
        print("1. Cifrar un mensaje")
        print("2. Descifrar un mensaje")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mensaje = input("Ingresa el mensaje a cifrar: ")
            cifrado = cifrar(mensaje)
            print("Mensaje cifrado:", cifrado)
        elif opcion == "2":
            cifrado = input("Ingresa el mensaje cifrado (sin espacios): ")
            try:
                descifrado = descifrar(cifrado)
                print("Mensaje descifrado:", descifrado)
            except ValueError as e:
                print("Error:", e)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

try:
    verificar_unicidad()
    menu()
except ValueError as e:
    print("Error en las claves:", e)
