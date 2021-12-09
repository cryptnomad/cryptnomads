from random import randint
from PIL import Image
from draw_mountains import draw_mountain_background
from helpful_operations import layer, recolor

# Define lists of possible elements
bags = [
    'btc',
    'eth'
    ]

skin_colors = [
    (141,85,36),
    (198,134,66),
    (224,172,105),
    (241,194,125),
    (255,219,172),
    (61, 12, 2)
]


def draw_random_composite(number=0):
    """
    Draws a randomized composite
    """
    # Get random elements
    print("Randomizing Elements")
    

    # Open relevant images
    # TODO: Randomize this
    print("Getting relevant images")
    background_image = draw_mountain_background()
    outline_image = Image.open('./components/body_outline_man.png').convert("RGBA")

    # Pants
    pants_image = Image.open('./components/pants.png').convert("RGBA")
    pants_color = (randint(0,255), randint(0,255), randint(0,255))
    pants_image = recolor(pants_image, color=pants_color)

    # Shirt
    shirt_image = Image.open('./components/shirt.png').convert("RGBA")
    shirt_color = (randint(0,255), randint(0,255), randint(0,255))
    shirt_image = recolor(shirt_image, color=shirt_color)

    # Skin
    skin_image = Image.open('./components/skin.png').convert("RGBA")
    skin_color = skin_colors[randint(0,len(skin_colors)-1)]
    skin_image = recolor(skin_image, skin_color)
    print(len(skin_colors)-1)

    #BAGGGG
    bag_num = randint(0, len(bags)-1)
    bag_image = Image.open('./components/bag/' + bags[bag_num] + '_bag.png').convert("RGBA")
    

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