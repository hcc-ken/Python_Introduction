from caja import muestra_caja

RESET = "\033[0m"
ROJO = "\033[31m"
VERDE = "\033[32m"

def _es_par(numero:int)->bool:
    return numero % 2 == 0

def mostrar_resultado(valor:int):
    if _es_par(valor):
        muestra_caja(f"{VERDE}El nu mero {valor} es par{RESET}")
    else:
        muestra_caja(f"{ROJO}El nu mero {valor} es impar{RESET}")

def main():
    cadena = muestra_caja("Dime un nu mero: ", "Pregunta")
    numero = int(input(cadena))
    mostrar_resultado(numero)

if __name__ == "__main__":
    main()