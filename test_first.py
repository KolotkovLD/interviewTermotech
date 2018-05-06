def combine(keys, values):
    key_len = len(keys)
    value_len = len(values)
    if key_len > value_len:
        for i in range(key_len-value_len):
            values.append(None)
    return dict(zip(keys, values))


key_lst = ['key1', 'key2', 'key3', 'key4', 'key5', 'key6']
value_lst = ['value1', 'value2', 'value3']
new_dict = combine(key_lst, value_lst)
