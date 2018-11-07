class BinaryTree: 
    
    def __init__(self):
        self.val = None # parent node value
        self.l = None # points left
        self.r = None # points right
        
    def insert(self, val):
        """ Inserts node into binary search tree
        """
        # create child node to be inserted
        child = BinaryTree()
        child.val = val
        
        if self.val == None: # start off tree if empty
            self.val = val
        
        else:
            while self.val: # also catches if node -> None from remove(...)
                # left branch
                if (child.val < self.val):
                    if self.l is None:
                        self.l = child # insert
                        break
                    else: # keep moving down left side
                        self = self.l

                # right branch
                else:
                    if self.r is None:
                        self.r = child # insert
                        break
                    else: # keep moving down right side
                        self = self.r
    
    def remove(self, val):
        """ Deletes node in three steps. 
        
        1) Replaces the node's value with its appropriate child's value
        
        2) Connects this overwritten node to its former grandchildren 
        
        3) Erases the original child. 
        """
        # move to node to be deleted
        if self.val == val:
            pass # root node handled in Case 3
        else:
            try:
                while self.val != val:
                    if val < self.val:
                        self = self.l
                    else:
                        self = self.r
            except AttributeError: # catch if val not in tree
                print('Node not in tree, not going to do anything')
                return
                       
        # Case 1: Node to delete has no children
        if (not self.l) and (not self.r):
            self.val = None
    
        # Case 2: Node to delete has 1 child
        elif self.l and (not self.r):
            self.val = self.l.val # replace with child value
            # connect to grandchildren
            if self.l.l: self.l = self.l.l
            if self.l.r: self.r = self.l.r
            self.l = None # erase child
        elif self.r and (not self.l):
            self.val = self.r.val # replace with child value
            # connect to grandchildren
            if self.r.l: self.l = self.r.l
            if self.r.r: self.r = self.r.r
            self.r = None # erase child
        
        # Case 3: Node to delete has two children
        elif self.l and self.r:
            max_node = self # create copy of node to be deleted [
            # will avoid overwriting where we are (at node to be deleted)]
            max_node = max_node.l # find max val in left sub-branch
            if max_node.r: # keep moving down right side
                while max_node.r:
                    max_node = max_node.r   
            # else, the largest value must be the first left child
            self.val = max_node.val # replace with child value
            # connect to grandchildren
            if max_node.l: self.l = max_node.l
            if max_node.r: self.r = max_node.r
            max_node = None # erase child
        else:
            print('something went wrong')
            
    def getValues(self, depth):
        """ Prints row of binary search tree at specified depth.

            ex) getValues(2) returns a list, where each element is the
            corresponding node (including blank spaces) on the 
            second row (zero-indexed)
        """
        if depth+1 > len(self):
            m = f'specified depth larger than max tree height={len(self)}'
            raise IndexError(m)

        if depth == 0: # root case
            return [self.val]
        
        row_current = [self] # will be replaced "row by row" in place
        for d in range(depth):
            row_print = [None]*2**(d+1) # reset row for next level
            row_idx = 0 # reset node index for next level
            row_next = [] # will hold row a level down
            for n in row_current: # loop through nodes at current level
                if n and n.l: 
                    row_next.append(n.l)
                    row_print[row_idx] = n.l.val
                    row_idx += 1
                else: # fill in gaps in tree
                    row_next.append(None) 
                    row_idx += 1
                if n and n.r: 
                    row_next.append(n.r)
                    row_print[row_idx] = n.r.val
                    row_idx += 1
                else: # fill in gaps in tree
                    row_next.append(None)
                    row_idx += 1
                    
            row_current = row_next # move down a level
        return row_print

    def max_height(self, n):
        # base case
        if n is None:
            return 0
        
        else:
            # recursively return depth below current node
            depth_l = self.max_height(n.l)
            depth_r = self.max_height(n.r)
            
            # the larger depth (+ 1 to include root level) is our max depth
            if depth_l > depth_r:
                return depth_l + 1
            else:
                return depth_r + 1

    def __len__(self):
        return self.max_height(self)

class DFSTraversal():
    def __init__(self, tree, traversalType):
        self.index = 0
        self.tree = tree
        self.traversalType = traversalType
    
    # Change the traversal type
    def changeTraversalType(self, traversalType):
        return
        
    #This is the initialization of an iterator
    def __iter__(self):
        return self
    
    # This is called in the iterator for getting the next value
    def __next__(self): 
        try:
            if self.traversalType.name == 'PREORDER':
                result = self.preorder(self.tree)[self.index]

            elif self.traversalType.name == 'INORDER':
                result = self.inorder(self.tree)[self.index]

            elif self.traversalType.name == 'POSTORDER':
                result = self.postorder(self.tree)[self.index]

            else:
                raise KeyError('Must supply appropriate enum object')

        except IndexError:
            raise StopIteration

        self.index += 1
        return result

    nodes = []
    def inorder(self, bt, nodes=nodes):

        if bt and bt.l:
            self.inorder(bt.l)

        nodes.append(bt.val)

        if bt and bt.r:
            self.inorder(bt.r)
        return nodes

    def preorder(self, bt):
        # implement here
        # bt is an instance of BinaryTree class from previous hw
        return

    def postorder(self, bt):
        # implement here
        # bt is an instance of BinaryTree class from previous hw
        return
