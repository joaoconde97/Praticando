import random

name = input("Seja bem vindo, qual o seu nome? ")

print(f"Olá {name}, boa sorte!")

lista_palavras = [
    "girassol", 
    "enigma", 
    "efemero", 
    "cafune", 
    "neblina", 
    "quimera", 
    "alcateia", 
    "sussurro", 
    "zenite", 
    "piquenique"
]

palavra = random.choice(lista_palavras)

print("Adivinhe as letras")

chutes = ""
tentativas = 12

while tentativas > 0:

    erros = 0

    for char in palavra:
        if char in chutes:
            print(char, end=" ")
        else:
            print("_")
            erros += 1

    if erros == 0:

        print()
        print("Você ganhou, parabéns!")
        print(f"A palavra é: {palavra}")
        break

    print()
    chute = input("Adivinhe uma letra ")
    chutes += chute

    if chute not in palavra:

        tentativas -= 1
        print("Errado")
        print(f"Você tem apenas, {tentativas} tentativas.")

        if tentativas == 0:
            print("Você perdeu.")
    