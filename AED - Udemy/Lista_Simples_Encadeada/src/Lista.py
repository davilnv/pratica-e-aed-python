class Node:
    def __init__(self, label):
        self.label = label
        self.next = None
    
    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class Linked_List:
    def __init__(self):
        self.first = None
        self.last = None
        self.len_list = 0

    def push(self, label, index):
        if index >= 0:
            # Cria um novo No
            node = Node(label)
            # Verifica se a lista está vazia
            if self.empty():
                self.first = node
                self.last = node
            else:
                if index == 0:
                    # Inserção no início
                    node.set_next(self.first)
                    self.first = node
                elif index >= self.len_list:
                    # Inserção no fim
                    self.last.set_next(node)
                    self.last = node
                else:
                    # Inserção no meio
                    prev_node = self.first
                    curr_node = self.first.get_next()
                    curr_index = 1
                    while curr_node != None:
                        if curr_index == index:
                            # seta o curr_node como o próximo do No
                            node.set_next(curr_node)
                            # seta o node como o próximo do prev_node
                            prev_node.set_next(node)
                            break
                        prev_node = curr_node
                        curr_node = curr_node.get_next()
                        curr_index += 1
                # Atualizar o tamanho da lsita
                self.len_list += 1
    def pop(self, index):
        if not self.empty and index >= 0 and index < self.len_list:
            flag_remove = False
            if self.first.get_next() == None:
                # Possui apenas um elemento
                self.first = None
                self.last = None
                flag_remove = True
            elif index == 0:
                # Remove do inicio, mas possui mais de um elemento
                self.first = self.first.get_next()
                flag_remove = True
            else:
                prev_node = self.first
                curr_node = self.first.get_next()
                curr_index = 1
                while curr_node != None:
                    if index == curr_index:
                        # O próximo do anterior aponta para o proximo No corrente
                        prev_node.set_next(curr_node.get_next())
                        curr_node.set_next(None)
                        flag_remove = True
                        break
                    prev_node = curr_node
                    curr_node = curr_node.get_next()
                    curr_index += 1
            if flag_remove:
                # Atualiza o tamanho da lista
                self.len_list -= 1               
    
    def empty(self):
        if self.first == None:
            return True
        return False
    
    def lenght(self):
        return self.len_list
    
    def show(self):
        curr_node = self.first
        print('[', end='')
        while curr_node != None:
            print(curr_node.get_label(), end='')
            curr_node = curr_node.get_next()
            if curr_node is not None:
                print(', ', end='')
        print(']')
        print()


lista = Linked_List()
lista.push(10, 0)
lista.push(20, 1)
lista.push(30, 2)
lista.push(40, 3)
lista.show()
lista.push(100, 3)
lista.show()
lista.pop(0)
lista.pop(1)
lista.show()
