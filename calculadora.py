# Funcion para pedir un numero al usuario y validarlo.
def pedir_numero(mensaje):
    # Bucle infinito hasta que el usuario escriba un numero valido.
    while True:
        # Muestra el mensaje recibido y guarda lo que escribe el usuario.
        entrada = input(mensaje)
        try:
            # Convierte la entrada a decimal y la regresa si es correcta.
            return float(entrada)
        except ValueError:
            # Se ejecuta si no se puede convertir a numero.
            print("Entrada invalida. Escribe un numero.")


# Funcion que muestra las opciones disponibles de la calculadora.
def mostrar_menu():
    # Titulo del menu.
    print("\n--- CALCULADORA ---")
    # Opciones de operaciones.
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicacion")
    print("4) Division")
    # Opcion para terminar el programa.
    print("5) Salir")


# Funcion principal que controla el flujo de la calculadora.
def calcular():
    # Bucle principal: se repite hasta que el usuario elija salir.
    while True:
        # Muestra el menu en cada vuelta.
        mostrar_menu()
        # Pide una opcion y elimina espacios extra al inicio/final.
        opcion = input("Elige una opcion (1-5): ").strip()

        # Si el usuario elige "5", se termina el programa.
        if opcion == "5":
            print("Saliendo de la calculadora. Hasta luego.")
            break

        # Verifica que la opcion sea una de las operaciones validas.
        if opcion not in {"1", "2", "3", "4"}:
            print("Opcion invalida. Intenta de nuevo.")
            # Vuelve al inicio del bucle sin hacer calculos.
            continue

        # Pide los dos numeros para realizar la operacion.
        numero1 = pedir_numero("Ingresa el primer numero: ")
        numero2 = pedir_numero("Ingresa el segundo numero: ")

        # Realiza la operacion segun la opcion elegida.
        if opcion == "1":
            resultado = numero1 + numero2
            operacion = "suma"
        elif opcion == "2":
            resultado = numero1 - numero2
            operacion = "resta"
        elif opcion == "3":
            resultado = numero1 * numero2
            operacion = "multiplicacion"
        else:
            # Validacion para evitar division entre cero.
            if numero2 == 0:
                print("No se puede dividir entre cero.")
                # Regresa al menu si el divisor es cero.
                continue
            resultado = numero1 / numero2
            operacion = "division"

        # Muestra el resultado de la operacion realizada.
        print(f"El resultado de la {operacion} es: {resultado}")


# Punto de entrada: ejecuta la funcion principal al correr el archivo.
if __name__ == "__main__":
    calcular()
