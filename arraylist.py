import random 

class array_list:
    def __init__(self):
        self.list = []

    def append(self, data):
        self.list.append(data)

    def append_multiple(self, *data):
        for d in data:
            self.append(d)

    def append_randoms_numbers(self, anzahl, bigestnumber):
        for i in range(anzahl):
            self.append(int(random.random()*bigestnumber))

    def insert(self, pos, data):
        self.list.insert(pos, data)

    def insert_multiple(self, pos, data):
        i = pos
        for d in data:
            self.list.insert(i, data)
            i = i+1

    def length(self):
        return self.list.count()

    def display(self):
        return self.list.__str__()
    
    def reverse_display(self):
        self.list.reverse()
        return self.list.__str__()

    def delete(self, pos):
        self.list.pop(pos)

    def pop(self):
        self.list.pop()

    def reverse(self):
        self.list.reverse()

    def clear(self):
        self.list = []

    def length(self):
       print(len(self.list))



if __name__ == '__main__':
    list = array_list()
    list.append_randoms_numbers(10,10)
    print(list.display())
    list.length()
    
