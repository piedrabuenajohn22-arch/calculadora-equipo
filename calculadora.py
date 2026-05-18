def main():
    print ("Bienvenido a la calculadora de Big N!")
    print ("Elija una de las siguientes opciones a continuacion: ")
    print ("-----------------------------------")
    print ("1- Sumar           3- Multiplicar")
    print ("-----------------------------------")
    print ("2- Restar          4- Dividir")
    print ("-----------------------------------")

    opcion = input("Escriba: ")

    if opcion == "1":
        print ("Opcion: Suma")
        print ("-----------------------------")
        suma1 = float(input("Escriba el primer numero: "))
        suma2 = float(input("Escriba el segundo numero: "))

        ResultadoSuma = suma1 + suma2

        print ("El resultado de la suma es: ", ResultadoSuma)

    elif opcion == "2":
        print ("Opcion: Resta")
        print ("-----------------------------")
        resta1 = float(input("Escriba el primer numero: "))
        resta2 = float(input("Escriba el segundo numero: "))

        ResultadoResta = resta1 - resta2

        print ("El resultado de la resta es: ", ResultadoResta)

    elif opcion == "3":
        print ("Opcion: Multiplicacion")
        print ("-----------------------------")
        multi1 = float(input("Escriba el primer numero: "))
        multi2 = float(input("Escriba el segundo numero: "))

        ResultadoMulti = multi1 * multi2

        print ("El resultado de la multiplicacion es: ", ResultadoMulti)

    elif opcion == "4":
        print ("Opcion: División")
        print ("-----------------------------")
        dividir1 = float(input("Escriba el primer numero: "))
        dividir2 = float(input("Escriba el segundo numero: "))

        ResultadoDivision = dividir1 / dividir2

        print ("El resultado de la división es: ", ResultadoDivision)

    else:
        print ("Error, numero equivocado")


    if name == "main":
        main()
