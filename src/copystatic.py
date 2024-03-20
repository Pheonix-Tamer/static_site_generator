from genericpath import isdir, isfile
import os
import shutil

def copy_dir_recursive(src_dir, dst_dir):# -> Any:
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)
        
    for filename in os.listdir(src_dir):
        from_path = os.path.join(src_dir, filename)
        dest_path = os.path.join(dst_dir, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_dir_recursive(from_path, dest_path)


