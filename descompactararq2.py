import heapq
from collections import defaultdict

# Função auxiliar: lê os bits do arquivo binário
def ler_bits(nome_arquivo):
    with open(nome_arquivo, 'rb') as f:
        bytes_lidos = f.read()
        bits = ''.join(f"{byte:08b}" for byte in bytes_lidos)
    return bits

# Função para reconstruir a árvore de Huffman a partir dos dados
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

# Função inversa: de código -> símbolo
def inverter_codigos(codigos):
    return {v: k for k, v in codigos.items()}

# Caminhos
entrada = "compactado_arq2.txt"
saida = "descompactado_arq2.txt"
original = "arquivo2.txt"

# Etapas
with open(original, "r") as f:
    texto_original = f.read()

# Refaz os mesmos passos para gerar a árvore de Huffman (baseado no texto original)
frequencias = defaultdict(int)
for c in texto_original:
    frequencias[c] += 1

codigos = construir_arvore(frequencias)
tabela_invertida = inverter_codigos(codigos)

# Lê os bits do arquivo compactado
bits = ler_bits(entrada)

# Decodificação bit a bit
buffer = ""
resultado = []

for bit in bits:
    buffer += bit
    if buffer in tabela_invertida:
        resultado.append(tabela_invertida[buffer])
        buffer = ""

# Salva o resultado
with open(saida, "w") as f:
    f.write(''.join(resultado))

print("Arquivo descompactado", saida)
