class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def isCompleted(self):
        return self.completed

    def markCompleted(self):
        self.completed = True


class Node:
    def __init__(self, task):
        self.task = task
        self.next = None


class ToDoList:
    def __init__(self):
        self.head = None

    def addToDo(self, task):
        new_node = Node(task)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def markToDoAsCompleted(self, title):
        current = self.head
        while current:
            if current.task.getTitle() == title:
                current.task.markCompleted()
                return
            current = current.next
        print(f"Task with title '{title}' not found.")

    def viewToDoList(self):
        current = self.head
        if not current:
            print("To-Do List is empty.")
        else:
            print("To-Do List:")
            while current:
                task = current.task
                status = "[Completed]" if task.isCompleted() else "[Incomplete]"
                print(f"- {task.getTitle()} {status}")
                print(f"  Description: {task.getDescription()}")
                current = current.next


def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add a new task")
        print("2. Mark a task as completed")
        print("3. View To-Do List")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.addToDo(Task(title, description))
            print("Task added successfully!")
        elif choice == "2":
            title = input("Enter title of the task to mark as completed: ")
            todo_list.markToDoAsCompleted(title)
        elif choice == "3":
            todo_list.viewToDoList()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()


