# -*- coding: utf-8 -*-
import shutil
import os

path = 'C:/Users/Administrator/Desktop/python_excel/files'
files = os.listdir(path)
for f in files:
    folder_name = os.path.join('.',f.split('.')[-1])
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        shutil.move(f,folder_name)
    else:
        shutil.move(f,folder_name)