import random

def hashtag():
    print()
    print("#" * 135)
    print()
    
tentativas = 0
palpite = 0

hashtag()
print("Seja bem vindo ao jogo Advinhe o Número, você possui ilimitadas tentativas de adivinhar mas quanto menos tentativas melhor. Vamos lá!")
hashtag()


minimo = int(input("Comece escolhendo o número inicial: "))
maximo = int(input("Agora escolha o número final: "))

hashtag()
print(f"Muito bem, o número secreto estara entre {minimo} e {maximo}, palpite com sabedoria!")

numero_secreto = (random.randint(minimo, maximo))

print("Tudo pronto!")
print()

while numero_secreto != palpite:
    tentativas += 1

    print()
    palpite = int(input("Insira o seu palpite: "))

    if palpite > numero_secreto:
        print("Palpite muito alto!")
    
    elif palpite < numero_secreto:
        print("Palpite muito baixo!")
    
    elif palpite == numero_secreto:
        if tentativas <= 10:
            print(f"Parabéns, seus palpites estão afiados você descobriu o número secreto com apenas {tentativas} palpites!")
            print()

        elif tentativas > 10 and tentativas < 15:
            print(f"Muito bem, você acertou o número secreto com {tentativas} palpites, continue assim.")
            print()

        elif tentativas > 15:
            print(f"Você acertou o número secreto com {tentativas} palpites, precisamos afiar mais esses palpites ;P!")
            print()
