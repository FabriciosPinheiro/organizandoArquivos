import os
import shutil

actual_dir = os.getcwd()

list_dir = os.listdir(actual_dir)

for item in list_dir:
    if os.path.isfile(item) and '.py' not in item:
        extensao = item.split('.')[1]

        if not os.path.exists(extensao):
            os.mkdir(extensao)

        from_path = os.path.join(actual_dir, item)
        to_path = os.path.join(actual_dir, extensao)
        
        shutil.move(from_path, to_path)