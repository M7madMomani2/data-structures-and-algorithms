# Singly Linked List
> - A singly linked list is a type of linked list that is unidirectional, that is, it can be traversed in only one direction from head to the last node (tail).
> - Each element in a linked list is called a node. A single node contains data and a pointer to the next node which helps in maintaining the structure of the list.


## Challenge
> - Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node. Within the LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.


## Approach & Efficiency
**Efficiency**

Big O :
> - O(1) Time/space performance for insert method.
> - O(n) Time and O(1) space performance for includes method.


**Approach**
> - to implement this data structure i used tow classes first ont Node and second one Linked-List class to connect nodes together

## API
Linked-List Class is the main class it has 3 main methods:

> - insert: It calls node class to fill the value of the node and make the node a Head node if the head is none
> - str: It iterates over the node and save them in Result value and finally return it
> - include: It iterate over the linked list to look for a specific value, then return a logical value.

## Solution
[Singly Linked List](https://miro.com/ app/board/o9J_lG44R2c=/)
