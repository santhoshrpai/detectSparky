__author__ = 'santhosh'

import Image
import os
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