from PIL import Image, ImageDraw
from perlin_noise import PerlinNoise
from random import randint
import numpy as np

# TODO Implement night time
def draw_sky(image, resolution=2, night= False, apocalypse=False):
    print("Drawing Sky")
    if night:
        draw = ImageDraw.Draw(image)
        noise = PerlinNoise(seed=randint(0,1000))
        step1 = randint(0, 100)
        for x in range(0, 128, resolution):
            step2=0
            for y in range(0, 128, resolution):
                c = abs(int(noise([step1, step2])*150))
                #print(c)
                draw.rectangle([(x, y), (x+resolution, y+resolution)], (c, c, c+40))
                step2+=0.02
            step1+=0.01
    elif apocalypse:
        draw = ImageDraw.Draw(image)
        noise = PerlinNoise(seed=randint(0,1000))
        step1 = randint(0, 100)
        for x in range(0, 128, resolution):
            step2=0
            for y in range(0, 128, resolution):
                c = abs(int(noise([step1, step2])*255))
                #print(c)
                draw.rectangle([(x, y), (x+resolution, y+resolution)], (c, c+80, c+80))
                step2+=0.05
            step1+=0.01
    else:
        draw = ImageDraw.Draw(image)
        noise = PerlinNoise(seed=randint(0,1000))
        step1 = randint(0, 100)
        for x in range(0, 128, resolution):
            step2=0
            for y in range(0, 128, resolution):
                ## multiplying noise causes more variance, adding changes base color
                c = abs(int(noise([step1, step2])*300))+20
                #print(c)
                draw.rectangle([(x, y), (x+resolution, y+resolution)], (c, c+30, c+100))
                step2+=0.03
            step1+=0.01

def layer(images = []):
    """
    Layers array of images, with first being the closest to the 'back'
    """
    composite = Image.new('RGBA', (128, 128))
    for image in images:
        composite = Image.alpha_composite(composite, image)
    return composite

def recolor(image, color=(255, 255, 255)):
    data = np.array(image)
    red, green, blue, alpha = data.T
    colored_areas = (red!=0) & (blue!=0) & (green!=0)
    data[..., :-1][colored_areas.T] = color# Transpose back needed

    recolored = Image.fromarray(data)
    return recolored
