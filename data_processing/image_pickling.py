__author__ = 'santhosh'

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


def prepare_data_for_keras(file_path, label_path):
    file_names =  os.listdir(file_path)
    files_label = get_labels(label_path)

    class_label = []
    values = []
    i = 0
    for file_name in file_names:
        try:
            pixel_array = numpy.asarray(Image.open(file_path+file_name))
            x = pixel_array.shape
            if x[0] == 256:
                matrix_values = []
                for h in range(x[0]):
                    col_values = []
                    for w in range(x[1]):
                        rgb = pixel_array[h][w]
                        mono = sum(rgb)
                        col_values.append(int(mono))
                    matrix_values.append(col_values)
                values.append(matrix_values)
                pic_label = files_label[file_name]
                class_label.append(pic_label)
                i = i+1
                if i == 100:
                    break
            feature = numpy.array(values)
            label = numpy.array(class_labels)
            print feature.shape
            print label.shape
        except:
            pass

    return values, class_label

def prepare_validation_data(file_path, label_path):
    file_names =  os.listdir(file_path)
    files_label = get_labels(label_path)

    class_label = []
    values = []
    i = 0
    for i in range(300,400):
        file_name = file_names[i]
        try:
            pixel_array = numpy.asarray(Image.open(file_path+file_name))
            x = pixel_array.shape
            if x[0] == 256:
                matrix_values = []
                for h in range(x[0]):
                    col_values = []
                    for w in range(x[1]):
                        rgb = pixel_array[h][w]
                        mono = sum(rgb)
                        col_values.append(int(mono))
                    matrix_values.append(col_values)
                values.append(matrix_values)
                pic_label = files_label[file_name]
                class_label.append(pic_label)
                i = i+1
        except:
            pass

    return values, class_label

def dump_gzip(values,class_labels,zip_file_name):
    feature = numpy.array(values)
    label = numpy.array(class_labels)

    print feature.shape
    print label.shape

    with gzip.open(zip_file_name, 'wb') as f:
        cPickle.dump((feature, label), f, cPickle.HIGHEST_PROTOCOL)

def dump_validation_gzip(values, zip_file_name):
    feature = numpy.array(values)
    print feature.shape

    with gzip.open(zip_file_name,'wb') as f:
        cPickle.dump(feature,f,cPickle.HIGHEST_PROTOCOL)

def write_validation_labels(labels, file_path):
    output_file = open(file_path,'wb')
    writer = csv.writer(output_file)
    for label in labels:
        writer.writerow([label])
    output_file.close()

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
    training_gzip_file_name = "training_data.pkl.gz"
    validation_gzip_file_name = "validation_data.pkl.gz"

    validation_class_labels_file ="./../files/validation_files_labels.csv"

    print "Dumping for testing data"
    values , class_labels = prepare_data_for_keras(testing_files_path,testing_class_label_mapping_path)
    dump_gzip(values,class_labels,testing_gzip_file_name)
    print "Dumping done for testing data" + "\n"

    print "Dumping for training data"
    values , class_labels = prepare_data_for_keras(training_files_path,training_class_label_mapping_path)
    dump_gzip(values,class_labels,training_gzip_file_name)
    print "Dumping done for training data"

    print "Dumping for validation data"
    values , class_labels = prepare_validation_data(testing_files_path,testing_class_label_mapping_path)
    dump_validation_gzip(values, validation_gzip_file_name)
    write_validation_labels(class_labels,validation_class_labels_file)

    # print "Creating Valid Data"
    # split_training_data(training_gzip_file_name)