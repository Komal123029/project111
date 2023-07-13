import os
import shutil

from_dir = "A:/Users/Naveen/Desktop/Python/class111"
to_dir = "A:/Users/Naveen/Desktop/Python/class111/test"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for i in list_of_files:
   root,ext = os.path.splitext(i)
   print(root)
   print(ext)