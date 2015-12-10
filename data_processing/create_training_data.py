'''
Created on Nov 27, 2015

@author: kannanharidas
'''

import Image
import os
from random import randint
from fileinput import filename
import csv

#REFERENCE: http://effbot.org/imagingbook/image.htm

if __name__ == '__main__':
    pass

testing_files_label ={}
training_files_label ={}

testing_files_path = "./../Test_Images/Testing/"
training_files_path = "./../Test_Images/Training/"

test_file_names =  os.listdir(testing_files_path)
train_file_names = os.listdir(training_files_path)
test_files_with_sparky =0
train_files_with_sparky =0

#Open test folder and superimpose Sparky in random positions

for file_name in test_file_names:
    try:
        rand_int = randint(0,9)
        if rand_int % 2 == 0 :
            background = Image.open(testing_files_path+file_name)
            foreground = Image.open("rsz_sparky.gif")
            new_foreground = foreground.convert('RGBA')
            x,y = foreground.size
            x_rand = randint(0,374)
            y_rand = randint (0,241)
            background.paste(new_foreground, (x_rand, y_rand ,x_rand+10 ,y_rand+15), new_foreground)
            background.save(testing_files_path+file_name)
            test_files_with_sparky = test_files_with_sparky +1
            testing_files_label[file_name] = 1
        else:
            testing_files_label[file_name] = 0
    except:
        pass    

#Open train folder and superimpose Sparky in random positions
for file_name in train_file_names:
    try:
        rand_int = randint(0,9)
        if rand_int % 2 == 0 :
            background = Image.open(training_files_path+file_name)
            foreground = Image.open("rsz_sparky.gif")
            new_foreground = foreground.convert('RGBA')
            x,y = foreground.size
            x_rand = randint(0,374)
            y_rand = randint (0,241)
            background.paste(new_foreground, (x_rand, y_rand ,x_rand+10 ,y_rand+15), new_foreground)
            background.save(training_files_path+file_name)
            train_files_with_sparky = train_files_with_sparky +1
            training_files_label[file_name] = 1
        else:
            training_files_label[file_name] = 0
    except:
        pass    
training_files_labels_file = open("training_files_labels.csv","wb")
writer1 = csv.writer(training_files_labels_file)
testing_files_labels_file = open("testing_files_labels.csv","wb")
writer2 = csv.writer(testing_files_labels_file)

for key, value in training_files_label.iteritems():
    writer1.writerow([key,value])
for key, value in testing_files_label.iteritems():
    writer2.writerow([key,value])

training_files_labels_file.close()
testing_files_labels_file.close()
