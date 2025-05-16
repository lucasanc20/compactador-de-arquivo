Etapas do funcionamento:

1- Contagem de Frequências
    O código lê todo o texto e conta quantas vezes cada caractere aparece. Esses valores de frequência são essenciais para determinar os códigos mais eficientes.

2- Construção da Árvore de Huffman
    Com as frequências, é criada uma árvore binária onde:
      .Cada nó folha representa um caractere.
      .Nós com menor frequência ficam mais distantes da raiz, gerando códigos mais longos.
      .Nós com maior frequência ficam mais próximos, gerando códigos curtos.

3- Geração dos Códigos Binários
    Percorremos a árvore para atribuir um código binário único para cada caractere:
      .Esquerda → adiciona 0 ao código.
      .Direita → adiciona 1.

4- Codificação do Texto
    Cada caractere do texto original é substituído pelo seu código binário de Huffman, formando uma longa sequência de bits.

5- Escrita em Arquivo Binário
    Os bits gerados são agrupados em bytes e gravados em um novo arquivo (compactado_arq2.txt), que ocupa menos espaço do que o arquivo original.
