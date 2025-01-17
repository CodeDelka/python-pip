import random

opciones = ("piedra", "papel", "tijera")

rounds = 1
while True: 
    print('*' * 10)
    print("ROUND", rounds)
    print('*' * 10)
    
    usuario = input("\nBienvenido al juego piedra, papel o tijera:  \n1: Tijera \n2: Papel \n3: Piedra \nElija => ")
    usuario = usuario.lower()
    
    pc = random.choice(opciones)

    if usuario not in opciones:
        print("Esa opción no es válida")
    else:
        if usuario == pc:
            print(f"El usuario ha elegido {usuario} y la CPU ha sacado {pc}, entonces han empatado")
        elif (usuario == "tijera" and pc == "papel") or (usuario == "papel" and pc == "piedra") or (usuario == "piedra" and pc == "tijera"):
            print(f"El usuario ha elegido {usuario} y la CPU ha sacado {pc}, entonces ha ganado el usuario")
        else:
            print(f"El usuario ha elegido {usuario} y la CPU ha sacado {pc}, entonces ha ganado la CPU")
    
    rounds += 1

    # Opción para salir del bucle
    continuar = input("¿Quieres jugar otra ronda? (s/n): ").lower()
    if continuar != 's':
        break

print("Gracias por jugar!")