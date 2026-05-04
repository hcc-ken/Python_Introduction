# palabra = input("Introduzca un texto: ").split()
# longitud = len(palabra)

# linea = "-" * (longitud + 4)
# print(linea)

# for p in palabra:
#     print(f"| {p.ljust(longitud)} |")
#     print(linea)

# Ejercicios dos

# try:
#     numero = -1
#     while numero != 0:
#         numero = int(input("Introduce un número: "))
#         if numero < 0:
#             print("El número no puede ser negativo")
#             continue

#         suma = 0
#         for i in range(1, numero + 1):
#             suma += i
#         print(suma)
# except ValueError:
#     print("El número no puede ser negativo.")

palabra = input("Introiduzca una palabra: ")
invertida = ""

for letra in palabra:
    invertida = letra + invertida

if palabra == invertida:
    print("Es palíndromo")
else:
    print("No es palíndromo.")