from PIL import Image, ImageDraw
from random import randint
from perlin_noise import PerlinNoise
# TODO Fuck this relative path bullshit
from helpful_operations import draw_sky

def draw_mountain_range(image, midpoint=60, shadow = 0, snow=True):
    print("Drawing a Mountain Range")
    draw = ImageDraw.Draw(image)
    noise = PerlinNoise(seed=randint(0,10000))
    for i in range(128):
        n = noise([i/32, .01])
        #print(n)
        # Mountain
        draw.rectangle([(i, 128), (i+1, midpoint-(n*64))], (160-shadow, 160-shadow, 160-shadow))
        # Darker
        draw.rectangle([(i, 128), (i+1, (midpoint+15)-(n*64))], (140-shadow, 140-shadow, 140-shadow))
        draw.rectangle([(i, 128), (i+1, (midpoint+35)-(n*64))], (120-shadow, 120-shadow, 120-shadow))
        # Snow
        if snow:
            offset = randint(-1,1)+midpoint+3
            draw.rectangle([(i, offset-(n*64)), (i+1, midpoint-(n*64))], (255, 255, 255))

def draw_trees(image, height=5, color = (26, 59, 31), smoothness =2):
    print("Drawing Trees")
    draw = ImageDraw.Draw(image)
    noise = PerlinNoise(seed=randint(0,1000))
    for i in range(128):
        n = abs(noise([i/smoothness,.01] )) # this noise val looks like a city
        #print(n)
        # draw.rectangle([(i, 128), (i+1, (128-height-n*50))], (36, 82, 43)) #lighter
        draw.rectangle([(i, 128), (i+1, (128-height-n*50))], color)

def draw_grass(image, height=3):
    print("Drawing Grass")
    draw = ImageDraw.Draw(image)
    noise = PerlinNoise(seed=randint(0,1000))
    for i in range(128):
        n = abs(noise([i/32,0.1] )) # this noise val looks like a city
        #print(n)
        draw.rectangle([(i, 128), (i+1, (128-height-n*10))], (36, 82, 43)) #lighter


#TODO parameterize options such as nighttime from the highest level
def draw_mountain_background():
    mountain_image = Image.new('RGBA', (128, 128), color= (62, 176, 211))
    draw_sky(mountain_image)

    draw_mountain_range(mountain_image)
    num_mountain_ranges = randint(0, 3)
    for i in range(num_mountain_ranges):
        draw_mountain_range(mountain_image, midpoint = 40+ 15*i, shadow = 10*i)
    draw_trees(mountain_image, height=30, color= (20, 49, 21))
    draw_trees(mountain_image)
    draw_grass(mountain_image)
    return mountain_image

def main():
    mountain = draw_mountain_background()
    mountain.save("./sandbox/mountain-background.png")

if __name__ == '__main__':
    main()