import os
import shutil

# Change These ##############################
input_path = "C:/working"
target_path = "C:/working/RandomFolder"
#############################################

directory = os.fsencode(input_path)

all_dir_nums = []

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    # print(filename)
    path = f"{input_path}/{filename}"
    # print(os.path.isdir(path))
    # print(filename.isdigit())
    # print(os.path.isfile(path))
    if os.path.isdir(path) and filename.isdigit():
        # print("int!" + int(file))
        all_dir_nums.append(int(filename))
    #     print(all_dir_nums)
    # print(top_num)

top_num = max(all_dir_nums)
path_to_top_num = os.fsencode(f"{input_path}/{str(top_num)}")

for top_num_file in os.listdir(path_to_top_num):
    filename1 = os.fsdecode(top_num_file)
    path_to_test_defs = f"{input_path}/{str(top_num)}/{filename1}"
    # print(filename1)
    # print(path_to_test_defs)
    if os.path.isfile(path_to_test_defs):
        # print("definitely")
        # print(top_num_file)
        shutil.copy(path_to_test_defs, target_path)

for test_def_file in os.listdir(f"{input_path}/{str(top_num)}/test_defs"):
    filename2 = os.fsdecode(test_def_file)
    # print(test_def_file)
    # print(filename2)
    if filename2 == "BASHDefs_64.zip" or filename2 == "IDSDefs_64.zip"\
            or filename2 == "PD-ET-Core3v5i64.exe" or filename2 == "SDSDefs_64.zip"\
            or filename2 == "SEFDefs_64.zip"\
            or filename2 == "STARi64_Full_test.exe" or filename2 == "STICDefs_64.zip"\
            or filename2 == "TDADDefs.zip":
        # print("yes!")
        path1 = f"{input_path}/{str(top_num)}/test_defs/{filename2}"
        shutil.copy(path1, target_path)

for file in os.listdir(target_path):
    filename3 = os.fsdecode(file)
    # print(filename)
    if filename3.endswith("_64.zip"):
        # print(filename3)
        new_filename = filename3.removesuffix("_64.zip") + ".zip"
        # print(new_filename)
        os.rename(f"{target_path}/{filename3}", f"{target_path}/{new_filename}")
