def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def calcular_factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    factorial = 1
    for i in range(2, numero + 1):
        factorial *= i
    return factorial

def es_palindromo(frase):
    frase = frase.replace(" ", "").lower()
    return frase == frase[::-1]

def mostrar_menu():
    print("\nMenú de Opciones:")
    print("1. Número Primo")
    print("2. Factorial")
    print("3. Palíndrome")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            numero = int(input("Ingrese un número entre 1 y 15: "))
            if 1 <= numero <= 15:
                if es_primo(numero):
                    print(f"El número {numero} es primo.")
                else:
                    print(f"El número {numero} no es primo.")
            else:
                print("El número ingresado está fuera del rango permitido.")
        elif opcion == '2':
            numero = int(input("Ingrese un número positivo entre 3 y 10: "))
            if 3 <= numero <= 10:
                factorial = calcular_factorial(numero)
                print(f"El factorial de {numero} es {factorial}.")
            else:
                print("El número ingresado está fuera del rango permitido.")
        elif opcion == '3':
            frase = input("Ingrese una frase: ")
            if es_palindromo(frase):
                print(f"La frase '{frase}' es un palíndromo.")
            else:
                print(f"La frase '{frase}' no es un palíndromo.")
        elif opcion == '4':
            print("Gracias por usar el programa. Autor: Chiko Tinder")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    main()
