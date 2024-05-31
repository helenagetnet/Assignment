#1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data, position):
        new_node = Node(data)
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        count = 0
        while current is not None and count < position - 1:
            current = current.next
            count += 1
        
        if current is None:
            raise IndexError("Position out of bounds")
        
        # Insert the new node at the desired position
        new_node.next = current.next
        current.next = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#Example Usage
if __name__ == "__main__":
    llist = LinkedList()
    
    # Insert elements at various positions
    llist.push(3, 0)  
    llist.push(5, 1)  
    llist.push(2, 1)  
    llist.push(7, 2)  
    llist.print_list()  
print("\n")


#2


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
          
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def deleteNodeAtGivenPosition(self, position):
		if self.head is None:
			return
		index = 0
		current = self.head
		while current.next and index < position:
			previous = current
			current = current.next
			index += 1
		if index < position:
			print("\nIndex is out of range.")
		elif index == 0:
			self.head = self.head.next
		else:
			previous.next = current.next

	def printList(self):
		temp = self.head
		while(temp):
			print(" %d " % (temp.data), end=" ")
			temp = temp.next

# Example usage 
llist = LinkedList()
llist.push(10)
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)

print("Created Linked List: ")
llist.printList()
llist.deleteNodeAtGivenPosition(4)
print("\nLinked List after Deletion : ")
llist.printList()

print("\n")

#3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_after_node(self, prev_node_data):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        # Find the given node
        while current is not None and current.data != prev_node_data:
            current = current.next
        # If the given node is not found or the given node is the last node
        if current is None:
            print("Given node not found in the list.")
            return
        if current.next is None:
            print("No node exists after the given node.")
            return
        next_node = current.next
        current.next = next_node.next
        next_node = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_end(1)
    sll.insert_at_end(2)
    sll.insert_at_end(3)
    sll.insert_at_end(4)
    #sll.print_list()  

    sll.delete_after_node(2)
    sll.print_list()  
print("\n")

#4
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0
        while current is not None and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            raise IndexError("Position out of bounds")
        
        new_node.next = current.next
        current.next = new_node

    def search(self, key):
        current = self.head

        while current is not None:
            if current.data == key:
                return True
            current = current.next
        
        return False
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example Usage

if __name__ == "__main__":
    llist = LinkedList()
    
    # Insert elements at various positions
    llist.push(3, 0) 
    llist.push(5, 1)  
    llist.push(2, 1)  
    llist.push(7, 2)  
    llist.push(1, 0)  
    
    print("Original List:")
    llist.print_list()  

    print("Searching for 7:", llist.search(7)) 
print("\n")
#5

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class Stack:

	def __init__(self):
		self.head = None

	def isempty(self):
		if self.head == None:
			return True
		else:
			return False

	def push(self, data):

		if self.head == None:
			self.head = Node(data)

		else:
			newnode = Node(data)
			newnode.next = self.head
			self.head = newnode

	def pop(self):

		if self.isempty():
			return None

		else:
			poppednode = self.head
			self.head = self.head.next
			poppednode.next = None
			return poppednode.data

	def peek(self):

		if self.isempty():
			return None

		else:
			return self.head.data

	def display(self):

		iternode = self.head
		if self.isempty():
			print("Stack Underflow")

		else:

			while(iternode != None):

				print(iternode.data, end = "")
				iternode = iternode.next
				if(iternode != None):
					print(" -> ", end = "")
			return


# Example usage
if __name__ == "__main__":
    MyStack = Stack()

MyStack.push(11)
MyStack.push(22)
MyStack.push(33)
MyStack.push(44)

MyStack.display()
#print("\n")

MyStack.pop()
MyStack.pop()
print ("\nElements after pop: " )  
MyStack.display()
print("\nTop element is ", MyStack.peek())