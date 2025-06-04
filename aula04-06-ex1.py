n1 = 0
n2 = 0
resultado = 0
resultado_menos1 = 0

def somar_numeros(numero1, numero2):
    resultadoLocal = numero1 + numero2
    return resultadoLocal, resultadoLocal - 1

n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))
resultado, resultado_menos1 = somar_numeros(n1,n2)
print(f"A soma dos numeros é: {resultado}")
print(f"A soma dos numeros é: {resultado_menos1}")