"""Exercício 3: Word Ladder (Escada de Palavras)

    - Descrição: Neste exercício, você deve implementar uma função que encontra o comprimento do caminho mais curto de transformação de uma palavra inicial para uma palavra final, seguindo as regras abaixo:
    1. A cada transformação, apenas uma letra pode ser alterada.
    2. Cada palavra intermediária deve existir no dicionário fornecido.
    
    A entrada do exercício será composta por duas palavras de mesma dimensão e uma lista de palavras. Sua tarefa é encontrar a sequência mais curta de transformações, ou retornar 0 caso não seja possível.
    
    Exemplo:
    ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])  
    # Saída: 5 ("hit" -> "hot" -> "dot" -> "dog" -> "cog")

    ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])  
    # Saída: 0 (não há caminho possível)"""

def ladderLength(initWord, finalWord, wordList):

    words = set(wordList) 
    abc = 'abcdefghijklmnopqrstuvwxyz'

    if finalWord not in words:
        return 0
    
    queue = [(initWord, 1)]
    visited = {initWord}

    while queue:
        word, path_length = queue.pop(0)

        for i in range(len(word)):
            for j in abc:
                tempWord = word[:i] + j + word[i+1:]

                if tempWord == finalWord:
                    return path_length + 1
                
                if tempWord in words and tempWord not in visited:
                    visited.add(tempWord)
                    queue.append((tempWord, path_length + 1))
    
    return 0


def main():
    print("Quantidade de Movimentos: \n" + str(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])))
    print("Quantidade de Movimentos: \n" + str(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"])))

if __name__ == "__main__":
    main()