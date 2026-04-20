class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None
        self.prev = None

class PriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, value, priority):
        new_node = Node(value, priority)

        if self.head is None:
            self.head = new_node
            return

        if priority > self.head.priority:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        while current.next is not None and current.next.priority >= priority:
            current = current.next

        new_node.next = current.next
        new_node.prev = current

        if current.next is not None:
            current.next.prev = new_node
        
        current.next = new_node

    def dequeue(self):
        if self.head is None:
            return None
        
        removed_value = self.head.value
        self.head = self.head.next
        
        if self.head is not None:
            self.head.prev = None
            
        return removed_value

    def peek(self):
        if self.head is None:
            return None
        return self.head.value

    def show(self):
        if self.head is None:
            return "Черга порожня"
        
        current = self.head
        result = []
        while current is not None:
            result.append(f"{current.value}({current.priority})")
            current = current.next
        return " -> ".join(result)

if __name__ == "__main__":
    q = PriorityQueue()
    n = int(input("Скільки елементів додати: "))

    for i in range(n):
        val = input("Введіть значення: ")
        pri = int(input("Введіть пріоритет: "))
        q.enqueue(val, pri)

    print("\nПоточна черга:", q.show())
    print("Перший у черзі:", q.peek())
    print("Видаляємо елемент:", q.dequeue())
    print("Черга після видалення:", q.show())