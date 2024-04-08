from Set_AVL_Tree import BST_Node, Set_AVL_Tree
#######################################
# DO NOT REMOVE THIS IMPORT STATEMENT #
# DO NOT MODIFY IMPORTED CODE         #
#######################################

class Key_Val_Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self): 
        return "%s,%s" % (self.key, self.val)

class Part_B_Node(BST_Node):
    def subtree_update(A):
        super().subtree_update()
        #########################################
        # ADD ANY NEW SUBTREE AUGMENTATION HERE #
        #########################################
        # update sum
        left_sum = 0 if A.left is None else A.left.sum
        right_sum = 0 if A.right is None else A.right.sum
        A.sum = A.item.val + left_sum + right_sum
        # update max_prefix & key
        A.max_prefix, A.max_key = max(
            ((A.left.max_prefix, A.left.max_key) if A.left else (-10000, None)),
            (left_sum + A.item.val, A.item.key),
            ((left_sum + A.item.val + A.right.max_prefix, A.right.max_key) if A.right else (-10000, None))
        )
        # print(A.item.key, A.sum, A.max_prefix, A.max_key)

class Part_B_Tree(Set_AVL_Tree):
    def __init__(self): 
        super().__init__(Part_B_Node)

    def max_prefix(self):
        '''
        Output: (k, s) | a key k stored in tree whose
                       | prefix sum s is maximum
        '''
        k, s = 0, 0
        ##################
        # YOUR CODE HERE #
        ##################
        if self.root:
            k, s = self.root.max_key, self.root.max_prefix
        return (k, s)

def tastiest_slice(toppings):
    '''
    Input:  toppings | List of integer tuples (x,y,t) representing 
                     | a topping at (x,y) with tastiness t
    Output: tastiest | Tuple (X,Y,T) representing a tastiest slice 
                     | at (X,Y) with tastiness T
    '''
    B = Part_B_Tree()   # use data structure from part (b)
    X, Y, T = 0, 0, 0
    ##################
    # YOUR CODE HERE #
    ##################
    toppings = sorted(toppings, key=lambda x: x[1])
    for x, y, t in toppings:
        B.insert(Key_Val_Item(x, t))
        tx, tt = B.max_prefix()
        T, X, Y = max((T, X, Y), (tt, tx, y))
    return (X, Y, T)
