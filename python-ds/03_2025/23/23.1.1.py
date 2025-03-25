
import os

file_name = 'admin.bat'

print(os.path.abspath(file_name))
print(os.path.relpath(file_name))

abs_path = os.path.abspath(file_name)
print('   Абсолютный путь до файла:', abs_path)

rel_path = os.path.join(file_name)
print('Относительный путь до файла:', rel_path)


