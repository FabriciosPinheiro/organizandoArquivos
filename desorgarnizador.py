import os

dir_actual = os.getcwd()

# Compreensao em Lista
folder_list = [i for i in os.listdir(dir_actual) if os.path.isdir(i)]

for folder in folder_list:
    path = os.path.join(dir_actual, folder)
    files = os.listdir(path)

    for file in files:
        from_path = os.path.join(path, file)
        to_path = os.path.join(dir_actual, file)

        os.replace(from_path, to_path)

    os.rmdir(path)