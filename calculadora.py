numero1 = input("digite o primeiro numero:")

numero2 = input("digite o segundo numero:")

numero1 = float(numero1)
numero2 = float(numero2)

operador = input("digite o operador (+, -, *, /):")

if operador == "+":
        print(f"o resultado é: {numero1 + numero2}")
elif operador == "-":
        print(f"o resultado é: {numero1 - numero2}")
elif operador == "*":
        print(f"o resultado é: {numero1 * numero2}")
elif operador == "/":
        print(f"o resultado é: {numero1 / numero2}")
else: print("operador invalido")