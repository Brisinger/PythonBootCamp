

# Creates a new dictionary with keys and values interchanged.
def transposeDictionary(dict_current: dict) -> dict:
    result = {}
    for key, val in dict_current.items():
        if result.get(val, None):
            result[val].append(key)
        else:
            result[val] = list([key])
    return result

if __name__ == '__main__':
    my_dict = {1 : 'a', 2: 'c', 3: 'c', 4: 'a', 5: 'b'}
    result = transposeDictionary(my_dict)
    print(result)