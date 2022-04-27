from timeit import timeit

ids = ["1", "2", "3"]
values = ["a", "b", "c"]
keys = ["id", "value"]


def map_row():  # mapping + dict init
    return list(map(lambda row: dict(zip(keys, row)), zip(ids, values)))

def list_row():  # list comprehension + dict init
    return [dict(zip(keys, row)) for row in zip(ids, values)]

def map_dict():  # mapping + dict comprehension
    return list(map(lambda row: {keys[0]: row[0], keys[1]: row[1]}, zip(ids, values)))

def list_dict():  # list comprehension + dict comprehension
    return [{keys[0]: id, keys[1]: value} for id, value in zip(ids, values)]


#  [{'id': '1', 'value': 'a'}, {'id': '2', 'value': 'b'}, {'id': '3', 'value': 'c'}]
print(map_row())
print(list_row())
print(map_dict())
print(list_dict())


print(timeit(map_row, number=100000))  # 0.024576399999205023
print(timeit(list_row, number=100000))  # 0.024218899983679876
print(timeit(map_dict, number=100000))  # 0.013014900003327057
print(timeit(list_dict, number=100000))  # 0.009650299994973466
