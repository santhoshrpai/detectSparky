__author__ = 'santhoshraja'

"""Manipulating datasets into a pickle file

    allowing the creation of multiple pickle files from a set of
    images, including their properties. Followed by writing the
    images out of the pickle file
    __author__ = "Gil Tamari"
    __copyright__ = "Copyright 2014"
    __version__ = "0.0.1"
    __status__ = "Dev"
"""
import errno
import glob
# import pathlib <- python 3.4+ better than our use
import pickle
import os
from PIL import Image, ImageFilter


class PickleWrangling:
    """Summary of class here.

    Manipulates a dataset by converting the images into a pickle file
    with their properties, properties can be added

    Attributes:
        datasets: array of dictionaries, that represent a file, its private
    """

    def __init__(self,in_datasets):
        """Inits PickleWrangling with a datasets array """
        self.datasets = in_datasets or []


    def create_pickle_from_datasets(self):
        """loops through the datasets, reading the directory and building a pickle file for each dataset
            Returns:
                void
        """
        for dataset in self.datasets:
            files = glob.glob(dataset['path'])
            files_no = len(files)
            i = 1
            images = []
            for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
                try:
                    with open(name) as f: # No need to specify 'r': this is the default.

                        try:
                            original_image = Image.open(name)
                            print('The format, size, mode of the Image is: ')
                            print original_image.format, original_image.size, original_image.mode
                            file_name, extension = os.path.splitext(name)
                            print 'reading image: ',file_name,' [',i,'/',files_no,']'
                            # try:
                            #     extension = name[- (len(name) - name.index('.') - 1):]
                            # except ValueError:
                            #     extension = ''
                            images.append({'pixels': original_image.tobytes(),
                                            'original_name': file_name + extension,
                                            'ext': extension,
                                            'size': original_image.size,
                                            'mode': original_image.mode })
                            original_image.close()
                            i += 1
                        except:
                            print 'Unable to load image:', name
                except IOError as exc:
                    if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
                        raise # Propagate other kinds of IOError.
            print 'About to dump file with: ' , len(images), ' # of images'
            pickle.dump( images, open( dataset['outputPickleFile'], "wb" ) )
            print 'Written file: ',dataset['outputPickleFile']

    # testing the process did work:
    def create_files_from_pickles(self,output_path = None):
        """loops through the datasets, reading the outputted pickle file and writing the images
            Args:
                output_path: an optional, an output path
            Returns:
                void
        """
        for dataset in self.datasets:
            output_pickle_file = dataset['outputPickleFile']
            try:
                loaded_pickle_file = pickle.load( open( output_pickle_file, "rb" ) )
                files_no = len(loaded_pickle_file)
                i = 0
                print 'number of images it holds: ', files_no

                for image_obj in loaded_pickle_file:
                    # taking the file path
                    name = os.path.split(os.path.abspath(image_obj['original_name']))[1].strip()
                    image = Image.frombytes(image_obj['mode'], image_obj['size'], image_obj['pixels'])
                    print 'im here!',name
                    i += 1
                    try:

                        if (output_path is not None):
                            name = output_path + name
                        print 'writing image: ',name,' [',i,'/',files_no,']'
                        image.save(name)
                        print 'verify'
                        image.verify()
                        print 'wrote successfully!'
                        image.close()

                    except IOError:
                        print 'Unable to save image: ',name

            except:
                print 'Unable to load pickle file: ',output_pickle_file

if __name__ == '__main__':
     g_datasets = [{'name': 'MIT CBCL CAR DATABASE',
                    'path': './cars128x128/*.ppm' ,
                    'outputPickleFile': 'mit.pkl'}
                 ]
     # handle files
     handle_files = PickleWrangling(g_datasets)

     # build pickle file from all the image files
     handle_files.create_pickle_from_datasets()

     # extract images out of the pickle file
     handle_files.create_files_from_pickles('delete_me/')