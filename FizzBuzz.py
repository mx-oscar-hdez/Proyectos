# Ejercicio B: FizzBuzz con repeticion hasta que el usuario escriba "salir".
while True:  # Repite el programa indefinidamente.
    a = input("Numero o 'salir': ")  # Lee un valor como texto.

    if a == "salir":  # Si el usuario quiere terminar...
        break  # ...sale del ciclo y finaliza el programa.

    a = int(a)  # Convierte la entrada de texto a numero entero.
    b = "Fizz"  # Texto para multiplos de 3.
    c = "Buzz"  # Texto para multiplos de 5.
    d = "Error"  # Texto para valores fuera del rango.

    if (a < 1):  # Valida limite inferior del rango.
        print(d)  # Muestra error si es menor que 1.
    elif (a > 50):  # Valida limite superior del rango.
        print(d)  # Muestra error si es mayor que 50.
    elif (a % 3 == 0) and (a % 5 == 0):  # Multiplo de 3 y de 5.
        print(b+c)  # Imprime FizzBuzz.
    elif (a % 3 == 0):  # Multiplo solo de 3.
        print(b)  # Imprime Fizz.
    elif (a % 5 == 0):  # Multiplo solo de 5.
        print(c)  # Imprime Buzz.
    else:  # Si no es multiplo de 3 ni de 5.
        print(a)  # Imprime el numero original.