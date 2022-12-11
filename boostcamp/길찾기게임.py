import sys

class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.left = None
        self.right = None

    def __lt__(self, other):
        if(self.y == other.y):
            return self.x < other.x

        return self.y > other.y

def addNode(parent, child):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            addNode(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            addNode(parent.right, child)

def preorder(ans, node):
    if node is None:
        return
    ans.append(node.id)
    preorder(ans, node.left)
    preorder(ans, node.right)

def postorder(ans, node):
    if node is None:
        return
    postorder(ans, node.left)
    postorder(ans, node.right)
    ans.append(node.id)

def solution(nodeinfo):
    sys.setrecursionlimit(1500)
    size = len(nodeinfo)
    nodelist = []
    for i in range(size):
        nodelist.append(Node(i+1, nodeinfo[i][0], nodeinfo[i][1]))
    
    nodelist.sort()
    root = nodelist[0]
    for i in range(1,size):
        addNOde(root, nodelist[i])

    answer = [[],[]]
    preorder(answer[0], root)
    postorder(answer[1], root)
    return answer