import os
import shutil
import random

path = './data_total'
file_path_list = os.listdir(path)
file_list_sub = random.sample(file_path_list, int(len(file_path_list)*0.3))
for i in range(len(file_list_sub)):
    shutil.move(path+'/'+file_list_sub[i], './data_val/'+file_list_sub[i])
