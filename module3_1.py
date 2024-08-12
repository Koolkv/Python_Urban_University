calls = 0
string = 'APPLE'
list_to_search = ['Perry', 'm1lk', 'Milk', 'Cheese', 'Tomato', 'APPLE']


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    len_ = len(string)
    up_str = string.upper()
    low_str = string.lower()
    return (len_, up_str, low_str)


def is_contains(string, list_to_search):
    count_calls()
    transform_list = []
    low_str = string.lower()
    for i in list_to_search:
        transform_list.append(i.lower())
    if low_str in transform_list:
        return True
    else:
        return False


result_string_info = string_info(string)
result_is_contains = is_contains(string,list_to_search)
print(result_string_info)
print(result_is_contains)
print(calls)

string = 'abra-kadabra'

result_string_info = string_info(string)
result_is_contains = is_contains(string,list_to_search)
print(result_string_info)
print(result_is_contains)
print(calls)

result_string_info = string_info('raketa')
result_is_contains = is_contains('surprise',['super', 'puper', 'mega', 'gigabite'])
print(result_string_info)
print(result_is_contains)
print(calls)