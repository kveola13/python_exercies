import os
import random
import shutil


def remove_folders(folder):
    if os.path.exists(folder):
        shutil.rmtree(folder)


def create_folder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)
        os.chdir(folder)
        print(os.getcwd())
        rand_list = random.sample(range(97, 123), 26)
        for el in rand_list:
            os.mkdir(chr(el))


def main():
    folder_name = "testfolder"
    create_folder(folder_name)
    remove_folders(folder_name)


if __name__ == '__main__':
    main()
