def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)   
        print(root.data)                
        in_order_traversal(root.right)  

            
def pre_order_traversal(root):
    if root is not None: 
        print(root.data)
        pre_order_traversal(root.left)                  
        pre_order_traversal(root.right)  
        
def post_order_traversal(root):
    if root is not None: 
        post_order_traversal(root.left)                  
        post_order_traversal(root.right)  
        print(root.data)