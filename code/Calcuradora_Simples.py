
def start():
    print("\n******************* Python Calculator *******************")
    print("Selecione o número da operação desejada:\n")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

def calcular(option, num1, num2 ):
    print("\n")
    if option == 1 :
        print("%s + %s = %r" %(num1, num2,num1 + num2))
    elif option == 2 :
        print("%s - %s = %r" %(num1, num2,num1 - num2))
    elif option == 3 :
        print("%s * %s = %r" %(num1, num2,num1 * num2))
    elif option == 4 :
        print("%s / %s = %r" %(num1, num2,num1 / num2))
    else:
        print("\nOpção Inválida!")


start()

option = int(input("\nDigite sua opção (1/2/3/4): "))
num1   = int(input("\nDigite o primeiro número: "))
num2   = int(input("\nDigite o segundo número: "))

calcular(option,num1,num2)

