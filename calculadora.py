def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Você não pode dividir por zero!"
    return a / b

def calculadora():
    print("=== Calculadora Simples de matemática ===")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")

    opcao = input("Escolha uma opção (1/2/3/4): ")

    if opcao in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == '1':
            print(f"Resultado: {num1} + {num2} = {somar(num1, num2)}")
        elif opcao == '2':
            print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
        elif opcao == '3':
            print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
        elif opcao == '4':
            print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    calculadora()