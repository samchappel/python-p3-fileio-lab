def write_file(file_name, file_content):
    if not file_name.endswith('.txt'):
        file_name += '.txt'

    with open(file_name, mode='w', encoding='utf-8') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as file:
        file.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt') as file:
       return file.read()