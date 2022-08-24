"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
sexo = input("Digite F para Feminino ou M para Masculino: ")
if sexo == "F":
   sexo = sexo.strip().upper
    print("Feminino")
elif sexo == "M":
    sexo = sexo.strip().upper
    print("Masculino")
else:
    print("Sexo Inválido")
