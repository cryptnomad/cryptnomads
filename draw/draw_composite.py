from random import randint
from PIL import Image
from draw_mountains import draw_mountain_background
from helpful_operations import layer, recolor

# Define lists of possible elements
BAGS = [
    'btc',
    'eth',
    'usdc'
    ]

SKIN_COLORS = [
    (141,85,36),
    (198,134,66),
    (224,172,105),
    (241,194,125),
    (255,219,172),
    (61, 12, 2)
]

NUM_STYLES = 2


def draw_random_composite(number=0):
    """
    Draws a randomized composite
    """
    # Get random elements
    print("Randomizing Elements")
    

    # Open relevant images
    # TODO: Randomize this
    print("Getting relevant images")
    style_num = randint(0, NUM_STYLES-1)
    background_image = draw_mountain_background()
    outline_image = Image.open('./components/body_outline-{}.png'.format(style_num)).convert("RGBA")

    # Skin
    skin_image = Image.open('./components/skin-{}.png'.format(style_num)).convert("RGBA")
    skin_color = SKIN_COLORS[randint(0,len(SKIN_COLORS)-1)]
    skin_image = recolor(skin_image, skin_color)

    # Pants
    pants_image = Image.open('./components/pants-{}.png'.format(style_num)).convert("RGBA")
    pants_color = (randint(0,255), randint(0,255), randint(0,255))
    if style_num == 1:
        pants_color = skin_color
    pants_image = recolor(pants_image, color=pants_color)

    # Shirt
    shirt_image = Image.open('./components/shirt-{}.png'.format(style_num)).convert("RGBA")
    shirt_color = (randint(0,255), randint(0,255), randint(0,255))
    shirt_image = recolor(shirt_image, color=shirt_color)

    # hair
    hair_image = Image.open('./components/hair-{}.png'.format(style_num)).convert("RGBA")
    hair_color = (randint(0,255), randint(0,255), randint(0,255))
    hair_image = recolor(hair_image, hair_color)

    hair_outline_image = Image.open('./components/hair_outline-{}.png'.format(style_num)).convert("RGBA")
    darkness_modifier = -20
    hair_outline_color = (
        hair_color[0]+darkness_modifier, 
        hair_color[1]+darkness_modifier, 
        hair_color[2]+darkness_modifier)
    hair_outline_image = recolor(hair_outline_image, hair_outline_color)

    #BAGGGG
    bag_num = randint(0, len(BAGS)-1)
    bag_image = Image.open('./components/bag/' + BAGS[bag_num] + '_bag.png').convert("RGBA")
    

    #Composite
    print("Compositing image")
    composite_image = layer([
        background_image, 
        outline_image, 
        shirt_image,
        skin_image,
        pants_image,
        hair_image,
        hair_outline_image,
        bag_image,
        
        ])
    composite_image.save(f"./../nomads/nomad-{number}.png")
    return composite_image



def main():
    num = input("How many?")
    for i in range(int(num)):
      draw_random_composite(i)


if __name__ == '__main__':
    main()