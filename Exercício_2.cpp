/*
Exercício 2: Mesclar Intervalos

- Descrição: Dada uma lista de intervalos, você deve implementar uma função que mescla os intervalos sobrepostos. Cada intervalo é representado por um par de números [início, fim]. Caso dois intervalos se sobreponham, eles devem ser combinados em um único intervalo.

Exemplo:
merge_intervals([[1,3], [2,6], [8,10], [15,18]])  
# Saída: [[1, 6], [8, 10], [15, 18]]

merge_intervals([[1,4], [4,5]])  
# Saída: [[1, 5]]
*/

#include <iostream>

using namespace std;

struct Node {
    int inicio;
    int fim;
    Node* prev;
    Node* next;
};

Node* createNode(int inicio, int fim) {
    Node* newNode = new Node();
    newNode->inicio = inicio;
    newNode->fim = fim;
    newNode->prev = nullptr;
    newNode->next = nullptr;
    return newNode;
}

void insertNode(Node*& head, int inicio, int fim) {
    Node* newNode = createNode(inicio, fim);
    if (head == nullptr) {
        head = newNode;
        return;
    }
    
    Node* temp = head;
    while (temp->next != nullptr) {
        temp = temp->next;
    }
    
    temp->next = newNode;
    newNode->prev = temp;
}

void displayList(Node* head) {
    Node* temp = head;
    while (temp != nullptr) {
        cout << "[" << temp->inicio << ", " << temp->fim << "]";
        temp = temp->next;
        if (temp != nullptr) {
            cout << ", ";
        }
    }
}

void merge_intervals(Node*& head) {
    if (head == nullptr || head->next == nullptr) {
        return;  
    }

    Node* temp = head;
    while (temp != nullptr && temp->next != nullptr) {
        if (temp->fim >= temp->next->inicio) {
            temp->fim = max(temp->fim, temp->next->fim);
            
            Node* nodeToDelete = temp->next;
            temp->next = nodeToDelete->next;
            if (nodeToDelete->next != nullptr) {
                nodeToDelete->next->prev = temp;
            }
            delete nodeToDelete;
        } else {
            temp = temp->next;
        }
    }
}

int main() {
    Node* head = nullptr;

    insertNode(head, 1, 3);
    insertNode(head, 2, 6);
    insertNode(head, 8, 10);
    insertNode(head, 15, 18);

    cout << "Intervalos antes de mesclar: ";
    displayList(head);
    cout << endl;
    
    merge_intervals(head);

    cout << "Intervalos após mesclar: ";
    displayList(head);

    return 0;
}