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

def verificar_vencedor(cartelas, sorteadas):
    """Verifica se alguma cartela tem todas as dezenas sorteadas."""
    for i, cartela in enumerate(cartelas):
        numeros_cartela = {num for coluna in cartela for num in coluna}
        if numeros_cartela.issubset(set(sorteadas)):
            return i + 1  # Retorna o número da cartela vencedora
    return None

def main():
    print("Bem-vindo ao Simulador de Bingo!")
    modo = input("Escolha o modo de jogo (rápido/demorado): ").strip().lower()
    while modo not in ['rápido', 'demorado']:
        modo = input("Modo inválido! Escolha entre 'rápido' ou 'demorado': ").strip().lower()
    
    cartelas = gerar_cartela(modo)
    sorteadas = []
    
    print("\nCartelas geradas:\n")
    for i, cartela in enumerate(cartelas):
        print(f"Jogador {i + 1}:")
        imprimir_cartela(cartela, sorteadas)
    
    print("Iniciando o sorteio...\n")
    
    vencedor = None
    while not vencedor:
        input("Pressione ENTER para sortear a próxima dezena...")
        
        dezena = sortear_dezena(sorteadas)
        print(f"Dezena sorteada: {dezena}")
        print(f"Dezenas sorteadas até agora: {sorted(sorteadas)}\n")
        
        for i, cartela in enumerate(cartelas):
            print(f"Jogador {i + 1}:")
            imprimir_cartela(cartela, sorteadas)
        
        vencedor = verificar_vencedor(cartelas, sorteadas)
        if vencedor:
            print(f"Parabéns! O Jogador {vencedor} venceu!\n")
            break
    
    print("Fim da sessão de Bingo!")

if __name__ == "__main__":
    main()