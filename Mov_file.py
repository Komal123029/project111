import os
import shutil

from_dir = "A:/Users/Naveen/Desktop/Python/class111"
to_dir = "A:/Users/Naveen/Desktop/Python/class111/test"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for i in list_of_files:
   root,ext = os.path.splitext(i)
   #print(root)
   #print(ext)

   if(ext == " "):
    continue
   if(ext in [".txt",".doc",".docx",".pdf"]):
    path1 = from_dir + "/" + i
    path2 = to_dir + "/" + "document_files"
    path3 = path2 +  "/" + i  
    if os.path.exists(path2):
      print("moving " + i)
      shutil.move(path1,path3)
    else:
      os.makedirs(path2)
      print("moving " + i)
      shutil.move(path1,path3)
        

   

      