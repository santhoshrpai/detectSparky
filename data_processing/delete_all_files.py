import os, shutil

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

list_of_folders = [training_files_path_with_small_sparky, training_files_path_with_large_sparky,
                 training_files_path_with_small_sparky_rotate, training_files_path_with_large_sparky_rotate, training_files_path_with_random_sparky,
                 testing_files_path_with_small_sparky, testing_files_path_with_large_sparky, testing_files_path_with_small_sparky_rotate,
                 testing_files_path_with_large_sparky_rotate, testing_files_path_with_random_sparky]

for folder_name in list_of_folders:
    for the_file in os.listdir(folder_name):
        file_path = os.path.join(folder_name, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                # elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception, e:
            print e
