import json
import os

# read: read_path/file.json to dict{}
def read_json(read_path):
    with open(read_path, 'r') as jsonFile:
        read_data = json.loads(jsonFile.read())
    return read_data


# write: write_data to store_path/file.json
def write_json(store_path, write_data):
    with open(store_path, 'w') as jsonFile:
        json.dump(write_data, jsonFile, indent=4)

# check & create: directory
def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

# write: statistics to data/statistics.json
def write_statistics(mode, daytime, image_counter, start_time, end_time):
    settings = read_json("./settings.json")
    data = read_json(settings["statistics"]["json"])    
    id_counter = len(data[mode][daytime].keys())

    if settings["statistics"]["enable"]:
        update_data = {
            id_counter: {
                "images": image_counter,
                "start": start_time,
                "end": end_time 
            }
        }

        data[mode][daytime].update(update_data)
        write_json(settings["statistics"]["json"], data)

# colors: print(colors.bg.green, "data", colors.fg.red, "this is text")
class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
# colors_subclass: foreground colors
    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'
# colors_subclass: background colors
    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'