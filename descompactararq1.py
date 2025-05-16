arq_compactado = "compactado.txt"
arq_recuperado = "descompactado.txt"

# Lê o arquivo compactado
abre = open(arq_compactado, "r", encoding="utf-8")
compactado = abre.read()
abre.close()

descompactado = ""
i = 0

# Percorre o conteúdo compactado e reconstrói o original
while i < len(compactado):
    caractere = compactado[i]  # Obtém o caractere
    i += 1
    quantidade = ""

    # Captura o número de repetições do caractere
    while i < len(compactado) and compactado[i].isdigit():
        quantidade += compactado[i]
        i += 1
    
    descompactado += caractere * int(quantidade)  # Expande o caractere

# Salva o texto descompactado em um novo arquivo
abre = open(arq_recuperado, "w", encoding="utf-8")
abre.write(descompactado)
abre.close()

quant_letras = len(descompactado)

print(f"arquivo recuperado '{arq_recuperado}' com '{quant_letras}' letras")
