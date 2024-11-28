class node:
    def init (self,data):
    self.right = None
    self.left = None
    self.data = data

def insert(self,data):
    if self.data:
        if data < self.data:

            if self.left is None:
                self.left = node(data)

            else:

                self.left.insert(data)
        elif data > self.data:

            if self.right is None:
                self.right = node(data)

        else:

            self.right.insert(data)

    else:

        self.data = data

def printTree(self):
    if self.left:

        self.left.printTree()

    print(self.data,end=" ")
    if self.right:
        self.right.printTree()

def delete_node(root,key):
    if root is None:

        return root

    if key<root.data:
        root.left=delete_node(root.left,key)

    elif (key>root.data):
        root.right=delete_node(root.right,key)

    else:

        if root.left is None:
            temp=root.right
            root=None
            return temp

        elif root.right is None:
            temp=root.left
            root=None

        return temp

        temp=inorder_successsor(root.right)
        root.data=temp.data
        root.right=delete_node(root.right,tem.data)

        return root

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print("\nTree:")
root.printTree()
print()

print("\ndeleting node 14 ")
delete_node(root,14)

print("\nAfter the deletion of node 14: ")
root.printTree()
