import types

def flat_generator(list_of_list):
    current_list = iter(list_of_list)  
    upper_list = []
    while True:
        try:
            item = next(current_list)
        except:
            if upper_list:
                current_list = upper_list.pop()
                continue
            else:
                break
        if type(item) is not list:
            yield item
        else:
            upper_list.append(current_list)
            current_list = iter(item)

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()