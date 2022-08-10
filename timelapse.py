from time import sleep
from datetime import datetime
from lib import read_json, create_folder, write_statistics, colors as col

from picamera import PiCamera, Color
from fractions import Fraction

date = datetime.now()
settings = read_json("./settings.json")
camera = PiCamera()

camera.rotation = settings["rotation"]
camera.resolution = (settings["resolution"]["width"], settings["resolution"]["height"])
camera.annotate_text_size = settings["text"]["size"]
camera.annotate_foreground = Color(settings["text"]["foreground"])
camera.annotate_background = Color(settings["text"]["background"])

capture_options = ["day", "night"]

def timelapse(daytime):
    capture_folder = f"./captures/{date.strftime('%d.%m.%Y')}/{daytime}_{date.strftime('%H-%Mh')}/"
    create_folder(capture_folder)
    start_time = datetime.now().strftime("%d.%m.%Y-%H:%M:%S")
    image_counter = 0

    if daytime == "night":
        camera.framerate = Fraction(1, 6) 
        camera.sensor_mode = 3
        camera.exposure_mode = "off"
        camera.iso = settings["night"]["iso"]
        camera.shutter_speed = settings["night"]["shutter_speed"]

    try:
        print(f"{col.fg.cyan}\nTimelapse   {col.reset}: {col.fg.lightgreen}Start")
        print(f"{col.fg.cyan}Mode        {col.reset}: {daytime}")
        print(f"{col.fg.cyan}Duration    {col.reset}: {settings['timelapse']['images']} Images")
        print(f"{col.fg.cyan}Start Time  {col.reset}: {start_time}")

        for i in range(settings["timelapse"]["images"]):
            camera.capture(capture_folder + "img{0:06d}.jpg".format(i))
            camera.annotate_text = datetime.now().strftime(" %d.%m.%Y - %H:%M:%S ")
            image_counter += 1
            sleep(settings["timelapse"]["interval"])
        
    except KeyboardInterrupt:
        print(f"{col.fg.red}\nAbort       {col.reset}: by User")

    finally:
        end_time = datetime.now().strftime("%d.%m.%Y-%H:%M:%S")
        write_statistics("timelapse", daytime, image_counter, start_time, end_time)

        print(f"{col.fg.cyan}Image taken {col.reset}: {image_counter}")
        print(f"{col.fg.cyan}End Time    {col.reset}: {end_time}")
        print(f"{col.fg.cyan}Folder      {col.reset}: {capture_folder}")
        print(f"{37*'-'}")



print(f"{3*'-'}[ {col.underline}{col.fg.cyan}{settings['name']}: {settings['version']}{col.reset} ]{20*'-'}")

if settings["timelapse"]["auto_mode"]:
    if settings["timelapse"]["auto_capture_mode"] in capture_options:
        timelapse(settings["timelapse"]["auto_capture_mode"])
    else:
        print(f"{col.fg.red}Error {col.reset}: settings.json['auto_capture_mode'], try 'auto_capture_mode': 'day or night'")
        user_input = input(f"Which Mode [day|night]{col.reset}: ")
        if user_input in capture_options:
            timelapse(user_input)
        else: 
            print(f"{col.fg.red}Error {col.reset}: wrong option, try day or night")

else:
    user_input = input(f"Which Mode [day|night]{col.reset}: ")
    if user_input in capture_options:
        timelapse(user_input)
    else: 
        print(f"{col.fg.red}Error {col.reset}: wrong option, try day or night")
