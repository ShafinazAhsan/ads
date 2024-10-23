import os
import time

def directory_structure_preorder(path):
    print(path)
    
    if os.path.isdir(path):
        for entry in os.listdir(path):
            Path = os.path.join(path, entry)
            directory_structure_preorder(Path)
    else:
        size = os.path.getsize(path)
        time_created = time.ctime(os.path.getctime(path))
        print(f"  (Size: {size} bytes, Created: {time_created})")

directory = '/Users/shafinazahsan/Desktop/ads-trees'
directory_structure_preorder(directory)
