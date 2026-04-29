def muestra_caja(texto: str, titulo: str = ""):
    # Convertimos todo a string por si acaso
    texto = str(texto)
    titulo = str(titulo)

    # Calculamos el ancho de la caja según el contenido más largo
    contenido = [texto]
    if titulo:
        contenido.append(titulo)

    ancho = max(len(linea) for linea in contenido)

    # Parte superior
    print("+" + "-" * (ancho + 2) + "+")

    # Título (si existe)
    if titulo:
        print(f"| {titulo.ljust(ancho)} |")
        print("+" + "-" * (ancho + 2) + "+")

    # Texto principal
    print(f"| {texto.ljust(ancho)} |")

    # Parte inferior
    print("+" + "-" * (ancho + 2) + "+")