from PIL import Image, ImageDraw
from random import randint
from perlin_noise import PerlinNoise

image_path = "./../img/"
NUMBER_OF_BACKGROUNDS = 3
SNOW_ALTITUDE = 70

def draw_mountain_range(image, midpoint=60, shadow = 0, snow=True):
    print("Drawing a Mountain Range")
    draw = ImageDraw.Draw(image)
    noise = PerlinNoise(seed=randint(0,1000))
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

def generate_mountains():
    num_mountains = randint(1, 10)
    for i in range(num_mountains):
        for i in range(128):
            pass



def draw_beach():
    return draw_sky()

def draw_city():
    mountain_image = draw_sky()
    draw = ImageDraw.Draw(mountain_image)
    noise = PerlinNoise()
    for i in range(128):
        n = abs(noise([i/2])) # this noise val looks like a city
        print(n)
        draw.rectangle([(i, 128), (i+1, 64-(n*64))], (160, 160, 160))
    return mountain_image

# TODO Implement night time
def draw_sky(image, resolution=2, night= False, apocalypse=False):
    print("Drawing Sky")
    if night:
        draw = ImageDraw.Draw(image)
        noise = PerlinNoise(seed=randint(0,1000))
        step1 = randint(0, 100)
        for x in range(0, 128, 2):
            step2=0
            for y in range(0, 128, resolution):
                c = abs(int(noise([step1, step2])*150))
                print(c)
                draw.rectangle([(x, y), (x+resolution, y+resolution)], (c, c, c+40))
                step2+=0.02
            step1+=0.01
    elif apocalypse:
        draw = ImageDraw.Draw(image)
        noise = PerlinNoise(seed=randint(0,1000))
        step1 = randint(0, 100)
        for x in range(0, 128, 2):
            step2=0
            for y in range(0, 128, resolution):
                c = abs(int(noise([step1, step2])*255))
                print(c)
                draw.rectangle([(x, y), (x+resolution, y+resolution)], (c, c+80, c+80))
                step2+=0.05
            step1+=0.01
    else:
        draw = ImageDraw.Draw(image)
        noise = PerlinNoise(seed=randint(0,1000))
        step1 = randint(0, 100)
        for x in range(0, 128, 2):
            step2=0
            for y in range(0, 128, resolution):
                ## multiplying noise causes more variance, adding changes base color
                c = abs(int(noise([step1, step2])*300))+20
                print(c)
                draw.rectangle([(x, y), (x+resolution, y+resolution)], (c, c+30, c+100))
                step2+=0.03
            step1+=0.01


def random_background():
    random_number = randint(NUMBER_OF_BACKGROUNDS-1)
    if random_number == 0:
        return draw_mountain_background()
    elif random_number == 1:
        return draw_beach()
    elif random_number == 2:
        return draw_city()


def main():
    mountain = draw_mountain_background()
    mountain.save("./sandbox/mountain-background.png")
    # city = draw_city()
    # city.save("./sandbox/city-background.png")
    # beach = draw_beach()
    # beach.save("./sandbox/beach-background.png")

if __name__ == '__main__':
    main()