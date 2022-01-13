class Node():
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key
class BinarySequenceNumberTree():
    def __init__(self,value = None):
        super().__init__()
        self.root = Node(value)
        self.deepSize = 0
        self.numberOfElements = 0
        self.nodes = ""
    
    #Add new item
    def insertNode(self, key):
        tempSearch = self.root
        tempParent = self.root

        #Travel in tree
        while tempSearch != None:
            tempParent = tempSearch
            if key == tempSearch.value:
                return
            elif key < tempSearch.value:
                tempSearch = tempSearch.left
            elif key > tempSearch.value:
                tempSearch = tempSearch.right
        
        #Add to the appropriate position
        if tempParent == None:
            tempParent = Node(key)
        elif key<tempParent.value:
            tempParent.left = Node(key)
        else:
            tempParent.right = Node(key)

    #Find item in tree
    def search(self,value):
        if self.root == None:
            return None
        elif self.value == value:
            return self
        elif self.value > value:
            return self.left.search(value)
        else:
            return self.right.search(value)

    #Delete item
    def removeNode(self,value):
        tempCurrent = self.root
        tempParent = self.root
        issol = True 

        #Find Node
        while (tempCurrent.value != value):
            tempParent = tempCurrent 
            if value < tempCurrent.value:
                issol = True 
                tempCurrent = tempCurrent.left 
            else:
                issol = False 
                tempCurrent = tempCurrent.right
            if tempCurrent == None:
                return False 
        
        #No Child
        if tempCurrent.left == None and tempCurrent.right == None:
            if tempCurrent == self.root:
                self.root = None 
            elif issol:
                tempParent.left = None 
            else:
                tempParent.right = None 
        
        #One Child
        elif tempCurrent.right == None:
            if tempCurrent == self.root:
                self.root = tempCurrent.left 
            elif issol:
                tempParent.left = tempCurrent.left 
            else:
                tempParent.right = tempCurrent.left 
        
        elif tempCurrent.left == None:
            if tempCurrent == self.root:
                self.root = tempCurrent.right 
            elif issol:
                tempParent.left = tempCurrent.right 
            else:
                tempParent.right = tempCurrent.right 
        
        #Two Child
        else:
            successor = self.successor(tempCurrent) 
            if tempCurrent == self.root:
                self.root = successor 
            elif issol:
                tempParent.left = successor 
            else:
                tempParent.right = successor 
            successor.left = tempCurrent.left 
            
        return True 

    def successor(self,deleteNode):
        successorParent = deleteNode
        successor = deleteNode
        current = deleteNode.right

        while current != None:
            successorParent = successor
            successor = current
            current = current.left

        if successor != deleteNode.right:
            successorParent.left = successor.right
            successor.right = deleteNode.right

        return successor

    def minValue(self):
        tempLeft = self.root
        while tempLeft.left != None:
            tempLeft = tempLeft.left
        return tempLeft

    def maxValue(self):
        tempRight = self.root
        while tempRight.right != None:
            tempRight = tempRight.right
        return tempRight

    #Navigate prioritizing root after left nodes then right nodes
    def inorder(self,node):
        if node == None:
            return
        self.preorder(node.left)
        self.visit(node)
        self.preorder(node.right)

    #Navigate prioritizing the left nodes after root then right nodes
    def preorder(self,node):
        if node == None:
            return
        self.visit(node)
        self.preorder(node.left)
        self.preorder(node.right)

    #Navigate prioritizing the right nodes after left nodes then root
    def postorder(self,node):
        if node == None:
            return
        self.preorder(node.left)
        self.preorder(node.right)
        self.visit(node)

    def visit(self,node):
        self.nodes += str(node.value) + " "