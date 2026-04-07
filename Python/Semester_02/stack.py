class Stack:
    def __init__(self):
        self.__stack_l = []
    
    def push(self, param):
        self.__stack_l.append(param)
    
    def pop(self):
        val = self.__stack_l[-1]
        del self.__stack_l[-1]
        return val
    
    def print_stack(self):
        for x in self.__stack_l:
            print(x)
        
stack_o = Stack()
stack_o.push(1)
stack_o.push("brabo")
stack_o.push("hora do show")
stack_o.push("que não vai da oq")
stack_o.pop()

stack_o2 = Stack()
stack_o2.push(85)
stack_o2.push("ce louco")
stack_o2.push("é mais de 8000")
stack_o2.push("hum é mesmo?")
stack_o2.pop()

print(stack_o.print_stack())