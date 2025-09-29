import random

# Lista de palabras temática ; equipos de futbol 
palabras = ["marsella", "river", "racing", "brown", "levante", "chelsea", "rayados", "barcelona", "psg"]

# Función para elegir una palabra aleatoria
def elegir_palabra():
    return random.choice(palabras)

# Función principal del juego
def jugar_ahorcado():
    palabra = elegir_palabra()
    letras_adivinadas = []  # Letras que el jugador ya adivinó
    letras_usadas = []      # Letras que el jugador ya usó
    intentos = 6            # Número de intentos permitidos

    print("Bienvenido al ahorcado")
    print("La temática es: equipos de fútbol.")
    print("🎩")
    print(" O")
    print("/|\\ ")
    print("/ \\ ")

    # Bucle del juego (6 intentos)
    while intentos > 0:
        # Mostrar estado actual de la palabra
        estado = ""
        for letra in palabra:
            if letra in letras_adivinadas:
                estado += letra + " "
            else:
                estado += "_ "
        print("\nPalabra: ", estado.strip())
        
        # Verificar si el jugador ganó
        if all(letra in letras_adivinadas for letra in palabra):
            print("Felicidades, adivinaste la palabra crack:", palabra)
            print("( ͡° ͜ʖ ͡°)")
            break
        
        # Mostrar letras ya usadas
        if letras_usadas:
            print("Letras ya ingresadas:", ", ".join(letras_usadas))
        print(f"Te quedan {intentos} intentos.")

        # Pedir una letra
        intento = input("Ingresa una letra: ").lower()
        
        # Validar que sea una sola letra
        if len(intento) != 1 or not intento.isalpha():
            print("Por favor ingresa solo una letra válida.")
            continue
        
        # Verificar si ya se usó esa letra
        if intento in letras_usadas:
            print("Ya habías usado esa letra, probá con otra.")
            print("Letras ya ingresadas:", ", ".join(letras_usadas))
            continue
        
        # Agregar la letra a la lista de letras usadas
        letras_usadas.append(intento)

        # Si la letra está en la palabra, también se agrega a adivinadas
        if intento in palabra:
            letras_adivinadas.append(intento)
            print("Adivinaste una letra correctamente.")
        else:
            intentos -= 1
            print("Esa letra no está en la palabra. Intenta de nuevo.")

    # Si se quedó sin intentos
    if intentos == 0:
        print("\nHas perdido. La palabra era:", palabra)
        print("🤦‍♂️╾━╤デ╦︻")

# Ejecutar el juego
if __name__ == "__main__":
    jugar_ahorcado()
