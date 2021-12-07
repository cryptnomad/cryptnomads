from helpful_operations import layer
from random import randint
from PIL import Image
from draw_backgrounds import draw_mountain

components_path = "./components/"
bags_path = "./components/bag/"

# Define lists of possible elements
bags = ['btc_bag']
backgrounds = [draw_mountain]


def draw_random_composite(number=0):
    """
    Draws a randomized composite
    """
    # Get random elements
    print("Randomizing Elements")
    bag_num = randint(0, len(bags)-1)

    # Open relevant images
    print("Getting relevant images")
    background_image = draw_mountain()
    avatar_image = Image.open("./components/avatar.png").convert("RGBA")
    bag_image = Image.open(bags_path + bags[bag_num] + '.png').convert("RGBA")

    #Composite
    print("Compositing image")
    composite_image = layer([background_image, avatar_image, bag_image])
    composite_image.save(f"./../nomads/nomad-{number}.png")
    return composite_image

def main():
    draw_random_composite()


if __name__ == '__main__':
    main()