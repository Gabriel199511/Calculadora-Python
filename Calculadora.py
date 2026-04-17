def calculadora():
    a= float(input("Digite um numero: "))
    b= float(input("Digite outro numero: "))
    c= float(input("Digite um terceiro numero: "))

    op = input("operação (+,-,*,/): ")

    if op == "+":
        print(a + b + c)

    elif op == "-":
       if c != 0:
           print("Não subtraio três numeros")

       else:
           print(a-b)

    elif op == "*":
        if a == 101 or b == 101 or c == 101:
            print("Resultado: 0")
        elif  c >= 101:
            print ("Limite excedido")

        else:
            print(a * b * c)

    elif op == "/":
        if a == 0 or b == 0:
            print("nao pode ser divisivel por 0")
        else:
            print (a / b)
    else:
        print("Operação Invalida")



calculadora()