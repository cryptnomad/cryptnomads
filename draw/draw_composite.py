from helpful_operations import layer
from random import randint
from PIL import Image
from draw_backgrounds import draw_mountain_background

components_path = "./components/"
bags_path = "./components/bag/"

# Define lists of possible elements
bags = ['btc_bag']


def draw_random_composite(number=0):
    """
    Draws a randomized composite
    """
    # Get random elements
    print("Randomizing Elements")
    bag_num = randint(0, len(bags)-1)

    # Open relevant images
    # TODO: Randomize this
    print("Getting relevant images")
    background_image = draw_mountain_background()
    outline_image = Image.open('./components/body_outline_man.png').convert("RGBA")
    pants_image = Image.open('./components/pants.png').convert("RGBA")
    shirt_image = Image.open('./components/shirt.png').convert("RGBA")
    skin_image = Image.open('./components/skin.png').convert("RGBA")
    bag_image = Image.open(bags_path + bags[bag_num] + '.png').convert("RGBA")
    

    #Composite
    print("Compositing image")
    composite_image = layer([
        background_image, 
        outline_image, 
        shirt_image,
        skin_image,
        pants_image,
        bag_image
        ])
    composite_image.save(f"./../nomads/nomad-{number}.png")
    return composite_image

def main():
    draw_random_composite()


if __name__ == '__main__':
    main()