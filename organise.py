import os
import shutil

from_dir="C:/Users/HMT/Downloads/Document_Files"
to_dir="D:/D DRIVE/JESHU/white hat jr/project102/folder2"
list_of_files=os.listdir(from_dir)
#print(list_of_files)
for filename in list_of_files:
    name,extension=os.path.splitext(filename)

    if extension=="":
        continue

    if extension in [ ".txt", ".doc", ".docx", ".pdf"]:
        path1=from_dir+"/"+filename
        path2=to_dir+"/"+"text_files"
        path3=to_dir+"/"+"text_files"+"/"+filename
        print("path1",path1)
        print("path3",path3)

        if os.path.exists(path2):
            print("moving"+filename+"...")
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("moving"+filename+"...")
            shutil.move(path1,path3)    