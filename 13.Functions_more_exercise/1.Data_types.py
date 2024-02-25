def string_reader(data_type, data_number):
    if data_type == 'int':
        data_number = int(data_number) * 2
    elif data_type == 'real':
        data_number = float(data_number) * 1.5
        result = f'{data_number:.2f}'
        return result
    elif data_type == 'string':
        data_number = f'${data_number}$'
    return data_number

data_type = input()
data_number = input()
print(string_reader(data_type, data_number))