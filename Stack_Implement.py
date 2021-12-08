stack = []

def push():
    element = input("Enter the elemenet = ")
    stack.append(element)
    print(stack)

def pop():
    if not stack:
        print("Stack is empty!")
    else:
        a = stack.pop()
        print("The removed element is", a)
        print(stack)
    
while True:
    choice = int(input("Select the opertaion : push(1), pop(2) or quit(3) = "))
    if(choice == 1):
        push()
    elif(choice == 2):
        pop()
    elif(choice == 3):
        break
    else:
        print("Enter the correct opertaion.")