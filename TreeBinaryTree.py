class BinaryTree():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.parent = None

    def set_left(self,node):
       self.left = node
       self.left.parent = self
       #print("\n %s" %(self.left.parent))

    def set_right(self,node):
       self.right = node
       self.right.parent = self

    def inorder(self):
     left_vals = self.left.inorder() if self.left is not None else []
     #print(left_vals)
     right_vals = self.right.inorder() if self.right is not None else []
     return left_vals + [self.value] + right_vals

    def preorder(self):
     left_vals=self.left.preorder()if self.left is not None else[]
     right_vals=self.right.preorder()if self.right is not None else[]
     return [self.value]+left_vals+right_vals

    def postorder(self):
       left_vals=self.left.postorder() if self.left is not None else[]
       right_vals=self.right.postorder() if self.right is not None else[]
       return left_vals + right_vals + [self.value]


#outside the class
if __name__ == '__main__':
    #root = BinaryTree("I'm the root")
    #left = BinaryTree("I'm left first")
    #left.parent = root
    #root.left = left
    tree = BinaryTree(4)
    left = BinaryTree("I'm first left 3")
    left.set_left(BinaryTree("I'm first left left 2"))
    left.set_right(BinaryTree("I'm first left right 1"))
    right = BinaryTree("I'm right first 8")
    right.set_left(BinaryTree("I'm left of right 9"))
    right.set_right(BinaryTree("I'm right right 10"))
    tree.set_left(left)
    tree.set_right(right)
    print("Now inorder")
    print (tree.inorder())
    print("Now preorder")
    print (tree.preorder())
    print("Now postorder")
    print (tree.postorder())
