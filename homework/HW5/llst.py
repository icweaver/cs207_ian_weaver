class LinkedList():
    
    def __init__(self, head):
        self._headNode = [head, None] # only one node, so points to None
    
    def __len__(self):
        node = self._headNode # create pointer
        node_count = 0 # keeps track of node index
        while node is not None:
            node = node[1] # move pointer to next node 
            node_count += 1 # update node index as well
        return node_count
        
    def __getitem__(self, index):
        node = self._headNode # create pointer
        
        # catch user trying to getitem on empty list
        try: node[index]
        except IndexError:
            print('trying to index empty list')

        # catch user trying to get index outside of current list
        if (index+1) > len(self): # catch if index is out of bounds
            raise IndexError   
        
        node_idx = 0 # keeps track of node index            
        while node is not None:
            if node_idx == index: # found a match
                return node[0]
                break # don't need to keep walking along chain
            node = node[1] # move pointer to next node
            node_idx += 1 # update node index as well 
    
    def __repr__(self):
        s = f'llst.LinkedList({self._headNode[0]})'
        return s
    
    def insert_front(self, element):
        # sets element as head node
        self._headNode = [element, self._headNode]
    
    def insert_back(self, element):
        # appends element to end
        tail = self._headNode # pointer for self._headNode
        while tail[1] is not None: 
            tail = tail[1] # traverse pointer to last node
            
        tail[1] = [element, None] # append element
