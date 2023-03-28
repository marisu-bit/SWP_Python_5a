import random
class dNode:

    def __init__(self, data):

        self.prev = None
		# Daten vom Node
        self.data = data

        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail= None
		
    def append(self, data):
        new = dNode(data)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            new.prev = self.tail 
            self.tail = new
	    
    def display(self):
		## printing the data in normal order
        print("Normal Order: ", end='')

        temp_node = self.head
        while temp_node != None:
            print(temp_node.data, end=' ')
            temp_node = temp_node.next
	    
    def reverse_display(self):
		## getting the last node
        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next

        temp_node = last_node
        while temp_node != None:
            print(temp_node.data, end=' ')
            temp_node = temp_node.prev

    def length(self):
        cur = self.head
        l = 0
        while cur != None:
            l +=1
            cur = cur.next 
        print(l)	
	
        return l
       
	
    def clear(self):
        self.head = None
        self.tail = None
    def append_randoms_numbers(self, anz, limit):
        for i in range(anz):
            self.append(int(random.random()*limit))



    def first(self):
        return self.get_element(0)

    def last(self):
        return self.get_element(self.length()-1)
    
    def get_element(self, pos):
        if pos == 0: return self.head.data
        cur = self.head
        for i in range(0,pos):
            cur = cur.next
        return cur.data
    
    def search(self,element):
            current = self.head
            for i in range(self.length()-1):
                if current.data == element: 
                    return i
                current = current.next 
            return None	
    
if __name__ == '__main__':

    list=LinkedList()

    list.append_randoms_numbers(10,10)		
    list.display()

    list.reverse_display()
    print(list.search(4))
    print(list.last())
    print(list.first)

    list.clear()
    list.display