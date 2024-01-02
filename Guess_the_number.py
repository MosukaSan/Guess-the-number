import random
import os

def main():
    print("Bem vindo ao adivinhe o número!")
    print("Digite qualquer coisa para continuar:")
    input()

    print("Escolha o intervalo:")
    numero_escolhido = int(input())
    numero_achar = random.randint(1, numero_escolhido)

    print("Adivinhe o número no intervalo de 1 e " + str(numero_escolhido))

    def acertar():    
        numero_achado = int(input())    
        if numero_achado == numero_achar:
            print("Parabéns vc acertou!")
            print("Jogar novamente?")
            sim_não = input()
            if sim_não == "sim":
                os.system("cls")
                main()
            elif sim_não == "não" or "nao":
                exit()
            else:
                print("insira um valor válido")
        elif numero_achado >= numero_achar:
            print("Menor!")
            acertar()
        elif numero_achado <= numero_achar:
            print("Maior!")
            acertar()
    acertar()
main()

  



    




