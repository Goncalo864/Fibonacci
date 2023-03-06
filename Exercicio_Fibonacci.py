import random


# Escolhe um numero random por cada intervalo inserido
def num_randoms(num_intervalos, intervalos):
    num_random = []
    for x in range(num_intervalos):
        random_number = random.choice(range(intervalos[x * 2], intervalos[x * 2 + 1]))
        num_random.append(random_number)

    return num_random


# Forma a sequencia de febonacci, escolhendo um dos numeros criados da função "num_randoms"
def seq_febonacci(num_random):
    valor_max = random.choice(num_random)
    seq_fib = [0, 1]
    # for _ in range(2, random_number): caso o pretendido seja repetir n vezes

    while seq_fib[-1] < valor_max:
        fib = seq_fib[-1] + seq_fib[-2]
        seq_fib.append(fib)

    return seq_fib[:-1], valor_max


# Verifica os numeros impares da sequencia
def num_impares(seq_febonacci):
    num_impares = []
    for x in seq_febonacci:
        if x % 2 == 1:
            num = x
            num_impares.append(num)

    return num_impares


intervalos = []

num_intervalos = int(input("Quantos intervalos quer introduzir? "))

for x in range(num_intervalos):
    primeiro_num = int(input(f"Introduza o limite inferior do intervalo {x + 1}: "))
    segundo_num = int(input(f"Introduza o limite superior do intervalo {x + 1}: "))
    if primeiro_num > segundo_num:
        print("O segundo numero tem de ser superior ao limite inferior!")
        exit(0)
    intervalos.extend([primeiro_num, segundo_num])

num_randoms = num_randoms(num_intervalos, intervalos)
seq_febonacci, valor_max = seq_febonacci(num_randoms)
num_impares = num_impares(seq_febonacci)
q_impares = len(num_impares)

print("------------------")
print("Numeros introduzidos:", intervalos)
print("Numeros random dos intervalos: ", num_randoms)
print("Limite da sequência: ", valor_max)
print("Sequencia de febonacci: ", seq_febonacci)
print("Numeros impares da sequencia: ", num_impares)
print("Quantidade de impares: ", q_impares)


