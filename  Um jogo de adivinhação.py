import random

def jogo_adivinhacao():
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("O computador escolheu um número entre 1 e 100.")
    print("Você tem 10 tentativas para adivinhar o número corretamente.")
    
    numero_secreto = random.randint(1, 100)
    tentativas_restantes = 10
    
    while tentativas_restantes > 0:
        try:
            palpite = int(input("Insira seu palpite: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue
        
        if palpite < 1 or palpite > 100:
            print("Seu palpite deve estar entre 1 e 100.")
            continue

        if palpite == numero_secreto:
            print("Parabéns! Você adivinhou o número corretamente!")
            break
        elif palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        else:
            print("Muito alto! Tente novamente.")
        
        tentativas_restantes -= 1
        print(f"Você tem {tentativas_restantes} tentativas restantes.")
    
    if tentativas_restantes == 0:
        print(f"Que pena! Você não conseguiu adivinhar o número. O número era {numero_secreto}.")

# Executa o jogo
if __name__ == "__main__":
    jogo_adivinhacao()