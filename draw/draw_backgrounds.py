from PIL import Image, ImageColor
from random import randint

image_path = "./../img/"
NUMBER_OF_BACKGROUNDS = 3

def draw_mountain():
    mountain_image = draw_sky()
    return mountain_image

def draw_beach():
    return draw_sky()

def draw_city():
    return draw_sky()

def draw_sky(night= False):
    print("Drawing Sky")
    if night:
        im = Image.new('RGB', (128, 128), color= (255, 255, 255))
    else:
        im = Image.new('RGB', (128, 128), color= (62, 176, 211))
    return im.convert("RGBA")

def random_background():
    random_number = randint(NUMBER_OF_BACKGROUNDS-1)
    if random_number == 0:
        return draw_mountain()
    elif random_number == 1:
        return draw_beach()
    elif random_number == 2:
        return draw_city()


def main():
    mountain = draw_mountain()
    mountain.save("./sandbox/mountain-background.png")
    city = draw_city()
    city.save("./sandbox/city-background.png")
    beach = draw_beach()
    beach.save("./sandbox/beach-background.png")

if __name__ == '__main__':
    main()