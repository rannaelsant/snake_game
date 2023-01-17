print("Seja bem vindo á montanha russa do desespero")

quantidade_pessoas = int(input("Por favor digite a quantidade de pessoas: "))
idade = int(input("Por favor digite a sua idade: "))

if idade < 12:
    conta = 5
    print("Você pagará apenas 5 reais!")
elif idade <= 18:
    conta = 10
    print("Você pagará 10 reais!")
else:
    conta = 15
    print("Você pagará 15 reais!")

if quantidade_pessoas > 0:
    quantidade_pessoas *= conta
    print(quantidade_pessoas)

adicionar_fotos = input("Você vai querer adicionar alguma foto s/n? ")

if adicionar_fotos == "s":
    conta += 3
    print(f"Com o adicional de foto sua conta deu {conta}, reais.")
elif adicionar_fotos == "n":
    print("Ok, fechamos sua conta!")
else:
    print("Por favor digite uma entrada válida!")