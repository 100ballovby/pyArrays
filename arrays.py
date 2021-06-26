class Array:
    def __init__(self, size, defaultValue=None):
        self.size = size
        if not defaultValue:
            self.items = list()
            for i in range(size):
                self.items.append(defaultValue)
        else:
            self.items = list()
            if len(defaultValue) <= size:
                for j in range(len(defaultValue)):
                    self.items.append(defaultValue[j])
                for k in range(len(defaultValue), size):
                    self.items.append(None)
            else:
                print('Elements are more than the size specified!')

    def __str__(self):
        '''Выводит содержимое получившегося массива'''
        return f'{self.items}'

    def getLength(self):
        '''Возвращает фактическую длину массива БЕЗ None'''
        length = 0
        for i in self.items:
            if i is not None:
                length += 1
        return length

    def insertFirst(self, element):
        if self.getLength() < self.size:
            for i in range(self.getLength(), 0, -1):
                self.items[i] = self.items[i - 1]
            self.items[0] = element
        else:
            print('Element index out of range!')

    def insertAtIndex(self, index, element):
        if self.getLength() < self.size:
            for i in range(self.getLength(), index, -1):
                self.items[i] = self.items[i - 1]
            self.items[index] = element
        else:
            print('Element index out of range')

    def insertAfterIndex(self, index, element):
        if self.getLength() < self.size:
            for i in range(self.getLength(), index + 1, -1):
                self.items[i] = self.items[i - 1]
            self.items[index + 1] = element
        else:
            print('Element index out of range')

    def insertBeforeIndex(self, index, element):
        if self.getLength() < self.size:
            for i in range(self.getLength(), index - 1, -1):
                self.items[i] = self.items[i - 1]
            self.items[index - 1] = element
        else:
            print('Element index out of range')

    def delete(self, element):
        if element in self.items:
            Index = self.items.index(element)
            self.items[Index] = None
        else:
            print('This element is not in the Array!')

    def search(self, element):
        if element in self.items:
            position = 0
            for i in range(self.getLength()):
                if self.items[i] == element:
                    break
                else:
                    position += 1
            print(f'Element {element} found at position {position}')
        else:
            print('This element is not in the Array!')


a = Array(8, [1, 4, 5, 12, 89, 9])
print(a)
a.delete(12)
print(a)


