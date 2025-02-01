import random

def gerar_cartela(modo):
    """Gera cartelas de bingo com base no modo escolhido."""
    if modo == 'rápido':
        num_cartelas = 2
    else:
        num_cartelas = 4
    
    cartelas = []
    for _ in range(num_cartelas):
        cartela = [
            random.sample(range(1, 11), 2),  # Primeira coluna [1-10]
            random.sample(range(11, 21), 2),  # Segunda coluna [11-20]
            random.sample(range(21, 31), 2)   # Terceira coluna [21-30]
        ]
        cartelas.append(cartela)
    
    return cartelas

def imprimir_cartela(cartela, sorteadas):
    """Exibe a cartela formatada, marcando as dezenas sorteadas."""
    print("Cartela:")
    for linha in zip(*cartela):
        print(" ".join(f"({num:2})" if num in sorteadas else f" {num:2} " for num in linha))
    print()

def sortear_dezena(sorteadas):
    """Sorteia uma nova dezena que ainda não tenha sido sorteada."""
    while True:
        dezena = random.randint(1, 30)
        if dezena not in sorteadas:
            sorteadas.append(dezena)
            return dezena
