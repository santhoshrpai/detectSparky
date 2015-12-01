__author__ = 'santhoshraja'

import Image
import os
import cPickle
import gzip
import numpy
import csv

def get_labels(path):
    files_label ={}
    with open(path, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            files_label[row[0]] = int(row[1])
    return files_label

def create_array(file_path, label_path):
    file_names =  os.listdir(file_path)
    files_label = get_labels(label_path)

    class_label = []
    values = []
    i = 0

    for file_name in file_names:
        try:
            # print file_name
            pixel_array = numpy.asarray(Image.open(file_path+file_name))
            x = pixel_array.shape
            if x[0] == 256:
                values.append(pixel_array)
                pic_label = files_label[file_name]
                class_label.append(pic_label)
                i = i+1
                if i==10:
                    break
        except:
            pass

    return values, class_label

def get_grey_scale_data(file_path, label_path,flag):
    file_names =  os.listdir(file_path)
    files_label = get_labels(label_path)

    class_label = []
    values = []
    i = 0

    for file_name in file_names:
        try:
            # print file_name
            pixel_array = numpy.asarray(Image.open(file_path+file_name))
            x = pixel_array.shape
            if x[0] == 256:
                matrix_values = []
                for h in range(x[0]):
                    mono = 0
                    sum = 0
                    for w in range(x[1]):
                        rgb = pixel_array[h][w]
                        mono = int(rgb[0]) + int(rgb[1]) + int(rgb[2])
                        sum = sum + mono
                    matrix_values.append(int(sum/x[1]))
                i = i+1
                values.append(matrix_values)
                pic_label = files_label[file_name]
                class_label.append(pic_label)
            if i == flag:
                break
        except:
            pass

    return values, class_label

def dump_gzip(values,class_labels,zip_file_name):
    feature = numpy.array(values)
    label = numpy.array(class_labels)

    print feature.shape
    print label.shape

    with gzip.open(zip_file_name, 'wb') as f:
        cPickle.dump((feature, label), f)

def split_training_data(filename):
    f = gzip.open(filename, 'rb')
    train_set, valid_set = cPickle.load(f)
    cPickle.dump(train_set, gzip.open('training_data.pkl.gz','wb'), cPickle.HIGHEST_PROTOCOL)
    cPickle.dump(valid_set, gzip.open('valid_data.pkl.gz','wb'), cPickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    testing_class_label_mapping_path = "./../files/testing_files_labels.csv"
    training_class_label_mapping_path = "./../files/training_files_labels.csv"

    testing_files_path = "./../files/images/Testing/"
    training_files_path = "./../files/images/Training/"

    testing_gzip_file_name = "testing_data.pkl.gz"
    training_gzip_file_name = "train_data.pkl.gz"

    print "Dumping for testing data"
    values , class_labels = get_grey_scale_data(testing_files_path,testing_class_label_mapping_path,10)
    dump_gzip(values,class_labels,testing_gzip_file_name)
    print "Dumping done for testing data" + "\n"

    print "Dumping for training data"
    values , class_labels = get_grey_scale_data(training_files_path,training_class_label_mapping_path,30)
    dump_gzip(values,class_labels,training_gzip_file_name)
    print "Dumping done for training data"

    print "Creating Valid Data"
    split_training_data(training_gzip_file_name)




# testing_files_label ={}
# training_files_label ={}
#
# testing_class_label_mapping_path = "./../files/testing_files_labels.csv"
# training_class_label_mapping_path = "./../files/training_files_labels.csv"
#
# testing_files_path = "./../files/images/Testing/"
# training_files_path = "./../files/images/Training/"
#
# testing_gzip_file_name = "testing_data.pkl.gz"
# training_gzip_file_name = "testing_data.pkl.gz"
#
#
# with open(testing_class_label_mapping_path, 'rb') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         testing_files_label[row[0]] = int(row[1])
#
# with open(training_class_label_mapping_path, 'rb') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         training_files_label[row[0]] = int(row[1])
#
#
#
#
# test_file_names =  os.listdir(testing_files_path)
# train_file_names = os.listdir(training_files_path)
#
# class_label = []
# values = []
# i = 0
#
# # print len(testing_files_label)
#
# for file_name in test_file_names:
#     try:
#         # print file_name
#         pixel_array = numpy.asarray(Image.open(testing_files_path+file_name))
#         x = pixel_array.shape
#         if x[0] == 256:
#             values.append(pixel_array)
#             pic_label = testing_files_label[file_name]
#             print pic_label
#             class_label.append(pic_label)
#             # print class_label[i]
#             i = i+1
#     except:
#         pass
#
# feature = numpy.array(values)
# label = numpy.array(class_label)
#
# print feature.shape
# print label.shape
#
# with gzip.open(testing_gzip_file_name, 'wb') as f:
#     cPickle.dump((feature, label), f)