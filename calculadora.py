print("=== Calculadora ===")
print("Digite 'sair' a qualquer momento para encerrar.")
print("Operações: +  -  *  /")

while True:
    num1 = input("Digite o primeiro número: ")
    if num1.lower() == "sair":
        break
    num1 = float(num1)
    operacao = input("Digite a operação (+, -, *, /): ")
    if operacao.lower() == "sair":
        break
    while True:
        num2 = input("Digite o segundo número: ")
        if num2.lower() == "sair":
            num2 = None
            break
        num2 = float(num2)
        if operacao == "/" and num2 == 0:
            print("Não é possível dividir por zero! Digite outro número.")
        else:
            break
    if num2 is None:
        break
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        resultado = num1 / num2
    else:
        print("Operação inválida!")
        continue
    if isinstance(resultado, float) and resultado.is_integer():
        print(f"Resultado: {int(resultado)}")
    else:
        print(f"Resultado: {resultado:.2f}")

    print("---")