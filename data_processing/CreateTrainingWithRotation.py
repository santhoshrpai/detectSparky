'''
Created on Nov 27, 2015

@author: kannanharidas
'''

import Image
import os
from random import randint
from fileinput import filename
import csv
import shutil


def super_impose_image_for_testing(image_file, rotate, filepath_to_save, file_name, type):
    # background = Image.open(testing_files_path+file_name)
    if type == 0:
        background = Image.open(testing_files_path + file_name)
    else:
        background = Image.open(training_files_path + file_name)

    foreground = Image.open(image_file)
    new_foreground = foreground.convert('RGBA')
    # size = new_foreground.size
    # angle_rand = randint(0,340)
    # print "size = "+str(new_foreground.size)
    new_foreground_rotate = new_foreground.rotate(rotate)
    # new_foreground.rotate(180).show()
    print file_name + " modified!"
    x, y = foreground.size
    x_rand = randint(0, (384 - x))
    y_rand = randint(0, (256 - y))
    background.paste(new_foreground_rotate, (x_rand, y_rand, x_rand + x, y_rand + y), new_foreground_rotate)
    background.save(filepath_to_save)
    # test_files_with_sparky = test_files_with_sparky +1
    testing_files_label[file_name] = 1


def write_csv(file_path_to_save, values):
    training_files_labels_file = open(file_path_to_save, "wb")
    writer1 = csv.writer(training_files_labels_file)
    # testing_files_labels_file = open(testing_filepath+"testing_files_labels.csv","wb")
    # writer2 = csv.writer(testing_files_labels_file)

    for key, value in values.iteritems():
        writer1.writerow([key, value])
    # for key, value in values_testing.iteritems():
    #     writer2.writerow([key,value])
    training_files_labels_file.close()
    # testing_files_labels_file.close()


########################################################################################################################


def randomize_spary_superimposition(filepath_to_save, file_name, type):
    rand_int_for_sparky = randint(0, 20)
    if rand_int_for_sparky % 4 == 0:
        super_impose_image_for_testing("rsz_sparky.gif", 0, filepath_to_save, file_name, type)
    elif rand_int_for_sparky % 4 == 1:
        super_impose_image_for_testing("sparky_large.gif", 0, filepath_to_save, file_name, type)
    elif rand_int_for_sparky % 4 == 2:
        super_impose_image_for_testing("rsz_sparky.gif", randint(0, 340), filepath_to_save, file_name, type)
    elif rand_int_for_sparky % 4 == 3:
        super_impose_image_for_testing("sparky_large.gif", randint(0, 340), filepath_to_save, file_name, type)


def testing_data_full_random():
    for file_name in test_file_names:
        try:
            rand_int = randint(0, 20)
            if rand_int % 2 == 0:
                randomize_spary_superimposition(testing_files_path_with_random_sparky + file_name, file_name, 0)
            else:
                shutil.copyfile(testing_files_path + file_name, testing_files_path_with_random_sparky + file_name)
                testing_files_label[file_name] = 0
        except Exception as detail:
            print "Something bad has happened!!! This is the error ==> ", detail
    write_csv(testing_files_path_with_random_sparky + "testing_files_labels.csv", testing_files_label)

    for file_name in train_file_names:
        try:
            rand_int = randint(0, 20)
            if rand_int % 2 == 0:
                randomize_spary_superimposition(training_files_path_with_random_sparky + file_name, file_name, 1)
            else:
                shutil.copyfile(training_files_path + file_name, training_files_path_with_random_sparky + file_name)
                training_files_label[file_name] = 0
        except Exception as detail:
            print "Something bad has happened!!! This is the error ==> ", detail
    write_csv(training_files_path_with_random_sparky + "training_files_labels.csv", training_files_label)


########################################################################################################################

def small_sparky_superimposition(filepath_to_save, file_name, type):
    super_impose_image_for_testing("rsz_sparky.gif", 0, filepath_to_save, file_name, type)


def output_data_small_sparky():
    for file_name in test_file_names:
        try:
            rand_int = randint(0, 20)
            if rand_int % 2 == 0:
                small_sparky_superimposition(testing_files_path_with_small_sparky + file_name, file_name, 0)
            else:
                shutil.copyfile(testing_files_path + file_name, testing_files_path_with_small_sparky + file_name)
                testing_files_label[file_name] = 0
        except Exception as detail:
            print "Something bad has happened!!! This is the error ==> ", detail

    write_csv(testing_files_path_with_small_sparky + "testing_files_labels.csv", testing_files_label)

    for file_name in train_file_names:
        try:
            rand_int = randint(0, 20)
            if rand_int % 2 == 0:
                small_sparky_superimposition(training_files_path_with_small_sparky + file_name, file_name, 1)
            else:
                shutil.copyfile(training_files_path + file_name, training_files_path_with_small_sparky + file_name)
                training_files_label[file_name] = 0
        except Exception as detail:
            print "Something bad has happened!!! This is the error ==> ", detail
    write_csv(training_files_path_with_small_sparky + "training_files_labels.csv", training_files_label)


########################################################################################################################


def large_sparky_superimposition(filepath_to_save, file_name, type):
    super_impose_image_for_testing("sparky_large.gif", 0, filepath_to_save, file_name, type)


def output_data_large_sparky():
    for file_name in test_file_names:
        try:
            rand_int = randint(0, 20)
            if rand_int % 2 == 0:
                large_sparky_superimposition(testing_files_path_with_large_sparky + file_name, file_name, 0)
            else:
                shutil.copyfile(testing_files_path + file_name, testing_files_path_with_large_sparky + file_name)
                testing_files_label[file_name] = 0
        except Exception as detail:
            print "Something bad has happened!!! This is the error ==> ", detail

    write_csv(testing_files_path_with_large_sparky + "testing_files_labels.csv", testing_files_label)

    for file_name in train_file_names:
        try:
            rand_int = randint(0, 20)
            if rand_int % 2 == 0:
                large_sparky_superimposition(training_files_path_with_large_sparky + file_name, file_name, 1)
            else:
                shutil.copyfile(training_files_path + file_name, training_files_path_with_large_sparky + file_name)
                training_files_label[file_name] = 0
        except Exception as detail:
            print "Something bad has happened!!! This is the error ==> ", detail
    write_csv(training_files_path_with_large_sparky + "training_files_labels.csv", training_files_label)


########################################################################################################################


def small_sparky_with_angle_superimposition(filepath_to_save, file_name, type):
    super_impose_image_for_testing("rsz_sparky.gif", randint(0, 340), filepath_to_save, file_name, type)


def output_data_small_sparky_with_angle():
    for file_name in test_file_names:
        try:
            rand_int = randint(0, 20)
            if rand_int % 2 == 0:
                small_sparky_with_angle_superimposition(testing_files_path_with_small_sparky_rotate + file_name,
                                                        file_name, 0)
            else:
                shutil.copyfile(testing_files_path + file_name, testing_files_path_with_small_sparky_rotate + file_name)
                testing_files_label[file_name] = 0
        except Exception as detail:
            print "Something bad has happened!!! This is the error ==> ", detail
    write_csv(testing_files_path_with_small_sparky_rotate + "testing_files_labels.csv", testing_files_label)

    for file_name in train_file_names:
        try:
            rand_int = randint(0, 20)
            if rand_int % 2 == 0:
                small_sparky_with_angle_superimposition(training_files_path_with_small_sparky_rotate + file_name,
                                                        file_name, 1)
            else:
                shutil.copyfile(training_files_path + file_name,
                                training_files_path_with_small_sparky_rotate + file_name)
                training_files_label[file_name] = 0
        except Exception as detail:
            print "Something bad has happened!!! This is the error ==> ", detail
    write_csv(training_files_path_with_small_sparky_rotate + "training_files_labels.csv", training_files_label)


########################################################################################################################


def large_sparky_with_angle_superimposition(filepath_to_save, file_name, type):
    super_impose_image_for_testing("sparky_large.gif", randint(0, 340), filepath_to_save, file_name, type)


def output_data_large_sparky_with_angle():
    testing_files_label = {}
    training_files_label = {}
    for file_name in test_file_names:
        try:
            rand_int = randint(0, 20)
            if rand_int % 2 == 0:
                large_sparky_with_angle_superimposition(testing_files_path_with_large_sparky_rotate + file_name, file_name, 0)
            else:
                shutil.copyfile(testing_files_path + file_name, testing_files_path_with_large_sparky_rotate + file_name)
                testing_files_label[file_name] = 0
        except Exception as detail:
            print "Something bad has happened!!! This is the error ==> ", detail
    write_csv(testing_files_path_with_large_sparky_rotate + "testing_files_labels.csv", testing_files_label)

    for file_name in train_file_names:
        try:
            rand_int = randint(0, 20)
            if rand_int % 2 == 0:
                large_sparky_with_angle_superimposition(training_files_path_with_large_sparky_rotate + file_name, file_name, 1)
            else:
                shutil.copyfile(training_files_path + file_name,
                                training_files_path_with_large_sparky_rotate + file_name)
                training_files_label[file_name] = 0
        except Exception as detail:
            print "Something bad has happened!!! This is the error ==> ", detail
    write_csv(training_files_path_with_large_sparky_rotate + "training_files_labels.csv", training_files_label)


########################################################################################################################



if __name__ == '__main__':
    pass

testing_files_label = {}
training_files_label = {}

testing_files_path = "./../Test_Images/Testing_input/"
training_files_path = "./../Test_Images/Training_input/"

# Training file paths
training_files_path_with_small_sparky = "./../Test_Images/Output_files/Small_sparky/Training/"
training_files_path_with_large_sparky = "./../Test_Images/Output_files/Large_sparky/Training/"
training_files_path_with_small_sparky_rotate = "./../Test_Images/Output_files/Small_sparky_rotate/Training/"
training_files_path_with_large_sparky_rotate = "./../Test_Images/Output_files/Large_sparky_rotate/Training/"
training_files_path_with_random_sparky = "./../Test_Images/Output_files/Random_sparky/Training/"

# Testing file paths
testing_files_path_with_small_sparky = "./../Test_Images/Output_files/Small_sparky/Testing/"
testing_files_path_with_large_sparky = "./../Test_Images/Output_files/Large_sparky/Testing/"
testing_files_path_with_small_sparky_rotate = "./../Test_Images/Output_files/Small_sparky_rotate/Testing/"
testing_files_path_with_large_sparky_rotate = "./../Test_Images/Output_files/Large_sparky_rotate/Testing/"
testing_files_path_with_random_sparky = "./../Test_Images/Output_files/Random_sparky/Testing/"

test_file_names = os.listdir(testing_files_path)
train_file_names = os.listdir(training_files_path)
test_files_with_sparky = 0
train_files_with_sparky = 0

print "large sparky with angle - start"
output_data_large_sparky_with_angle()
print "large sparky with angle - end"

testing_files_label = {}
training_files_label = {}

print "small sparky with angle - start"
output_data_small_sparky_with_angle()
print "small sparky with angle - end"

testing_files_label = {}
training_files_label = {}

print "large sparky - start"
output_data_large_sparky()
print "large sparky - end"

testing_files_label = {}
training_files_label = {}

print "small sparky - start"
output_data_small_sparky()
print "small sparky - end"

testing_files_label = {}
training_files_label = {}

print "random sparky - start"
testing_data_full_random()
print "random sparky - end"

# for file_name in train_file_names:
#     try:
#         rand_int = randint(0,9)
#         if rand_int % 2 == 0 :
#             background = Image.open(training_files_path+file_name)
#             foreground = Image.open("rsz_sparky.gif")
#             new_foreground = foreground.convert('RGBA')
#             x,y = foreground.size
#             x_rand = randint(0,374)
#             y_rand = randint (0,241)
#             background.paste(new_foreground, (x_rand, y_rand ,x_rand+10 ,y_rand+15), new_foreground)
#             background.save(training_files_path+file_name)
#             train_files_with_sparky = train_files_with_sparky +1
#             training_files_label[file_name] = 1
#         else:
#             training_files_label[file_name] = 0
#     except:
#         pass
# training_files_labels_file = open("training_files_labels.csv","wb")
# writer1 = csv.writer(training_files_labels_file)
# testing_files_labels_file = open("testing_files_labels.csv","wb")
# writer2 = csv.writer(testing_files_labels_file)



# training_files_labels_file.close()
# testing_files_labels_file.close()
