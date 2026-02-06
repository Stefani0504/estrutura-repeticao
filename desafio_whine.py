'''
🧠 Atividade Prática – Tabuada Personalizada com while | Dia 05/02
 
🎯 Objetivo da Atividade
 
Praticar o uso do laço de repetição while, trabalhando com entrada de dados do usuário (input) e controle de repetição.
 
📋 Enunciado
 
Você deve criar um programa em Python que gere a tabuada de um número escolhido pelo usuário, indo até um limite também definido pelo usuário.
 
Diferente do exemplo visto em sala (onde a tabuada era fixa), agora o programa deve ser dinâmico, permitindo diferentes valores.
 
🔧 Requisitos do programa
 Pedir ao usuário:
O número da tabuada
Até qual número a tabuada deve ir
Utilizar a estrutura while
Mostrar o cálculo no formato:
5 x 3 = 15
Encerrar quando atingir o limite informado
 
 
✅ Critérios para a atividade estar correta
Utilizar input() para receber os valores
Utilizar while corretamente
Exibe a tabuada no formato correto
 
⭐⭐ Desafio extra (opcional) ⭐⭐
Não permitir números negativos
Perguntar ao final se o usuário deseja gerar outra tabuada

'''

#Criar uma tabuada 


numero1 = int(input("Digite o numero desejavel:"))
numerolimite = int(input("Limete de multiplicacao:"))

contador = 0

while contador <= numerolimite:
    print(numero1, "x", contador, "=", contador * numero1)
    contador += 1







