class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list    

    def __iter__(self):
        self.current_list = iter(self.list_of_list)  
        self.upper_list = []
        return self
    
    def __next__(self):
        try:
            item = next(self.current_list)
        except:
            if self.upper_list:
                self.current_list = self.upper_list.pop()
                return next(self)
            else:
                raise StopIteration
        if type(item) is not list:
            return item
        else:
            self.upper_list.append(self.current_list)
            self.current_list = iter(item)
            return next(self)

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()