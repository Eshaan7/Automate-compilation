"""
Author: Eshaan Bansal
github: github.com/eshaan7

                         WHAT THE SCRIPT DOES:
    1. goes into a directory(user inputs the directory path)
    2. Add all files recursively to <>.tar and pipe them through gzip -9 to get
       best compression creating <>.tar.gz
    3. Appends all of these individual <>.tar.gz files into another tarball.
    4. Finally <>.tar #{compress ffs please} > <>.tar.gz  
"""

import os

dir_name=str(raw_input("Full path to Directory name(example: /home/...): ")) #Step 1
os.chdir(dir_name) 
os.system("ls > file_names.txt")
file=open("file_names.txt", 'r')
lines=file.readlines()
lines = [perline.rstrip('\n') for perline in lines]
lines.remove("file_names.txt")
file.close()
os.system('rm file_names.txt')
print lines
os.system("touch `basename %(dir_name)s`.tar" % locals() )
for name in lines:
    os.system("tar -cv --recursively \"%(name)s\" | gzip -9 > \"%(name)s\".tar.gz" % locals()) #Step 2
    os.system("tar --append --remove-file --file=Desktop.tar \"%(name)s\".tar.gz " % locals()) #Step 3
os.system("gzip -9 Desktop.tar > Desktop.tar.gz") #Step 4


