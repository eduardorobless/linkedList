class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.start_node = None        
    def traverse_list(self):
        if self.start_node is None:
            print('List has no element')
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.ref

    def countLL(self, i):
        occur=0
        if self.start_node is not None:        
            n = self.start_node            
            while n is not None:
                if n.item==i:
                    occur+=1
                n = n.ref
        return occur

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node= new_node    
    

if __name__=="__main__":
    new_linked_list = LinkedList()
    new_linked_list.insert_at_start(5)
    new_linked_list.insert_at_start(2)
    new_linked_list.insert_at_start(4)
    new_linked_list.insert_at_start(9)
    new_linked_list.insert_at_start(0)
    new_linked_list.insert_at_start(0)
    new_linked_list.insert_at_start(4)
    new_linked_list.insert_at_start(9)
    new_linked_list.insert_at_start(0)
    new_linked_list.insert_at_start(9)
    

    new_linked_list.traverse_list()
    
    el=0
    print('\n')


    diccionario={}
    for i in range(11):
        #print(i, new_linked_list.countLL(i))
        diccionario[i]=new_linked_list.countLL(i)
    
    for i,v in diccionario.items():
        print('soy un diccionario', i,v)

    mayor=0
    for i,v in diccionario.items():        
        mayor=max(mayor,v)
    print(mayor)
    indexMayor=0
    for i,v in diccionario.items():        
        if v==mayor:            
            indexMayor=max(indexMayor,i)

    print(indexMayor)
    
    
