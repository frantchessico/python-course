import subprocess
import os
# f = open('index.js', 'rt')

# print(f.read())


# Abre o arquivo index.js em modo de leitura de texto
with open('index.js', 'rt') as file:
    # Lê o conteúdo do arquivo
    js_code = file.read()

# Executa o código JavaScript usando o interpretador Node.js
result = subprocess.run(['node', '-e', js_code])

# Imprime a saída do código JavaScript
print(result.stdout)

file_txt = open('file.txt', 'w');

file_txt.write('Full name: Francisco Jaime Inoque');
file_txt.close()

file_txt = open('file.txt', 'rt');
print(file_txt.read())


if os.path.exists('file.txt'):
    os.remove('file.txt')
    print('Removed successfully')

os.rmdir('folder')