#atividade 1
def programas_infantis():
    print("\n=== Programas Infantis ===")
    print("- Peppa Pig")
    print("- Bob Esponja")
    print("- Turma da Mônica")
    print("- Patrulha Canina")
    print("- Galinha Pintadinha")

def lista_de_carros():
    print("\n=== Lista de Carros ===")
    print("1. Fiat Uno - R$ 25.000")
    print("2. Honda Civic - R$ 90.000")
    print("3. Toyota Corolla - R$ 100.000")
    print("4. Ford Ka - R$ 40.000")
    print("5. Jeep Compass - R$ 150.000")


idade = int(input("Digite sua idade: "))

if idade < 18:
    programas_infantis()
else:
    lista_de_carros()

#atividade 2
def verificar_par_ou_impar(numero):
    
    return numero % 2 == 0

def jogar_par_ou_impar():
    print("==== JOGO PAR OU ÍMPAR ====")

    
    num_computador = int(input("Digite o número do computador (1 a 10): "))
    
    
    num_usuario = int(input("Digite seu número (1 a 10): "))

    
    soma = num_computador + num_usuario
    print(f"\nComputador jogou: {num_computador}")
    print(f"Você jogou: {num_usuario}")
    print(f"Soma: {soma}")

    
    if verificar_par_ou_impar(soma):
        print("A soma é PAR. Você venceu! 🎉")
    else:
        print("A soma é ÍMPAR. O computador venceu! 🤖")


jogar_par_ou_impar()

#atividade 3
def saudacao(nome, cidade):
    if cidade.lower() == "rio de janeiro":
        print(f"\nOlá, {nome}! Seja bem-vindo à Cidade Maravilhosa!")
    else:
        print(f"\nOlá, {nome}! Você está em {cidade}.")


nome = input("Digite seu nome: ")
cidade = input("Digite a cidade de onde está falando: ")


saudacao(nome, cidade)
