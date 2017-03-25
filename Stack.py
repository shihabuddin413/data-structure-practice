class Stack():
    """
    @description: This class will define several methods for stack.
    """

    def __init__(self):
        # defining a list which will act as stack container
        self.mystack = []

    def is_empty(self):
        # this method will check whether the stack is empty or not
        if len(self.mystack) > 0:
            return False
        else:
            return True

    def push(self, item):
        # this method will push an item to the defined stack
        return self.mystack.append(item)

    def pop(self):
        # this method will pop an item from defined stack
        return self.mystack.pop()

    def peek(self):
        # this method will peek an item from the stack means won't remove
        # it
        return self.mystack[len(self.mystack) - 1]


def main():
    # defining the main function for the stack
    s = Stack()
    # s is an object of Stack class
    while True:
        print("1. Push \n2. Pop \n3. Peek \n4. Show \n5. Quit")
        print("\nWhat do you wanna do now?")
        case = int(input())
        # starting something, equivalent to Switch statement in C/C++
        if case == 1:
            # in this case, we will call our push function
            print("Input item, you wanna push to stack:")
            item = int(input())
            s.push(item)
            print("Congrats!", item, "has been pushed.")
        elif case == 2:
            # in this case, we will call our pop function
            if s.is_empty():
                print("Sorry, the stack is empty.")
            else:
                print(s.pop())
        elif case == 3:
            # in this case, we will call our peek function
            if s.is_empty():
                print("Sorry, the stack is empty.")
            else:
                print(s.peek(), "has been peeked.")
        elif case == 4:
            # in this case, we will print the current condition of our
            # stack
            if s.is_empty():
                print("Sorry, the stack is empty.")
            else:
                print("The current condition of our stack:", s.mystack)
        elif case == 5:
            # in this case, we will quit our script
            print("The script is gonna quit.")
            quit()
        else:
            print("Oops! Wrong Choice.")
            main()
            # finishing something, equivalent to Switch statement in C/C++

if __name__ == "__main__":
    main()
