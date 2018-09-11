allWords = []  # Salva todas as palavras do txt na lista allWords
f = open("Lista-de-Palavras.txt", "r")
for w in f:
    allWords.append(w[:-1])  # removendo o "enter" do final
f.close()

letters = int(input("Digite a quantidade de letras: "))  # Pega a quantidade de letras

avaiableWords = []  # Cria uma nova lista onde apenas as palavras disponiveis com a quantidade de letras recebida serão armazenadas

for word in allWords:  # Para cada palavra na lista allWords,
    if len(word) == letters:  # verifica se a palavra tem o mesmo tamanho da quantidade de letras
        avaiableWords.append(word)  # Se sim, adiciona ela à lista de palavras disponíveis

secretWord = []  # Cria uma nova lista onde será armazenada as letras da palavra que o programa secreta tem que descobrir

for i in range(0, letters):  # Loop que é rodado x vezes, onde x é a quantidade de letras que o usuário colocou
    secretWord.append("_")  # Para cada iteração do loop, adiciona " _ " à palavra

wordFound = False  # Variavel criada para entrar no while

while wordFound == False:  # Enquanto a palavra ainda não tiver sido encontrada, continua pedindo entradas do usuario
    print("Palavra: "),
    for letter in secretWord:  # Imprime todas as letras que estão armazenadas na lista da palavra secreta
        print(letter).lower(),  # a vírgula serve para imprimir tudo sem pular nenhuma linha

    print("")
    userLetter = raw_input("Letra: ")  # Pede a letra do usuario
    userLetter = userLetter.upper()  # Converte para upper case
    userPosition = int(input("Posição: "))  # Pede a posição da letra
    if userPosition > 0:  # Só faz a alteração na palavra secreta se a posição for maior do que 0
        secretWord[userPosition - 1] = userLetter
    if userPosition == 0:
        for I in avaiableWords:
            if userLetter in I:
                avaiableWords.remove(I)
    newAvaiableWords = []  # Cria uma nova lista, onde serão armazenadas as novas palavras disponíveis de acordo com a letra recebida anteriormente

    for word in avaiableWords:  # Para cada palavra nas palavras disponíveis
        isWordOk = True  # Declara inicialmente que essa palavra é válida
        for index, letter in enumerate(word):  # Para cada letra na palavra
            # Se alguma letra da palavra for diferente de alguma letra da palavra secreta na mesma posição
            if (secretWord[index] != "_") & (word[index] != secretWord[index]):
                isWordOk = False  # Declara que a palavra e inválida, pois ela possui letras diferentes
        if isWordOk == True:  # No final do loop, verificamos se a palavra, por fim, é ou não é válida.
            newAvaiableWords.append(word)  # Caso ela seja, nós adicionamos ela à nova lista de palavras disponíveis

    print("Palavras disponíveis: ").lower()
    for word in newAvaiableWords:  # Mostra todas as novas palavras disponíveis na tela
        print(word).lower()

    # A cada iteração do while, as palavras disponíveis vão diminuindo ate que no final só vai sobrar uma
    # Quando isso acontecer, dizemos que a palavra foi encontrar, e saimos do while.
    if len(newAvaiableWords) == 1:
        wordFound = True

print("Palavra encontrada!")
