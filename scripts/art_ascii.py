import cv2
import main
import os
import platform
import sys

from codeholder import ascii_artvid_run
from codeholder import ascii_artvid_instructions
from PIL import Image
from shutil import copyfile

video_length = 218
ASCII_CHARS = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. '
inputsec: str = 'None'

def scale_image(image, new_width=100, new_height=30):
    """Resizes an image preserving the aspect ratio.
    """
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    if new_height == 0:
        new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image


def convert_to_grayscale(image):
    return image.convert('L')


def map_pixels_to_ascii_chars(image, range_width=3.69):
    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[int(pixel_value/range_width)] for pixel_value in
            pixels_in_image]

    return "".join(pixels_to_chars)


def convert_image_to_ascii(image, new_width=100, new_height=30):
    image = scale_image(image, new_width, new_height)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width] for index in
            range(0, len_pixels_to_chars, new_width)]

    return "\n".join(image_ascii)


def handle_image_conversion(image_filepath):
    image = None
    try:
        image = Image.open(image_filepath)
    except Exception as e:
        print("Unable to open image file {image_filepath}.".format(image_filepath=image_filepath))
        return
    image_ascii = convert_image_to_ascii(image)
    return image_ascii


def conv():
    if len(inputsec) == 0:
        print('ERROR: Cannot locate the specified path.')
        createinput()
        return
    if inputsec == 'exit':
        print('Ending script process..')

        if platform.system() == 'Linux':
            os.system('clear')
        elif platform.system() == 'Windows':
            os.system('cls')

        os.system(main.pythonExec + ' scripts/main.py')
        exit(0)
        return
    if not os.path.exists(inputsec):
        print('ERROR: Path does not exists or is a directory.')
        createinput()
        return
    if not os.path.exists('ascii_art/converted/'
                          + os.path.basename(inputsec)
                          + '/'):
        os.makedirs('ascii_art/converted/'
                    + os.path.basename(inputsec)
                    + '/')
    elif os.path.exists('ascii_art/converted/'
                        + os.path.basename(inputsec)
                        + '/'):
        if os.path.exists('ascii_art/converted/'
                          + os.path.basename(inputsec)
                          + '/converted.txt'):
            os.remove('ascii_art/converted/'
                      + os.path.basename(inputsec)
                      + '/converted.txt')
    if not os.path.exists('ascii_art/converted/'
                      + os.path.basename(inputsec)
                      + '/' + os.path.basename(inputsec)):
        copyfile(src=inputsec, dst='ascii_art/converted/'
                               + os.path.basename(inputsec)
                               + '/' + os.path.basename(inputsec))

    f = open('ascii_art/converted/'
             + os.path.basename(inputsec)
             + '/converted.txt', 'x')
    f.close()

    if inputsec.endswith(('.mp4', '.mkv', '.3gp', '.mov')):
        print('---------------------------------------')
        vidcap = cv2.VideoCapture(inputsec)
        time_count = 0
        frames = []

        while time_count <= video_length * 1000:
            print('Converting: ' + str(time_count))
            vidcap.set(0, time_count)
            success, image = vidcap.read()
            if success:
                cv2.imwrite('ascii_art/converted/'
                            + os.path.basename(inputsec)
                            + '/temp.jpg', image)
            frames.append(handle_image_conversion('ascii_art/converted/'
                                                  + os.path.basename(inputsec)
                                                  + '/temp.jpg'))
            time_count = time_count + 100

        f = open('ascii_art/converted/'
                 + os.path.basename(inputsec)
                 + '/converted.txt', 'w')
        f2 = open('ascii_art/converted/'
                  + os.path.basename(inputsec)
                  + '/run.py', 'w')
        f3 = open('ascii_art/converted/'
                  + os.path.basename(inputsec)
                  + '/instructions.txt', 'w')
        os.remove('ascii_art/converted/'
                  + os.path.basename(inputsec)
                  + '/temp.jpg')
        f.write('SPLIT'.join(frames))
        ascii_artvid_run.basevideofile = os.path.basename(inputsec)
        f2.write(ascii_artvid_run.code)
        f3.write(ascii_artvid_instructions.code)
        f.close()
        f2.close()
        f3.close()
        print('---------------------------------------')
    elif inputsec.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
        f = open('ascii_art/converted/'
                 + os.path.basename(inputsec)
                 + '/converted.txt', 'w')
        f.write(handle_image_conversion(inputsec))
        f.close()

    print('Convert successful! Converted videos/images'
          ' are located at "/ascii_art/converted/".')
    createinput()


def createinput():
    global inputsec
    print('---------------------------------------')
    inputsec = input('Enter video/image path: ')
    sys.stdout.write("\033[F")
    print('')
    print('Convert path: ' + inputsec)
    conv()


print('DevScripts art_ascii.py')
print('ArtASCII')
createinput()