import os
# os.rename("C:/working/yesyes.rtf", "C:/working/just-yes.rtf")

directory_in_str = "C:/working"
directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    # print(filename)
    if filename.endswith("_x64.zip"):
        # print(filename)
        new_filename = filename.removesuffix("_x64.zip") + ".zip"
        # print(new_filename)
        os.rename(f"C:/working/{filename}", f"C:/working/{new_filename}")
    # if filename.endswith(".asm") or filename.endswith(".py"):
    #     # print(os.path.join(directory, filename))
    #     continue
    # else:
    #     continue
