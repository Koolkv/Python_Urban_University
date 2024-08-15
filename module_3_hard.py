data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]


def unpacks(data):
    for item in data:
        if isinstance(item, list):
            for sub_item in unpacks(item):
                yield sub_item
        elif isinstance(item, dict):
            for sub_item in unpacks(item.items()):
                yield sub_item
        elif isinstance(item, tuple):
            for sub_item in unpacks(item):
                yield sub_item
        elif isinstance(item, set):
            for sub_item in unpacks(item):
                yield sub_item
        elif isinstance(item, str):
            yield len(item)
        else:
            yield item


print(sum(list(unpacks(data_structure))))
