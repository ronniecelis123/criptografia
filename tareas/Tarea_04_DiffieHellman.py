def es_raiz_primitiva(g, p):
    """Verifica si g es una raíz primitiva módulo p"""
    conjunto_requerido = set(num for num in range(1, p))
    conjunto_generado = set(pow(g, pot, p) for pot in range(1, p))
    return conjunto_requerido == conjunto_generado

def diffie_hellman(p, g, secreto1, secreto2):
    valor1 = pow(g, secreto1, p)
    valor2 = pow(g, secreto2, p)

    clave_compartida1 = pow(valor2, secreto1, p)
    clave_compartida2 = pow(valor1, secreto2, p)

    return valor1, valor2, clave_compartida1, clave_compartida2

p = int(input("Ingresa un número primo p: "))
g = int(input("Ingresa un número g (posible raíz primitiva de p): "))

if es_raiz_primitiva(g, p):
    print(f"{g} es una raíz primitiva módulo {p}")
else:
    print(f"{g} NO es una raíz primitiva módulo {p}. El algoritmo aún puede funcionar, pero puede no ser seguro.")

secreto1 = int(input("Ingresa el secreto privado 1: "))
secreto2 = int(input("Ingresa el secreto privado 2: "))


valor1, valor2, clave1, clave2 = diffie_hellman(p, g, secreto1, secreto2)

print("\n--- Intercambio de claves ---")
print(f"Valor público 1: {valor1}")
print(f"Valor público 2: {valor2}")
print(f"Clave compartida (1): {clave1}")
print(f"Clave compartida (2): {clave2}")
