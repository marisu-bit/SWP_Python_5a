#Folgende Anforderungen sind gegeben:
#- Datenstruktur als Objekt instanzierbar
#- Ganzahl-werte als Werte der Datenstruktur
#- programmiere Methode "am Ende Hinzufügen"
#- programmiere Ausgabe Länge der Datenstruktur
#- Ausgabe aller Elemente
#- main mit exemplarischen (Zufallszahlen) Befüllen

import random


class Node:

	def __init__(self, data):
		## data of the node
		self.data = data

		## next pointer
		self.next = None

class LinkedList:

    def __init__(self):
		## initializing the head with None macht die node class
        self.head = None

    def insert(self, new_node):
		# ist der Kopf leer?
        if self.head:
            #der letzte knoten
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next

			#neuer knoten ist der nächste des letzten knoten
            last_node.next = new_node

        else:
			#ist leer
            #neuer knoten
            self.head = new_node




    def display(self):
		## variable for iteration
        temp_node = self.head
       
		## iterating until we reach the end of the linked list
        while temp_node != None:
			## printing the node data
            print(temp_node.data, end=',')

			## moving to the next node
            temp_node = temp_node.next

      
    
   
    def length(self):
        temp_node=self.head
        cnt=0
        while temp_node is not None:
            cnt +=1
            temp_node=temp_node.next
        return cnt


if __name__ == '__main__':
	
    linked_list = LinkedList()

	## inserting the data into the linked list
    for num in range(21):
        linked_list.append(random.randint(1, 100))
  


	## printing the linked list
    linked_list.display()