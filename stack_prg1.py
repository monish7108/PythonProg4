class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    userstring=input("Enter the string: ")
    import re
    if re.search(r"^[(][()]+[)]$",userstring):
        # print("valid")
        userstring= list(userstring)
        obj=Stack()
        for elem in userstring:
            # print(elem)
            if elem=="(":
                obj.push(elem)
                # print(obj.size())
                # print(obj.peek())
            else:
                try:
                    obj.pop()
                    # print(obj.size())
                except Exception:
                    print("Invalid opening and closing of brackets")

                    exit()
        if obj.isEmpty() :
            print("It is valid string.")
        else:
            print("String is invalid")
    else:exit()
