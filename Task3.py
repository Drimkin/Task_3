import os

files = os.listdir('.')

files = [file for file in files if file.endswith('.txt')]

files_info = {}

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        files_info[file] = {
            'num_lines': len(lines),
            'content': lines
        }

files_sorted = sorted(files_info.items(), key=lambda x: x[1]['num_lines'])

with open('result.txt', 'w', encoding='utf-8') as f:
    for file_info in files_sorted:
        file_name = file_info[0]
        num_lines = file_info[1]['num_lines']
        content = file_info[1]['content']

        f.write(file_name + '\n')
        f.write(str(num_lines) + '\n')
        f.write(''.join(content) + '\n')
