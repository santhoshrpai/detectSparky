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
from data_processing.ImagePickling import PickleWrangling

def main():

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

if __name__ == '__main__':
    main()