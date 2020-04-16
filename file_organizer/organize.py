import mimetypes
import os

import easygui

selected_path = easygui.diropenbox(default='~/Desktop')

files_in_selected_dir = os.listdir(selected_path)

# map that holds names of directories based on their mimetype + data to be added to new directories later
TYPE_DIRNAME_MAP = {
    "image": {
        "dirname": "Pictures",
        "data": []
    },
    "video": {
        "dirname": "Videos",
        "data": []
    }
}

for file in files_in_selected_dir:
    if file == ".DS_Store": continue

    ## get the mimetype of file
    mimetype = mimetypes.guess_type(f"{selected_path}/{file}")[0]

    if not mimetype:
        print(file)
        continue

    ## name of mimetype
    mimetype = mimetype.split('/')[0]

    ## if mimetype is not in our map we are skipping it
    if (mimetype not in TYPE_DIRNAME_MAP.keys()): continue

    ## create list of files to be added to new directory
    TYPE_DIRNAME_MAP[mimetype]["data"].append(file)


for key, value in TYPE_DIRNAME_MAP.items():
    try:
        os.mkdir(f"{selected_path}/{value['dirname']}")
    except FileExistsError:
        print(f"Directory {value['dirname']} exists! Skipping ...")
        pass

    ## move the file
    for file in value['data']:
        os.rename(f"{selected_path}/{file}",
                  f"{selected_path}/{value['dirname']}/{file}")
