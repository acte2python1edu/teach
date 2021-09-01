def generate_ints(N):
   for i in range(N):
       yield i
        
r=generate_ints(5)
next(r)



def inorder(t):
    if t:
        for x in inorder(t.left):
            yield x

        yield t.label

        for x in inorder(t.right):
            yield x
            
            
            
            
            
