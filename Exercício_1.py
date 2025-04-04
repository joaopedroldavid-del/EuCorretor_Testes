"""
Exercício 1: Encontrar o Primeiro Caractere Não Repetido em uma String

- Descrição: Neste exercício, você deve implementar uma função que encontra o primeiro caractere que não se repete em uma string. Caso todos os caracteres sejam repetidos, a função deve retornar -1.
 
Exemplo:
firstUniqChar("abacabad")  # Saída: 3 ('c')
firstUniqChar("aaabb")      # Saída: -1 (não há caracteres não repetidos)
"""
def firstUniqChar(phrase: str) -> None:
    char_count = {}  
    
    for char in phrase:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in phrase:
        if char_count[char] == 1:
            print(f"Elemento: {char}")
            return
    
    print("Não há caracteres exclusivos")


def main():
    
    print("Teste 1:")
    firstUniqChar("abacabad")
    print("\nTeste 2:")
    firstUniqChar("aabb")
    print("\nTeste 3:")
    firstUniqChar("aabbccddeffgghjj")


if __name__ == "__main__":
    main()