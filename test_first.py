
def combine(keys, values):
    key_len = len(keys)
    value_len = len(values)
    if key_len > value_len:
        for i in range(key_len-value_len):values.append(None)
    my_dict = dict(zip(keys, values))
    return my_dict


key_lst = ['key1', 'key2', 'key3', 'key4', 'key5', 'key6']
value_lst = ['value1', 'value2', 'value3']
print(combine(key_lst, value_lst))
