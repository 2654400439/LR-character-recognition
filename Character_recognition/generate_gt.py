import os

file_path = './data_test/gt.txt'
file_path_list = os.listdir('./data_test/test')
with open(file_path,'w') as file:
    for i in range(len(file_path_list)):
        # file.write('test/'+file_path_list[i]+'\t@#&:'+ file_path_list[i].split('.')[0].split('_')[0] +'\n')
        file.write('test/' + file_path_list[i] + '\t@#&:0' + str(i) + '\n')
