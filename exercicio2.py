'''Escreva um programa que solicite ao usuário seu nome e sua idade.
Na sequência o programa deve exibir duas mensagens: uma com o nome e outra com a idade do
usuário.
Exemplo:
Suponha que o usuário digite o nome João e a idade 25. Para esses dados de entrada o seu
programa deve exibir uma mensagem no seguinte formato:
Seu nome é João e você tem 25 anos
'''
nome = str(input("Informe seu nome: "))
idade = int(input("Informe sua idade: "))
print("Seu nome é", nome, "e você tem", idade, "anos")

# Outras maneiras para formatar a saída:
# print("Seu nome é {} e você tem {} anos".format(nome, idade))
# print(f"Seu nome é {nome} e você tem {idade} anos")
