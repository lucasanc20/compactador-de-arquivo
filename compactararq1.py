arq_bruto = "arquivo1.txt"
arq_compactado = "compactado.txt"

abre = open(arq_bruto, "r", encoding="utf-8")
conteudo = abre.read()
abre.close()

compactado = ""
contador = 1

for i in range(len(conteudo) - 1):
    if conteudo[i] == conteudo[i + 1]:
        contador += 1
    else:
        compactado += conteudo[i] + str(contador)
        contador = 1

# Adiciona o último grupo de caracteres
compactado += conteudo[-1] + str(contador)

abre = open(arq_compactado, "w", encoding="utf-8")
abre.write(compactado)
abre.close()

quant_letras = len(compactado)
quant_letras_arq_bruto = len(arq_bruto)

print(f"arq compactado para '{quant_letras}' caracteres")
