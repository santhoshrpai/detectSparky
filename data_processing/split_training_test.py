'''
Created on Nov 27, 2015

@author: kannanharidas
'''

import os
import shutil
from random import randint
from fileinput import filename

if __name__ == '__main__':
    pass

input_path = "./../image.cd/2/"
testing_files_path = "./../Test_Images/Testing/"
training_files_path = "./../Test_Images/Training/"

input_file_names = os.listdir(input_path)

test_count = 0
train_count =0

for file_name in input_file_names:
    rand_int = randint(0,9)
    if rand_int % 2 ==0:
        test_count = test_count + 1
        shutil.copy2(input_path+file_name, testing_files_path+file_name)
    else:
        train_count = train_count + 1
        shutil.copy2(input_path+file_name , training_files_path + file_name)

print test_count
print train_count