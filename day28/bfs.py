from binary_tree import Node

def bfs(root):
    if root is None:
        return
    queue = [root]
    result = []
    
    while queue:
        ele = queue.pop(0)
        result.append(ele.data)
        if ele.left:
            queue.append(ele.left)
        if ele.right:
            queue.append(ele.right)
            
    print(result)

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')

bfs(root)