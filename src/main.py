import os
import shutil

from copystatic import copy_dir_recursive

os_static_path = "./static/"
os_public_path = "./public/"

def main():
    copy_static_files(os_static_path, os_public_path)
    

def copy_static_files(src_dir, dest_dir):
    print("Deleting Public Directory...")
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    print("Copying files to public directory...")
    copy_dir_recursive(src_dir, dest_dir)


main()
