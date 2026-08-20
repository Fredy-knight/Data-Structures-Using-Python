class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
            
        if key < root.key:
            return self._search(root.left, key)
            
        return self._search(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            root.key = self._min_value(root.right).key
            
            root.right = self._delete(root.right, root.key)

        return root

    def _min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, root, result):
        if root:
            self._inorder(root.left, result)
            result.append(root.key)
            self._inorder(root.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, root, result):
        if root:
            result.append(root.key)                  
            self._preorder(root.left, result)   
            self._preorder(root.right, result)  

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, root, result):
        if root:
            self._postorder(root.left, result)  
            self._postorder(root.right, result) 
            result.append(root.key)


bst = BinarySearchTree()

n = int(input("Enter no.of elements : "))
list=[]
for i in range (0,n):
    element = int(input("Enter element : "))
    list.append(element)

for l in list:
    bst.insert(l)
    
print("In-order Traversal:", bst.inorder())
print("Pre-order Traversal:", bst.preorder())
print("Post-order Traversal:", bst.postorder())

search_e = int(input("Enter element to search : "))

print(f"Is {search_e} in the tree?", bst.search(search_e))

delete_e = int(input("Enter element to delete : "))
bst.delete(delete_e)

print("After deletions:", bst.inorder())

