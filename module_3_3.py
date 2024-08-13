def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, '2', (3, 4, True)]
values_dict = {'a': 5, 'b': 'surprise', 'c': (6, 'seven', [8, 9, 10])}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['True', False]
print_params(*values_list_2, 42)
