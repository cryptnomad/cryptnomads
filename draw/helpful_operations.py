from PIL import Image


def layer(images = []):
    """
    Layers array of images, with first being the closest to the 'back'
    """
    composite = images[0]
    for image in images:
        composite = Image.alpha_composite(composite, image)
    return composite