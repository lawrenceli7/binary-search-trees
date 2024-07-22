class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, array):
        self.root = self.buildTree(sorted(set(array)))

    def buildTree(self, array):
        if not array:
            return None
        middle = len(array) // 2
        root = Node(array[middle])
        root.left = self.buildTree(array[:middle])
        root.right = self.buildTree(array[middle + 1 :])
        return root

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insertRecursive(self.root, value)

    def insertRecursive(self, node, value):
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insertRecursive(node.left, value)
        elif value > node.data:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insertRecursive(node.right, value)

    def delete(self, value):
        self.root = self.deleteRecursive(self.root, value)

    def deleteRecursive(self, node, value):
        if node is None:
            return node
        if value < node.data:
            node.left = self.deleteRecursive(node.left, value)
        elif value > node.data:
            node.right = self.deleteRecursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            tempVal = self.minValueNode(node.right)
            node.data = tempVal.data
            node.right = self.deleteRecursive(node.right, tempVal.data)
        return node

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find(self, value):
        return self.findRecursive(self.root, value)

    def findRecursive(self, node, value):
        if node is None or node.data == value:
            return node
        if value < node.data:
            return self.findRecursive(node.left, value)
        return self.findRecursive(node.right, value)

    def levelOrder(self, callback=None):
        if self.root is None:
            return []
        queue = [self.root]
        result = []
        while queue:
            node = queue.pop(0)
            if callback:
                callback(node)
            else:
                result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result if not callback else None

    def inOrder(self, callback=None):
        result = []
        self.inOrderRecursive(self.root, result, callback)
        return result if not callback else None

    def inOrderRecursive(self, node, result, callback):
        if node:
            self.inOrderRecursive(node.left, result, callback)
            if callback:
                callback(node)
            else:
                result.append(node.data)
            self.inOrderRecursive(node.right, result, callback)

    def preOrder(self, callback=None):
        result = []
        self.preOrderRecursive(self.root, result, callback)
        return result if not callback else None

    def preOrderRecursive(self, node, result, callback):
        if node:
            if callback:
                callback(node)
            else:
                result.append(node.data)
            self.preOrderRecursive(node.left, result, callback)
            self.preOrderRecursive(node.right, result, callback)

    def postOrder(self, callback=None):
        result = []
        self.postOrderRecursive(self.root, result, callback)
        return result if not callback else None

    def postOrderRecursive(self, node, result, callback):
        if node:
            self.postOrderRecursive(node.left, result, callback)
            self.postOrderRecursive(node.right, result, callback)
            if callback:
                callback(node)
            else:
                result.append(node.data)

    def height(self, node):
        if node is None:
            return -1
        leftHeight = self.height(node.left)
        rightHeight = self.height(node.right)
        return max(leftHeight, rightHeight) + 1

    def depth(self, node):
        return self.depthRecursive(self.root, node, 0)

    def depthRecursive(self, current, node, depth):
        if current is None:
            return -1
        if current.data == node.data:
            return depth
        if node.data < current.data:
            return self.depthRecursive(current.left, node, depth + 1)
        return self.depthRecursive(current.right, node, depth + 1)

    def isBalanced(self):
        return self.isBalancedRecursive(self.root)

    def isBalancedRecursive(self, node):
        if node is None:
            return True
        leftHeight = self.height(node.left)
        rightHeight = self.height(node.right)
        if abs(leftHeight - rightHeight) > 1:
            return False
        return self.isBalancedRecursive(node.left) and self.isBalancedRecursive(
            node.right
        )

    def rebalance(self):
        nodes = self.inOrder()
        self.root = self.buildTree(nodes)


import random


def generateRandomArray(size, maxValue=100):
    return random.sample(range(maxValue), size)


randomArray = generateRandomArray(15)
bst = BST(randomArray)

print("Is tree balanced?", bst.isBalanced())

print("Level-order:", bst.levelOrder())
print("Pre-order:", bst.preOrder())
print("Post-order:", bst.postOrder())
print("In-order:", bst.inOrder())

for value in [101, 102, 103, 104, 105]:
    bst.insert(value)

print("Is tree balanced?", bst.isBalanced())

bst.rebalance()

print("Is tree balanced?", bst.isBalanced())

print("Level-order:", bst.levelOrder())
print("Pre-order:", bst.preOrder())
print("Post-order:", bst.postOrder())
print("In-order:", bst.inOrder())
