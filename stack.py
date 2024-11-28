class mystack:
    def  init (self):
        self.data = []

    def push(self,data):
        self.data.append(data)
    def pop(self):
        if self.data == []:
            return None
        else:
            return self.data.pop()
    def size(self):
        return len(self.data)
    def empty(self):
        return self.data == []
def reverse(string):
        temstr = ''
        stack = mystack()


        for i in range(len(string)):
            stack.push(string[i])
        while not stack.empty():
            tem = stack.pop()
            temstr = temstr + tem
            return temstr


string = input('Enter a string: ')
print(reverse(string))
