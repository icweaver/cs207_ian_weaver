class BinaryTree: 
    
    def __init__(self):
        self.val = None # parent node value
        self.l = None # points left
        self.r = None # points right
        
    def insert(self, val):
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
        # to "delete" a node, this actually replaces the node's value with 
        # its appropriate child's value, then connects this overwritten node to 
        # its former grandchildren before erasing the original child.
        
        # move to node to be deleted
        if self.val == val:
            pass # root node handled in Case 3
        else:
            while self.val != val:
                if val < self.val:
                    self = self.l
                else:
                    self = self.r
                       
        # Case 1: Node to delete has no children
        if (not self.l) and (not self.r):
            self = None
    
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
        if depth == 0: # easiest case
            return [self.val]
        
        # else
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
