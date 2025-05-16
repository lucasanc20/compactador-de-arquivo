import heapq
from collections import defaultdict

# 1. Conta a frequência de cada caractere
def contar_frequencias(texto):
    freq = defaultdict(int)
    for c in texto:
        freq[c] += 1
    return freq

# 2. Constrói a árvore de Huffman usando heap
def construir_arvore(freq):
    heap = [[peso, [simbolo, ""]] for simbolo, peso in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        baixo = heapq.heappop(heap)
        alto = heapq.heappop(heap)
        for par in baixo[1:]:
            par[1] = '0' + par[1]
        for par in alto[1:]:
            par[1] = '1' + par[1]
        heapq.heappush(heap, [baixo[0] + alto[0]] + baixo[1:] + alto[1:])
    return dict(heap[0][1:])

# 3. Codifica o texto com os códigos de Huffman
def codificar(texto, codigos):
    return ''.join(codigos[c] for c in texto)

# 4. Salva os bits como bytes em um arquivo binário
def salvar_como_binario(bits, nome_arquivo):
    with open(nome_arquivo, 'wb') as f:
        byte = 0
        bits_preenchidos = 0
        for bit in bits:
            byte = (byte << 1) | int(bit)
            bits_preenchidos += 1
            if bits_preenchidos == 8:
                f.write(bytes([byte]))
                byte = 0
                bits_preenchidos = 0
        if bits_preenchidos > 0:
            byte = byte << (8 - bits_preenchidos)
            f.write(bytes([byte]))

# Caminho para o arquivo original
entrada = "arquivo2.txt"
saida = "compactado_arq2.txt"

# Lê o conteúdo
with open(entrada, "r") as f:
    texto = f.read()

# Executa os passos
frequencias = contar_frequencias(texto)
arvore = construir_arvore(frequencias)
codigos = codificar(texto, arvore)
salvar_como_binario(codigos, saida)

print("Arquivo compactado com sucesso:", saida)
