#!/bin/sh

: '
Author: Eshaan Bansal
github: github.com/eshaan7

                    WHAT THE SCRIPT DOES:
    1. goes into a directory(user inputs the directory path)
    2. Archive all files recursively to .tar and pipe them through gzip -9 to get
       best compression creating <>.tar.gz
    3. Appends all of these individual <>.tar.gz files into another tarball.
    4. Finally .tar #{compress ffs please} > .tar.gz  
'
    
echo "Full path to Directory name(example: /home/...): "
read dir_name #Step 1
cd "$dir_name"
dir_base_name=`basename $dir_name` 
ls > file_name.txt
touch ${dir_base_name}.tar
while IFS="" read -r lines || [ -n "$lines" ]
do
  tar -acv --recursion $lines | gzip -9 > ${lines}.tar.gz  #Step 2
  tar --append --remove-file --file=${dir_base_name}.tar ${lines}.tar.gz #Step 3
done < file_name.txt
gzip -9 ${dir_base_name}.tar > ${dir_base_name}.tar.gz #Step 4
rm file_name.txt

