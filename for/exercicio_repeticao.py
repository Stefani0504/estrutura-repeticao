'''
A empresa definiu a seguinte regra:
 
Nota maior ou igual a 7 → Funcionário aprovado
Nota menor que 7 → Funcionário em acompanhamento
 
🔧 O que você deve fazer
 
Criar uma lista com as notas de desempenho dos funcionários
Utilizar o laço for para percorrer a lista
Utilizar um if dentro do for para verificar a nota
Mostrar no console a situação de cada funcionário
 
💻 Exemplo de lista
notas = [8, 5, 9, 6, 7]
 
💻 Exemplo de saída esperada
Nota 8 - Funcionário aprovado
Nota 5 - Funcionário em acompanhamento
Nota 9 - Funcionário aprovado
Nota 6 - Funcionário em acompanhamento
Nota 7 - Funcionário aprovado
 
'''

nota =  [8, 5, 9, 6, 7]

for notas in nota:

    if notas >= 7:
        print("Funcionario Aprovado", notas)
    else:
        print("Funcionario em Acompanhamento", notas)




